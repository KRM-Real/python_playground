# %% Imports
import pandas as pd
import numpy as np

# %% Load data
df = pd.read_csv("datasets/Heart_Disease_Prediction.csv")
df.head()

# %% EDA
df.describe()

# %% Plot
import matplotlib.pyplot as plt
plt.hist(df["Cholesterol"], bins=20)
plt.show()

# %%
