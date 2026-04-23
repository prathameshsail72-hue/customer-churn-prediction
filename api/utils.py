import joblib
import pandas as pd

# Load model
model = joblib.load("models/churn_model.pkl")


def get_reasons(data):
    reasons = []

    if data.MonthlyCharges > 80:
        reasons.append("High monthly charges")

    if data.Contract == "Month-to-month":
        reasons.append("Short-term contract")

    if data.tenure < 12:
        reasons.append("Low tenure")

    return reasons


def get_action(prob):
    if prob > 0.8:
        return "Offer discount or retention call"
    elif prob > 0.6:
        return "Send promotional email"
    else:
        return "No immediate action needed"


def predict_churn(data):
    # ✅ Create DataFrame (VERY IMPORTANT)
    input_data = pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges": data.MonthlyCharges,
        "TotalCharges": data.TotalCharges,
        "Contract": data.Contract,
        "InternetService": data.InternetService
    }])

    # ✅ Predict
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    # ✅ Business logic
    reasons = get_reasons(data)
    action = get_action(prob)

    return prediction, prob, reasons, action