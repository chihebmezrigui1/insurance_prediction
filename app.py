import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit user interface
st.title("Predicting Medical Insurance Charges")

# User input fields
age = st.number_input("Age", min_value=0, max_value=100, value=30)
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
sex = st.selectbox("Sex", ["female", "male"])  # Corresponds to sex_female and sex_male
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker?", ["no", "yes"])  # Corresponds to smoker_no and smoker_yes
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# One-Hot Encoding for sex (2 columns)
sex_female = 1 if sex == "female" else 0
sex_male = 1 if sex == "male" else 0

# One-Hot Encoding for smoker (2 columns)
smoker_no = 1 if smoker == "no" else 0
smoker_yes = 1 if smoker == "yes" else 0

# One-Hot Encoding for region (4 columns)
region_northeast = 1 if region == "northeast" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Check the total number of columns sent to the model
features = np.array([[age, bmi, children, sex_female, sex_male, smoker_no, smoker_yes, 
                      region_northeast, region_northwest, region_southeast, region_southwest]])

# Button for prediction
if st.button("Predict Medical Insurance Charges"):
    prediction = model.predict(features)
    st.success(f"Predicting Medical Insurance Charges: **{prediction[0]:,.2f} USD**")
