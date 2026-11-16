import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

print("USER ENGAGEMENT ANALYSIS")

# Average engagement metrics
print("\nAverage Page Views:")
print(df["Page Views"].mean())

print("\nAverage Session Duration:")
print(df["Session Duration"].mean())

print("\nAverage Time on Page:")
print(df["Time on Page"].mean())

print("\nAverage Bounce Rate:")
print(df["Bounce Rate"].mean())

# Compare engagement by traffic source
print("\nEngagement by Traffic Source:")
print(
    df.groupby("Traffic Source")[
        ["Page Views", "Session Duration", "Time on Page", "Bounce Rate"]
    ].mean()
)

print("\nUSER ENGAGEMENT ANALYSIS COMPLETED!")