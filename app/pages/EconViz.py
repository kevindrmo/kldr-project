from utils.common_imports import *
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import statsmodels.api as sm
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patheffects as path_effects

IN_QUESTION3 = ROOT/"data"/"output"/"question3"

if "q3_mode" not in st.session_state:
    st.session_state.q3_mode = None

def set_q3_mode(mode):
    st.session_state.q3_mode = mode

def reset_q3_mode():
    st.session_state.q3_mode = None

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


tab1, tab2, tab3 = st.tabs([
    "Q3: The Digital Divide", 
    "Q4: Regional Growth Impact",
    "Summary" 
])


with tab1:
    if st.session_state.q3_mode is None:
        st.markdown("<h3 style='text-align: center; color: white;'>Choose Your Visualization Style</h3><br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2, gap= "large")
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 30px; border: 1px solid #333; border-radius: 15px; background: #16213e; height: 100%;">
                <div style="font-size: 50px; margin-bottom: 10px;">📰</div>
                <h3 style="color: #00FFFF; margin-bottom: 10px;">Journalistic Narrative</h3>
                <p style="color: #ccc; font-size: 16px; min-height: 60px;">A high-end, "Economist-style" data story focusing on the convergence of the digital divide.</p>
                <p style="color: #666; font-size: 14px; font-style: italic;">Best for: Storytelling & Impact</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Launch Journalistic View", key="btn_journalistic", use_container_width=True):
                set_q3_mode("journalistic")
                st.rerun()

        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 30px; border: 1px solid #333; border-radius: 15px; background: #16213e; height: 100%;">
                <div style="font-size: 50px; margin-bottom: 10px;">📊</div>
                <h3 style="color: #FF007F;">Analytical Overview</h3>
                <p style="color: #ccc; font-size: 16px; min-height: 60px;">A clean, standard interactive chart for exploring the raw adoption trends over time.</p>
                <p style="color: #666; font-size: 14px; font-style: italic;">Best for: Data Analysis & KPIs</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Launch Interactive View", key="btn_interactive", use_container_width=True):
                set_q3_mode("interactive")
                st.rerun()
    elif st.session_state.q3_mode == "journalistic":
        st.button("← Back to Selection", on_click=reset_q3_mode, type="secondary")

        st.title("📡 Question 3: The Digital Divide")
        st.subheader("Is the gap between developed and developing countries closing?")
        years = list(range(2010, 2024))
        data = {
            'Year': years,
            'Developed': [65.0, 67.9, 71.1, 73.7, 75.9, 77.9, 80.6, 82.5, 84.3, 85.8, 88.1, 90.5, 91.1, 91.8],
            'Developing': [16.8, 19.4, 22.1, 24.4, 27.6, 30.8, 34.7, 39.1, 43.5, 46.5, 51.6, 57.8, 60.6, 68.9] 
        }
        df_chart = pd.DataFrame(data)

        # --- 2. CALCULATIONS ---
        # Get start and end values
        val_dev_start = df_chart['Developed'].iloc[0]
        val_dev_end = df_chart['Developed'].iloc[-1]
        val_ing_start = df_chart['Developing'].iloc[0]
        val_ing_end = df_chart['Developing'].iloc[-1]

        # Calculate Gaps
        gap_start = val_dev_start - val_ing_start
        gap_end = val_dev_end - val_ing_end

        # Calculate Growth Rates (Percentage Growth)
        growth_rate_dev = (val_dev_end - val_dev_start) / val_dev_start
        growth_rate_ing = (val_ing_end - val_ing_start) / val_ing_start

        # Calculate Ratio
        if growth_rate_dev > 0:
            growth_ratio = growth_rate_ing / growth_rate_dev
        else:
            growth_ratio = 0

        # --- 3. PAGE HEADER STYLING ---
        st.markdown("""
            <style>
            .economist-header-line {
                border-top: 4px solid #E3120B; /* The Economist Red */
                width: 100%;
                margin-bottom: 10px;
            }
            .title-text {
                font-size: 40px;
                font-weight: 900;
                margin-top: 0px;
                margin-bottom: 5px;
            }
            .subtitle-text {
                font-size: 16px;
                color: #B0B0B0;
                margin-bottom: 30px;
                font-style: italic;
            }
            </style>
            <div class="economist-header-line"></div>
            <div class="title-text">The Great Convergence</div>
            <div class="subtitle-text">Global internet adoption rates are harmonizing, though equality remains distant.</div>
            """, unsafe_allow_html=True)

        # --- 4. PLOTLY CHART CREATION ---

        fig = go.Figure()

        # 1. VISUAL ART: "DNA" Ladder Lines
        # Stronger, more distinct lines to mimic the "flow" connectors in your example
        for i in range(len(df_chart)):
            fig.add_shape(
                type="line",
                x0=df_chart['Year'][i], y0=df_chart['Developed'][i],
                x1=df_chart['Year'][i], y1=df_chart['Developing'][i],
                line=dict(color="rgba(255, 255, 255, 0.15)", width=1.5)
            )

        # 2. Main Lines & Markers (Thicker, smoother flow)
        fig.add_trace(go.Scatter(
            x=df_chart['Year'], 
            y=df_chart['Developed'],
            mode='lines',
            name='Developed',
            line=dict(color='#00FFFF', width=4, shape='spline'), # Thicker Neon Cyan
        ))

        fig.add_trace(go.Scatter(
            x=df_chart['Year'], 
            y=df_chart['Developing'],
            mode='lines',
            name='Developing',
            fill='tonexty', 
            fillcolor='rgba(255, 0, 127, 0.08)', # The "River" of the gap
            line=dict(color='#FF007F', width=4, shape='spline'), # Thicker Neon Pink
        ))

        # 3. CONTEXT: Event Lines (Vertical Timeline Markers)
        # Similar to the "Noon", "1 p.m." markers in your image
        events = [
            {"year": 2012, "label": "Smartphone<br>Explosion"},
            {"year": 2020, "label": "Pandemic<br>Surge"}
        ]

        for event in events:
            fig.add_shape(
                type="line",
                x0=event["year"], y0=0, x1=event["year"], y1=100,
                line=dict(color="rgba(255,255,255,0.1)", width=1, dash="longdash")
            )
            fig.add_annotation(
                x=event["year"], y=5,
                text=event["label"],
                showarrow=False,
                yanchor="bottom",
                font=dict(size=10, color="gray")
            )

        # 4. NARRATIVE CALLOUTS (Journalistic Style)
        # "The Mobile Boom" Callout
        fig.add_annotation(
            x=2014, y=27.6,
            xref="x", yref="y",
            text="<b>The Mobile Boom</b><br>Affordable Android devices<br>reach the Global South.",
            showarrow=True,
            arrowhead=2,
            ax=0, ay=-60,
            font=dict(color="white", size=11),
            bgcolor="#0E1117", bordercolor="#333", borderwidth=1, borderpad=4
        )

        # "Pandemic Acceleration" Callout
        fig.add_annotation(
            x=2021, y=57.8,
            xref="x", yref="y",
            text="<b>COVID-19 Acceleration</b><br>Lockdowns force rapid<br>digital adoption.",
            showarrow=True,
            arrowhead=2,
            ax=0, ay=-50,
            font=dict(color="white", size=11),
            bgcolor="#0E1117", bordercolor="#333", borderwidth=1, borderpad=4
        )

        # 5. LABELS: Start & End Values (Big Numbers)
        # Start
        fig.add_annotation(
            x=2010, y=val_dev_start,
            text=f"<b>{val_dev_start:.0f}%</b>",
            showarrow=False,
            xanchor="right", xshift=-15,
            font=dict(size=14, color="#00FFFF")
        )
        fig.add_annotation(
            x=2010, y=val_ing_start,
            text=f"<b>{val_ing_start:.0f}%</b>",
            showarrow=False,
            xanchor="right", xshift=-15,
            font=dict(size=14, color="#FF007F")
        )
        # End
        fig.add_annotation(
            x=2023, y=val_dev_end,
            text=f"<b>{val_dev_end:.1f}%</b>",
            showarrow=False,
            xanchor="left", xshift=15,
            font=dict(size=18, color="#00FFFF")
        )
        fig.add_annotation(
            x=2023, y=val_ing_end,
            text=f"<b>{val_ing_end:.1f}%</b>",
            showarrow=False,
            xanchor="left", xshift=15,
            font=dict(size=18, color="#FF007F")
        )

        # 6. Labeling the Lines directly (Cleaner than a legend)
        # Shifted "Developing Nations" label down to fix overlap
        fig.add_annotation(
            x=2011, y=69,
            text="<b>DEVELOPED NATIONS</b>",
            showarrow=False,
            yshift=15,
            font=dict(size=12, color="#00FFFF")
        )
        fig.add_annotation(
            x=2016, y=36,
            text="<b>DEVELOPING NATIONS</b>",
            showarrow=False,
            yshift=-25, # Pushed further down to clear the line
            font=dict(size=12, color="#FF007F")
        )


        # Layout adjustments
        fig.update_layout(
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            showlegend=False, 
            height=650, # Taller to accommodate narrative elements
            margin=dict(l=50, r=80, t=40, b=40),
            xaxis=dict(
                showgrid=False,
                linecolor='white',
                linewidth=1,
                tickfont=dict(color='gray'),
                dtick=2
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                gridwidth=1,
                zeroline=False,
                showticklabels=True, 
                tickfont=dict(color='gray'),
                side='right', 
                ticksuffix="%"
            ),
        )

        st.plotly_chart(fig, use_container_width=True)

        # --- 5. CONCLUSION TEXT ---
        # Simplified Drop Cap (No magazine styling on the 'Y')
        st.markdown(f"""
        <div style="font-size: 18px; line-height: 1.6; color: #E0E0E0; border-left: 3px solid #E3120B; padding-left: 20px; margin-top: 20px;">
            <b>Yes</b>, the gap is closing. 
            In 2010, the digital divide was a staggering <b>{gap_start:.1f} points</b>. Today, 
            <strong style="color:#FF007F">developing nations ●</strong> have surged to <b>{val_ing_end:.1f}%</b> connectivity, 
            shrinking the gap to just <b>{gap_end:.1f} points</b>. 
            While <strong style="color:#00FFFF">developed nations ●</strong> approach saturation, the rest of the world is catching up at 
            <b>{growth_ratio:.1f}x the speed</b>.
        </div>
        <br>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("How are adoption rates changing over time?")
        
        st.markdown("A regional breakdown of the global catch-up in internet adoption.")

# --- 1. Data Preparation ---
# We use the same regional_data.csv file

        df_regional = pd.read_csv(IN_QUESTION3/ "df_merged_for_DiD.csv")
        df_regional['year'] = df_regional['year'].astype(int)
        df_regional['internet_usage_pct'] = pd.to_numeric(df_regional['internet_usage_pct'], errors='coerce')

        # Group by year and region to get the AVERAGE adoption rate
        regional_adoption = df_regional.groupby(['year', 'region'])['internet_usage_pct'].mean().reset_index()


            # --- STATIC, ARTISTIC VERSION ---
        st.subheader("Static Infographic: The Pace of Adoption")

        # Pivot data for Matplotlib


        adoption_pivot = regional_adoption.pivot(index='year', columns='region', values='internet_usage_pct').fillna(0)
        
        COLOR_BG = '#0E1117'
        COLOR_TEXT = '#FAFAFA'
        COLOR_SUBTLE = '#4C566A'
        # Create the Matplotlib figure
        fig_static_adoption, ax = plt.subplots(figsize=(14, 10))
        fig_static_adoption.set_facecolor(COLOR_BG) # Assuming COLOR_BG is defined
        ax.set_facecolor(COLOR_BG)

        # Define a color palette
        colors = plt.cm.plasma(np.linspace(0, 1, len(adoption_pivot.columns)))

        # Plot each region
        for i, region in enumerate(adoption_pivot.columns):
            ax.plot(adoption_pivot.index, adoption_pivot[region], color=colors[i], linewidth=2.5, label=region)

        # --- Aesthetics ---
        ax.spines[['top', 'right']].set_visible(False)
        ax.spines[['left', 'bottom']].set_color(COLOR_SUBTLE)
        ax.tick_params(colors=COLOR_TEXT, which='both', length=0)
        ax.set_ylim(0, 100)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))
        
        ax.grid(False)

        # --- Storytelling ---
        ax.text(0, 1.12, "The Race to Connect", transform=ax.transAxes, ha='left', fontsize=28, weight='bold', color=COLOR_TEXT)
        ax.text(0, 1.05, "While North America started with a massive lead, South Asia and Sub-Saharan Africa show the steepest catch-up trajectories.", transform=ax.transAxes, ha='left', fontsize=16, color=COLOR_SUBTLE)

        # Direct Labeling
        for i, region in enumerate(adoption_pivot.columns):
            ax.text(adoption_pivot.index[-1] + 0.2, adoption_pivot[region].iloc[-1], region, color=colors[i], va='center', ha='left', fontsize=12, weight='bold')

        st.pyplot(fig_static_adoption)

        st.success("""
    **Key Takeaways: The Regional Race to Connect**

    The visual analysis of regional adoption rates reveals a multi-speed world, telling a more nuanced story than the simple "developed vs. developing" divide.

    *   **The Forerunners:** **North America** and **Europe & Central Asia** began the period with a commanding lead and have since approached near-total saturation, with adoption rates now plateauing above 90%.

    *   **The Great Accelerators:** The most dramatic story is the explosive growth in **South Asia** and **Sub-Saharan Africa**. Starting from the lowest bases, these regions exhibit the steepest growth curves, demonstrating a powerful catch-up effect driven by the proliferation of mobile technology.

    *   **The Steady Climbers:** **East Asia & Pacific** and **Latin America & Caribbean** show consistent, strong growth, successfully closing the gap and positioning themselves as major digital economies.

    **Conclusion:** While every region is moving in the right direction, the *pace* of change is the real story. The data strongly suggests that the next billion internet users will come primarily from South Asia and Sub-Saharan Africa, fundamentally reshaping the global digital landscape.
""")








    elif st.session_state.q3_mode == "interactive":
        st.button("← Back to Selection", on_click=reset_q3_mode, type="secondary")

        st.title("📡 Question 3: The Digital Divide")
        st.subheader("Is the gap between developed and developing countries closing?")

        avg_adoption_wide = pd.read_csv(IN_QUESTION3/"avg_adoption_wide.csv")

        avg_adoption_wide = avg_adoption_wide.rename(columns={"0": "Developed", "1": "Developing"})

        #Creating an empty canvas

        fig_gap = go.Figure()

        # add top line (developed countries)
        fig_gap.add_trace(go.Scatter(
            x=avg_adoption_wide['year'],
            y=avg_adoption_wide['Developed'],
            mode='lines',
            line=dict(color='#00CC96', width=4), # A nice green color
            name='Developed Nations'
        ))

        # Add the 'Developing' line and FILL THE GAP down to it
        fig_gap.add_trace(go.Scatter(
            x=avg_adoption_wide['year'],
            y=avg_adoption_wide['Developing'],
            fill='tonexty', # This fills the area to the previous trace
            mode='lines',
            line=dict(color='#EF553B', width=4), # A contrasting orange/red
            name='Developing Nations',
            fillcolor='rgba(255, 255, 255, 0.1)' # A subtle, semi-transparent white fill
        ))

        # --- 3. Improve the Layout for a "NY Times" Feel ---
        fig_gap.update_layout(
            title="The Digital Divide: Average Internet Adoption Over Time",
            xaxis_title="Year",
            yaxis_title="Average Internet Usage (% of Population)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            yaxis_range=[0, 100], # Set a clear 0-100% range
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(color="white") # Ensure all font is white
        )

        # --- 4. Display the Main Plot ---
        st.plotly_chart(fig_gap, use_container_width=True)

        # --- 5. Add Supporting KPIs and Conclusion ---
        st.write("---")
        st.subheader("Quantifying the Gap")

        # Calculate the gap at the start and end
        start_year = avg_adoption_wide['year'].min()
        end_year = avg_adoption_wide['year'].max()
        
        # Use .loc to safely get the first matching value
        gap_start = avg_adoption_wide.loc[avg_adoption_wide['year'] == start_year, 'Developed'].iloc[0] - avg_adoption_wide.loc[avg_adoption_wide['year'] == start_year, 'Developing'].iloc[0]
        gap_end = avg_adoption_wide.loc[avg_adoption_wide['year'] == end_year, 'Developed'].iloc[0] - avg_adoption_wide.loc[avg_adoption_wide['year'] == end_year, 'Developing'].iloc[0]

        kpi_col1, kpi_col2 = st.columns(2)
        with kpi_col1:
            st.metric(
                label=f"Adoption Gap in {start_year}",
                value=f"{gap_start:.1f} percentage points"
            )
        with kpi_col2:
            st.metric(
                label=f"Adoption Gap in {end_year}",
                value=f"{gap_end:.1f} percentage points",
                delta=f"{gap_end - gap_start:.1f} points",
                delta_color="inverse" # Green for a decrease in the gap
            )

        st.success(f"""
        **Conclusion:** Yes, the gap is closing. While a significant digital divide still exists, it has narrowed considerably. The gap in average internet adoption between developed and developing nations has shrunk from **{gap_start:.1f} points** in {start_year} to **{gap_end:.1f} points** in {end_year}.
        """)



        st.markdown("---")
        st.subheader("How are adoption rates changing over time?")
            # --- INTERACTIVE VERSION ---
        df_regional = pd.read_csv(IN_QUESTION3/ "df_merged_for_DiD.csv")
        df_regional['year'] = df_regional['year'].astype(int)
        df_regional['internet_usage_pct'] = pd.to_numeric(df_regional['internet_usage_pct'], errors='coerce')

        # Group by year and region to get the AVERAGE adoption rate
        regional_adoption = df_regional.groupby(['year', 'region'])['internet_usage_pct'].mean().reset_index()

        
        st.subheader("Interactive Line Chart: Regional Adoption Growth")
        
        fig_interactive_adoption = px.line(
            regional_adoption,
            x='year',
            y='internet_usage_pct',
            color='region',
            title="Evolution of Internet Adoption by Region",
            labels={
                "year": "Year",
                "internet_usage_pct": "Average Internet Adoption (%)",
                "region": "Region"
            },
            markers=True
        )
        
        fig_interactive_adoption.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color="#FAFAFA",
            yaxis_range=[0, 100] # Adoption is a percentage
        )
        
        st.plotly_chart(fig_interactive_adoption, use_container_width=True)
        st.success("""
    **Key Takeaways: The Regional Race to Connect**

    The visual analysis of regional adoption rates reveals a multi-speed world, telling a more nuanced story than the simple "developed vs. developing" divide.

    *   **The Forerunners:** **North America** and **Europe & Central Asia** began the period with a commanding lead and have since approached near-total saturation, with adoption rates now plateauing above 90%.

    *   **The Great Accelerators:** The most dramatic story is the explosive growth in **South Asia** and **Sub-Saharan Africa**. Starting from the lowest bases, these regions exhibit the steepest growth curves, demonstrating a powerful catch-up effect driven by the proliferation of mobile technology.

    *   **The Steady Climbers:** **East Asia & Pacific** and **Latin America & Caribbean** show consistent, strong growth, successfully closing the gap and positioning themselves as major digital economies.

    **Conclusion:** While every region is moving in the right direction, the *pace* of change is the real story. The data strongly suggests that the next billion internet users will come primarily from South Asia and Sub-Saharan Africa, fundamentally reshaping the global digital landscape.
""")





with tab2:
    st.title("💡 Question 4: Regional Growth Impact")
    st.subheader("Which regions are leading digital transformation?")
    st.caption("This analysis compares the annual grwoth thrend of digital service exports for each region against a baseline")





    st.subheader("How are digital service exports growing by region?")