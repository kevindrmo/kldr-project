import streamlit as st
import pandas as pd
from pathlib import Path

#app is only meant to define navigation between pages
# all work is happening within pages SEPARATELY

# Look @ justinas' commits, what edits he made etc..
# 1 Set up structure --> text as placeholders, HAVE VISION
# Some intro, some exploration and final things to show
# think about how you want to present it in the end --> power point? only showing app? html presentation? maybe an html presentation that accesses my streamlit page?
# dashboard data overview, analysis page ....


# in scripts: data-cleaning before --> only put clean data in the actual app

st.set_page_config("kldr-final-project", page_icon = "📊", layout = "wide")

# within the app ONLY define my pages!

homepage =st.Page("pages/homepage.py",
                title= "Homepage",
                icon="🏠")

briefing_page = st.Page("pages/Briefing.py",
                    icon = "📢")

data_assistant = st.Page("pages/data_assistant.py",
                        title="Data Assistant",
                        icon = "⚙️")
data_page = st.Page("pages/data_overview.py",
                    title="Data Overview",
                    icon="📋")

econinsight_page = st.Page("pages/""EconInsight.py",
                        icon="💡")
econviz_page = st.Page("pages/""EconViz.py",
                    icon= "🔮")

user_pages = [homepage, briefing_page, data_assistant, data_page, econinsight_page, econviz_page]

pg = st.navigation(user_pages, position="sidebar", expanded=True)

pg.run()