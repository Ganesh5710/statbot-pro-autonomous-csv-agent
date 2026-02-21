import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="StatBot Pro v2", layout="wide")

st.title("📊 StatBot Pro v2 – Intelligent CSV Analyst")

# Memory initialization
if "history" not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader("Upload your CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("📈 Dataset Information")
    st.write("Shape:", df.shape)
    st.write("Columns:", df.columns.tolist())

    st.subheader("📊 Basic Statistics")
    st.write(df.describe())

    st.subheader("📊 Visualization")
    column = st.selectbox("Select column to visualize", df.columns)

    if st.button("Generate Chart"):
        plt.figure()
        if df[column].dtype == "object":
            df[column].value_counts().plot(kind='bar')
        else:
            df[column].plot(kind='hist')
        st.pyplot(plt)

    st.subheader("🧠 Ask a Question")
    query = st.text_input("Example: average of marks")

    if query:
        st.session_state.history.append(query)

        if "average" in query.lower():
            for col in df.select_dtypes(include='number').columns:
                st.write(f"Average of {col}:", df[col].mean())

        elif "max" in query.lower():
            for col in df.select_dtypes(include='number').columns:
                st.write(f"Max of {col}:", df[col].max())

        elif "min" in query.lower():
            for col in df.select_dtypes(include='number').columns:
                st.write(f"Min of {col}:", df[col].min())

        else:
            st.write("Query not recognized. Try average, max, or min.")

    st.subheader("🗂 Conversation History")
    st.write(st.session_state.history)