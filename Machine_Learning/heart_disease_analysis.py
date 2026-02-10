# heart_eda_train.py
# Run: python heart_eda_train.py
# If your file name is different, change CSV_PATH below.

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay,
    roc_auc_score, RocCurveDisplay
)

# Path
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "datasets" / "Heart_Disease_Prediction.csv"

# Load
df = pd.read_csv(CSV_PATH)

print("\n--- Shape ---")
print(df.shape)

print("\n--- Columns ---")
print(df.columns.tolist())

print("\n--- Head ---")
print(df.head())

print("\n--- Missing values per column ---")
print(df.isna().sum())

print("\n--- Basic stats (numeric) ---")
print(df.describe())

# ---------- 1) Clean target label ----------
# Your screenshot shows target values like "Presence" / "Absence".
# Adjust these if your CSV uses different spellings/cases.
TARGET_COL = "Heart Disease"

if TARGET_COL not in df.columns:
    raise ValueError(f"Target column '{TARGET_COL}' not found. Columns: {df.columns.tolist()}")

df[TARGET_COL] = (
    df[TARGET_COL]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Map to 1/0
target_map = {
    "presence": 1,
    "absence": 0,
    "1": 1,
    "0": 0
}
df[TARGET_COL] = df[TARGET_COL].map(target_map)

# If mapping failed for some rows, you'll see NaN here
bad = df[df[TARGET_COL].isna()]
if not bad.empty:
    print("\n--- Rows with unmapped target values ---")
    print(bad[[TARGET_COL]].drop_duplicates())
    raise ValueError("Fix target_map to match your file's label values.")

# ---------- 2) Quick visualization ----------
# A) Target balance
counts = df[TARGET_COL].value_counts().sort_index()
plt.figure()
plt.bar(["0 (Absence)", "1 (Presence)"], counts.values)
plt.title("Target class count")
plt.ylabel("Rows")
plt.tight_layout()
plt.show()

# B) Numeric histograms (simple but useful)
numeric_cols_guess = df.select_dtypes(include=[np.number]).columns.tolist()
# Remove target from hist list
numeric_cols_guess = [c for c in numeric_cols_guess if c != TARGET_COL]

df[numeric_cols_guess].hist(bins=20, figsize=(12, 8))
plt.suptitle("Numeric feature distributions")
plt.tight_layout()
plt.show()

# C) Correlation heatmap (matplotlib only)
# For small datasets this is fine. Correlation uses numeric cols.
corr = df[numeric_cols_guess + [TARGET_COL]].corr(numeric_only=True)

plt.figure(figsize=(10, 8))
plt.imshow(corr.values)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
plt.colorbar()
plt.title("Correlation heatmap (numeric)")
plt.tight_layout()
plt.show()

# ---------- 3) Train/test split ----------
X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL].astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y  # keeps class balance similar in train/test
)

# ---------- 4) Preprocessing ----------
# Treat columns with few unique values as categorical (often coded as 0/1/2/3).
# This is a simple heuristic for learning purposes.
categorical_cols = []
numeric_cols = []

for col in X.columns:
    if pd.api.types.is_numeric_dtype(X[col]):
        nunique = X[col].nunique(dropna=True)
        if nunique <= 10:
            categorical_cols.append(col)
        else:
            numeric_cols.append(col)
    else:
        categorical_cols.append(col)

print("\n--- Inferred column types ---")
print("Categorical:", categorical_cols)
print("Numeric:", numeric_cols)

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols),
    ]
)

# ---------- 5) Model ----------
# Logistic Regression is a good first model for classification.
model = LogisticRegression(max_iter=2000)

clf = Pipeline(steps=[
    ("preprocess", preprocess),
    ("model", model),
])

clf.fit(X_train, y_train)

# ---------- 6) Evaluate ----------
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("\n--- Results ---")
print("Accuracy:", round(acc, 4))
print("\nClassification report:")
print(classification_report(y_test, y_pred, digits=4))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Absence(0)", "Presence(1)"])
disp.plot()
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

# ROC-AUC (needs probabilities)
y_proba = clf.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_proba)
print("ROC-AUC:", round(auc, 4))

RocCurveDisplay.from_predictions(y_test, y_proba)
plt.title("ROC Curve")
plt.tight_layout()
plt.show()

# ---------- 7) Inspect feature importance (rough) ----------
# With one-hot encoding, feature names expand. We'll print top weights.
# This is optional but helpful.
try:
    ohe = clf.named_steps["preprocess"].named_transformers_["cat"].named_steps["onehot"]
    cat_feature_names = ohe.get_feature_names_out(categorical_cols)

    feature_names = []
    feature_names.extend(numeric_cols)
    feature_names.extend(cat_feature_names.tolist())

    coefs = clf.named_steps["model"].coef_.ravel()
    weights = pd.Series(coefs, index=feature_names).sort_values()

    print("\n--- Top 10 negative weights (push toward Absence) ---")
    print(weights.head(10))

    print("\n--- Top 10 positive weights (push toward Presence) ---")
    print(weights.tail(10))
except Exception as e:
    print("\nCould not print feature weights:", e)
