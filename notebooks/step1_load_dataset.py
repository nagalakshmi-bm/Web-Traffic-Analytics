import pandas as pd

# Load website traffic dataset
df = pd.read_csv("dataset/website_wata.csv")

# Display first 5 records
print("FIRST 5 RECORDS:")
print(df.head())

# Display dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())