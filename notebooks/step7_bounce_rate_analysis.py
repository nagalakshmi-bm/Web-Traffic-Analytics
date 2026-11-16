import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Bounce Rate Analysis
print("BOUNCE RATE ANALYSIS")

print("\nAverage Bounce Rate:")
print(df["Bounce Rate"].mean())

print("\nMaximum Bounce Rate:")
print(df["Bounce Rate"].max())

print("\nMinimum Bounce Rate:")
print(df["Bounce Rate"].min())

print("\nBounce Rate Statistics:")
print(df["Bounce Rate"].describe())

print("\nBOUNCE RATE ANALYSIS COMPLETED!")
