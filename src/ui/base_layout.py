import streamlit as st


def style_background_home():
    """Apply the dark landing-page palette without changing the page layout."""
    st.markdown("""
        <style>
        .stApp { background: radial-gradient(circle at 50% -20%, #26356f 0%, #111a35 42%, #090e1c 100%) !important; }
        .stApp [data-testid="stColumn"] { background: rgba(22,31,55,.92); padding: 2rem !important; border-radius: 24px; border: 1px solid #314064; box-shadow: 0 18px 40px rgba(0,0,0,.28); min-height: 335px; }
        .stApp [data-testid="stColumn"] h2 { color: #f8fafc !important; }
        .stApp [data-testid="stColumn"] [data-testid="stImage"] { margin: .5rem 0 .75rem; }
        @media (max-width: 700px) { .stApp [data-testid="stColumn"] { min-height: 0; padding: 1.5rem !important; } }
        </style>
        """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("<style>.stApp { background: #0b1020 !important; }</style>", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');

        /* Dark design tokens: page / surface / border / primary / text. */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { max-width: 1120px; padding: 2rem 2rem 3rem !important; }
        html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color: #e8edf9; }
        h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: #f8fafc !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2.25rem,5vw,3.75rem) !important; line-height: 1.02 !important; margin-bottom: .5rem !important; }
        h2 { font-size: clamp(1.65rem,3vw,2.15rem) !important; line-height: 1.12 !important; }
        h3 { font-size: 1.25rem !important; }
        p, label, [data-testid="stMarkdownContainer"], [data-testid="stCaptionContainer"] { color: #aebbd3; }

        .stButton > button { min-height: 2.75rem; border-radius: 12px !important; padding: .62rem 1rem !important; font-family:'DM Sans',sans-serif !important; font-weight:700 !important; border:1px solid transparent !important; box-shadow:none !important; transition:transform .16s ease,box-shadow .16s ease,background .16s ease !important; }
        .stButton > button[kind="primary"] { background: #6975ff !important; color: #fff !important; }
        .stButton > button[kind="secondary"] { background: #3d1837 !important; color: #f9a8d4 !important; border-color: #76345e !important; }
        .stButton > button[kind="tertiary"] { background: #18233d !important; color: #d5ddf1 !important; border-color: #334362 !important; }
        .stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 8px 18px rgba(73,87,222,.3) !important; }
        .stButton > button[kind="primary"]:hover { background: #7a84ff !important; }
        .stButton > button[kind="secondary"]:hover { background: #542044 !important; }
        .stButton > button[kind="tertiary"]:hover { background: #223052 !important; }

        [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div { color: #edf2ff !important; background: #121b30 !important; border-color: #334362 !important; }
        [data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: #71809d !important; }
        [data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: #7a84ff !important; box-shadow: 0 0 0 3px rgba(122,132,255,.16) !important; }
        [data-baseweb="popover"], [data-baseweb="menu"], [data-testid="stDialog"] > div { background: #18233d !important; color: #edf2ff !important; }
        [data-testid="stFileUploader"] section, [data-testid="stCameraInput"] > div { background: #121b30 !important; border-color: #334362 !important; }
        [data-testid="stExpander"] { background: #121b30 !important; border-color: #334362 !important; }
        [data-testid="stDataFrame"] { border: 1px solid #334362; border-radius: 14px; overflow: hidden; }
        [data-testid="stDataFrame"] iframe { background: #121b30 !important; }
        hr { border-color: #283654 !important; }

        .brand-lockup { display: flex; align-items: center; gap: 12px; }
        .brand-lockup img { height: 64px; width: 64px; object-fit: contain; }
        .brand-name { margin: 0; color: #8790ff; font: 800 1.55rem/.82 'Outfit',sans-serif; letter-spacing: -.07em; }
        .home-brand { display: flex; flex-direction: column; align-items: center; margin: .25rem 0 2.5rem; }
        .home-brand img { height: 92px; }
        .home-brand .brand-name { color: #fff; font-size: clamp(2.8rem,7vw,4.5rem); text-align: center; margin-top: .7rem; }

        .subject-card { background: #121b30; border: 1px solid #2d3d5e; border-radius: 18px; padding: 1.4rem; margin-bottom: .8rem; box-shadow: 0 8px 22px rgba(0,0,0,.16); }
        .subject-card__title { margin: 0; color: #f8fafc; font: 700 1.3rem 'Outfit',sans-serif; }
        .subject-card__meta { margin: .55rem 0 .9rem; color: #aebbd3; }
        .subject-code { display: inline-block; padding: .18rem .48rem; border-radius: 6px; background: #252c60; color: #b9c0ff; font-weight: 700; }
        .subject-stat { display: inline-flex; align-items: center; gap: .25rem; padding: .36rem .65rem; border-radius: 999px; background: #1c2946; color: #b7c4dc; font-size: .84rem; }
        .subject-stat b { color: #f2f6ff; }
        .app-footer { margin-top: 3rem; color: #71809d; font-size: .85rem; text-align: center; }
        @media (max-width:700px) { .block-container { padding:1.25rem 1rem 2rem !important; } }
        </style>
        """, unsafe_allow_html=True)
