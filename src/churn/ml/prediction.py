from churn.utils.save_load import load_object
import pandas as pd


class PredictionPipeline:

    def __init__(self):

        self.model = load_object(
            "artifacts/model_trainer/model.pkl"
        )

        self.preprocessor = load_object(
            "artifacts/data_transformation/preprocessor.pkl"
        )

    def predict(self, df):

        # same preprocessing as training

        df["Total Charges"] = pd.to_numeric(
            df["Total Charges"],
            errors="coerce"
        )

        df["Zip Code"] = pd.to_numeric(
            df["Zip Code"],
            errors="coerce"
        )

        drop_columns = [
            "CustomerID",
            "Country",
            "State",
            "City",
            "Lat Long",
            "Churn Label",
            "Churn Reason"
        ]

        existing_cols = [
            col for col in drop_columns
            if col in df.columns
        ]

        df = df.drop(
            columns=existing_cols
        )

        transformed_data = self.preprocessor.transform(df)

        prediction = self.model.predict(
            transformed_data
        )

        return prediction