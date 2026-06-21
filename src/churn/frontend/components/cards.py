import streamlit as st

def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
        </div>
        """,
        unsafe_allow_html=True
    )