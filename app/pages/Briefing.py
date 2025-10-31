from utils.common_imports import *

st.markdown("""
    <style>
        .briefing-title {
            font-size: 72px;
            font-weight: 700;
            color: #FF8C00;  /* Dark Orange */
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
            color: #FF8C00;  /* matching glow */
            margin-top: 10px;
            animation: subtitleGlowOrange 3s ease-in-out infinite;
        }

        @keyframes subtitleGlowOrange {
            0%, 100% {
                text-shadow: 0 0 0px rgba(255, 140, 0, 0);
            }
            50% {
                text-shadow: 0 0 20px rgba(255, 140, 0, 0.6);
            }
        }

        .briefing-tagline {
            font-size: 18px;
            font-weight: 300;
            text-align: center;
            color: #cccccc;
            margin-top: 6px;
        }

        .tidy-link {
            text-align: center;
            display: block;
            margin-top: 20px;
            font-size: 16px;
        }

        .tidy-link a {
            color: #FF8C00;
            font-weight: 500;
            text-decoration: none;
        }

        .tidy-link a:hover {
            text-decoration: underline;
        }
    </style>

    <h1 class="briefing-title">Briefing</h1>
    <p class="briefing-subtitle">Must-Know Data at Your Fingertips</p>
    <p class="briefing-tagline">Clean, tidy, and ready for exploration</p>
    <p class="tidy-link">
        Learn more about <a href="https://r4ds.had.co.nz/tidy-data.html" target="_blank">Tidy Data</a>
    </p>
""", unsafe_allow_html=True)



st.markdown("""
    <p style="text-align:center; font-size:16px; color:#dddddd; max-width:800px; margin:auto; line-height:1.6;">
        Understanding <strong>tidy data</strong> is crucial for working effectively with this app. 
        Tidy data is a standardized way of organizing datasets where each variable forms a column, 
        each observation forms a row, and each type of observational unit forms a table. 
        This structure makes data easier to manipulate, analyze, and visualize, 
        which is essential for exploring economic datasets efficiently. 
        By knowing what tidy data is and why it matters, users can ensure their CSV files 
        are ready for regression analysis, AI-powered interpretation, and all the interactive features of this app.
    </p>
""", unsafe_allow_html=True)

