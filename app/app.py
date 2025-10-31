import streamlit as st
import pandas as pd

st.title("Sample Project")

st.header("Hello world!")

st.markdown("Some additional text")


df_disney = pd.read_csv("app/data/disney_movies_clean.csv")

st.dataframe(df_disney)