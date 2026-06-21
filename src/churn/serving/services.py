import pandas as pd

from src.churn.ml.prediction import PredictionPipeline


def predict_dataframe(df: pd.DataFrame):

    if "Churn Label" in df.columns:
        df = df.drop(columns=["Churn Label"])

    pipeline = PredictionPipeline()

    predictions = pipeline.predict(df)

    total_customers = len(predictions)
    predicted_churn = int(sum(predictions))
    retained = total_customers - predicted_churn

    churn_rate = round(
        (predicted_churn / total_customers) * 100,
        2
    )

    return predictions, {
        "total_customers": total_customers,
        "predicted_churn": predicted_churn,
        "retained": retained,
        "churn_rate": f"{churn_rate}%"
    }




def generate_prediction_file(df):

    customer_ids = df["CustomerID"].tolist()

    if "Churn Label" in df.columns:
        df = df.drop(columns=["Churn Label"])

    pipeline = PredictionPipeline()

    predictions = pipeline.predict(df)

    result_df = pd.DataFrame({
        "CustomerID": customer_ids,
        "Prediction": predictions
    })

    return result_df