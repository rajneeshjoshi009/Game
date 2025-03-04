import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def create_stats_radar(stats, key_suffix=""):
    """
    Create a radar chart for stats visualization
    """
    # Create display labels and scale CPR to 100 for visualization
    display_stats = {
        'Risk Propensity': stats['RP'],
        'Cognitive Bias': stats['CB'],
        'Pattern Recognition': stats['CPR'] * 10  # Scale CPR from 1-10 to 1-100
    }

    categories = list(display_stats.keys())
    values = list(display_stats.values())

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#1f77b4'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=400,
        margin=dict(l=80, r=80, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return fig

def create_progress_bar(current, total):
    """Create a progress bar for scenario completion"""
    progress = current / total
    st.progress(progress)
    st.text(f"Progress: {current}/{total} scenarios completed")

def display_final_results(cpr_score, stats):
    """Display the final game results with stats"""
    st.title("Game Complete!")

    # Display final stats numerically
    st.markdown("### Final Statistics")
    st.markdown(f"""
    * **Risk Propensity (RP):** {stats['RP']}
    * **Cognitive Bias (CB):** {stats['CB']}
    * **Pattern Recognition (CPR):** {stats['CPR']}
    """)

    # Display CPR Score
    st.header(f"Final CPR Score: {cpr_score}")

    # Interpret CPR Score
    if cpr_score >= 80:
        st.success("Excellent! You show strong ethical judgment and balanced decision-making.")
    elif cpr_score >= 60:
        st.info("Good! You maintain a decent balance in your decisions.")
    else:
        st.warning("There's room for improvement in balancing risk and ethical considerations.")

    # Display Stats Radar Chart
    st.subheader("Final Stats Visualization")
    radar_chart = create_stats_radar(stats, key_suffix="final")
    st.plotly_chart(radar_chart, use_container_width=True)
