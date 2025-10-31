from utils.common_imports import *

st.markdown("""
    <style>
        .econinsight-title {
            font-size: 72px;
            font-weight: 700;
            color: #ffffff;
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

        .econinsight-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #16c784;
            margin-top: 10px;
            animation: subtitleGlow 3s ease-in-out infinite;
        }

        @keyframes subtitleGlow {
            0%, 100% {
                text-shadow: 0 0 0px rgba(22, 199, 132, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(22, 199, 132, 0.5);
            }
        }

        .econinsight-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }
    </style>

    <h1 class="econinsight-title">EconInsight</h1>
    <p class="econinsight-subtitle">Democratizing Econometric Analysis</p>
    <p class="econinsight-tagline">AI-Powered Data Understanding</p>
""", unsafe_allow_html=True)


