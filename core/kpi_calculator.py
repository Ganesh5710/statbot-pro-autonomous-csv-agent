import pandas as pd

def calculate_kpis(df):
    kpis = {}

    # Total rows & columns
    kpis["Total Rows"] = df.shape[0]
    kpis["Total Columns"] = df.shape[1]

    # Numeric columns
    numeric_cols = df.select_dtypes(include="number").columns
    kpis["Numeric Columns"] = len(numeric_cols)

    # Highest mean column (if numeric exists)
    if len(numeric_cols) > 0:
        means = df[numeric_cols].mean()
        highest_mean_col = means.idxmax()
        kpis["Highest Avg Column"] = highest_mean_col
    else:
        kpis["Highest Avg Column"] = "N/A"

    return kpis