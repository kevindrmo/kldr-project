from utils.common_imports import *

st.markdown("""
    <style>
        .econviz-title {
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

        .econviz-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #e94560;
            margin-top: 10px;
            animation: subtitleGlowRed 3s ease-in-out infinite;
        }

        @keyframes subtitleGlowRed {
            0%, 100% {
                text-shadow: 0 0 0px rgba(233, 69, 96, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(233, 69, 96, 0.6);
            }
        }

        .econviz-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }
    </style>

    <h1 class="econviz-title">EconViz</h1>
    <p class="econviz-subtitle">Transforming Economic Data into Visual Stories</p>
    <p class="econviz-tagline">Where Data Meets Art</p>
""", unsafe_allow_html=True)
