import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit user interface
st.title("Predicting Medical Insurance Charges")

# User input fields with default value as None (null-like behavior)
age = st.number_input("Age", min_value=0, max_value=100, value=None, placeholder="Enter your age")
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=None, placeholder="Enter your BMI")
sex = st.selectbox("Sex", [None, "female", "male"], index=0)  # Including None option
children = st.number_input("Number of Children", min_value=0, max_value=10, value=None, placeholder="Enter number of children")
smoker = st.selectbox("Smoker?", [None, "no", "yes"], index=0)  # Including None option
region = st.selectbox("Region", [None, "northeast", "northwest", "southeast", "southwest"], index=0)  # Including None option

# Ensure all inputs are provided
if st.button("Predict Medical Insurance Charges"):
    if None in [age, bmi, sex, children, smoker, region]:
        st.error("🚨 Please fill in all required fields before predicting!")
    else:
        # One-Hot Encoding
        sex_female = 1 if sex == "female" else 0
        sex_male = 1 if sex == "male" else 0
        smoker_no = 1 if smoker == "no" else 0
        smoker_yes = 1 if smoker == "yes" else 0
        region_northeast = 1 if region == "northeast" else 0
        region_northwest = 1 if region == "northwest" else 0
        region_southeast = 1 if region == "southeast" else 0
        region_southwest = 1 if region == "southwest" else 0

        # Feature array
        features = np.array([[age, bmi, children, sex_female, sex_male, smoker_no, smoker_yes, 
                              region_northeast, region_northwest, region_southeast, region_southwest]])

        # Make prediction
        prediction = model.predict(features)
        st.success(f"💰 Predicted Medical Insurance Charges: **{prediction[0]:,.2f} USD**")
