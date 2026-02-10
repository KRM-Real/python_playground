from pathlib import Path
import pandas as pd
import numpy as np

# Path
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "datasets" / "Heart_Disease_Prediction.csv"

# Load
df = pd.read_csv(CSV_PATH)

# Basic inspection
print(df.shape)
print(df.columns)
print(df.head())

# Missing values
print(df.isna().sum())

# Summary statistics
print(df.describe())
