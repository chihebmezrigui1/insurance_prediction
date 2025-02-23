
## License and Copyright

This project is ©2025 Chihab MEZRIGUI . All rights reserved.

You may not reproduce, distribute, or modify this project without permission from the author.

This project is for educational purposes only and is not intended for commercial use.


# Medical-Insurance-Cost-Estimation-Using-Machine-Learning

This repository contains a machine learning model built using linear regression to predict medical charges, along with a sensitivity analysis to assess the stability and reliability of the model.

## Overview

Understanding the determinants of healthcare costs is critical for both individuals and healthcare organizations. By identifying the key factors that influence medical charges, stakeholders can allocate resources more effectively and make informed policy decisions. This project leverages linear regression to predict healthcare costs based on demographic and health-related information.

## Dataset

The dataset consists of the following features:

- **age**: The age of the individual.
- **sex**: Gender of the individual (male or female).
- **bmi**: Body Mass Index (BMI) value.
- **children**: Number of children or dependents.
- **smoker**: Smoking status (yes or no).
- **region**: The region where the individual resides.
- **charges**: The medical expenses billed to the individual by insurance.

## Key Tasks

### Data Preprocessing
- Handle missing or inconsistent data.
- Convert categorical columns (such as sex, smoker, region) into numerical values using encoding techniques.
- Normalize or standardize numerical features if necessary.

### Exploratory Data Analysis (EDA)
- Investigate the distribution of important features like age, BMI, and charges.
- Explore relationships between input variables and medical charges.
- Identify any potential outliers or influential data points.

### Model Development
- Split the dataset into training and testing subsets.
- Build a linear regression model to make predictions.
- Evaluate the model using performance metrics like R-squared and Mean Squared Error (MSE).

### Advanced Techniques
- Explore regularized regression models (Ridge, Lasso) to evaluate whether they improve the model's performance.
- Perform a sensitivity analysis to determine the impact of changes in the training data on model outcomes.

## Project Files

- **medical_charges_prediction.ipynb**: Jupyter Notebook containing steps for data processing, exploratory analysis, model training, and sensitivity testing.
- **insurance.csv**: The dataset containing medical charges and associated attributes.

## Required Libraries

- Python 3.x
- Jupyter Notebook
- pandas
- scikit-learn
- matplotlib

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/chihebmezrigui1/insurance_prediction.git
    ```

2. Install dependencies if you haven't already:

    ```bash
    pip install -r requirements.txt
    ```

3. Open the Notebook `insurance_prediction.ipynb`  

## Model Performance

- The linear regression model produced an **R-squared** value of **0.78** and a **Mean Squared Error** of **0.23**.
- The sensitivity analysis indicated significant variability in the model's performance across different training and testing splits, suggesting that the model's results are sensitive to variations in the dataset.

## Streamlit Deployment

To make the prediction model accessible through a simple web interface, this project also includes a **Streamlit app**.

### How to Run the Streamlit App



1. In the project directory, run the following command to launch the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. The app will open in your web browser where you can input the necessary data (age, BMI, smoking status, etc.), and it will display the predicted medical charges based on the trained model.

### Streamlit Interface

The Streamlit app allows users to:
- Input their **age**, **BMI**, **number of children**, **smoking status**, and **region**.
- See a prediction of the **medical charges** based on the input data.

The app uses the trained model and presents the prediction in a user-friendly interface with interactive controls.

## Conclusion

Linear regression serves as a useful baseline for predicting medical expenses based on demographic and health-related information. Further refinements, such as using regularized regression methods and a deeper sensitivity analysis, could improve the model’s generalizability and robustness.

## Acknowledgements

The dataset used in this project is publicly available on Kaggle.
