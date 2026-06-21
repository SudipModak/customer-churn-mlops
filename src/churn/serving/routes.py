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

    # Save upload history
    upload_id = save_upload_history(
        host="localhost",
        user="root",
        password="Sudip@2003",
        database="churn_db",
        file_name=file.filename,
        total_records=len(df)
    )

    # Save raw uploaded data
    save_customer_uploads(
        host="localhost",
        user="root",
        password="Sudip@2003",
        database="churn_db",
        upload_id=upload_id,
        df=df
    )

    # Run prediction
    predictions, summary = predict_dataframe(df)

    # Save prediction results
    save_prediction_results(
        host="localhost",
        user="root",
        password="Sudip@2003",
        database="churn_db",
        upload_id=upload_id,
        customer_ids=customer_ids,
        predictions=predictions
    )

    
    summary["upload_id"] = upload_id

    return summary

@router.post("/download_predictions")
async def download_predictions(
    file: UploadFile = File(...)
):

    contents = await file.read()

    df = pd.read_excel(
        BytesIO(contents)
    )

    result_df = generate_prediction_file(df)

    os.makedirs(
        "artifacts/predictions",
        exist_ok=True
    )

    output_file = (
        f"artifacts/predictions/"
        f"prediction_{uuid.uuid4().hex}.xlsx"
    )

    result_df.to_excel(
        output_file,
        index=False
    )

    return FileResponse(
        path=output_file,
        filename="prediction_results.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )