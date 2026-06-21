import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def churn_donut():

    df = pd.DataFrame({
        "Category": ["Retained", "Churn"],
        "Count": [5440, 1603]
    })

    fig = px.pie(
        df,
        values="Count",
        names="Category",
        hole=0.65
    )

    fig.update_layout(
        title="Customer Retention Overview"
    )

    return fig


def churn_gauge():

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=22.76,
            title={"text": "Churn Rate"}
        )
    )

    return fig