import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Page Views Analysis
print("PAGE VIEWS ANALYSIS")

print("\nTotal Page Views:")
print(df["Page Views"].sum())

print("\nAverage Page Views:")
print(df["Page Views"].mean())

print("\nMaximum Page Views:")
print(df["Page Views"].max())

print("\nMinimum Page Views:")
print(df["Page Views"].min())

print("\nPage Views Statistics:")
print(df["Page Views"].describe())

print("\nPAGE VIEWS ANALYSIS COMPLETED!")