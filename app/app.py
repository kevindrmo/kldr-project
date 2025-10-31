import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config("kldr-final-project", page_icon = "📊", layout = "wide")

st.title("Sample Project")

st.header("Hello world!")

st.markdown("Some additional text")

ROOT = Path(__file__).parent
df_disney = pd.read_csv(ROOT/ "data"/ "disney_movies_clean.csv")

st.dataframe(df_disney)

# how to organize my code

st.header("Project Intro")

st.header("Data overview")


with st.sidebar:
    user_input_password = st.text_input("Enter your password", width=300)

true_pw = st.secrets["true_password"]



st.header(user_input_password) # now we return the password

if user_input_password == true_pw:
    st.subheader("This is a secret page")

    col_data, _, col_chart = st.columns((0.8, 0.005, 1))

    with col_data:
        st.subheader("Raw Data")
        st.dataframe(df_disney)

    with col_chart:
        st.subheader("Data Overview")
        st.markdown("Placeholder for chart")