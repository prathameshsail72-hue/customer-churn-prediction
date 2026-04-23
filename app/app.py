import streamlit as st
import requests

API_URL = "https://customer-churn-prediction-xkxz.onrender.com/predict"

st.set_page_config(page_title="Churn Predictor", page_icon="📊")

st.title("📊 Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges", 0.0, 200.0)
total = st.number_input("Total Charges", 0.0, 10000.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

if st.button("Predict"):
    payload = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "Contract": contract,
        "InternetService": internet
    }

    try:
        res = requests.post(API_URL, json=payload)

        if res.status_code == 200:
            data = res.json()

            st.subheader("Result")
            st.success(f"Churn: {data['churn_prediction']}")
            st.write(f"Probability: {data['probability']}")

            st.subheader("Reasons")
            for r in data["reasons"]:
                st.write(f"- {r}")

            st.subheader("Recommended Action")
            st.info(data["recommended_action"])

        else:
            st.error(f"API Error: {res.status_code}")

    except Exception as e:
        st.error(str(e))

