import streamlit as st
import requests
import plotly.express as px
import pandas as pd

FASTAPI_URL = "http://127.0.0.1:8000"

def show_prediction_page():


    st.markdown("## 🔮 Customer Churn Prediction")

    uploaded_file = st.file_uploader(
        "Upload Customer Dataset",
        type=["xlsx"]
    )

    if uploaded_file is not None:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

        if st.button(
            "🚀 Run Prediction",
            use_container_width=True
        ):

            with st.spinner(
                "Running prediction..."
            ):

                uploaded_file.seek(0)

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                }

                response = requests.post(
                    f"{FASTAPI_URL}/predict",
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.session_state["prediction_result"] = result

                    st.success(
                        "Prediction Completed Successfully"
                    )

                else:

                    st.error(
                        "Prediction Failed"
                    )

        if "prediction_result" in st.session_state:

            result = st.session_state["prediction_result"]

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Customers",
                    result["total_customers"]
                )

            with col2:
                st.metric(
                    "Churn Risk",
                    result["predicted_churn"]
                )

            with col3:
                st.metric(
                    "Retained",
                    result["retained"]
                )

            with col4:
                st.metric(
                    "Churn Rate",
                    result["churn_rate"]
                )

            st.markdown("---")

            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:

                chart_df = pd.DataFrame({
                    "Category": ["Retained", "Churn"],
                    "Count": [
                        result["retained"],
                        result["predicted_churn"]
                    ]
                })

                fig = px.pie(
                    chart_df,
                    values="Count",
                    names="Category",
                    hole=0.65,
                    title="Customer Retention Overview"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            with chart_col2:

                st.metric(
                    "Upload ID",
                    result["upload_id"]
                )

            st.markdown("---")

            uploaded_file.seek(0)

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            }

            download_response = requests.post(
                f"{FASTAPI_URL}/download_predictions",
                files=files
            )

            if download_response.status_code == 200:

                st.download_button(
                    label="📥 Download Prediction Report",
                    data=download_response.content,
                    file_name="prediction_results.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

