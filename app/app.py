import streamlit as st
import requests

API_URL = "https://customer-churn-prediction-xkxz.onrender.com/predict"

st.set_page_config(page_title="Churn Predictor", page_icon="📊", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.metric-card {
    padding: 1rem;
    border-radius: 10px;
    background: #1c1f26;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Customer Churn Intelligence")
st.caption("Predict customer churn risk using machine learning")

st.subheader("🧾 Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (months)", 0, 72)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0)

with col2:
    total = st.number_input("Total Charges", 0.0, 10000.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

if st.button("🚀 Predict Churn Risk", use_container_width=True):

    payload = {
        "tenure": int(tenure),
        "MonthlyCharges": float(monthly),
        "TotalCharges": float(total),
        "Contract": contract,
        "InternetService": internet
    }

    try:
        with st.spinner("Analyzing customer behavior..."):
            res = requests.post(API_URL, json=payload, timeout=15)

        if res.status_code == 200:
            data = res.json()
            prob = data["probability"]

            # ---------- Result ----------
            st.subheader("📊 Prediction Result")

            if prob > 0.7:
                st.error(f"🔴 High Risk of Churn ({prob})")
            elif prob > 0.4:
                st.warning(f"🟡 Moderate Risk ({prob})")
            else:
                st.success(f"🟢 Low Risk ({prob})")

            # ---------- Progress Bar ----------
            st.progress(min(int(prob * 100), 100))

            # ---------- Insights ----------
            st.subheader("🧠 Insights")

            if data.get("reasons"):
                for r in data["reasons"]:
                    st.write(f"• {r}")
            else:
                st.info("✅ Customer is stable. No major risk factors detected.")

            # ---------- Recommendation ----------
            st.subheader("💡 Recommended Action")
            st.info(data.get("recommended_action", "N/A"))

        else:
            st.error(f"API Error: {res.status_code}")
            st.write(res.text)

    except Exception as e:
        st.warning("⏳ Server might be waking up, try again...")
        st.error(str(e))