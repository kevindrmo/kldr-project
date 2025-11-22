from utils.common_imports import *
import plotly.express as px
import plotly.graph_objects as go

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


st.title("Question 1: Global Digital Trade")
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