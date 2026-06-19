
from churn.pipeline.stage_05_model_evaluation import (
    ModelEvaluationTrainingPipeline
)
from churn.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from churn.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from churn.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from churn.pipeline.stage_04_model_trainer import(ModelTrainerTrainingPipeline)
from churn.logger.logger import logging
STAGE_NAME ="DATA INGESTION STAGE"

if __name__ == "__main__":
    
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")

    obj= DataIngestionTrainingPipeline()
    obj.main()

    logging.info(f">>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")

    STAGE_NAME="DATA VALIDATION STAGE"

    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")

    obj= DataValidationTrainingPipeline()
    obj.main()

    logging.info(f">>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
    
    STAGE_NAME="DATA TRANSFORMATION STAGE"

    logging.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<<")
    obj=DataTransformationTrainingPipeline()
    obj.main()

    logging.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<")

    STAGE_NAME = "MODEL TRAINER STAGE"

    logging.info(
        f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<"
    )

    obj = ModelTrainerTrainingPipeline()

    obj.main()

    logging.info(
        f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<"
)
    STAGE_NAME = "MODEL EVALUATION STAGE"

    logging.info(
        f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<"
    )

    obj = ModelEvaluationTrainingPipeline()

    obj.main()

    logging.info(
        f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<"
    )