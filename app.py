import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("models\logistic_regression_model.pkl")
scaler = joblib.load("models\scaler.pkl")

st.title("Credit Risk Prediction")
st.write("Enter the financial & personal details to predict creditworthiness.")

# -----------------------------
# Input fields
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_val = 1 if gender == "Male" else 0



income = st.number_input("Annual Income", min_value=0, value=50000)

debt = st.number_input("Debt", min_value=0, value=10000)

credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)

loan_amount = st.number_input("Loan Amount", min_value=0, value=20000)

loan_term = st.number_input("Loan Term (months)", min_value=6, max_value=360, value=60)

num_credit_cards = st.number_input("Number of Credit Cards", min_value=0, max_value=20, value=2)

payment_history = st.selectbox("Payment History", ["Bad", "Average", "Good"])
pay_map = {"Bad": 0, "Average": 1, "Good": 2}
payment_val = pay_map[payment_history]

employment = st.selectbox("Employment Status", ["Employed", "Unemployed", "Self-Employed"])
# One-hot encode manually
emp_employed = 1 if employment == "Employed" else 0
emp_self = 1 if employment == "Self-Employed" else 0
# Unemployed → (0,0)

residence = st.selectbox("Residence Type", ["Rented", "Owned", "Mortgaged"])
res_map = {"Rented": 0, "Owned": 1, "Mortgaged": 2}
residence_val = res_map[residence]

marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
mar_map = {"Single": 0, "Married": 1, "Divorced": 2}
marital_val = mar_map[marital]

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    # Arrange features in same order as model training
    input_data = [[
        age, gender_val, income, debt, credit_score,
        loan_amount, loan_term, num_credit_cards, payment_val,
        residence_val, marital_val, emp_employed, emp_self
    ]]

    # Scale numeric features
    input_data_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_data_scaled)
    risk = "Low Risk" if prediction[0] == 1 else "High Risk"

    st.subheader(f"Predicted Credit Risk: {risk}")
