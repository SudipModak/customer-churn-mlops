from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import BytesIO
import uuid
import os
from src.churn.serving.services import predict_dataframe
from fastapi.responses import FileResponse

from src.churn.serving.services import (
    predict_dataframe,
    generate_prediction_file
)
from src.churn.database.mysql_operations import (
    save_upload_history,
    save_customer_uploads,
    save_prediction_results
)

router = APIRouter()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_excel(
        BytesIO(contents)
    )

    df = df.fillna("")

    customer_ids = df["CustomerID"].tolist()

    upload_id = None

    try:
        upload_id = save_upload_history(
            host="mysql",
            user="root",
            password="Sudip@2003",
            database="churn_db",
            file_name=file.filename,
            total_records=len(df)
        )

        save_customer_uploads(
            host="mysql",
            user="root",
            password="Sudip@2003",
            database="churn_db",
            upload_id=upload_id,
            df=df
        )

    except Exception as e:
        print(f"MySQL Error: {e}")

    predictions, summary = predict_dataframe(df)

    try:
        if upload_id:
            save_prediction_results(
                host="mysql",
                user="root",
                password="Sudip@2003",
                database="churn_db",
                upload_id=upload_id,
                customer_ids=customer_ids,
                predictions=predictions
            )
    except Exception as e:
        print(f"MySQL Error: {e}")

    summary["upload_id"] = upload_id

    return summary