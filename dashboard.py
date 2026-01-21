import streamlit as st
import pandas as pd
# To run, go to the terminal and run:
#   streamlit run dashboard.py
#   or
#   python -m streamlit run dashboard.py

st.title("Water Data Dashboard")
st.header("Spring 2026")
st.subheader("Prof. Greg Reis")

st.divider()

st.sidebar.header("Load Datasets")
file_uploaded=st.sidebar.file_uploader("Upload a file", type=["csv"])
if file_uploaded is not None:
    df = pd.read_csv(file_uploaded)
else:
    df = pd.read_csv("logs/biscayne_bay_water_quality.csv")


tab1, tab2, tab3 = st.tabs(["Raw Data","Charts","Maps"])

with tab1:
    st.subheader("Raw Data")
    st.dataframe(df)
    st.caption("Data collected from an underwater robot by Dr. Greg Reis")

    st.divider()

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())
