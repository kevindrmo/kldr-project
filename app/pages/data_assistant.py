from utils.common_imports import *
import plotly.graph_objects as go

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




# ... your existing imports and st.markdown code ...

# def show_construction_gauge():
#     fig = go.Figure(go.Indicator(
#         mode = "gauge+number",
#         value = 10,
#         title = {'text': "Module Construction Progress", 'font': {'size': 24, 'color': "#cccccc"}},
#         number = {'suffix': "%", 'font': {'color': "#9B59B6"}},
#         gauge = {
#             'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#cccccc"},
#             'bar': {'color': "#9B59B6"},  # Amethyst Purple
#             'bgcolor': "rgba(0,0,0,0)",
#             'borderwidth': 2,
#             'bordercolor': "#333",
#             'steps': [
#                 {'range': [0, 50], 'color': "rgba(155, 89, 182, 0.1)"},
#                 {'range': [50, 90], 'color': "rgba(155, 89, 182, 0.3)"}
#             ],
#             'threshold': {
#                 'line': {'color': "white", 'width': 4},
#                 'thickness': 0.75,
#                 'value': 99
#             }
#         }
#     ))

#     fig.update_layout(
#         paper_bgcolor='rgba(0,0,0,0)',
#         font={'color': "#cccccc", 'family': "Arial"},
#         height=300,
#         margin=dict(l=20, r=20, t=50, b=20)
#     )

#     st.plotly_chart(fig, use_container_width=True)
#     st.caption("Estimated time to completion: *Calculating...*")

# show_construction_gauge()



# def show_wireframe_construction():
#     # Create data for a cool wave shape
#     x = np.linspace(-5, 5, 50)
#     y = np.linspace(-5, 5, 50)
#     x, y = np.meshgrid(x, y)
#     r = np.sqrt(x**2 + y**2)
#     z = np.sin(r)

#     fig = go.Figure(data=[go.Surface(
#         z=z, 
#         x=x, 
#         y=y, 
#         colorscale=[[0, '#1a1a1a'], [1, '#9B59B6']], # Dark to Amethyst
#         opacity=0.8,
#         showscale=False
#     )])

#     fig.update_layout(
#         title={
#             'text': "Visualizing Architecture...",
#             'y':0.9,
#             'x':0.5,
#             'xanchor': 'center',
#             'yanchor': 'top',
#             'font': {'color': '#9B59B6', 'size': 20}
#         },
#         autosize=True,
#         width=500,
#         height=500,
#         margin=dict(l=0, r=0, b=0, t=50),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         scene=dict(
#             xaxis=dict(visible=False),
#             yaxis=dict(visible=False),
#             zaxis=dict(visible=False),
#             camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)) # Angled view
#         )
#     )

#     st.plotly_chart(fig, use_container_width=True)

# show_wireframe_construction()






def show_data_convergence():
    # Create a subtle spiral path representing data converging
    n = 150
    t = np.linspace(0, 10, n)
    # x and y equations for a logarithmic spiral inward
    x = t * np.cos(t*2.5) 
    y = t * np.sin(t*2.5)
    # Fade opacity as points get closer to center (t=0)
    opacity = np.linspace(0.1, 0.8, n)
    # Sizes get slightly smaller towards center
    sizes = np.linspace(8, 3, n)

    fig = go.Figure()

    # Add the points
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        marker=dict(
            color='#9B59B6', # Amethyst Purple
            size=sizes,
            opacity=opacity,
            line=dict(width=0)
        ),
        hoverinfo='skip'
    ))
    
    # Add a very subtle central glowing point
    fig.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers',
        marker=dict(color='#9B59B6', size=15, opacity=0.3),
        hoverinfo='skip'
    ))

    fig.update_layout(
        # Minimalist title
        title={
            'text': "Initializing Data Structure...",
            'y':0.1, 'x':0.5, 'xanchor': 'center',
            'font': {'color': 'rgba(155, 89, 182, 0.6)', 'size': 12, 'family': 'monospace'}
        },
        autosize=True, height=300,
        margin=dict(l=0, r=0, b=30, t=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(visible=False, fixedrange=True),
        yaxis=dict(visible=False, fixedrange=True)
    )

    yaxis = dict(
        visible = False,
        fixedrange= True,
        scaleanchor = "x", # locks y axis to x axis
        scaleratio = 1
        )
    # staticPlot: True is crucial for subtlety - removes the plotly toolbar
    st.plotly_chart(fig, use_container_width=True, config={'staticPlot': True})

show_data_convergence()

