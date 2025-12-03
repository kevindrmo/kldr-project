from utils.common_imports import *
import streamlit.components.v1 as components

st.markdown("""
    <style>
        .dataoverview-title {
            font-size: 72px;
            font-weight: 700;
            color: #1e90ff;  /* Dodger Blue */
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

        .dataoverview-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #1e90ff;  /* same blue for glow */
            margin-top: 10px;
            animation: subtitleGlowBlue 3s ease-in-out infinite;
        }

        @keyframes subtitleGlowBlue {
            0%, 100% {
                text-shadow: 0 0 0px rgba(30, 144, 255, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(30, 144, 255, 0.6);
            }
        }

        .dataoverview-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }
        
        .section-header {
            font-size: 36px;
            font-weight: 600;
            color: #FAFAFA;
            border-bottom: 2px solid #1e90ff;
            padding-bottom: 10px;
            margin-top: 50px;
            margin-bottom: 20px;
        }
        
        .kpi-box {
            background-color: #16213e;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #333;
            text-align: center;
        }
    </style>

    <h1 class="dataoverview-title">The Data Journey</h1>
    <p class="dataoverview-subtitle">From Raw Inputs to Analytical Gold</p>
    <p class="dataoverview-tagline">Understanding the foundation of my analysis</p>
""", unsafe_allow_html=True)


ROOT = Path(__file__).parent.parent
PATH_RAW_UNCTAD = ROOT/"data"/"UNCTAD_DE_WIDEF.csv"
PATH_RAW_WB = ROOT/"data"/"output"/"world_bank_raw_download_cleaned_controls.csv"
PATH_FINAL_PANEL = ROOT/"data"/"output"/"question1"/"final_panel_for_regression.csv"
PATH_REGIONAL = ROOT/"data"/"output"/"question3"/"df_merged_for_DiD.csv"


df_unctad = pd.read_csv(PATH_RAW_UNCTAD)
df_wb = pd.read_csv(PATH_RAW_WB)
df_panel = pd.read_csv(PATH_FINAL_PANEL)
df_regional = pd.read_csv(PATH_REGIONAL)

