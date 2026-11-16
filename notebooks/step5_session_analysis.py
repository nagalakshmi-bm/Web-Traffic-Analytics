import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Session Duration Analysis
print("SESSION DURATION ANALYSIS")

print("\nAverage Session Duration:")
print(df["Session Duration"].mean())

print("\nMaximum Session Duration:")
print(df["Session Duration"].max())

print("\nMinimum Session Duration:")
print(df["Session Duration"].min())

print("\nSession Duration Statistics:")
print(df["Session Duration"].describe())

print("\nSESSION ANALYSIS COMPLETED!")