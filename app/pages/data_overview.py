from utils.common_imports import *

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
    </style>

    <h1 class="dataoverview-title">Data Overview</h1>
    <p class="dataoverview-subtitle">Visualizing Insights Across Your Dataset</p>
    <p class="dataoverview-tagline">From Raw Numbers to Clear Understanding</p>
""", unsafe_allow_html=True)


ROOT = Path(__file__).parent.parent
df_unctad = pd.read_csv(ROOT/"data"/"UNCTAD_DE_WIDEF.csv")

st.subheader("Raw Dataset:")

st.dataframe(df_unctad)
