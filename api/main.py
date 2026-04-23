from fastapi import FastAPI
from api.schema import CustomerData
from api.utils import predict_churn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: CustomerData):
    prediction, prob, reasons, action = predict_churn(data)

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "probability": round(prob, 2),
        "reasons": reasons,
        "recommended_action": action
    }