from dotenv import load_dotenv
import dagshub
import mlflow

load_dotenv()

dagshub.init(
    repo_owner="sudipmodak",
    repo_name="customer-churn-mlops",
    mlflow=True
)

print("Connected Successfully")
print(mlflow.get_tracking_uri())

import mlflow

with mlflow.start_run():

    mlflow.log_param(
        "model_name",
        "LogisticRegression"
    )

    mlflow.log_metric(
        "accuracy",
        0.85
    )

    mlflow.log_metric(
        "f1_score",
        0.78
    )

print("Run Logged Successfully")