import pandas as pd

def generate_insights(df):
    insights = []

    # 1️⃣ Dataset Shape
    rows, cols = df.shape
    insights.append(f"📊 Dataset contains {rows} rows and {cols} columns.")

    # 2️⃣ Missing Values
    total_missing = df.isnull().sum().sum()
    insights.append(f"🧩 Total missing values in dataset: {total_missing}")

    # 3️⃣ Numeric Column Summary
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        means = df[numeric_cols].mean()
        highest_mean_col = means.idxmax()
        insights.append(f"📈 Column with highest average value: {highest_mean_col}")

        variances = df[numeric_cols].var()
        highest_variance_col = variances.idxmax()
        insights.append(f"📊 Column with highest variance: {highest_variance_col}")

    else:
        insights.append("No numeric columns found for statistical insights.")

    return insights
import pandas as pd
