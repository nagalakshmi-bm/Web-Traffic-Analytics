import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Time on Page Analysis
print("TIME ON PAGE ANALYSIS")

print("\nAverage Time on Page:")
print(df["Time on Page"].mean())

print("\nMaximum Time on Page:")
print(df["Time on Page"].max())

print("\nMinimum Time on Page:")
print(df["Time on Page"].min())

print("\nTime on Page Statistics:")
print(df["Time on Page"].describe())

print("\nTIME ON PAGE ANALYSIS COMPLETED!")