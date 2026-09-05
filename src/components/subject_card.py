import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    """Render one consistent, accessible subject summary card."""
    stats_html = ""
    if stats:
        stats_html = '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            stats_html += f'<span class="subject-stat">{icon} <b>{value}</b> {label}</span>'
        stats_html += "</div>"
    st.markdown(f'''<section class="subject-card"><p class="subject-card__title">{name}</p><p class="subject-card__meta">Code <span class="subject-code">{code}</span> &nbsp;·&nbsp; Section {section}</p>{stats_html}</section>''', unsafe_allow_html=True)
    if footer_callback:
        footer_callback()
