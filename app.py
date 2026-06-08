import streamlit as st
import sys
import subprocess
import pandas as pd
import plotly.express as px
import os

zagolovok = st.title("COINER")

ticker = st.text_input("Write a ticker (Ex. AAPL)")
st.write("", ticker)

if st.button("Run"):
    # st.write("Loading")
    subprocess.run([sys.executable, "src/ingest_bronze.py", ticker], check=True)
    subprocess.run([sys.executable, "src/transform_silver.py", ticker], check=True)
    subprocess.run([sys.executable, "src/transform_gold.py", ticker], check=True)
    st.success("Success", icon="✅")

if ticker:
    file_path = f"data/silver/{ticker.lower()}_silver.parquet"
    if os.path.exists(file_path):
        df = pd.read_parquet(file_path)
        with st.expander("show the data"):
            st.dataframe(df)
        fig = px.line(df, x="date", y="close")
        st.plotly_chart(fig)