import os
os.environ["HOME"] = os.getcwd()

import streamlit as st
import numpy as np
import pickle

# Load model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction features below:")

input_data = []
for i in range(30):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    input_data.append(val)

if st.button("Predict"):
    prediction = model.predict([input_data])[0]
    prob = model.predict_proba([input_data])[0][1]
    st.success(f"Prediction: **{'FRAUD' if prediction == 1 else 'NOT FRAUD'}**")
    st.info(f"Probability of Fraud: **{prob:.2%}**")
