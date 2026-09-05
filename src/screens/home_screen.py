import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():
    style_base_layout()
    style_background_home()
    header_home()
    st.markdown("<p style='text-align:center; color:rgba(255,255,255,.82); margin:-1.8rem 0 2.3rem;'>AI-powered attendance, made simple for every classroom.</p>", unsafe_allow_html=True)


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Student portal")
        st.caption("Check your subjects and attendance in one place.")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("Teacher portal")
        st.caption("Manage classes and take attendance with confidence.")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
