import streamlit as st
import sys
import subprocess

zagolovok = st.title("COINER")

ticker = st.text_input("Write a ticker (Ex. AAPL)")
st.write("", ticker)

if st.button("Run"):
    # st.write("Loading")
    subprocess.run([sys.executable, "src/ingest_bronze.py", ticker], check=True)
    subprocess.run([sys.executable, "src/transform_silver.py", ticker], check=True)
    subprocess.run([sys.executable, "src/transform_gold.py", ticker], check=True)
    st.success("Success", icon="✅")

