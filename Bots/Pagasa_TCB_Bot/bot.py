from datetime import datetime
import json
import re
from io import BytesIO
from pathlib import Path
from typing import Optional, Dict, List, Tuple
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# --- Config ---
TCB_DIR = "https://pubfiles.pagasa.dost.gov.ph/tamss/weather/bulletin/"
STATE_FILE = Path("state.json")

UA = {"User-Agent": "pagasa-tcb-bot/1.0"}
TIMEOUT = 25


# --- State helpers ---
def load_state() -> Dict:
    if STATE_FILE.exists():
        raw = STATE_FILE.read_text(encoding="utf-8").strip()
        return json.loads(raw) if raw else {}
    return {}


def save_state(state: Dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


# --- Web helpers ---
def fetch_html(url: str) -> str:
    r = requests.get(url, headers=UA, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text


def list_pdf_links(index_url: str) -> List[str]:
    html = fetch_html(index_url)
    soup = BeautifulSoup(html, "html.parser")

    links: List[str] = []
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        if not href.lower().endswith(".pdf"):
            continue

        if href.startswith("http"):
            links.append(href)
        else:
            links.append(index_url + href.lstrip("/"))

    # de-dup while keeping order
    seen = set()
    out = []
    for x in links:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def extract_bulletin_no_from_url(url: str) -> Optional[int]:
    """
    Handles patterns like:
    - .../TCB%233_*.pdf
    - .../TCB#3_*.pdf
    - .../TCB3_*.pdf (rare)
    """
    for pat in [r"TCB%23(\d+)", r"TCB#(\d+)", r"TCB\s*(\d+)"]:
        m = re.search(pat, url, flags=re.I)
        if m:
            return int(m.group(1))
    return None


def get_most_recent_pdf(index_url: str) -> Optional[Tuple[str, str]]:
    r = requests.get(index_url, headers=UA, timeout=TIMEOUT)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    pre = soup.find("pre")
    if not pre:
        return None

    latest_dt = None
    latest_href = None
    latest_name = None

    for a in pre.find_all("a", href=True):
        name = a.get_text(strip=True)
        href = a["href"]

        # only PDFs
        if not name.lower().endswith(".pdf") and not href.lower().endswith(".pdf"):
            continue

        # only TCB files (keeps your bot focused)
        # this covers name like "TCB#3_basyang.pdf" and href like "TCB%233_basyang.pdf"
        if not (name.lower().startswith("tcb#") or name.lower().startswith("tcb%23") or href.lower().startswith("tcb")):
            continue

        # Apache puts date/time after the link as text
        tail = (a.next_sibling or "").strip()

        # Find "04-Feb-2026 03:13" inside tail
        m = re.search(r"(\d{2}-[A-Za-z]{3}-\d{4})\s+(\d{2}:\d{2})", tail)
        if not m:
            continue

        date_str, time_str = m.group(1), m.group(2)

        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%d-%b-%Y %H:%M")
        except ValueError:
            continue

        if latest_dt is None or dt > latest_dt:
            latest_dt = dt
            latest_href = href
            latest_name = name  # this is the display name you want

    if not latest_href or not latest_name:
        return None

    if latest_href.startswith("http"):
        pdf_url = latest_href
    else:
        pdf_url = index_url + latest_href.lstrip("/")

    return pdf_url, latest_name

def download_pdf(url: str) -> bytes:
    r = requests.get(url, headers=UA, timeout=TIMEOUT)
    r.raise_for_status()
    return r.content


# --- PDF text ---
def pdf_to_text(pdf_bytes: bytes, max_pages: int = 3) -> str:
    reader = PdfReader(BytesIO(pdf_bytes))
    parts = []
    for page in reader.pages[:max_pages]:
        parts.append(page.extract_text() or "")
    text = "\n".join(parts)
    # normalize whitespace
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# --- Parsing ---
def grab(pattern: str, text: str, flags=0) -> Optional[str]:
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else None


def parse_tcb(text: str) -> Dict[str, Optional[str]]:
    """
    Extracts common TCB fields from PAGASA bulletin PDF text.
    This is built to be "good enough" across typical formats.
    """
    out: Dict[str, Optional[str]] = {
        "bulletin_no": None,
        "storm_name": None,
        "system_type": None,
        "issued_at": None,
        "valid_until": None,
        "headline": None,
        "center": None,
        "intensity": None,
        "movement": None,
        "highest_tcws": None,
    }

    # Bulletin number
    out["bulletin_no"] = grab(r"TROPICAL\s+CYCLONE\s+BULLETIN\s*(?:NR\.?|NO\.?)\s*([0-9]+)", text, re.I)

    # Storm name + type (often near top)
    # examples:
    # Tropical Depression "Basyang"
    # Tropical Storm "X"
    # Typhoon "Y"
    out["system_type"] = grab(r"\b(Tropical\s+Depression|Tropical\s+Storm|Severe\s+Tropical\s+Storm|Typhoon|Super\s+Typhoon)\b", text, re.I)
    out["storm_name"] = grab(r'(?:Tropical\s+Depression|Tropical\s+Storm|Severe\s+Tropical\s+Storm|Typhoon|Super\s+Typhoon)\s+[“"]([^”"]+)[”"]', text, re.I)

    # Issued at + Valid until (formats vary)
    out["issued_at"] = (
        grab(r"Issued\s+at\s*([0-9:]+\s*(?:AM|PM)\s*,?\s*\d{1,2}\s+\w+\s+\d{4})", text, re.I)
        or grab(r"Issued\s+at\s*([0-9:]+\s*(?:AM|PM)\s*,?\s*\d{1,2}\s+\w+\s+\d{4})", text, re.I)
    )
    out["valid_until"] = grab(r"Valid\s+for\s+broadcast\s+until\s+(.*?)(?:\n|$)", text, re.I)

    # Headline: usually a loud all-caps line; try to catch a long uppercase sentence
    out["headline"] = grab(r"\n[“\"]?([A-Z0-9][A-Z0-9 ,.'“”\"\-\(\)]+(?:MINDANAO|VISAYAS|LUZON|PHILIPPINES)[A-Z0-9 ,.'“”\"\-\(\)]*)\n", text)

    # Center / location line
    # Usually starts with "The center of ..."
    out["center"] = grab(r"(The\s+center\s+of.*?)(?:\n•|\n\s*Intensity|\nMaximum\s+sustained|\nPresent\s+Movement|\n$)", text, re.I | re.S)
    if out["center"]:
        out["center"] = re.sub(r"\s+", " ", out["center"]).strip()

    # Intensity line
    out["intensity"] = grab(r"(Maximum\s+sustained\s+winds.*?)(?:\n•|\n\s*Present\s+Movement|\n\s*Movement|\n$)", text, re.I | re.S)
    if out["intensity"]:
        out["intensity"] = re.sub(r"\s+", " ", out["intensity"]).strip()

    # Movement
    out["movement"] = (
        grab(r"Present\s+Movement\s*\n\s*([A-Za-z\- ]+\s+at\s+\d+\s*km/h)", text, re.I)
        or grab(r"\b([A-Za-z\- ]+\s+at\s+\d+\s*km/h)\b", text, re.I)
    )

    # Highest TCWS
    out["highest_tcws"] = grab(r"highest\s+Wind\s+Signal.*?Wind\s+Signal\s+No\.\s*([0-9]+)", text, re.I)
    if out["highest_tcws"]:
        out["highest_tcws"] = f"Signal No. {out['highest_tcws']}"

    return out


def build_summary(parsed: Dict[str, Optional[str]], bulletin_no_fallback: Optional[int] = None) -> str:
    storm = parsed.get("storm_name") or "(storm not found)"
    sys_type = parsed.get("system_type") or "Tropical Cyclone"
    bno = parsed.get("bulletin_no") or (str(bulletin_no_fallback) if bulletin_no_fallback is not None else "?")
    issued = parsed.get("issued_at") or "(issued time not found)"

    lines = [
        f"{storm} | {sys_type} | TCB #{bno}",
        f"Issued: {issued}",
    ]

    if parsed.get("headline"):
        lines.append(f"Headline: {parsed['headline']}")

    if parsed.get("center"):
        lines.append(f"Center: {parsed['center']}")

    if parsed.get("intensity"):
        lines.append(f"Intensity: {parsed['intensity']}")

    if parsed.get("movement"):
        lines.append(f"Movement: {parsed['movement']}")

    if parsed.get("highest_tcws"):
        lines.append(f"Highest TCWS: {parsed['highest_tcws']}")

    if parsed.get("valid_until"):
        lines.append(f"Valid until: {parsed['valid_until']}")

    return "\n".join(lines)


# --- Main ---
def main() -> None:
    state = load_state()

    latest = get_most_recent_pdf(TCB_DIR)
    if not latest:
        print("No bulletin found.")
        return

    latest_url, latest_file = latest
    
    print("Latest TCB:", latest_file)
    print("Link:", latest_url)

    # stop if already processed
    if state.get("last_tcb_file") == latest_file:
        print(f"No new TCB. Latest: {latest_file}")
        return

    # download + parse
    pdf_bytes = download_pdf(latest_url)
    text = pdf_to_text(pdf_bytes, max_pages=3)

    if len(text) < 50:
        print("PDF text extraction failed (might be image-based).")
        print(f"Link: {latest_url}")
    else:
        parsed = parse_tcb(text)
        print(build_summary(parsed))  # no fallback needed anymore
        print(f"Link: {latest_url}")

    # save state
    state["last_tcb_file"] = latest_file
    state["last_tcb_url"] = latest_url
    save_state(state)


if __name__ == "__main__":
    main()
