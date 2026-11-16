import pandas as pd

# Load original dataset
df = pd.read_csv("dataset/website_wata.csv")

print("ORIGINAL DATASET SHAPE:", df.shape)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with median
numerical_columns = df.select_dtypes(include="number").columns

for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Save cleaned dataset
df.to_csv("dataset/cleaned_website_traffic.csv", index=False)

print("\nCLEANING COMPLETED")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFINAL DATASET SHAPE:", df.shape)

print("\nCleaned dataset saved successfully!")