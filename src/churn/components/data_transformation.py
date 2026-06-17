
from churn.utils.save_load import save_object
from churn.logger.logger import logger
from churn.exception.exception import CustomException
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from churn.entity.config_entity import DataTransformationConfig
from churn.entity.artifact_entity import(DataValidationArtifact,DataTransformationArtifact)
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from churn.configuration.configuration import ConfigurationManager


class DataTransformation:
    def __init__(
            self,
            data_transformation_config: DataTransformationConfig,
            data_validation_artifact: DataValidationArtifact
    ):
        self.data_transformation_config = data_transformation_config
        self.data_validation_artifact = data_validation_artifact


    def initiate_data_transformation(self):
        try:
            logger.info("Data Transformation Started")

            if not self.data_validation_artifact.validation_status:
                raise Exception("Data Validation failed,Transformaton cannot proceed")
            
            logger.info("Reading dataset from MySQL")

            config = ConfigurationManager()

            mysql_config = config.get_mysql_config()

            password = quote_plus(mysql_config.password)

            engine = create_engine(
                f"mysql+pymysql://{mysql_config.user}:"
                f"{password}@"
                f"{mysql_config.host}:3306/"
                f"{mysql_config.database}"
            )

            df = pd.read_sql(
                "SELECT * FROM customer_churn_raw",
                con=engine
            )

            logger.info(f"Dataset loaded successfully from MySQL. Shape: {df.shape}")
            df["Total Charges"]=pd.to_numeric(df["Total Charges"],errors="coerce")
            df["Zip Code"] = pd.to_numeric(
    df["Zip Code"],
    errors="coerce"
)

            target_column = "Churn Value"

            drop_columns = [
    "CustomerID",
    "Country",
    "State",
    "City",
    "Lat Long",
    "Churn Label",
    "Churn Reason"
    
]

            X=df.drop(columns=[target_column]+drop_columns,axis=1)
            y=df[target_column]

            logger.info("Input and target features separated")

            X_train,X_test,y_train,y_test= train_test_split(
                X,y,test_size=.2,random_state=42
            )

            logger.info("Getting preprocessor object")
            preprocessor=self.get_data_transformation_object()

            logger.info("Preprocessor object loaded successfully")

            logger.info("Applying preprocessing on training dataset")
            X_train_transformed= preprocessor.fit_transform(X_train)
            logger.info("Applying preprocessing on testing dataset")

            X_test_transformed= preprocessor.transform(X_test)

            logger.info("Data transformation completed")

            train_arr=np.c_[X_train_transformed,np.array(y_train)]

            test_arr=np.c_[
                X_test_transformed,
                np.array(y_test)
            ]

            logger.info("Train and Test arrays created successfully")

            save_object(self.data_transformation_config.preprocessor_path,preprocessor)

            logger.info("Preprocessor saved successfully")

            np.save(self.data_transformation_config.transformed_train_path,train_arr)
            np.save(self.data_transformation_config.transformed_test_path,test_arr)

            logger.info("Transformed arrays saved successfully")

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_path=self.data_transformation_config.transformed_train_path,
                transformed_test_path=self.data_transformation_config.transformed_test_path,
                preprocessor_path=self.data_transformation_config.preprocessor_path
            )

            logger.info("Data Transformation Artifact Created")

            return data_transformation_artifact




        except Exception as e:
            raise CustomException(e, sys)
        

    def get_data_transformation_object(self):
        try:
            logger.info("Creating preprocessing pipeline")

            numerical_columns = ["Count",
                "Zip Code",
                "Latitude",
                "Longitude",
                "Tenure Months",
                "Monthly Charges",
                "Total Charges",
                ]
            categorical_columns = ["Gender",
                    "Senior Citizen",
                    "Partner",
                    "Dependents",
                    "Phone Service",
                    "Multiple Lines",
                    "Internet Service",
                    "Online Security",
                    "Online Backup",
                    "Device Protection",
                    "Tech Support",
                    "Streaming TV",
                    "Streaming Movies",
                    "Contract",
                    "Paperless Billing",
                    "Payment Method"]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder(handle_unknown="ignore",sparse_output=False))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            logger.info("Preprocessor object created successfully")

           

            return preprocessor
        
            

        except Exception as e:
            raise CustomException(e, sys)
        
           