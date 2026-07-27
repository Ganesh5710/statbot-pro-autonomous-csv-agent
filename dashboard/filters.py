import streamlit as st
import pandas as pd

def apply_filters(df):
    filtered_df = df.copy()

    st.sidebar.header("🔎 Filter Data")

    for col in df.columns:
        if df[col].dtype == "object":
            unique_values = df[col].dropna().unique()
            selected_values = st.sidebar.multiselect(
                f"Select {col}",
                options=unique_values,
                default=unique_values
            )
            filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

        elif df[col].dtype in ["int64", "float64"]:
            min_val = float(df[col].min())
            max_val = float(df[col].max())

            selected_range = st.sidebar.slider(
                f"Select range for {col}",
                min_val,
                max_val,
                (min_val, max_val)
            )
            filtered_df = filtered_df[
                (filtered_df[col] >= selected_range[0]) &
                (filtered_df[col] <= selected_range[1])
            ]

    return filtered_df