import streamlit as st
# To run, go to the terminal and run: streamlit run dashboard.py

st.title("Water Data Dashboard")
st.header("Spring 2026")
st.subheader("Prof. Greg Reis")

st.divider()

tab1, tab2, tab3 = st.tabs(["Raw Data","Charts","Maps"])