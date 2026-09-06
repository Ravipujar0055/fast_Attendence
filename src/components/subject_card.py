import streamlit as st


def subject_card(name, code, section, teacher_name=None, stats=None, footer_callback=None):
    """Render one consistent, accessible subject summary card."""
    stats_html = ""
    if stats:
        stats_html = '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            stats_html += f'<span class="subject-stat">{icon} <b>{value}</b> {label}</span>'
        stats_html += "</div>"
    teacher_html = (
        f'<p class="subject-card__meta">Teacher: {teacher_name}</p>'
        if teacher_name
        else ""
    )
    st.markdown(f'''<section class="subject-card"><p class="subject-card__title">{name}</p><p class="subject-card__meta">Code <span class="subject-code">{code}</span> &nbsp;·&nbsp; Section {section}</p>{teacher_html}{stats_html}</section>''', unsafe_allow_html=True)
    if footer_callback:
        footer_callback()
