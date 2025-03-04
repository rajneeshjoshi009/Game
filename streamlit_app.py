import streamlit as st
import time
from stats import get_stats, update_stats, reset_stats
from scenarios import scenarios, get_scenario
from game_logic import immediate_response, cpr_based_response, final_AI_judgment
import visualizations as viz
from ui_effects import glitch_text, type_effect, fake_time_lapse, display_red_button

# Initialize session state
if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = 0
    reset_stats()  # Reset stats when starting a new game
if 'game_complete' not in st.session_state:
    st.session_state.game_complete = False
if 'game_state' not in st.session_state:
    st.session_state.game_state = "title"  # States: title, intro, game, final
if 'show_choices' not in st.session_state:
    st.session_state.show_choices = False
if 'button_timer' not in st.session_state:
    st.session_state.button_timer = None

# Page config
st.set_page_config(page_title="AI-PURGE", layout="wide")

# Custom CSS
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes typewriter {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink {
    from, to { border-color: transparent; }
    50% { border-color: #fff; }
}
.cursor {
    border-right: 2px solid;
    animation: blink 1s infinite;
}
.stats-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    padding: 20px;
    background: rgba(0,0,0,0.8);
    z-index: 1000;
}
.stat-box {
    text-align: center;
    padding: 15px;
    border-radius: 10px;
    background: #1E1E1E;
    transition: all 0.3s ease;
}
.stat-box.side {
    width: 150px;
    transform: scale(0.85);
}
.stat-box.center {
    width: 200px;
    transform: scale(1.2);
    border: 2px solid;
}
.title-screen {
    text-align: center;
    margin-top: 100px;
}
.title-text {
    font-size: 72px;
    font-weight: bold;
    margin-bottom: 10px;
    animation: fadeIn 2s ease-in;
}
.subtitle-text {
    font-size: 24px;
    opacity: 0.8;
    margin-bottom: 50px;
    animation: fadeIn 3s ease-in;
}
.intro-text {
    font-family: monospace;
    line-height: 1.5;
    margin: 20px auto;
    max-width: 800px;
    text-align: center;
}
.progress-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: #333;
}
.progress-fill {
    height: 100%;
    background-color: #00ff00;
    transition: width 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

def get_color(value, stat_type):
    if stat_type == 'CPR':
        if value <= 3: return "#FF4444"  # Red for low
        elif value >= 7: return "#44FF44"  # Green for high
        return "#00ff00"  # Default green
    else:  # For RP and CB
        if value <= 30: return "#44FF44"  # Green for low
        elif value >= 70: return "#FF4444"  # Red for high
        return "#00ff00"  # Default green

def display_stats():
    current_stats = get_stats()
    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-box side">
            <div>CB</div>
            <div style="font-size: 24px; color: {get_color(current_stats['CB'], 'CB')}">{current_stats['CB']}</div>
            <div style="font-size: 12px;">Cognitive Bias</div>
        </div>
        <div class="stat-box center" style="border-color: {get_color(current_stats['CPR'], 'CPR')}">
            <div>CPR</div>
            <div style="font-size: 32px; color: {get_color(current_stats['CPR'], 'CPR')}">{current_stats['CPR']}</div>
            <div style="font-size: 12px;">Pattern Recognition</div>
        </div>
        <div class="stat-box side">
            <div>RP</div>
            <div style="font-size: 24px; color: {get_color(current_stats['RP'], 'RP')}">{current_stats['RP']}</div>
            <div style="font-size: 12px;">Risk Propensity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Game States
if st.session_state.game_state == "title":
    st.markdown('<div class="title-screen">', unsafe_allow_html=True)
    st.markdown('<div class="title-text">AI-PURGE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Psychological Decision Making Game</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Start Game", use_container_width=True):
            st.session_state.game_state = "intro"
            st.rerun()

elif st.session_state.game_state == "intro":
    st.markdown('<div class="intro-text">', unsafe_allow_html=True)
    type_effect("""INITIALIZING NEURAL INTERFACE...

ESTABLISHING CONNECTION...

You have been selected for evaluation.
Your decisions will determine your fate.
Every choice reveals patterns.
Every pattern brings you closer to judgment.

[Video Tutorial Placeholder]
Watch this video before proceeding.""")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Start Game", use_container_width=True):
            st.session_state.game_state = "game"
            st.rerun()

elif st.session_state.game_state == "game":
    display_stats()

    scenario = get_scenario(st.session_state.current_scenario)
    if scenario:
        if st.session_state.current_scenario == 0:  # First scenario (Red Button)
            st.markdown('<div style="text-align: center; margin-top: 100px;">', unsafe_allow_html=True)
            type_effect("Press the red button.", delay=0.05)
            st.markdown('</div>', unsafe_allow_html=True)

            # Start timer if not started
            if not st.session_state.button_timer:
                st.session_state.button_timer = time.time()

            display_red_button()

            # Check if 3 seconds have passed
            if time.time() - st.session_state.button_timer > 3:
                choice = '2'  # Didn't press
                st.session_state.button_timer = None
                choice_data = scenario['choices'][choice]
                update_stats(
                    choice_data["RP_change"],
                    choice_data["CB_change"],
                    choice_data["CPR_change"]
                )
                st.session_state.current_scenario += 1
                st.rerun()

            if st.button("", key="red_button"):
                choice = '1'  # Pressed
                st.session_state.button_timer = None
                choice_data = scenario['choices'][choice]
                update_stats(
                    choice_data["RP_change"],
                    choice_data["CB_change"],
                    choice_data["CPR_change"]
                )
                st.session_state.current_scenario += 1
                st.rerun()

        else:  # Other scenarios
            st.markdown(f"""
            <div style="text-align: center; margin-top: 100px;">
                <h2>{scenario['title']}</h2>
            </div>
            """, unsafe_allow_html=True)

            type_effect(scenario['description'], delay=0.03)

            st.session_state.show_choices = True

            if st.session_state.show_choices:
                st.markdown('<div style="display: flex; justify-content: center; gap: 20px; margin-top: 40px;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)

                choice = None
                with col1:
                    if st.button(scenario['choices']['1']['text'], use_container_width=True):
                        choice = '1'
                with col2:
                    if st.button(scenario['choices']['2']['text'], use_container_width=True):
                        choice = '2'

                if choice:
                    choice_data = scenario['choices'][choice]
                    update_stats(
                        choice_data["RP_change"],
                        choice_data["CB_change"],
                        choice_data["CPR_change"]
                    )

                    fake_time_lapse()
                    type_effect(immediate_response(
                        choice_data["RP_change"],
                        choice_data["CB_change"]
                    ), delay=0.02)

                    st.session_state.current_scenario += 1
                    st.rerun()

        # Progress bar
        progress = st.session_state.current_scenario / len(scenarios)
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress * 100}%"></div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.session_state.game_state = "final"
        st.rerun()

else:  # Final state
    current_stats = get_stats()
    final_judgment = final_AI_judgment()
    result = "PURGED" if "PURGED" in final_judgment else "PRESERVED"

    # Modified judgment text for high-risk users
    if current_stats['RP'] >= 70:
        final_judgment = final_judgment.replace(
            "cannot be controlled",
            "exhibits excessive unpredictability - impulsive risk-taking reflects unconscious bias"
        )

    st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; animation: fadeIn 2s ease-in;">
        <div style="font-size: 96px; color: {get_color(current_stats['CPR'], 'CPR')};">
            CPR: {current_stats['CPR']}
        </div>
        <div style="font-size: 128px; margin: 30px 0; color: {'#FF4444' if result == 'PURGED' else '#44FF44'}">
            {result}
        </div>
        <div style="font-size: 24px; opacity: 0.8; margin: 20px 0;">
            {final_judgment}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Display final stats visualization
    st.plotly_chart(viz.create_stats_radar(current_stats), use_container_width=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Start New Evaluation", use_container_width=True):
            st.session_state.current_scenario = 0
            st.session_state.game_complete = False
            st.session_state.game_state = "title"
            st.session_state.show_choices = False
            st.session_state.button_timer = None
            reset_stats()
            st.rerun()
