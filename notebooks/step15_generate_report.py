import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_website_traffic.csv")

# Create report folder
os.makedirs("report", exist_ok=True)

# PDF report location
pdf_path = "report/project_report.pdf"

with PdfPages(pdf_path) as pdf:

    # PAGE 1: Project Overview and Results
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.text(0.1, 0.95, "WEB TRAFFIC ANALYTICS", fontsize=20, weight="bold")
    fig.text(0.1, 0.90, "Project Report", fontsize=15)

    report_text = f"""
PROJECT OVERVIEW

Objective:
To examine website traffic data and understand visitor
behaviour, engagement, and conversion patterns.

DATASET INFORMATION

Total Records: {len(df)}
Total Columns: {len(df.columns)}

ANALYSIS RESULTS

Average Page Views: {df['Page Views'].mean():.2f}
Average Session Duration: {df['Session Duration'].mean():.2f}
Average Bounce Rate: {df['Bounce Rate'].mean():.2f}
Average Time on Page: {df['Time on Page'].mean():.2f}
Average Previous Visits: {df['Previous Visits'].mean():.2f}
Average Conversion Rate: {df['Conversion Rate'].mean():.4f}

ANALYSIS PERFORMED

1. Dataset inspection and cleaning
2. Page views analysis
3. Session duration analysis
4. Bounce rate analysis
5. Traffic source analysis
6. Time on page analysis
7. Previous visits analysis
8. Conversion rate analysis
9. User engagement analysis
10. Drop-off analysis
"""

    fig.text(0.1, 0.82, report_text, fontsize=11, va="top")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

    # Add visualization pages
    graph_files = [
        "page_views_distribution.png",
        "session_duration_distribution.png",
        "bounce_rate_distribution.png",
        "conversion_by_traffic_source.png",
        "time_on_page_by_traffic_source.png"
    ]

    for graph in graph_files:
        graph_path = os.path.join("visualizations", graph)

        image = plt.imread(graph_path)

        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.imshow(image)
        ax.set_title(graph.replace("_", " ").replace(".png", "").title())
        ax.axis("off")

        pdf.savefig(fig)
        plt.close()

    # Final page: Conclusion and limitations
    fig = plt.figure(figsize=(8.27, 11.69))

    conclusion = """
CONCLUSION

This project examined website traffic data to understand
visitor behaviour, engagement, and conversion patterns.

The analysis covered page views, session duration, bounce
rate, traffic sources, time on page, previous visits, and
conversion rates.

The visualizations provide insights into traffic patterns
and engagement metrics that can help guide website
improvement decisions.

LIMITATIONS

The dataset does not contain individual visitor IDs,
page-by-page navigation sequences, or exit-page records.
Therefore, exact individual user journeys and exit pages
cannot be reconstructed.

Drop-off analysis uses bounce rate and session duration
as indicators rather than confirmed exit events.

FUTURE IMPROVEMENTS

1. Collect page-level visitor journey data.
2. Track landing pages and exit pages.
3. Improve website engagement.
4. Monitor conversion performance.

PROJECT COMPLETED
"""

    fig.text(0.1, 0.9, conclusion, fontsize=12, va="top")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

print("PROJECT REPORT GENERATED SUCCESSFULLY!")
print("Saved at:", pdf_path)