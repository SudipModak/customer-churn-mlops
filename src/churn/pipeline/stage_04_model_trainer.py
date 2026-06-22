from pathlib import Path

from src.churn.configuration.configuration import ConfigurationManager
from src.churn.components.model_trainer import ModelTrainer
from src.churn.entity.artifact_entity import DataTransformationArtifact


class ModelTrainerTrainingPipeline:

    def main(self):

        config = ConfigurationManager()

        trainer_config = config.get_model_trainer_config()

        transformation_artifact = DataTransformationArtifact(
            transformed_train_path=Path(
                "artifacts/data_transformation/train.npy"
            ),
            transformed_test_path=Path(
                "artifacts/data_transformation/test.npy"
            ),
            preprocessor_path=Path(
                "artifacts/data_transformation/preprocessor.pkl"
            )
        )

        trainer = ModelTrainer(
            model_trainer_config=trainer_config,
            data_transformation_artifact=transformation_artifact
        )

        trainer.initiate_model_trainer()