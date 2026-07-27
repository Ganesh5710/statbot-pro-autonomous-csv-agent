import pandas as pd

def get_correlation_matrix(df, selected_cols=None, method="pearson"):
    numeric_df = df.select_dtypes(include="number")

    if selected_cols:
        numeric_df = numeric_df[selected_cols]

    if numeric_df.shape[1] < 2:
        return None

    return numeric_df.corr(method=method)