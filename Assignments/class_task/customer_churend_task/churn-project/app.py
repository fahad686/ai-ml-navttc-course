import streamlit as st
import pandas as pd
import joblib
import json

# Load Model, Encoders, and Feature Names
MODEL_PATH = "models/best_model.joblib"
ENCODER_PATH = "models/label_encoders.joblib"
FEATURE_PATH = "models/feature_names.json"

model = joblib.load(MODEL_PATH)
label_encoders = joblib.load(ENCODER_PATH)
with open(FEATURE_PATH, "r") as f:
    feature_names = json.load(f)

st.set_page_config(page_title="📊 Customer Churn Prediction", layout="centered")
st.title("🔮 Fahad Customer Churn Prediction System")

st.write("Enter customer details below or select a test example:")

# 🔥 NEW: Predefined test examples
test_examples = {
    "— Select —": {},
    "Loyal Premium Member (Stay)": {
        "Gender": "Male",
        "Subscription Type": "Premium",
        "Contract Length": "Annual",
        "Age": 35,
        "Tenure": 36,
        "Usage Frequency": 25,
        "Support Calls": 1,
        "Payment Delay": 0,
        "Total Spend": 3000,
        "Last Interaction": 5,
    },
    "New Low-Usage User (Churn)": {
        "Gender": "Female",
        "Subscription Type": "Basic",
        "Contract Length": "Monthly",
        "Age": 22,
        "Tenure": 1,
        "Usage Frequency": 2,
        "Support Calls": 6,
        "Payment Delay": 25,
        "Total Spend": 100,
        "Last Interaction": 60,
    },
    "Frequent Standard User (Stay)": {
        "Gender": "Male",
        "Subscription Type": "Standard",
        "Contract Length": "Quarterly",
        "Age": 29,
        "Tenure": 12,
        "Usage Frequency": 20,
        "Support Calls": 2,
        "Payment Delay": 5,
        "Total Spend": 1500,
        "Last Interaction": 10,
    },
    "At-Risk Annual User (Churn)": {
        "Gender": "Female",
        "Subscription Type": "Premium",
        "Contract Length": "Annual",
        "Age": 45,
        "Tenure": 6,
        "Usage Frequency": 5,
        "Support Calls": 4,
        "Payment Delay": 15,
        "Total Spend": 400,
        "Last Interaction": 50,
    },
}

# 🔥 NEW: Dropdown to auto-fill form
selected_example = st.selectbox("Choose a test example:", list(test_examples.keys()))

example_data = test_examples[selected_example]

with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"], index=0 if not example_data else ["Male", "Female"].index(example_data["Gender"]))
    subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"], 
                                     index=0 if not example_data else ["Basic", "Standard", "Premium"].index(example_data["Subscription Type"]))
    contract_length = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"],
                                   index=0 if not example_data else ["Monthly", "Quarterly", "Annual"].index(example_data["Contract Length"]))
    age = st.number_input("Age", min_value=18, max_value=100, value=example_data.get("Age", 30))
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=example_data.get("Tenure", 12))
    usage_freq = st.number_input("Usage Frequency", min_value=0, max_value=50, value=example_data.get("Usage Frequency", 10))
    support_calls = st.number_input("Support Calls", min_value=0, max_value=20, value=example_data.get("Support Calls", 1))
    payment_delay = st.number_input("Payment Delay (days)", min_value=0, max_value=100, value=example_data.get("Payment Delay", 10))
    total_spend = st.number_input("Total Spend ($)", min_value=0, max_value=5000, value=example_data.get("Total Spend", 500))
    last_interaction = st.number_input("Last Interaction (days ago)", min_value=0, max_value=365, value=example_data.get("Last Interaction", 5))
    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    try:
        input_data = {
            "Gender": [gender],
            "Subscription Type": [subscription_type],
            "Contract Length": [contract_length],
            "Age": [age],
            "Tenure": [tenure],
            "Usage Frequency": [usage_freq],
            "Support Calls": [support_calls],
            "Payment Delay": [payment_delay],
            "Total Spend": [total_spend],
            "Last Interaction": [last_interaction],
        }

        input_df = pd.DataFrame(input_data)

        # Encode categorical features
        for col in label_encoders.keys():
            le = label_encoders[col]
            input_df[col] = le.transform(input_df[col])

        # ✅ Auto-fix feature order and missing columns
        for col in feature_names:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[feature_names]

        # Predict
        pred = model.predict(input_df)[0]

        # 🎯 Display result clearly on screen
        st.markdown("---")
        st.subheader("📊 Prediction Result:")

        if pred == 1:
            st.error("⚠️ **Customer will CHURN (Leave the service)**")
        else:
            st.success("✅ **Customer will STAY (Continue the service)**")

    except Exception as e:
        st.error(f"❌ Error: {e}")
