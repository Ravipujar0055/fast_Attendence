import streamlit as st

LOGO_URL = "https://i.ibb.co/YTYGn5qV/logo.png"


def header_home():
    st.markdown(f'''<div class="home-brand"><img src="{LOGO_URL}" alt="SnapClass logo" /><p class="brand-name">SNAP<br>CLASS</p></div>''', unsafe_allow_html=True)


def header_dashboard():
    st.markdown(f'''<div class="brand-lockup"><img src="{LOGO_URL}" alt="SnapClass logo" /><p class="brand-name">SNAP<br>CLASS</p></div>''', unsafe_allow_html=True)
