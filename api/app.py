import pandas as pd 
import joblib
from flask import Flask, request
model = joblib.load(r'C:\Users\juman\OneDrive\Desktop\Prog\telecom-churn\models\telcomdata.joblib')

app = Flask(__name__)
def prepare_data(data):
    gender = data.get('gender')
    SeniorCitizen = data.get('SeniorCitizen')
    Partner = data.get('Partner')
    Dependents = data.get('Dependents')
    tenure = data.get('tenure')
    PhoneService = data.get('PhoneService')
    MultipleLines = data.get('MultipleLines')
    InternetService = data.get('InternetService')
    OnlineSecurity = data.get('OnlineSecurity')
    OnlineBackup = data.get('OnlineBackup')
    DeviceProtection = data.get('DeviceProtection')
    TechSupport = data.get('TechSupport')
    StreamingTV = data.get('StreamingTV')
    StreamingMovies = data.get('StreamingMovies')
    Contract = data.get('Contract')
    PaperlessBilling = data.get('PaperlessBilling')
    PaymentMethod = data.get('PaymentMethod')
    MonthlyCharges = data.get('MonthlyCharges')
    TotalCharges = data.get('TotalCharges')
    example_customer = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [int(tenure)],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [float(MonthlyCharges)],
        "TotalCharges": [float(TotalCharges)]
    })
    return example_customer

@app.route('/predict', methods=['GET'])
def predict():
    data = request.form
    prepared_data = prepare_data(data)
    pred = model.predict(prepared_data)[0]
    if pred == 'Yes':
        return 'Churn'
    else:
        return 'Not Churn'
    
app.run()
