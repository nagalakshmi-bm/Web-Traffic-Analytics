# Web Traffic Analytics

## Project Overview
Web Traffic Analytics is a data analysis project that examines website traffic data to understand visitor behaviour, engagement, and conversion patterns.

## Objectives
- Analyze website page views.
- Study session duration and bounce rate.
- Understand traffic sources.
- Examine time spent on pages.
- Analyze previous visits and conversion rates.
- Identify possible visitor drop-off patterns.
- Create visualizations to present insights.

## Technologies Used
- Python
- Pandas
- Matplotlib
- VS Code

## Dataset
The project uses `website_wata.csv`, containing 2,000 records and 7 columns.

The dataset includes:
- Page Views
- Session Duration
- Bounce Rate
- Traffic Source
- Time on Page
- Previous Visits
- Conversion Rate

## Project Structure
```text
Web_Traffic_Analytics/
│
├── dataset/
│   ├── website_wata.csv
│   └── cleaned_website_traffic.csv
│
├── notebooks/
│   ├── step1_load_dataset.py
│   ├── step2_data_inspection.py
│   ├── step3_data_cleaning.py
│   ├── step4_traffic_analysis.py
│   ├── step5_session_analysis.py
│   ├── step6_page_views_analysis.py
│   ├── step7_bounce_rate_analysis.py
│   ├── step8_traffic_source_analysis.py
│   ├── step9_time_on_page_analysis.py
│   ├── step10_previous_visits_analysis.py
│   ├── step11_conversion_rate_analysis.py
│   ├── step12_user_engagement_analysis.py
│   ├── step13_dropoff_analysis.py
│   ├── step14_visualizations.py
│   └── step15_generate_report.py
│
├── visualizations/
│
├── report/
│   └── project_report.pdf
│
└── README.md
```

## Analysis Performed
1. Dataset inspection and cleaning.
2. Page views analysis.
3. Session duration analysis.
4. Bounce rate analysis.
5. Traffic source analysis.
6. Time on page analysis.
7. Previous visits analysis.
8. Conversion rate analysis.
9. User engagement analysis.
10. Drop-off analysis.
11. Data visualization.
12. PDF report generation.

## Project Output
Five visualizations and a PDF project report are generated and stored in their respective folders.

## Limitation
The dataset does not contain individual visitor IDs or page-by-page navigation records. Therefore, exact individual user journeys and exit pages cannot be identified.

## Conclusion
This project demonstrates how Python-based data analysis and visualization can help understand website traffic, visitor engagement, and conversion patterns.