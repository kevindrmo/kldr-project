from utils.common_imports import *

st.markdown("""
    <style>
        .must-know-title {
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

        .must-know-subtitle {
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

        .must-know-tagline {
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

    <h1 class="must-know-title">Must-Know</h1>
    <p class="must-know-subtitle">Must-Know Data at Your Fingertips</p>
    <p class="must-know-tagline">Clean, tidy, and ready for exploration</p>
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

st.markdown("""
    <style>
        .rule-card {
            background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
            padding: 30px;
            border-radius: 12px;
            border-left: 4px solid #ff8800;
            margin: 20px 0;
        }
        
        .rule-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }
        
        .rule-title {
            font-size: 22px;
            font-weight: 700;
            color: #ff8800;
            margin-bottom: 15px;
        }
        
        .rule-description {
            font-size: 16px;
            color: #cccccc;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .example-label {
            font-weight: 600;
            color: #ff8800;
            margin-top: 15px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Rule 1
st.markdown("""
    <div class="rule-card">
        <div class="rule-icon">📊</div>
        <div class="rule-title">Rule 1: Each Variable Forms a Column</div>
        <div class="rule-description">
            Each column should represent ONE variable (characteristic or measurement).
            For example: name, age, salary, department - each gets its own column.
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**❌ MESSY:**")
    messy_data = pd.DataFrame({
        "Person": ["Alice", "Bob"],
        "Age_Name": ["25 Alice", "30 Bob"],
        "Salary_Dept": ["50k HR", "60k IT"]
    })
    st.dataframe(messy_data, use_container_width=True)

with col2:
    st.markdown("**✅ TIDY:**")
    tidy_data = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Age": [25, 30],
        "Salary": ["50k", "60k"],
        "Department": ["HR", "IT"]
    })
    st.dataframe(tidy_data, use_container_width=True)

st.markdown("""
**Why it matters:** Makes it easy to analyze each variable independently.
""")

st.markdown("---")

# Rule 2
st.markdown("""
    <div class="rule-card">
        <div class="rule-icon">📈</div>
        <div class="rule-title">Rule 2: Each Observation Forms a Row</div>
        <div class="rule-description">
            Each row should represent ONE observation (one unit of analysis).
            For example: one person, one movie, one transaction - each gets its own row.
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**❌ MESSY:**")
    messy_obs = pd.DataFrame({
        "Movie": ["Avatar", "Titanic"],
        "Ratings": ["8.0, 7.9, 8.1", "7.2, 7.3, 7.1"]
    })
    st.dataframe(messy_obs, use_container_width=True)

with col2:
    st.markdown("**✅ TIDY:**")
    tidy_obs = pd.DataFrame({
        "Movie": ["Avatar", "Avatar", "Avatar", "Titanic", "Titanic", "Titanic"],
        "Rating": [8.0, 7.9, 8.1, 7.2, 7.3, 7.1]
    })
    st.dataframe(tidy_obs, use_container_width=True)

st.markdown("""
**Why it matters:** Makes filtering, grouping, and statistical analysis straightforward.
""")

st.markdown("---")

# Rule 3
st.markdown("""
    <div class="rule-card">
        <div class="rule-icon">📋</div>
        <div class="rule-title">Rule 3: Each Type of Observational Unit Forms a Table</div>
        <div class="rule-description">
            If you have different types of entities (movies, directors, genres), 
            they should be in SEPARATE tables, not mixed in one table.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("**❌ MESSY (Different units in one table):**")
messy_units = pd.DataFrame({
    "Movie": ["Avatar", "Avatar", "Titanic"],
    "Director": ["James Cameron", "James Cameron", "James Cameron"],
    "Director_Born": [1954, 1954, 1954],
    "Genre": ["Sci-Fi", "Sci-Fi", "Drama"]
})
st.dataframe(messy_units, use_container_width=True)
st.warning("⚠️ Problem: Director info is repeated for every movie!")

st.markdown("**✅ TIDY (Separate tables for different units):**")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Movies Table:**")
    tidy_movies = pd.DataFrame({
        "Movie_ID": [1, 2],
        "Movie": ["Avatar", "Titanic"],
        "Director_ID": [1, 1]
    })
    st.dataframe(tidy_movies, use_container_width=True)

with col2:
    st.markdown("**Directors Table:**")
    tidy_directors = pd.DataFrame({
        "Director_ID": [1],
        "Director": ["James Cameron"],
        "Born": [1954]
    })
    st.dataframe(tidy_directors, use_container_width=True)

st.markdown("""
**Why it matters:** Reduces redundancy and makes relationships clear.
""")

st.markdown("---")

# Summary
st.markdown("""
### 🎯 Summary: The 3 Rules of Tidy Data

| Rule | Meaning | Why It Matters |
|------|---------|----------------|
| **Variables as Columns** | Each column = one variable | Easy to analyze each variable |
| **Observations as Rows** | Each row = one observation | Enables filtering & statistics |
| **Types in Tables** | Different entities = separate tables | Reduces redundancy |

**Result:** Clean, organized data that's ready for analysis, visualization, and AI interpretation!
""")
st.markdown("""
---
## Methodology: Appliance of the rules on a Dataset
### 🧰 A simple example for Data-cleansing and applying the tidy-data concept
#### 💾 1 Raw Dataset:
            """)

ROOT  = Path(__file__).parent.parent

df_disney_raw = pd.read_csv(ROOT/"data"/ "disney_movies_clean.csv")

st.dataframe(df_disney_raw.head(20))

st.markdown("""
However with this unorganized dataset, we're not quite able to do something with it 
either is it interpreting or to do some calculation with it, we have alter its structure in order do get some more insght
            """)

st.markdown("""
#### 🔍 2 Inspecting the Dataset:
        - Using .describe() gives us the variables --> since columns are """)


