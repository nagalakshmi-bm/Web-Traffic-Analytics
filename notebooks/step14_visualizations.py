import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Create visualization folder if it does not exist
os.makedirs("visualizations", exist_ok=True)

# 1. Page Views Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Page Views"], bins=20)
plt.title("Page Views Distribution")
plt.xlabel("Page Views")
plt.ylabel("Number of Visitors")
plt.tight_layout()
plt.savefig("visualizations/page_views_distribution.png")
plt.close()

# 2. Session Duration Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Session Duration"], bins=20)
plt.title("Session Duration Distribution")
plt.xlabel("Session Duration")
plt.ylabel("Number of Visitors")
plt.tight_layout()
plt.savefig("visualizations/session_duration_distribution.png")
plt.close()

# 3. Bounce Rate Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Bounce Rate"], bins=20)
plt.title("Bounce Rate Distribution")
plt.xlabel("Bounce Rate")
plt.ylabel("Number of Visitors")
plt.tight_layout()
plt.savefig("visualizations/bounce_rate_distribution.png")
plt.close()

# 4. Average Conversion Rate by Traffic Source
conversion = df.groupby("Traffic Source")["Conversion Rate"].mean()

plt.figure(figsize=(9, 5))
conversion.plot(kind="bar")
plt.title("Average Conversion Rate by Traffic Source")
plt.xlabel("Traffic Source")
plt.ylabel("Average Conversion Rate")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/conversion_by_traffic_source.png")
plt.close()

# 5. Average Time on Page by Traffic Source
time_page = df.groupby("Traffic Source")["Time on Page"].mean()

plt.figure(figsize=(9, 5))
time_page.plot(kind="bar")
plt.title("Average Time on Page by Traffic Source")
plt.xlabel("Traffic Source")
plt.ylabel("Average Time on Page")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/time_on_page_by_traffic_source.png")
plt.close()

print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("Check the visualizations folder.")