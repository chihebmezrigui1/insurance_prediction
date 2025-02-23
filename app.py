import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit user interface
st.title("Predicting Medical Insurance Charges")

# User input fields with default value as None (null-like behavior)
age = st.number_input("Age", min_value=0, max_value=100, value=None)
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=None)
sex = st.selectbox("Sex", ["female", "male", None])  # Including None option
children = st.number_input("Number of Children", min_value=0, max_value=10, value=None)
smoker = st.selectbox("Smoker?", ["no", "yes", None])  # Including None option
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest", None])  # Including None option

# Check for None values and handle accordingly
sex_female = 1 if sex == "female" else (0 if sex != None else None)
sex_male = 1 if sex == "male" else (0 if sex != None else None)

smoker_no = 1 if smoker == "no" else (0 if smoker != None else None)
smoker_yes = 1 if smoker == "yes" else (0 if smoker != None else None)

region_northeast = 1 if region == "northeast" else (0 if region != None else None)
region_northwest = 1 if region == "northwest" else (0 if region != None else None)
region_southeast = 1 if region == "southeast" else (0 if region != None else None)
region_southwest = 1 if region == "southwest" else (0 if region != None else None)

# Features array with possible None values
features = np.array([[age if age is not None else 0, 
                      bmi if bmi is not None else 0, 
                      children if children is not None else 0, 
                      sex_female, sex_male, smoker_no, smoker_yes, 
                      region_northeast, region_northwest, region_southeast, region_southwest]])

# Button for prediction
if st.button("Predict Medical Insurance Charges"):
    # Handle the prediction if any value is None
    if None in features:
        st.warning("Please fill all the fields.")
    else:
        prediction = model.predict(features)
        st.success(f"Predicting Medical Insurance Charges: **{prediction[0]:,.2f} USD**")
