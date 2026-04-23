import requests

url = "https://customer-churn-prediction-xkxz.onrender.com/predict"

data = {
    "tenure": 12,
    "MonthlyCharges": 70,
    "TotalCharges": 800,
    "Contract": "Month-to-month",
    "InternetService": "Fiber optic"
}

res = requests.post(url, json=data)
print(res.status_code)
print(res.text)