import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
ROOT = Path(__file__).parent.parent


st.markdown("""
    <style>
        .briefing-title {
            font-size: 72px;
            font-weight: 700;
            color: #ff8800;
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

        .briefing-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #ff8800;
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

        .briefing-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
            margin-bottom: 40px;
        }

        /* Section divider */
        .section-divider {
            margin: 50px 0;
            border-top: 2px solid #ff8800;
            opacity: 0.3;
        }

        /* Question card styling */
        .question-card {
            background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
            padding: 25px;
            border-radius: 12px;
            border-left: 4px solid #ff8800;
            margin: 15px 0;
        }

        .question-title {
            font-size: 20px;
            font-weight: 600;
            color: #ff8800;
            margin-bottom: 10px;
        }

        .question-description {
            font-size: 16px;
            color: #cccccc;
            line-height: 1.6;
        }

        /* Section header */
        .section-header {
            font-size: 32px;
            font-weight: 700;
            color: #ff8800;
            margin-top: 30px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #ff8800;
        }

        /* Info box */
        .info-box {
            background: rgba(255, 136, 0, 0.1);
            padding: 20px;
            border-left: 4px solid #ff8800;
            border-radius: 8px;
            margin: 20px 0;
        }
    </style>

    <h1 class="briefing-title">Project Briefing</h1>
    <p class="briefing-subtitle">Exploring Digital Economy Transformation</p>
    <p class="briefing-tagline">A data-driven analysis of global digital trade and technology adoption</p>
""", unsafe_allow_html=True)

# Guiding Question

st.markdown(""" The digital economy is reshaping how countries trade, develop, and compete globally.
            This analysis explores the interaction of digital trade, technology adoption and economic development
            using data from the United Nations Conference on Trade and Development (UNCTAD)""")

st.markdown("""
---
### 🌍 Main Question
**How is the digital economy reshaping global trade and development?**

I explore this through 4 key analyses:
1. **Global Digital Trade** - Which countries lead?
2. **Technology Adoption** - How are businesses adapting?
3. **Digital Divide** - Is the gap closing?
4. **Development Impact** - Does it correlate with growth?
""")

# Load clean data
#ROOT = Path(__file__).parent.parent
#df = pd.read_csv(ROOT / "data" / "clean" / "unctad_clean.csv")

col_econinsight, col_econviz = st.columns(2)
# ---------------LEFT COLUMN: ECONINSIGHT ----------------
with col_econinsight:
    st.markdown("""
        <h3 style="color: #ff8800; font-size: 24px; margin-bottom: 20px;">
            💡 EconInsight: Data Analysis
        </h3>
    """, unsafe_allow_html=True)
    st.page_link("pages/EconInsight.py", label="Go to EconInsight")
    st.markdown("""
        <div class="question-card">
            <div class="question-title">🌍 Question 1: Global Digital Trade</div>
            <div class="question-description">
                Which countries lead in digital service exports? 
                How has digital trade evolved over the past decade?
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="question-card">
            <div class="question-title">⚙️ Question 2: Technology Adoption & Trade</div>
            <div class="question-description">
                Is there a relationship between internet adoption and digital service exports? 
                Do countries with higher technology adoption export more digital services?
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <strong>Focus:</strong> Understanding relationships in the data through analysis and correlation
        </div>
    """, unsafe_allow_html=True)

# ----- RIGHT COLUMN: ECONVIZ --------
with col_econviz:
    st.markdown("""
        <h3 style="color: #ff8800; font-size: 24px; margin-bottom: 20px;">
            🔮 EconViz: Visual Storytelling
        </h3>
    """, unsafe_allow_html=True)
    st.page_link("pages/EconINsight.py", label="Go to EconViz")
    
    st.markdown("""
        <div class="question-card">
            <div class="question-title">📡 Question 3: The Digital Divide</div>
            <div class="question-description">
                Is the gap between developed and developing countries closing? 
                How are adoption rates changing over time?
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="question-card">
            <div class="question-title">💡 Question 4: Regional Growth Impact</div>
            <div class="question-description">
                Which regions are leading digital transformation? 
                How are digital service exports growing by region?
            </div>
        </div>
    """, unsafe_allow_html=True)



    st.markdown("""
        <div class="info-box">
            <strong>Focus:</strong> Telling stories through trends and visual comparisons
        </div>
    """, unsafe_allow_html=True)



# Preview Chart
st.subheader("📊 Preview: Top Digital Exporters")
#top_exporters = df.nlargest(10, 'digital_exports')
#fig = px.bar(top_exporters, x='digital_exports', y='country', orientation='h',
color_continuous_scale=['#0f3460', '#ff8800']
#st.plotly_chart(fig, use_container_width=True)

st.markdown("""
---
**👉 Start exploring:** Use the sidebar to navigate to different analyses.
""")
