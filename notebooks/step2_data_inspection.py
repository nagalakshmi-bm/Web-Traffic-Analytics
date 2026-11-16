import pandas as pd

# Load dataset
df = pd.read_csv("dataset/website_wata.csv")

# 1. Dataset information
print("DATASET INFORMATION:")
print(df.info())

# 2. Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# 3. Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# 4. Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# 5. Dataset dimensions
print("\nDATASET DIMENSIONS:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])