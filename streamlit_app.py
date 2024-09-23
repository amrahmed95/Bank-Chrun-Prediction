import os
import streamlit as st
import pandas as pd
import numpy as np

from src.BankChurn.pipeline.prediction import PredictionPipeline

# Set the title of the Streamlit app
st.title("Bank Churn Prediction")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Train", "Predict"])

if options == "Home":
    st.header("Welcome to the Bank Churn Prediction App")
    st.write("""
        This application allows you to predict whether a customer will leave the bank 
        based on various features. Use the sidebar to navigate between training the model 
        and making predictions.
    """)
    
elif options == "Train":
    st.header("Train the Prediction Model")
    st.write("Click the button below to train the model.")

    if st.button("Train Model"):
        with st.spinner("Training in progress..."):
            try:
                # Execute the training script
                os.system("python main.py")
                st.success("Training Successful!")
            except Exception as e:
                st.error(f"An error occurred during training: {e}")

elif options == "Predict":
    st.header("Predict Customer Churn")

    # Create a form for user inputs
    with st.form(key='prediction_form'):
        CreditScore = st.number_input("Credit Score", min_value=300, max_value=850, value=600, step=1)
        Geography = st.selectbox("Geography", options=["France", "Spain", "Germany"])
        Gender = st.selectbox("Gender", options=["Male", "Female"])
        Age = st.number_input("Age", min_value=18, max_value=100, value=40, step=1)
        Tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=5, step=1)
        Balance = st.number_input("Balance", min_value=0.0, max_value=250000.0, value=100000.0, step=1000.0)
        NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4, value=2, step=1)
        IsActiveMember = st.selectbox("Is Active Member", options=["Yes", "No"])
        EstimatedSalary = st.number_input("Estimated Salary", min_value=10000, max_value=200000, value=50000, step=1000)

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        try:
            # Encode categorical variables
            geography_mapping = {"France": 0, "Spain": 1, "Germany": 2}
            gender_mapping = {"Male": 0, "Female": 1}
            is_active_mapping = {"No": 0, "Yes": 1}

            Geography_encoded = geography_mapping.get(Geography, 0)
            Gender_encoded = gender_mapping.get(Gender, 0)
            IsActiveMember_encoded = is_active_mapping.get(IsActiveMember, 0)

            # Prepare input data
            pred_args = [
                CreditScore,
                Geography_encoded,
                Gender_encoded,
                Age,
                Tenure,
                Balance,
                NumOfProducts,
                IsActiveMember_encoded,
                EstimatedSalary
            ]
            pred_args = np.array(pred_args).reshape(1, -1)

            # Make prediction
            pred_pipeline = PredictionPipeline()
            prediction = pred_pipeline.predict(pred_args)

            # Interpret the prediction
            if prediction == 0:
                msg = "The customer most probably **will not** leave the bank."
            elif prediction == 1:
                msg = "The customer most probably **will** leave the bank soon."
            else:
                msg = "The prediction is neither 0 nor 1."

            st.success(f"Prediction: {prediction}")
            st.info(msg)

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
