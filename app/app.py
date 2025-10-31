import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Sample Project")

st.header("Hello world!")

st.markdown("Some additional text")

ROOT = Path(__file__).parent
df_disney = pd.read_csv(ROOT/ "data"/ "disney_movies_clean.csv")

st.dataframe(df_disney)