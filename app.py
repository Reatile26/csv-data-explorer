import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSV Data Explorer", layout="wide")#C
st.title("CSV Data Explorer")#D
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])#E
if uploaded_file is not None:#F
    df = pd.read_csv(uploaded_file)#G
    st.dataframe(df.head(5))#H
    st.metric("Rows", len(df))#I
    column = st.selectbox("Column", options=df.columns.tolist())#J
    filter_enabled = st.checkbox("Enable filter", value=False)#K
    filtered = df.copy()#N
    if filter_enabled:
      choices = sorted(df[column].dropna().astype(str).unique().tolist())#L
      selected = st.multiselect("Values", options=choices, default=choices)#M
      filtered = filtered[filtered[column].astype(str).isin(selected)]#O
    st.dataframe(filtered)#P
    st.metric("Filtered rows", filtered.shape[0])#Q
    counts = filtered[column].fillna("Missing").value_counts().to_frame()#R
    st.bar_chart(counts)#S
    st.download_button("Download CSV", filtered.to_csv(index=False), file_name="filtered.csv", mime="text/csv")#T
    
