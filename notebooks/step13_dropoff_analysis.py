import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

print("DROP-OFF ANALYSIS")

# High bounce rate records
high_bounce = df[df["Bounce Rate"] >= df["Bounce Rate"].median()]

print("\nRecords with Bounce Rate at or Above Median:")
print(len(high_bounce))

# Short session records
short_sessions = df[
    df["Session Duration"] <= df["Session Duration"].median()
]

print("\nRecords with Session Duration at or Below Median:")
print(len(short_sessions))

# Average metrics
print("\nAverage Bounce Rate:")
print(df["Bounce Rate"].mean())

print("\nAverage Session Duration:")
print(df["Session Duration"].mean())

print("\nDROP-OFF ANALYSIS COMPLETED!")