import streamlit as st

from churn.frontend.components.charts import (
    churn_donut,
    churn_gauge
)


def show_dashboard():

    st.markdown("## 📈 Executive Dashboard")

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            churn_donut(),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            churn_gauge(),
            use_container_width=True
        )