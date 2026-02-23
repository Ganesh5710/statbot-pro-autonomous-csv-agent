from core.insight_engine import generate_insights
from core.correlation_analysis import get_correlation_matrix
from core.outlier_detection import detect_outliers_for_column
from core.kpi_calculator import calculate_kpis
from dashboard.filters import apply_filters
from core.pdf_report import generate_pdf_report

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="StatBot Pro v4", layout="wide")
st.title("📊 StatBot Pro v4 – AI Data Analytics Dashboard")

# -------------------- SESSION MEMORY --------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("Upload your CSV file")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Apply sidebar filters
    df = apply_filters(df)

    # Create Tabs
    tabs = st.tabs([
        "📊 Overview",
        "📈 Correlation",
        "🚨 Outliers",
        "📊 Visualization",
        "🧠 Ask AI"
    ])

    # ======================================================
    # TAB 1: OVERVIEW
    # ======================================================
    with tabs[0]:

        st.subheader("📊 Key Performance Indicators")

        kpis = calculate_kpis(df)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Rows", kpis["Total Rows"])
        col2.metric("Total Columns", kpis["Total Columns"])
        col3.metric("Numeric Columns", kpis["Numeric Columns"])
        col4.metric("Highest Avg Column", kpis["Highest Avg Column"])

        st.divider()

        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

        st.divider()

        st.subheader("🔎 Automatic Insights")
        insights = generate_insights(df)
        for insight in insights:
            st.write(insight)

        st.divider()

        # -------------------- PDF DOWNLOAD SECTION --------------------
        st.subheader("📥 Download Analytics Report")

        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        if len(numeric_cols) > 0:
            sample_col = numeric_cols[0]
            outliers = detect_outliers_for_column(df, sample_col)
            outlier_summary = f"Column '{sample_col}' has {len(outliers)} outliers."
        else:
            outlier_summary = "No numeric columns available for outlier detection."

        pdf_filename = "statbot_report.pdf"

        if st.button("Generate PDF Report"):

            generate_pdf_report(
                pdf_filename,
                kpis,
                insights,
                outlier_summary
            )

            with open(pdf_filename, "rb") as f:
                st.download_button(
                    label="Download Report",
                    data=f,
                    file_name="StatBot_Report.pdf",
                    mime="application/pdf"
                )

        st.divider()

        # -------------------- CSV DOWNLOAD SECTION --------------------
        st.subheader("📥 Download Filtered Dataset")

        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Filtered CSV",
            data=csv_data,
            file_name="filtered_data.csv",
            mime="text/csv"
        )

    # ======================================================
    # TAB 2: CORRELATION
    # ======================================================
    with tabs[1]:

        st.subheader("📊 Correlation Analysis")

        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        if len(numeric_cols) >= 2:

            selected_corr_cols = st.multiselect(
                "Select Columns for Correlation",
                options=numeric_cols,
                default=numeric_cols
            )

            corr_method = st.selectbox(
                "Select Correlation Method",
                ["pearson", "spearman", "kendall"]
            )

            corr_matrix = get_correlation_matrix(
                df,
                selected_cols=selected_corr_cols,
                method=corr_method
            )

            if corr_matrix is not None:
                fig, ax = plt.subplots()
                sns.heatmap(
                    corr_matrix,
                    annot=True,
                    fmt=".2f",
                    cmap="coolwarm",
                    linewidths=0.5,
                    ax=ax
                )
                st.pyplot(fig)
            else:
                st.warning("Please select at least 2 numeric columns.")
        else:
            st.info("Not enough numeric columns for correlation analysis.")

    # ======================================================
    # TAB 3: OUTLIERS
    # ======================================================
    with tabs[2]:

        st.subheader("🚨 Outlier Detection")

        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        if len(numeric_cols) > 0:

            selected_outlier_col = st.selectbox(
                "Select Column for Outlier Detection",
                numeric_cols
            )

            outliers = detect_outliers_for_column(df, selected_outlier_col)

            st.write(f"Total Outliers in '{selected_outlier_col}': {len(outliers)}")

            if len(outliers) > 0:
                st.dataframe(outliers)
            else:
                st.success("No significant outliers detected.")
        else:
            st.info("No numeric columns available for outlier detection.")

    # ======================================================
    # TAB 4: VISUALIZATION
    # ======================================================
    with tabs[3]:

        st.subheader("📈 Visualization")

        column = st.selectbox("Select column to visualize", df.columns)

        if st.button("Generate Chart"):

            fig, ax = plt.subplots()

            if df[column].dtype == "object":
                df[column].value_counts().plot(kind="bar", ax=ax)
            else:
                df[column].plot(kind="hist", ax=ax)

            st.pyplot(fig)

    # ======================================================
    # TAB 5: ASK AI
    # ======================================================
    with tabs[4]:

        st.subheader("🧠 Ask a Question")

        query = st.text_input("Example: average, max, min")

        if query:

            st.session_state.history.append(query)

            numeric_cols = df.select_dtypes(include='number').columns

            if "average" in query.lower():
                for col in numeric_cols:
                    st.write(f"Average of {col}:", df[col].mean())

            elif "max" in query.lower():
                for col in numeric_cols:
                    st.write(f"Max of {col}:", df[col].max())

            elif "min" in query.lower():
                for col in numeric_cols:
                    st.write(f"Min of {col}:", df[col].min())

            else:
                st.warning("Query not recognized. Try: average, max, or min.")

        st.subheader("🗂 Conversation History")
        st.write(st.session_state.history)

else:
    st.info("Please upload a CSV file to begin analysis.")