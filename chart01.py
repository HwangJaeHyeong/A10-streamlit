import pandas as pd
import streamlit as st

df = pd.read_excel('C:/Users/lg/���꾩떆 �ы쉶臾몄젣 �닿껐.xlsx', index_col = "Unnamed: 0")

st.bar_chart(df)
