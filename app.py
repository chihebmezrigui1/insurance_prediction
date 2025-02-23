import streamlit as st
import pickle
import numpy as np

# Charger le modèle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Interface utilisateur Streamlit
st.title("Predicting Medical Insurance Charges")

# Saisie des entrées utilisateur
age = st.number_input("Âge", min_value=0, max_value=100, value=30)
bmi = st.number_input("BMI (Indice de Masse Corporelle)", min_value=10.0, max_value=50.0, value=25.0)
sex = st.selectbox("Sexe", ["female", "male"])  # Correspond à sex_female et sex_male
children = st.number_input("Nombre d'enfants", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Fumeur ?", ["no", "yes"])  # Correspond à smoker_no et smoker_yes
region = st.selectbox("Région", ["northeast", "northwest", "southeast", "southwest"])

# Encodage One-Hot pour le sexe (2 colonnes)
sex_female = 1 if sex == "female" else 0
sex_male = 1 if sex == "male" else 0

# Encodage One-Hot pour fumeur (2 colonnes)
smoker_no = 1 if smoker == "no" else 0
smoker_yes = 1 if smoker == "yes" else 0

# Encodage One-Hot pour la région (4 colonnes)
region_northeast = 1 if region == "northeast" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Vérifier le nombre total de colonnes envoyées au modèle
features = np.array([[age, bmi, children, sex_female, sex_male, smoker_no, smoker_yes, 
                      region_northeast, region_northwest, region_southeast, region_southwest]])

# Bouton pour la prédiction
if st.button("Prédire les Charges Médicales"):
    prediction = model.predict(features)
    st.success(f"Predicting Medical Insurance Charges: **{prediction[0]:,.2f} USD**")
