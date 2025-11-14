import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

st.markdown("""
    <style>
        .homepage-title {
            font-size: 72px;
            font-weight: 700;
            color: #ff8800;  /* Vibrant Orange */
            text-align: center;
            margin: 0;
            line-height: 1.1;
            letter-spacing: -1px;
            animation: fadeSlide 1s ease-out forwards;
        }

        @keyframes fadeSlide {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .homepage-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #ff8800;  /* matching orange glow */
            margin-top: 10px;
            animation: subtitleGlowOrange 3s ease-in-out infinite;
        }

        @keyframes subtitleGlowOrange {
            0%, 100% {
                text-shadow: 0 0 0px rgba(255, 136, 0, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(255, 136, 0, 0.6);
            }
        }

        .homepage-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }
    </style>

    <h1 class="homepage-title">Welcome to MyApp</h1>
    <p class="homepage-subtitle">Discover Insights & Explore Data Effortlessly</p>
    <p class="homepage-tagline">Your gateway to data-driven decisions</p>
""", unsafe_allow_html=True)


st.header("Hello world!")

st.markdown("Some additional text")

ROOT = Path(__file__).parent.parent
df_disney = pd.read_csv(ROOT/"data"/ "disney_movies_clean.csv")

#st.dataframe(df_disney)

# how to organize my code

st.header("Project Intro")

st.header("Data overview")


with st.sidebar:
    user_input_password = st.text_input("Enter your password", width=300)

true_pw = st.secrets["true_password"]





if user_input_password == true_pw:
    st.subheader("This is a secret page")

    col_data, _, col_chart = st.columns((0.8, 0.005, 1))

    with col_data:
        st.subheader("Raw Data")
        st.dataframe(df_disney)

    with col_chart:
        st.subheader("Data Overview")
        st.markdown("Placeholder for chart")