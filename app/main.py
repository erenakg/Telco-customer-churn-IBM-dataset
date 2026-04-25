from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import pickle
import os

app = FastAPI(
    title="P2P Telco Churn Tahmin API",
    description="XGBoost ve Özellik Mühendisliği Barındıran Canlı Tahmin Servisi",
    version="2.0.0"
)

# Model dosyalarını yüklüyoruz
model = joblib.load('models/churn_model.pkl')
with open('models/model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

class MüşteriVerisi(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def predict(data: MüşteriVerisi):
    input_df = pd.DataFrame([data.model_dump()])
    
    # --- Özellik Mühendisliği (Notebook ile aynı mantık) ---
    # 1. Maliyet/Bağlılık Oranı
    input_df['Tenure_to_MonthlyCharges'] = input_df['tenure'] / input_df['MonthlyCharges']
    
    # 2. Toplam Hizmet Sayısı
    hizmetler = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    input_df['Total_Services_Count'] = (input_df[hizmetler] != 'No').sum(axis=1)
    
    # Encoding ve Hizalama
    input_encoded = pd.get_dummies(input_df)
    input_final = input_encoded.reindex(columns=model_columns, fill_value=0)
    
    # Tahmin
    prediction = model.predict(input_final)[0]
    probability = model.predict_proba(input_final)[0][1]
    
    return {
        "churn_tahmini": "Yes" if prediction == 1 else "No",
        "ayrilma_olasiligi": f"%{round(probability * 100, 2)}",
        "durum": "Riskli" if probability > 0.5 else "Guvenli"
    }

@app.get("/")
def home():
    return {"mesaj": "API Canlı! Tahmin için /docs adresine gidin."}
