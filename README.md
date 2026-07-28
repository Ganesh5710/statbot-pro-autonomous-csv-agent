# 🚀 StatBot Pro – Autonomous CSV Analysis Agent

**StatBot Pro** is an intelligent web-based CSV data analysis application built using Streamlit. It performs automated statistical analysis, correlation detection, KPI calculation, outlier detection, and generates downloadable analytical reports.

🌐 **Live Demo:** [statbot-pro.streamlit.app]                                                                                                                                           (https://statbot-pro.streamlit.app/)

---

## 📌 Project Overview

StatBot Pro acts as an autonomous data analysis agent designed to streamline data exploration.

* **CSV Upload & Data Preview:** Upload any dataset and instantly preview tabular data.
* **Automated Statistical Summaries:** Get quick descriptive statistics ($mean, median, std, quartiles$).
* **Correlation Analysis:** Automatically identify and visualize relationships between variables.
* **KPI & Outlier Engine:** Detect key metrics and flag statistical anomalies.
* **Insight Generation Engine:** Translate raw data patterns into plain-English insights.
* **PDF Report Export:** Download formatted, executive-ready analytical reports.

---

## 👥 Team Work Distribution

StatBot Pro was designed, built, and deployed collaboratively by a team of 3 developers:

Janardhan P — *Core Engine & Data Analytics Lead*
* **Core Analytics Modules (`core/analyzer.py`, `core/correlation_analysis.py`):** Developed descriptive statistics summary pipelines and heatmap correlation generation.
* **KPI & Outlier Engine (`core/kpi_calculator.py`, `core/outlier_detection.py`):** Implemented statistical outlier detection algorithms ($IQR / Z\text{-score}$) and quantitative KPI calculation logic.
* **Insight Engine (`core/insight_engine.py`):** Built automated natural language summaries based on processed statistical outputs.

Ganesh B — *Frontend & Dashboard Engineer*
* **Streamlit UI Layout (`app.py`):** Structured the primary user interface, app theme, navigation flow, and session state memory handling.
* **Filtering Engine (`dashboard/filters.py`):** Designed branch-wise and brand-wise interactive dataset filtering components.
* **Visual Interfaces:** Configured visual chart layouts, dynamic table previews, and interactive dataset views.

Chinni krishna K  — *PDF Engine & Deployment Specialist*
* **PDF Generation (`core/pdf_report.py`):** Built the automated PDF export engine using **ReportLab**, formatting statistics, visual charts, and generated insights into downloadable reports.
* **Architecture & Dependencies:** Organized modular directory structures (`core/`, `dashboard/`) and optimized `requirements.txt` configurations.
* **Git, GitHub & Deployment:** Managed version control workflows, set up the GitHub repo, and handled live production deployment via **Streamlit Community Cloud**.

---

## 🗓 Development Journey (4-Week Timeline)
| **Week 1** | Built statistical summary functions & raw data parser. | Designed initial UI layout and file uploader setup. | Organized directory structure, setup Git repo & `requirements.txt`. |
| **Week 2** | Built correlation matrix & KPI extraction engine. | Designed dynamic filters (`dashboard/filters.py`) and data preview components. | Built initial PDF layout structure & modularized core functions. |
| **Week 3** | Developed outlier detection algorithms ($IQR$ method). | Integrated branch/brand filters with the main Streamlit dashboard. | Integrated analytics outputs into dynamic ReportLab PDF exports. |
| **Week 4** | Tested analytics engine across complex datasets. | Polished UI/UX, metrics styling, and responsive layout elements. | Deployed app to Streamlit Cloud, resolved dependencies, and published live app. |

---

## 🏗 Modular Architecture

```text
statbot-pro/
│
├── app.py                      # Main Streamlit UI Entrypoint
├── core/
│   ├── analyzer.py             # Core Data Parsing & Summary
│   ├── correlation_analysis.py # Heatmap & Correlation Processing
│   ├── kpi_calculator.py       # Metrics & KPI Calculations
│   ├── insight_engine.py       # Automated Natural Language Insights
│   ├── outlier_detection.py    # IQR & Z-score Anomaly Detection
│   └── pdf_report.py           # ReportLab PDF Generation Script
│
├── dashboard/
│   └── filters.py              # Brand & Branch Filtering Controls
│
├── requirements.txt            # Python Package Dependencies
└── README.md                   # Project Documentation

👨‍💻 Developer

Ganesh B(Frontend & Dashboard Engineer)
Janardhan P(Core Engine & Data Analytics Lead)
Chinni Krishna K(PDF Engine & Deployment Specialist)
Autonomous Data Analysis System Developer
GitHub: https://github.com/Ganesh5710

⭐ Final Status

StatBot Pro is successfully:

✔ Developed
✔ Modularized
✔ Version Controlled
✔ Deployed
✔ Live & Public
