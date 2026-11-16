import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Display dataset columns
print("DATASET COLUMNS:")
print(df.columns.tolist())

# Display first 10 records
print("\nFIRST 10 RECORDS:")
print(df.head(10))

# Display data types
print("\nDATA TYPES:")
print(df.dtypes)

# Display statistical information
print("\nTRAFFIC STATISTICS:")
print(df.describe())

print("\nTRAFFIC ANALYSIS DATA LOADED SUCCESSFULLY!")