st.markdown('<p class="section-header">Step 1: The Raw Ingredients</p>', unsafe_allow_html=True)
st.markdown("My analysis begins by combining two primary sources: detailed digital economy data from **UNCTAD** and key macroeconomic indicators from the **World Bank**.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("UNCTAD Digital Economy Data")
    st.markdown(f"""
    <div class="kpi-box">
        <p style="font-size: 16px; color: #ccc; margin:0;">Rows</p>
        <p style="font-size: 32px; font-weight: bold; color: #1e90ff; margin:0;">{df_unctad.shape[0]:,}</p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("View UNCTAD Raw Data & Columns"):
        st.dataframe(df_unctad.head())
        st.code(f"Columns: {', '.join(df_unctad.columns.tolist())}")

with col2:
    st.subheader("World Bank Macro Data")
    st.markdown(f"""
    <div class="kpi-box">
        <p style="font-size: 16px; color: #ccc; margin:0;">Rows</p>
        <p style="font-size: 32px; font-weight: bold; color: #1e90ff; margin:0;">{df_wb.shape[0]:,}</p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("View World Bank Raw Data & Columns"):
        st.dataframe(df_wb.head())
        st.code(f"Columns: {', '.join(df_wb.columns.tolist())}")

# --- 4. Section 2: The Transformation Process ---
st.markdown('<p class="section-header">Step 2: The Transformation</p>', unsafe_allow_html=True)
st.markdown("Raw data is never analysis-ready. The crucial middle step involves a meticulous process of **cleaning, merging, and feature engineering**. This ensures our models are built on a foundation of quality and consistency.")

# Use an HTML component for a more visually appealing "process flow"
components.html("""
<div style="display: flex; justify-content: space-around; align-items: center; font-family: sans-serif; color: white; margin: 30px 0;">
    
    <!-- Step 1: Cleaning -->
    <div style="text-align: center; max-width: 200px;">
        <div style="font-size: 40px;">🧹</div>
        <div style="font-weight: bold; font-size: 18px; margin-top: 5px;">Clean Data</div>
        <div style="font-size: 14px; color: #1e90ff; font-weight: 500; margin-top: 2px;">(Data Integrity)</div>
        <div style="font-size: 14px; color: #ccc; margin-top: 8px; line-height: 1.3;">Handle missing values, correct data types, and reshape for tidy data.</div>
    </div>
    
    <div style="font-size: 40px; color: #1e90ff; align-self: center;">&rarr;</div>
    
    <!-- Step 2: Merging -->
    <div style="text-align: center; max-width: 200px;">
        <div style="font-size: 40px;">🔗</div>
        <div style="font-weight: bold; font-size: 18px; margin-top: 5px;">Merge Sources</div>
        <div style="font-size: 14px; color: #1e90ff; font-weight: 500; margin-top: 2px;">(Data Consolidation)</div>
        <div style="font-size: 14px; color: #ccc; margin-top: 8px; line-height: 1.3;">Join UNCTAD & World Bank data on country and year to create a unified view.</div>
    </div>
    
    <div style="font-size: 40px; color: #1e90ff; align-self: center;">&rarr;</div>
    
    <!-- Step 3: Engineering -->
    <div style="text-align: center; max-width: 200px;">
        <div style="font-size: 40px;">🛠️</div>
        <div style="font-weight: bold; font-size: 18px; margin-top: 5px;">Engineer Features</div>
        <div style="font-size: 14px; color: #1e90ff; font-weight: 500; margin-top: 2px;">(Econometrics)</div>
        <div style="font-size: 14px; color: #ccc; margin-top: 8px; line-height: 1.3;">Create log transformations, time trends, and interaction terms for modeling.</div>
    </div>

</div>
""", height=250)


# --- 5. Section 3: The Final Products ---
st.markdown('<p class="section-header">Step 3: The Analysis-Ready Datasets</p>', unsafe_allow_html=True)
st.markdown("This transformation process yields the final, clean datasets that power every chart and regression in this dashboard. Each is tailored for a specific analytical question.")

st.subheader("Panel Dataset for Regression Analysis")
st.markdown("This is the primary dataset used for the OLS and Fixed Effects models in **Question 1 & 2**. It's a 'long' format panel dataset, structured for econometric analysis.")
st.markdown(f"""
<div class="kpi-box">
    <p style="font-size: 16px; color: #ccc; margin:0;">Final Rows for Modeling</p>
    <p style="font-size: 32px; font-weight: bold; color: #1e90ff; margin:0;">{df_panel.shape[0]:,}</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Explore the Final Panel Dataset"):
    st.dataframe(df_panel)
    st.markdown("""
    **Key Variables for Analysis:**
    - **`Exports_Digital_Service`**: Volume of digital service exports.
    - **`internet_usage_pct`**: Percentage of population using the internet.
    - **`gdp_per_capita`**: Gross Domestic Product per capita.
    - **`population`**: Total population.
    - **`is_developing`**: Development status classification (1 for developing, 0 for developed).
    """)


st.subheader("Regional Dataset for Growth Analysis")
st.markdown("This dataset is aggregated by region and year, specifically created for the regional growth comparisons in **Question 3 & 4**.")
st.markdown(f"""
<div class="kpi-box">
    <p style="font-size: 16px; color: #ccc; margin:0;">Final Rows for Regional Analysis</p>
    <p style="font-size: 32px; font-weight: bold; color: #1e90ff; margin:0;">{df_regional.shape[0]:,}</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Explore the Regional Dataset"):
    st.dataframe(df_regional)
    st.markdown("""
    **Key Variables for Analysis:**
    - **`region`**: The geographical region for aggregation.
    - **`year`**: The year of observation.
    - **`Exports_Digital_Service`**: Aggregated volume of digital service exports for the region.
    - **`internet_usage_pct`**: Average internet adoption rate for the region.
    - **`time`**: A numeric time trend variable for regression (`year - min(year)`).
    """)