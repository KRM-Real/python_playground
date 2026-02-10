import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch page")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Example: get the page title
title = soup.find("h1")

if title:
    print("Page title:", title.text.strip())
else:
    print("No title found")
