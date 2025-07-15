# 🧠 Medical Insurance Cost Estimation Using Machine Learning

This project predicts **medical insurance charges** using a **linear regression model**, and includes a **sensitivity analysis** to test the model’s stability. A user-friendly **Streamlit web app** is also provided for live predictions.

---

## 📌 Overview

Predicting healthcare costs helps individuals plan better and assists healthcare providers in making data-driven decisions. This project explores how demographic and health-related factors influence medical charges, using machine learning for prediction and analysis.

---

## 📂 Dataset

The dataset (`insurance.csv`) contains the following features:

| Feature     | Description                                 |
|-------------|---------------------------------------------|
| `age`       | Age of the individual                       |
| `sex`       | Gender (`male` or `female`)                 |
| `bmi`       | Body Mass Index                             |
| `children`  | Number of children/dependents               |
| `smoker`    | Smoking status (`yes` or `no`)              |
| `region`    | Geographic region                           |
| `charges`   | Medical charges billed by insurance         |

---

## ✅ Project Workflow

### 1. 📊 Data Preprocessing
- Handle missing or inconsistent data
- Encode categorical features (`sex`, `smoker`, `region`)
- Normalize or standardize numerical features if needed

### 2. 🕵️ Exploratory Data Analysis (EDA)
- Visualize distributions of features like `age`, `bmi`, and `charges`
- Identify relationships and correlations
- Detect outliers or extreme values

### 3. 🧪 Model Development
- Split data into training and testing sets
- Train a Linear Regression model
- Evaluate using **R² score** and **Mean Squared Error (MSE)**

### 4. 📈 Sensitivity Analysis
- Analyze how the model performance varies with different data splits
- Assess model robustness and generalization

---

## 🗂 Project Files

- `medical_charges_prediction.ipynb`: Jupyter notebook with all steps (EDA, modeling, sensitivity analysis)
- `insurance.csv`: Dataset used for training
- `app.py`: Streamlit app to make real-time predictions
- `requirements.txt`: List of required packages

---

## 🛠 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
