import streamlit as st
from churn.frontend.views.upload_history import (
    show_upload_history
)
from churn.frontend.components.sidebar import render_sidebar
from churn.frontend.views.dashboard import show_dashboard
from churn.frontend.views.prediction import show_prediction_page

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open(
    "src/churn/frontend/assets/style.css",
    encoding="utf-8"
) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Sidebar
page = render_sidebar()

st.sidebar.markdown("---")

st.sidebar.markdown("""
## 👨‍💻 Developer

**Sudip Modak**

MIS Analyst

Data Science • Machine Learning • MLOps
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### ⚙️ MLOps Stack

✅ MLflow

✅ DagsHub

✅ FastAPI

✅ MySQL

✅ Streamlit

✅ Docker

✅ AWS EC2
""")

st.sidebar.markdown("---")

st.sidebar.caption(
    "Customer Churn Intelligence Platform v1.0"
)

# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.markdown(
        """
        <div class="hero-title">
            🚀 Customer Churn Intelligence Platform
        </div>

        <div class="hero-subtitle">
            AI Powered Customer Retention Analytics with MLOps Monitoring
        </div>

        <div style="
            margin-top:15px;
            color:#94A3B8;
            font-size:16px;
            font-weight:500;
        ">
            Designed & Developed by <b>Sudip Modak</b>
        </div>

        <br>
        """,
        unsafe_allow_html=True
    )

    show_dashboard()

# ==================================================
# PREDICTION
# ==================================================

elif page == "Prediction":

    st.title("🔮 Customer Churn Prediction")

    st.markdown(
        "Upload customer data and generate churn predictions using the trained Machine Learning model."
    )

    show_prediction_page()

# ==================================================
# UPLOAD HISTORY
# ==================================================

elif page == "Upload History":

    show_upload_history()    

# ==================================================
# ABOUT
# ==================================================

# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.title("ℹ️ About Project")

    st.markdown("---")

    st.subheader("👨‍💻 About The Developer")

    st.markdown("""
### Sudip Modak

**MIS Analyst | Data Science & MLOps Enthusiast**

Currently working in the Logistics & Supply Chain domain, specializing in data analytics, business reporting, dashboard development, and process automation.

This project was developed as an end-to-end Machine Learning and MLOps solution to demonstrate real-world industry practices including data validation, transformation pipelines, model training, experiment tracking, API development, database integration, and cloud-ready deployment.

### Professional Focus

- Machine Learning Systems
- MLOps & Model Lifecycle Management
- Data Engineering
- Predictive Analytics
- Supply Chain Analytics
- Business Intelligence

### Project Vision

The objective behind building this platform was to create a production-style machine learning application that goes beyond model training and covers the complete lifecycle of a modern ML product—from raw data ingestion to deployment, monitoring, and user-facing analytics.

### Key Highlights

✅ End-to-End Machine Learning Pipeline

✅ MLflow Experiment Tracking

✅ DagsHub Integration

✅ FastAPI Backend Services

✅ MySQL Database Integration

✅ Interactive Streamlit Dashboard

✅ Docker & AWS Deployment Ready
""")

    st.markdown("---")

    st.info(
        "🚀 Customer Churn Intelligence Platform | Developed by Sudip Modak | Version 1.0"
    )