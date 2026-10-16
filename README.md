# Heart-Disease-Prediction-Model

An interactive web application built with Streamlit that utilizes a Machine Learning model to predict the likelihood of heart disease based on clinical patient metrics.

## 🚀 Features
* **User-Friendly UI:** Built using Streamlit for seamless data input via sliders, dropdowns, and number inputs.
* **Predictive Power:** Utilizes a pre-trained K-Nearest Neighbors (KNN) classification model.
* **Real-time Inference:** Automatically scales user inputs to provide immediate predictions upon clicking the interface.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Machine Learning Framework:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** Joblib

## 📁 Repository Structure
* `app.py` - The main Python script containing the Streamlit web application layout and prediction logic.
* `KNN_model_heart.pkl` - The trained K-Nearest Neighbors machine learning model.
* `scaler.pkl` - The saved feature scaler object used to normalize raw user inputs.
* `columns.pkl` - The saved structure containing the expected feature names and order for the model.
* `heart.csv` - The raw dataset used for training and evaluating the model.

## 💻 Installation & Setup

Follow these steps to run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Install Required Dependencies
Ensure you have Python installed, then install the necessary libraries:
```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the Application
Start the local development server using Streamlit:
```bash
streamlit run app.py
```
Once executed, the application will automatically open in your default web browser at `http://localhost:8501`.

## 📊 Model Features Analysed
The application takes the following clinical inputs to determine the risk status:
* **Age & Gender**
* **Chest Pain Type:** ATA, NAP, TA, ASY
* **Resting Blood Pressure:** (mm Hg)
* **Cholesterol Level:** (mg/dl)
* **Fasting Blood Sugar:** (> 120 mg/dl)
* **Resting ECG Results:** Normal, ST, LVH
* **Max Heart Rate**
* **Exercise-Induced Angina:** Yes / No
* **Oldpeak:** ST depression induced by exercise relative to rest
* **ST Slope:** Up, Flat, Down
