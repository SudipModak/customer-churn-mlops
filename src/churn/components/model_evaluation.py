import json
import mlflow
import dagshub
import sys
from pathlib import Path

from src.churn.logger.logger import logger
from src.churn.exception.exception import CustomException
from src.churn.entity.artifact_entity import ModelEvaluationArtifact

class ModelEvaluation:


    def initiate_model_evaluation(self):

        try:

            logger.info("Model Evaluation Started")

            dagshub.init(
                repo_owner="sudipmodak",
                repo_name="customer-churn-mlops",
                mlflow=True
            )

            metrics_path = Path(
                "artifacts/model_trainer/metrics.json"
            )

            model_path = Path(
                "artifacts/model_trainer/model.pkl"
            )

            with open(metrics_path, "r") as f:
                metrics = json.load(f)

            run_ids = []

            for model_name, model_metrics in metrics.items():

                with mlflow.start_run(
                    run_name=model_name
                ) as run:

                    mlflow.log_param(
                        "model_name",
                        model_name
                    )

                    mlflow.log_metric(
                        "train_accuracy",
                        model_metrics["train_accuracy"]
                    )

                    mlflow.log_metric(
                        "test_accuracy",
                        model_metrics["test_accuracy"]
                    )

                    mlflow.log_metric(
                        "precision",
                        model_metrics["precision"]
                    )

                    mlflow.log_metric(
                        "recall",
                        model_metrics["recall"]
                    )

                    mlflow.log_metric(
                        "f1_score",
                        model_metrics["f1_score"]
                    )

                    mlflow.log_artifact(
                        str(model_path)
                    )

                    logger.info(
                        f"{model_name} logged successfully"
                    )

                    run_ids.append(
                        run.info.run_id
                    )

            logger.info(
                "All models logged successfully"
            )

            return ModelEvaluationArtifact(
                run_id=run_ids[-1]
            )

        except Exception as e:
            raise CustomException(e, sys)


