# PredictAQI – Air Quality Prediction System

## Overview
PredictAQI is a machine learning-based system that predicts Air Quality Index (AQI) using air pollution and weather parameters.  
It also provides AQI category, health advice, and a 24-hour forecast.

---

## Features
- AQI prediction using trained ML model  
- AQI category classification  
- Health recommendations  
- 24-hour AQI forecast  
- Interactive web interface using Gradio  

---

## Input Parameters
- PM2.5  
- PM10  
- NO2  
- CO  
- Temperature  
- Humidity  
- Wind Speed  

---

## Output
- Predicted AQI  
- AQI Category  
- Health Advice  
- 24-hour AQI Forecast  

---

## Project Structure
predict-aqi/
│
├── aqi_prediction_project.ipynb
├── app.py
├── aqi_model.pkl
├── requirements.txt
└── README.md


---

## Notebook Description
The notebook (AQI_Model_Training.ipynb) contains:
- Data preprocessing  
- Feature engineering  
- Model training and evaluation  
- Model selection (Random Forest)  
- Saving the trained model  

---

## Application Description
The app.py file:
- Loads the trained model  
- Takes user input  
- Predicts AQI  
- Displays category and health advice  
- Generates 24-hour forecast  

---

## Tech Stack
- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Gradio  

---

## Model
The model is trained using historical pollution and weather data.  
Random Forest Regressor is selected as the best-performing model.

---



---

