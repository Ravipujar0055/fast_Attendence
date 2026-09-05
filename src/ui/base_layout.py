import streamlit as st


def style_background_home():
    """Apply the focused, high-contrast landing page treatment."""
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #4656df 0%, #6574f7 100%) !important; }
        .stApp [data-testid="stColumn"] { background: rgba(255,255,255,.96); padding: 2rem !important; border-radius: 24px; border: 1px solid rgba(255,255,255,.45); box-shadow: 0 18px 40px rgba(28,37,117,.18); min-height: 335px; }
        .stApp [data-testid="stColumn"] h2 { color: #172554 !important; }
        .stApp [data-testid="stColumn"] [data-testid="stImage"] { margin: .5rem 0 .75rem; }
        @media (max-width: 700px) { .stApp [data-testid="stColumn"] { min-height: 0; padding: 1.5rem !important; } }
        </style>""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("<style>.stApp { background: #f5f7ff !important; }</style>", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { max-width: 1120px; padding: 2rem 2rem 3rem !important; }
        html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
        h1,h2,h3 { font-family: 'Outfit',sans-serif !important; color: #172554 !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2.25rem,5vw,3.75rem) !important; line-height: 1.02 !important; margin-bottom: .5rem !important; }
        h2 { font-size: clamp(1.65rem,3vw,2.15rem) !important; line-height: 1.12 !important; }
        h3 { font-size: 1.25rem !important; }
        p,label,[data-testid="stMarkdownContainer"] { color: #475569; }
        .stButton > button { min-height: 2.75rem; border-radius: 12px !important; padding: .62rem 1rem !important; font-family:'DM Sans',sans-serif !important; font-weight:700 !important; border:1px solid transparent !important; box-shadow:none !important; transition:transform .16s ease,box-shadow .16s ease,background .16s ease !important; }
        .stButton > button[kind="primary"] { background:#4f5ee8 !important; color:#fff !important; }
        .stButton > button[kind="secondary"] { background:#fdf2f8 !important; color:#be185d !important; border-color:#fbcfe8 !important; }
        .stButton > button[kind="tertiary"] { background:#fff !important; color:#334155 !important; border-color:#dbe3f0 !important; }
        .stButton > button:hover { transform:translateY(-1px) !important; box-shadow:0 8px 18px rgba(79,94,232,.18) !important; }
        .stButton > button[kind="secondary"]:hover { background:#fce7f3 !important; }
        .stButton > button[kind="tertiary"]:hover { background:#f8fafc !important; }
        [data-testid="stTextInput"] input { border-radius:10px !important; border-color:#dbe3f0 !important; background:#fff !important; }
        [data-testid="stTextInput"] input:focus { border-color:#6875f5 !important; box-shadow:0 0 0 3px rgba(104,117,245,.14) !important; }
        hr { border-color:#e5eaf4 !important; }
        [data-testid="stDataFrame"] { border:1px solid #e2e8f0; border-radius:14px; overflow:hidden; }
        .brand-lockup { display:flex; align-items:center; gap:12px; }
        .brand-lockup img { height:64px; width:64px; object-fit:contain; }
        .brand-name { margin:0; color:#4f5ee8; font:800 1.55rem/.82 'Outfit',sans-serif; letter-spacing:-.07em; }
        .home-brand { display:flex; flex-direction:column; align-items:center; margin:.25rem 0 2.5rem; }
        .home-brand img { height:92px; }
        .home-brand .brand-name { color:white; font-size:clamp(2.8rem,7vw,4.5rem); text-align:center; margin-top:.7rem; }
        .subject-card { background:#fff; border:1px solid #dfe6f2; border-radius:18px; padding:1.4rem; margin-bottom:.8rem; box-shadow:0 8px 22px rgba(30,41,59,.05); }
        .subject-card__title { margin:0; color:#172554; font:700 1.3rem 'Outfit',sans-serif; }
        .subject-card__meta { margin:.55rem 0 .9rem; color:#64748b; }
        .subject-code { display:inline-block; padding:.18rem .48rem; border-radius:6px; background:#eef0ff; color:#4656df; font-weight:700; }
        .subject-stat { display:inline-flex; align-items:center; gap:.25rem; padding:.36rem .65rem; border-radius:999px; background:#f4f6fb; color:#475569; font-size:.84rem; }
        .subject-stat b { color:#172554; }
        .app-footer { margin-top:3rem; color:#94a3b8; font-size:.85rem; text-align:center; }
        @media (max-width:700px) { .block-container { padding:1.25rem 1rem 2rem !important; } }
        </style>""", unsafe_allow_html=True)
