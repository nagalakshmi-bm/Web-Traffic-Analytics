import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Previous Visits Analysis
print("PREVIOUS VISITS ANALYSIS")

print("\nAverage Previous Visits:")
print(df["Previous Visits"].mean())

print("\nMaximum Previous Visits:")
print(df["Previous Visits"].max())

print("\nMinimum Previous Visits:")
print(df["Previous Visits"].min())

print("\nPrevious Visits Statistics:")
print(df["Previous Visits"].describe())

print("\nPREVIOUS VISITS ANALYSIS COMPLETED!")