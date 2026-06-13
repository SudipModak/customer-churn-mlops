

from churn.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from churn.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

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
    
    