from utils.common_imports import *
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import statsmodels.api as sm

IN_QUESTION1 = ROOT/"data"/"output"/"question1" # ROOT has already app in it

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

tab1, tab2 = st.tabs([
    "Q1: Global Leaders Analysis", 
    "Q2: Adoption vs. Exports Analysis", 
])

with tab1:
    st.title("🌍 Question 1: Global Digital Trade")
    st.subheader("Which countries lead in digital service exports?")


    st.subheader("Digital Export and Import Visualitzion")


    df_exports_imports = pd.read_csv(IN_QUESTION1/ "df_exports_imports.csv")
    df_final_country_data = pd.read_csv(IN_QUESTION1/ "final_country_data.csv")


    st.write("---")

    st.header("Dashboard Controls")

    control_col1, control_col2, control_col3 = st.columns([1, 2, 3])

    with control_col1:
        indicator_choice = st.selectbox(
        "Select an Indicator to Display:",
        df_final_country_data["indicator_name"].unique()
    )

    with control_col2:
        year_choice = st.slider(
            "Select Year:",
            min_value= int(df_final_country_data["year"].min()),
            max_value= int(df_final_country_data["year"].max()),
            value= int(df_final_country_data["year"].min()) # default value
        )

    with control_col3:
        top_n_choice = st.slider("Select the number of Top N countries to display:",
                                    min_value= 5,
                                    max_value = 50, 
                                    value =10, # default value
                                    step = 5)

    # Filter Dataframe to user's choice

    #df_fitlered = df_exports_imports[df_exports_imports["indicator_name"] == indicator_choice].copy()

    #df_top_n = df_fitlered.sort_values("value", ascending = False).groupby("year").head(top_n_choice)

    df_filtered = df_final_country_data[
        (df_final_country_data["indicator_name"] == indicator_choice) &
        (df_final_country_data["year"] == year_choice)
    ].copy()

    df_top_n = df_filtered[df_filtered["rank"] <= top_n_choice]
    # --- COLOR SYNCHRONIZATION SETUP ---
    COLOR_SCALE = px.colors.sequential.Plasma
    cmin = df_top_n['value_true'].min()
    cmax = df_top_n['value_true'].max()


    st.write("---")

    map_col, rank_col = st.columns([3, 1.5])

    with map_col:
        st.subheader(f"Top {top_n_choice} {indicator_choice.replace('_', ' ')} Countries in {year_choice}")

        fig = go.Figure()

        # Layer 1: Base map of all countries in a neutral gray
        fig.add_trace(go.Choropleth(
            locations=df_filtered['country_code'],
            z=[0] * len(df_filtered),
            colorscale=[[0, '#EAEAEA'], [1, '#EAEAEA']],
            showscale=False,
            hoverinfo='none'
        ))

        # Layer 2: Colored Top N countries
        fig.add_trace(go.Choropleth(
            locations=df_top_n['country_code'],
            z=df_top_n['value_true'],
            colorscale="Plasma",
            colorbar_title='Value (USD)',
            customdata=df_top_n[['rank', 'value_formatted']],
            hovertext=df_top_n['country_name'],
            # --- CORRECTED HOVERTEMPLATE ---
            hovertemplate="""<b>%{hovertext}</b>  
        

                            Rank: %{customdata[0]}  

                            Value: %{customdata[1]}
                            <extra></extra>"""
        ))

        fig.update_layout(
            height=600,
            margin={"r":0, "t":40, "l":0, "b":0},
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='natural earth'
            ),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig, use_container_width=True)

    with rank_col:
        st.subheader(f"Ranking for {year_choice}")

        # --- Prepare data and colors ---
        ranking_df = df_top_n.sort_values('rank', ascending=True)
        from plotly.colors import sample_colorscale
        if cmax > cmin:
            colors = sample_colorscale(COLOR_SCALE, [(n - cmin) / (cmax - cmin) for n in ranking_df['value_true']])
        else:
            colors = [px.colors.sequential.Plasma[0]] * len(ranking_df)

        # --- NEW: Multi-column logic ---
        wrap_at = 25
        if len(ranking_df) > wrap_at:
            rank_col1, rank_col2 = st.columns(2)
            dfs_to_render = [ranking_df.iloc[:wrap_at], ranking_df.iloc[wrap_at:]]
            cols_to_render_in = [rank_col1, rank_col2]
        else:
            dfs_to_render = [ranking_df]
            cols_to_render_in = [rank_col]

        # --- Loop through the columns and render the data ---
        for i, col in enumerate(cols_to_render_in):
            with col:
                df_slice = dfs_to_render[i]
                
                # Add the connecting "subway line" for this column
                col.markdown("""
                <style> .metro-line { position: absolute; left: 33px; top: 0; bottom: 0; width: 4px; background-color: #444; z-index: -1; } </style>
                <div class="metro-line"></div>
                """, unsafe_allow_html=True)

                for j, row in enumerate(df_slice.itertuples()):
                    rank = int(row.rank)
                    country_name = row.country_name
                    value_display = row.value_formatted_display
                    
                    # Find the original index to get the correct color
                    original_index = ranking_df.index.get_loc(row.Index)
                    bar_color = colors[original_index]

                    # --- FINAL FIX: Use a single HTML table for robust layout ---
                    st.markdown(f"""
                    <div style="display: flex; align-items: center; margin-bottom: 8px;">
                        <!-- Rank Circle -->
                        <div style="width: 35px; height: 35px; border-radius: 50%; background-color: {bar_color}; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px; text-shadow: 1px 1px 2px #333; border: 2px solid white; flex-shrink: 0;">
                            {rank}
                        </div>
                        <!-- Country and Value Text -->
                        <div style="margin-left: 10px; flex-grow: 1;">
                            <div style="font-weight: bold; color: #ECEFF4; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{country_name}</div>
                            <div style="font-size: 12px; color: #88C0D0;">{value_display}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


    st.write("---")
    st.subheader("How has digital trade evolved over the past decade?")


    st.write("---")
    st.header("Evolution of Digital Trade Over Time")
    st.subheader("Select countries to compare their trade evolution from 2010-2023.")

    # --- Step 1: Create a multiselect widget for countries ---
    # Get a sorted list of unique country names for the dropdown
    all_countries = sorted(df_final_country_data['country_name'].unique())

    # Set some interesting default countries to show on first load
    default_countries = ['United States', 'United Kingdom', 'China', 'India', 'Germany']

    selected_countries = st.multiselect(
        "Select countries to compare:",
        options=all_countries,
        default=default_countries
    )

    # --- Step 2: Filter the data for the selected countries and indicator ---
    if selected_countries: # Only proceed if the user has selected at least one country
        evolution_df = df_final_country_data[
            (df_final_country_data['country_name'].isin(selected_countries)) &
            (df_final_country_data['indicator_name'] == indicator_choice) # Reuse the indicator choice from above!
        ]

        # --- Step 3: Create the line chart ---
        fig_line = px.line(
            evolution_df,
            x='year',
            y='value_true',
            color='country_name', # Creates a different line for each country
            title=f"Evolution of {indicator_choice.replace('_', ' ')}",
            labels={
                "year": "Year",
                "value_true": "Trade Value (USD)",
                "country_name": "Country"
            },
            markers=True # Adds dots on each data point for clarity
        )

        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            legend_title_text=''
        )
        
        # Use the smart "Billion/Million" format for the hover text
        # This is the corrected code
        fig_line.update_traces(
            customdata=evolution_df[['value_formatted_display']],
            hovertemplate="""<b>%{data.name}</b>  
        

                            Year: %{x}  

                            Value: %{customdata[0]}
                            <extra></extra>"""
        )


        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Please select at least one country to visualize its evolution.")


    st.header("Bar Chart Race: The Shifting Top 10")

    # We can reuse the df_filtered from the top of your script, but this time for all years
    race_df = df_final_country_data[
        (df_final_country_data['indicator_name'] == indicator_choice) &
        (df_final_country_data['rank'] <= 10) # Only show the Top 10
    ]

    fig_race = px.bar(
        race_df,
        x="value_true",
        y="country_name",
        orientation='h',
        color="country_name",
        animation_frame="year",
        animation_group="country_name",
        text="country_name",
        title=f"Top 10 {indicator_choice.replace('_', ' ')} from 2010-2023",

        labels= {
            "value_true": "Trade Value (USD)",
            "country_name" :"Country"
            }
    )
    # --- ADD THIS SNIPPET TO CONTROL THE SPEED ---

    # The duration is in milliseconds (ms). 
    # 1000ms = 1 second.
    # A good value is between 500ms and 1500ms per frame.
    frame_duration = 1000  # Set the duration for each year's frame (e.g., 1 second)
    transition_duration = 300 # The time it takes to animate between frames (e.g., 0.3 seconds)



    # Improve layout and sort bars for each frame
    fig_race.update_layout(
        yaxis={'categoryorder':'total ascending'},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )


    fig_race.update_traces(texttemplate=None) # Hide text on bars if it's cluttered

    st.plotly_chart(fig_race, use_container_width=True)




with tab2:
    st.title("⚙️ Question 2: Technology Adoption & Trade")

    st.write("---")


    st.header("Is there a relationship between internet adoption and digital service exports? ")

    st.subheader("Baseline OLS Model Results")
    st.subheader("Econometric Analysis: The Impact of Digital Adoption")
    st.markdown("Here we explore the relationship between a country's digital adoption and its success in exporting digital services, controlling for GDP and population.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Interactive 3D Data Cloud")
        
        # Define the path to your saved HTML file
        plot_path_3d = IN_QUESTION1 / "interactive_3d_plot.html"

        # --- This try/except block is for the 3D PLOT ---
        try:
            with open(plot_path_3d, 'r', encoding='utf-8') as f:
                html_string = f.read()
            components.html(html_string, height=600, scrolling=False)
        except FileNotFoundError:
            st.warning(f"3D plot file not found at {plot_path_3d}. Please run the analysis notebook to generate it.")

        plot_path_3d = IN_QUESTION1 / "interactive_3d_plot.html"

    with col2:
        st.subheader("Baseline OLS Model Results")

        try:
            # --- Re-run the model to get the results object ---
            df = pd.read_csv(IN_QUESTION1/"final_panel_for_regression.csv")
            Y = np.log(df['Exports_Digital_Service'] + 1)
            X = df[['internet_usage_pct', 'gdp_per_capita', 'population']]
            X['log_gdp_per_capita'] = np.log(X['gdp_per_capita'] + 1)
            X['log_population'] = np.log(X['population'] + 1)
            X = X[['internet_usage_pct', 'log_gdp_per_capita', 'log_population']]
            X = sm.add_constant(X)
            model_ols = sm.OLS(Y, X)
            results_ols = model_ols.fit()
            
            # --- Create a Clean DataFrame from the Results ---
            results_df = pd.DataFrame({
                "Variable": results_ols.params.index,
                "Coefficient": results_ols.params.values,
                "Std. Error": results_ols.bse.values,
                "P-value": results_ols.pvalues.values
            })
            
            def get_stars(p_value):
                if p_value < 0.001: return '***'
                elif p_value < 0.01: return '**'
                elif p_value < 0.05: return '*'
                else: return ''
            
            results_df['Significance'] = results_df['P-value'].apply(get_stars)

            # --- Display the Clean Table ---
            st.markdown("##### Key Variable Effects")
            display_df = results_df[['Variable', 'Coefficient', 'Std. Error', 'Significance']].copy()
            display_df = display_df[display_df['Variable'] != 'const']
            
            st.dataframe(
                display_df.style.format({
                    'Coefficient': '{:.4f}',
                    'Std. Error': '{:.4f}',
                }),
                use_container_width=True,
                hide_index=True
            )
            st.caption("Significance levels: *** p<0.001, ** p<0.01, * p<0.05")

            st.write("---")

            # --- Display R-squared and Observations ---
            col_a, col_b = st.columns(2)
            col_a.metric("R-squared", f"{results_ols.rsquared:.3f}")
            col_b.metric("Observations", f"{int(results_ols.nobs)}")

            # --- CORRECTED Expander for Interpretation ---
            with st.expander("How to Interpret These Results"):
                st.markdown("""
                ##### 1. The Model Equation:
                ```
                log(Digital Exports) = β₀ + β₁*(Internet Usage %) + β₂*log(GDP) + β₃*log(Population)
                ```
                This model helps us understand how different factors relate to a country's digital exports.

                ---
                ##### 2. Interpreting the Coefficients:
                *   **`internet_usage_pct` (β₁):** The coefficient is **0.0109**. This means that for each **1 percentage point increase** in a country's internet usage, we expect to see a **1.09% increase** in its digital service exports, holding other factors constant.

                *   **`log_gdp_per_capita` (β₂):** The coefficient is **1.4666**. This is an *elasticity*. For each **1% increase** in GDP per capita, we expect a **1.47% increase** in digital exports.

                *   **`log_population` (β₃):** The coefficient is **1.1576**. This is also an *elasticity*. For each **1% increase** in population, we expect a **1.16% increase** in digital exports.

                ---
                ##### 3. Key Statistics:
                *   **Significance (***):** The stars confirm that all our results are highly statistically significant and not due to random chance.
                *   **R-squared:** Our model explains **63.1%** of the variation in digital service exports.
                """)

            # --- CORRECTED Expander for the Full Raw Output ---
            with st.expander("View Full OLS Summary Table"):
                st.code(str(results_ols.summary()), language='text')

        except FileNotFoundError:
            st.error("The regression data file ('final_panel_for_regression.csv') was not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    # In your EconInsight.py, inside the tab for Question 2

# ... (after the code for the simple OLS results) ...
# In your EconInsight.py, inside the tab for Question 2

# ... (after the code for the simple OLS results) ...

# In your EconInsight.py, inside the tab for Question 2

# ... (after the code for the simple OLS results) ...

# In your EconInsight.py, inside the tab for Question 2

# ... (after the code for the simple OLS results) ...

    st.write("---")

    # --- 1. THE INTERACTIVE "DEBUNKING" SECTION ---
    st.subheader("Debunking the Simple Model: An Interactive Look")
    st.caption("Our first model was a good start, but it has hidden flaws. Let's uncover them.")

    # Create the interactive layout
    col1, col2 = st.columns([1, 1.5])

    # The Demonstration Area (Right Column)
    with col2:
        # Initialize session state
        if 'active_effect' not in st.session_state:
            st.session_state.active_effect = 'none'

        # Display content based on the active effect
        if st.session_state.active_effect == 'country':
            st.info("##### The 'Country Effect' (e.g., DE vs. IN)")
            st.markdown("""
            Imagine Germany and India. Germany has a long history of industrial exports and robust infrastructure. India has a booming software and service industry.

            These unique, deep-seated characteristics (culture, policy, infrastructure) are **constant** for each country over the years.

            A simple OLS model lumps these powerful effects in with everything else, potentially distorting the true impact of variables like internet usage. It can't tell if high exports are due to internet adoption or just because it's 'Germany'.
            """)

        elif st.session_state.active_effect == 'time':
            st.warning("##### The 'Time Effect' (e.g., 2008 vs. 2020)")
            st.markdown("""
            Think about the years 2008 and 2020.

            *   **2008:** The Global Financial Crisis hit, depressing trade worldwide.
            *   **2020:** The COVID-19 pandemic caused a massive, unprecedented surge in demand for remote work and digital services.

            These are global shocks that affect *all* countries at the same time. A simple OLS model might see a jump in exports in 2020 and wrongly give all the credit to a small rise in GDP, ignoring the giant global event.
            """)

        else: # The default state
            st.write("#### Click a button to the left to reveal a hidden flaw in the simple model.")
            st.markdown(
                """
                <div style="
                    border: 2px dashed #444;
                    border-radius: 10px;
                    height: 250px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    color: #666;
                    font-family: sans-serif;
                    padding: 20px;
                ">
                    The evidence will appear here...
                </div>
                """,
                unsafe_allow_html=True
            )

    # The Control Panel (Left Column)
    with col1:
        st.markdown("#### The Problem:")
        st.markdown("A simple regression assumes all data points are independent. But our data has two hidden patterns:")

        # --- THE FIX IS HERE ---
        # Buttons now correctly assign the session state
        if st.button("1. Unseen Country Differences", use_container_width=True):
            st.session_state.active_effect = 'country' # <-- CORRECTED

        if st.button("2. Unseen Global Shocks", use_container_width=True):
            st.session_state.active_effect = 'time' # <-- CORRECTED

        st.markdown("---")
        st.success("**The Solution:** To fix this, we must use **Panel Data Analysis**, a method that controls for these hidden effects.")


    # --- 2. THE DETAILED SCIENTIFIC EXPLANATION ---
    with st.expander("Read the detailed econometric explanation"):
        # ... (The text for the expander remains the same as it was correct) ...
        st.markdown("""
        While our initial OLS model gives us valuable clues, it operates on a major simplifying assumption: it treats each data point (a country in a specific year) as an independent event. This is like assuming that Germany in 2015 has no relationship to Germany in 2016, or that France and Germany are completely dissimilar.

        This assumption is flawed for two main reasons:

        **1. Unobserved Country-Specific Effects:**
        *   Every country is unique. Factors like culture, political systems, historical trade relationships, and geography are deeply embedded and don't change much year to year.
        *   These "hidden" characteristics can influence both digital exports and our predictor variables (like GDP or internet usage).
        *   Simple OLS can't distinguish the effect of our variables from these hidden country-specific traits, leading to a risk of **omitted variable bias** and potentially misleading conclusions.

        **2. Unobserved Time-Specific Effects:**
        *   The world changes. Global events like a financial crisis, a pandemic, or a major technological breakthrough affect *all* countries in a given year.
        *   These global shocks can influence digital trade across the board.
        *   Simple OLS might incorrectly attribute the impact of these global trends to our specific variables.

        > **In short, our current model is likely missing a crucial part of the story.** It cannot properly account for the unique, unchangeable characteristics of each country or the global shocks that affect all countries over time.

        To build a more robust and trustworthy model, we must use a technique designed for this exact type of data: **Panel Data Analysis**. This method allows us to control for both country-specific and time-specific effects, giving us a much clearer and more accurate picture of the true relationships.
        """)







    st.write("---")

    st.header("Do countries with higher technology adoption export more digital services?")
    # In your EconInsight.py file, inside the "Q2" tab

    # ... (after the interactive section and the detailed expander) ...

    st.write("---")
    st.subheader("The Solution: Comparing Panel Data Models")
    st.markdown("""
    Here we present the results from three models. We start with a simple Pooled OLS and progressively add controls to arrive at our most reliable estimate, the **Two-way Fixed Effects (FE)** model.

    Notice how the coefficients and their significance (the numbers in parentheses are t-statistics) change dramatically.
    """)

# In EconInsight.py, after the "Detailed Interpretation" expander

    # --- FINAL EXPANDER: Full Raw Regression Output ---
    with st.expander("View Full Regression Output Table"):
        try:
            # Define the path to the .txt file
            panel_txt_path = ROOT/ "data" / "output" / "question2p_paneldata" / "panel_models_comparison.txt"
            
            # Open and read the text file
            with open(panel_txt_path, "r") as f:
                full_results_text = f.read()
            
            # --- THIS IS THE FIX  ---> We fix it with st.code !! 
            # Use st.code() to guarantee a monospace font and preserve alignment.
            st.code(full_results_text, language='text')

        except FileNotFoundError:
            st.warning("The full regression output file (`panel_models_comparison.txt`) was not found. Please re-run the final cell of the analysis notebook.")


    # --- Add the final interpretation ---
    st.markdown("""
    #### Interpretation of the Two-way Fixed Effects Model:

    This is our most robust model, controlling for both country-specific attributes and global, year-specific shocks. The results are striking:

    1.  **`internet_usage_pct` & `log_gdp_per_capita`:** Both variables are now **statistically insignificant**. This suggests that once we account for the deep-seated characteristics of a country and global trends, the isolated, year-to-year changes in internet use or GDP per capita don't have a strong, independent effect on digital exports in this model. The effect we saw in the simple OLS was likely due to omitted variables.

    2.  **`log_population`:** The effect is now **negative and significant**. This is a fascinating result that warrants further investigation. It could imply that, all else being equal, larger countries have a harder time translating their size into per-capita digital export dominance, but this is just one possible interpretation.

    This analysis shows the immense value of Fixed Effects. It prevents us from drawing simple, and likely wrong, conclusions, pushing us toward a more nuanced and accurate understanding of the data.
    """)





    st.write("---")
    st.subheader("The Coefficient Journey: From Simple to Sophisticated")
    # ... (caption and data loading code is correct) ...

    DATA_PATH = ROOT/ "data" / "output" / "question2p_paneldata"
    plot_df = pd.read_csv(DATA_PATH / "panel_plot_data.csv")
    model_order = ["Standard OLS", "Country FE", "Two-way FE"]
    plot_df['Model_Stage'] = pd.Categorical(plot_df['Model'], categories=model_order, ordered=True)

    fig = px.line(
        plot_df,
        x="Model_Stage",
        y="Coefficient",
        color="Variable",
        markers=True,
        labels={
            "Model_Stage": "Model Specification",
            "Coefficient": "Estimated Coefficient (Effect Size)",
            "Variable": "Explanatory Variable"
        },
        title="<b>The Journey of Coefficients Across Model Specifications</b>"
    )

    # --- Add the Confidence Interval Bands ---
    for i, var in enumerate(plot_df['Variable'].unique()):
        var_df = plot_df[plot_df['Variable'] == var].sort_values('Model_Stage')
        line_color = fig.data[i].line.color # This gives a hex color like '#636EFA'
        
        # --- THIS IS THE DEFINITIVE FIX ---
        # Manually convert the hex color string to an rgba string for the fill color.
        # This removes the need for any special conversion functions.
        hex_color = line_color.lstrip('#')
        rgb_tuple = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        fill_color = f'rgba({rgb_tuple[0]}, {rgb_tuple[1]}, {rgb_tuple[2]}, 0.2)'


        fig.add_traces(go.Scatter(
            x=var_df['Model_Stage'],
            y=var_df['Conf. Upper'],
            fill=None,
            mode='lines',
            line=dict(width=0),
            showlegend=False
        ))
        fig.add_traces(go.Scatter(
            x=var_df['Model_Stage'],
            y=var_df['Conf. Lower'],
            fill='tonexty',
            mode='lines',
            line=dict(width=0),
            fillcolor=fill_color,
            showlegend=False
        ))

    # --- Final Touches (This part is correct) ---
    fig.add_hline(y=0, line_width=2, line_dash="dash", line_color="grey")
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend_title_text=None,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    # Display the plot in your app
    st.plotly_chart(fig, use_container_width=True)




    st.write("---")
    st.subheader("The Coefficient Explorer")
    st.caption("Select a variable to see how its estimated effect changes as we improve our model.")

    # --- Helper function ---
    def get_significance_icon(p_value):
        return "✅" if p_value < 0.05 else "❌"

    # --- Define paths and load data ---
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    DATA_PATH = PROJECT_ROOT / "app" / "data" / "output" / "question2p_paneldata"

    df_ols = pd.read_csv(DATA_PATH / "summary_standard_ols.csv")
    df_fe = pd.read_csv(DATA_PATH / "summary_country_fe.csv")
    df_twfe = pd.read_csv(DATA_PATH / "summary_twfe.csv")

    # --- The Interactive Selectbox ---
    variable_to_explore = st.selectbox(
        "**Explore a variable:**",
        ['internet_usage_pct', 'log_gdp_per_capita', 'log_population'],
        index=0
    )
    st.write("")

    # --- Create the three-column layout ---
    col1, col2, col3 = st.columns(3, gap="large")

    # --- A function to display a model's results for the chosen variable ---
    # --- THE FIX IS HERE: The entire block below is now correctly indented ---
    def display_variable_in_model(column, model_name, model_df):
        with column:
            st.markdown(f"<h5>{model_name}</h5>", unsafe_allow_html=True)

            # Extract the specific variable's data
            var_row = model_df[model_df['Variable'] == variable_to_explore].iloc[0]
            coeff = var_row['Coefficient']
            pval = var_row['P-Value']

            # Display the main coefficient
            st.metric(
                label=f"Coefficient for {variable_to_explore}",
                value=f"{coeff:.4f}",
                help="This is the estimated effect of the variable in this model."
            )

            # Display the significance
            st.markdown(f"**Significant?** {get_significance_icon(pval)} (p-value: {pval:.3f})")

            st.markdown("---")

            # Find and display the model's R-squared
            r_squared_row = model_df[model_df['Variable'].str.contains("R-Squared", na=False)]
            if not r_squared_row.empty:
                r_squared_label = r_squared_row['Variable'].iloc[0]
                r_squared_val = r_squared_row['Coefficient'].iloc[0]
                st.markdown(f"**{r_squared_label}:** `{r_squared_val:.3f}`")
            else:
                st.markdown("**R-Squared:** `Not Found`")

    # --- Populate each column ---
    display_variable_in_model(col1, "Standard OLS", df_ols)
    display_variable_in_model(col2, "Country FE", df_fe)
    display_variable_in_model(col3, "Two-way FE", df_twfe)


    # --- The Detailed Interpretation Expander ---
    with st.expander("See the Detailed Interpretation"):
        st.markdown("""
        #### How to Read This Dashboard:
        By selecting a variable from the dropdown, you can track its journey across the three models. This tells a story about the importance of controlling for hidden variables.

        *   **Standard OLS:** This is our naive starting point. It looks at the raw correlation and often shows strong effects for all variables.
        *   **Country FE (Fixed Effects):** Here, we control for each country's unique, unchanging characteristics. Notice how the effect of some variables shrinks or becomes insignificant.
        *   **Two-way FE (Our Best Model):** Finally, we *also* control for global shocks that affect all countries in a given year. For many variables, the effect becomes insignificant (marked with ❌).

        ---
        **Conclusion:** The initial correlations we saw in the Standard OLS model were likely misleading. After applying robust panel data methods, we find that the story is much more complex. This demonstrates the critical importance of choosing the right econometric model.
        """)
