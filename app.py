import streamlit as st
import pandas as pd
import os

# Title
st.title("📘 LeetCode Company-Wise All-Time Questions")

# Path to data folder
DATA_DIR = "data"

# Find all *_alltime.csv files
csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith("_alltime.csv")]

# Map file names to company names
company_map = {
    f.replace("_alltime.csv", "").capitalize(): os.path.join(DATA_DIR, f)
    for f in csv_files
}

# Dropdown
selected_company = st.selectbox("Select a company", sorted(company_map.keys()))

# Load and show data
if selected_company:
    df = pd.read_csv(company_map[selected_company])

    # If there are unnamed columns or missing headers, fix that
    if df.columns[0].lower().startswith("unnamed") or df.columns[0] == '':
        df.columns = ['ID', 'Title', 'Frequency']

    st.subheader(f"📋 {selected_company} - All Time Questions")
    st.dataframe(df)
