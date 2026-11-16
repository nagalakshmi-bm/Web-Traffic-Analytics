import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Traffic Source Analysis
print("TRAFFIC SOURCE ANALYSIS")

print("\nNumber of Visits by Traffic Source:")
print(df["Traffic Source"].value_counts())

print("\nAverage Page Views by Traffic Source:")
print(df.groupby("Traffic Source")["Page Views"].mean())

print("\nAverage Session Duration by Traffic Source:")
print(df.groupby("Traffic Source")["Session Duration"].mean())

print("\nAverage Conversion Rate by Traffic Source:")
print(df.groupby("Traffic Source")["Conversion Rate"].mean())

print("\nTRAFFIC SOURCE ANALYSIS COMPLETED!")