import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Conversion Rate Analysis
print("CONVERSION RATE ANALYSIS")

print("\nAverage Conversion Rate:")
print(df["Conversion Rate"].mean())

print("\nMaximum Conversion Rate:")
print(df["Conversion Rate"].max())

print("\nMinimum Conversion Rate:")
print(df["Conversion Rate"].min())

print("\nConversion Rate Statistics:")
print(df["Conversion Rate"].describe())

print("\nAverage Conversion Rate by Traffic Source:")
print(df.groupby("Traffic Source")["Conversion Rate"].mean())

print("\nCONVERSION RATE ANALYSIS COMPLETED!")