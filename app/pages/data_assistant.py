from utils.common_imports import *

st.markdown("""
    <style>
        .assistant-title {
            font-size: 72px;
            font-weight: 700;
            color: #9B59B6;  /* Amethyst Purple */
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

        .assistant-subtitle {
            font-size: 28px;
            font-weight: 500;
            text-align: center;
            color: #9B59B6;  /* matching glow */
            margin-top: 10px;
            animation: subtitleGlowPurple 3s ease-in-out infinite;
        }

        @keyframes subtitleGlowPurple {
            0%, 100% {
                text-shadow: 0 0 0px rgba(155, 89, 182, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(155, 89, 182, 0.6);
            }
        }

        .assistant-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }
    </style>

    <h1 class="assistant-title">Data Assistant</h1>
    <p class="assistant-subtitle">Interactive Guidance at Your Fingertips</p>
    <p class="assistant-tagline">Ask questions, explore data, and get instant insights</p>
""", unsafe_allow_html=True)