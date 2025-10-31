import streamlit as st
import pandas as pd
from pathlib import Path

#app is only meant to define navigation between pages
# all work is happening within pages SEPARATELY

st.set_page_config("kldr-final-project", page_icon = "📊", layout = "wide")

# within the app ONLY define my pages!

homepage =st.Page("pages/homepage.py", title= "Homepage")

data_page = st.Page("pages/data_overview.py")

user_pages = [homepage, data_page]

pg = st.navigation(user_pages, position="sidebar", expanded=True)

pg.run()