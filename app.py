import pandas as pd
import streamlit as st

st.write("Hello world")

df = pd.read_excel('./assets/chart01.xlsx', index_col = "Unnamed: 0")

st.bar_chart(df)
