import streamlit as st

def render_sidebar():

    st.sidebar.title("🚀 Churn Platform")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Prediction",
            "Upload History",
            "About"
        ]
    )

    return page