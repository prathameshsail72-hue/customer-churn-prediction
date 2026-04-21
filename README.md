# 🚀 Customer Churn Prediction using Machine Learning

An end-to-end **Machine Learning project** that predicts whether a telecom customer is likely to churn based on their demographics, account details, and service usage.

This project demonstrates a **production-style ML pipeline**, model training, and deployment using an interactive **Streamlit web application**.

---

## 📌 Problem Statement

Customer churn is a critical business problem in the telecom industry. Retaining existing customers is significantly more cost-effective than acquiring new ones.

👉 The goal of this project is to:
- Predict whether a customer will churn
- Help businesses take proactive retention actions

---

## 🧠 Project Highlights

- ✅ End-to-end ML pipeline (Preprocessing → Feature Selection → Model)
- ✅ Handling missing values and categorical data
- ✅ Feature scaling and encoding using `ColumnTransformer`
- ✅ Feature selection using `RandomForest`
- ✅ Model training using **Gradient Boosting**
- ✅ Evaluation using **Accuracy & ROC-AUC**
- ✅ Modular and production-ready code structure
- ✅ Interactive UI using **Streamlit**

---

## 🏗️ Project Structure
```
customer-churn-prediction/
│
├── app/
│ └── app.py # Streamlit UI
│
├── src/
│ ├── pipeline.py # ML pipeline creation
│ ├── train.py # Model training script
│ └── predict.py # Prediction logic
│
├── models/
│ └── churn_model.pkl # Trained model (generated)
│
├── data/
│ └── raw/
│ └── Customer-Churn.csv
│
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Libraries:**  
  - Pandas, NumPy  
  - Scikit-learn  
  - Joblib  
  - Streamlit  

---

## 📊 Model Details

- **Feature Engineering:**
  - Missing value imputation
  - One-hot encoding for categorical variables
  - Standard scaling for numerical features

- **Feature Selection:**
  - `SelectFromModel` using Random Forest

- **Model Used:**
  - Gradient Boosting Classifier

- **Evaluation Metrics:**
  - Accuracy
  - ROC-AUC Score

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

## 🖥️ Application Preview

### 📌 User Interface
<img src="assets\p1.png" width="700">

### 📊 Prediction Result
<img src="assets\p2.png" width="700">

### 🎥 Demo Video
Watch the demo here:  
👉 https://github.com/prathameshsail72-hue/customer-churn-prediction/blob/main/assets/p3.mp4
