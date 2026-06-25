import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

def show_upload_history():

    st.title("📂 Upload History")

    try:

        
        engine = create_engine(
    "mysql+pymysql://root:Sudip%402003@mysql:3306/churn_db"
)
        

        df = pd.read_sql(
            """
            SELECT
                upload_id,
                file_name,
                total_records,
                upload_time
            FROM upload_history
            ORDER BY upload_id DESC
            """,
            con=engine
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.success(
            f"{len(df)} uploads found"
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )