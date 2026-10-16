import streamlit as st 
import pandas as pd
import joblib

model = joblib.load('KNN_model_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart Disease Prediction Model")
st.markdown("Kindly provide the following detailes")

age = st.slider("Age", 18,100, 40)
gender = st.selectbox ("gender",['M','F'])
chest_pain = st.selectbox("Chst pain type",["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST" , "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
ExerciseAngina = st.selectbox ("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak", 0.0, 10.0, 1.0)
st_slope = st.selectbox("ST Slope", ["UP", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        'Age' : age,
        "RestingBP" : resting_bp,
        'Cholesterol' : cholesterol,
        'FastingBS' : FastingBS,
        'MaxHR' : max_hr,
        'Oldpeak' : oldpeak,
        'Gender'  + gender : 1,
        'ChestPainType_' + chest_pain : 1,
        "RestingECG_" + resting_ecg : 1,
        'ExerciseAngina_' + ExerciseAngina : 1,
        'ST_Slope' + st_slope : 1
    }
    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
            
    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")