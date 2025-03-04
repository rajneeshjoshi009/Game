import streamlit as st
import time
import random

def glitch_text(text):
    """
    Displays text with random glitch effects
    """
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    container = st.empty()
    for _ in range(3):  # Show 3 glitch frames
        glitched = ""
        for char in text:
            if random.random() < 0.1:  # 10% chance to glitch each character
                glitched += random.choice(glitch_chars)
            else:
                glitched += char
        container.markdown(f"""
        <div style="font-family: monospace; color: #00ff00; margin: 5px 0;">
            {glitched}
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)
    container.markdown(f"""
    <div style="font-family: monospace; color: #00ff00; margin: 5px 0;">
        {text}
    </div>
    """, unsafe_allow_html=True)

def type_effect(text, delay=0.03):
    """
    Displays text with a typewriter effect and random glitches
    """
    container = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        if random.random() < 0.05:  # 5% chance for glitch effect
            glitch_display = displayed_text + random.choice("!@#$%^&*")
            container.markdown(f"""
            <div style="font-family: monospace; padding: 10px; background: #1E1E1E; border-radius: 5px;">
                {glitch_display}<span class="cursor">|</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.05)
        container.markdown(f"""
        <div style="font-family: monospace; padding: 10px; background: #1E1E1E; border-radius: 5px;">
            {displayed_text}<span class="cursor">|</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(delay)

    # Final display without cursor
    container.markdown(f"""
    <div style="font-family: monospace; padding: 10px; background: #1E1E1E; border-radius: 5px;">
        {text}
    </div>
    """, unsafe_allow_html=True)

def display_red_button():
    """
    Display an animated red button
    """
    st.markdown("""
    <div style="display: flex; justify-content: center; margin: 40px 0;">
        <button style="
            background-color: #ff0000;
            border: none;
            color: white;
            padding: 20px 40px;
            font-size: 24px;
            border-radius: 10px;
            cursor: pointer;
            box-shadow: 0 0 20px #ff0000;
            animation: pulse 2s infinite;
        ">
            PRESS
        </button>
    </div>
    <style>
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 20px #ff0000; }
        50% { transform: scale(1.05); box-shadow: 0 0 30px #ff0000; }
        100% { transform: scale(1); box-shadow: 0 0 20px #ff0000; }
    }
    </style>
    """, unsafe_allow_html=True)

def fake_time_lapse():
    """
    Simulates a loading delay with glitch effects
    """
    container = st.empty()
    for _ in range(6):
        text = "PROCESSING" + "." * random.randint(1, 3)
        if random.random() < 0.3:  # 30% chance for glitch
            text = text.replace("O", "0").replace("I", "1")
        container.markdown(f"""
        <div style="font-family: monospace; color: #00ff00;">
            {text}
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.2)
    container.empty()
