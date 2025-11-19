# import all relevant libraries --> can't use utils since it is a jupyter notebook
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

ROOT = Path(__file__).parent.parent/"app"

df_raw = pd.read_csv(ROOT/"data"/ "UNCTAD_DE_WIDEF.csv")

df = df_raw.copy()

df.info()