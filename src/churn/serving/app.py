from fastapi import FastAPI
from churn.serving.routes import router

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Customer Churn API Running"
    }