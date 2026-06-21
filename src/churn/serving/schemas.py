from pydantic import BaseModel

class PredictionResponse(BaseModel):
    total_customer: int
    churn_count: int
    retention_count: int