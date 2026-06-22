from pathlib import Path
import json
import numpy as np
import sys

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
accuracy_score,
precision_score,
recall_score,
f1_score,
classification_report
)
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from src.churn.logger.logger import logger
from src.churn.exception.exception import CustomException
from src.churn.utils.save_load import save_object

from src.churn.entity.config_entity import ModelTrainerConfig
from src.churn.entity.artifact_entity import (
DataTransformationArtifact,
ModelTrainerArtifact
)

class ModelTrainer:


    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        data_transformation_artifact: DataTransformationArtifact
    ):

        self.model_trainer_config = model_trainer_config
        self.data_transformation_artifact = data_transformation_artifact

    def initiate_model_trainer(self):


        try:

            logger.info("Model Training Started")

            train_arr = np.load(
                self.data_transformation_artifact.transformed_train_path
            )

            test_arr = np.load(
                self.data_transformation_artifact.transformed_test_path
            )

            logger.info("Train and Test arrays loaded successfully")

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1].astype(int)

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1].astype(int)

            logger.info("Features and target separated")

            models = {
                "LogisticRegression": LogisticRegression(
                    max_iter=2000,
                    random_state=42
                ),

                "RandomForest": RandomForestClassifier(
                    n_estimators=200,
                    random_state=42
                ),

                "XGBoost": XGBClassifier(
                    random_state=42,
                    eval_metric="logloss"
                )
            }

            all_metrics = {}

            best_model = None
            best_model_name = None
            best_f1 = 0

            for model_name, model in models.items():

                logger.info(f"Training {model_name}")

                model.fit(X_train, y_train)

                y_pred_train = model.predict(X_train)
                y_pred_test = model.predict(X_test)

                train_accuracy = accuracy_score(
                    y_train,
                    y_pred_train
                )

                test_accuracy = accuracy_score(
                    y_test,
                    y_pred_test
                )

                precision = precision_score(
                    y_test,
                    y_pred_test
                )

                recall = recall_score(
                    y_test,
                    y_pred_test
                )

                f1 = f1_score(
                    y_test,
                    y_pred_test
                )

                logger.info(
                    f"{model_name} | "
                    f"Train Accuracy: {train_accuracy:.4f} | "
                    f"Test Accuracy: {test_accuracy:.4f} | "
                    f"F1: {f1:.4f}"
                )

                all_metrics[model_name] = {
                    "train_accuracy": float(train_accuracy),
                    "test_accuracy": float(test_accuracy),
                    "precision": float(precision),
                    "recall": float(recall),
                    "f1_score": float(f1)
                }

                if f1 > best_f1:

                    best_f1 = f1
                    best_model = model
                    best_model_name = model_name

            logger.info(
                f"Best Model: {best_model_name}"
            )

            logger.info(
                f"Best F1 Score: {best_f1}"
            )

            save_object(
                self.model_trainer_config.trained_model_path,
                best_model
            )

            logger.info(
                "Best model saved successfully"
            )

            metrics_path = (
                Path(self.model_trainer_config.root_dir)
                / "metrics.json"
            )

            with open(metrics_path, "w") as f:

                json.dump(
                    all_metrics,
                    f,
                    indent=4
                )

            logger.info(
                f"Metrics saved successfully at {metrics_path}"
            )

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_path=self.model_trainer_config.trained_model_path,
                train_accuracy=all_metrics[best_model_name]["train_accuracy"],
                test_accuracy=all_metrics[best_model_name]["test_accuracy"],
                f1_score=all_metrics[best_model_name]["f1_score"]
            )

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)

