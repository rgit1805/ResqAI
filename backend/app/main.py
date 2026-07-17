from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Disaster Readiness API", version="1.0")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Models
models = {}
# Get the directory where this script (main.py) is located: .../backend/app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Models are in .../backend/models
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

@app.on_event("startup")
def load_models():
    try:
        models["flood"] = joblib.load(os.path.join(MODEL_DIR, "flood_model.pkl"))
        models["earthquake"] = joblib.load(os.path.join(MODEL_DIR, "earthquake_model.pkl"))
        print(f"Models loaded successfully from {MODEL_DIR}")
    except Exception as e:
        print(f"Error loading models: {e}")

# Data Models
class FloodInput(BaseModel):
    rainfall: float
    humidity: float
    river_level: float

class EarthquakeInput(BaseModel):
    magnitude: float
    depth: float

@app.get("/")
def home():
    return {"message": "Disaster Readiness API is Online"}

@app.post("/predict/flood")
def predict_flood(data: FloodInput):
    if "flood" not in models:
        raise HTTPException(status_code=503, detail="Flood model not loaded")
    
    df = pd.DataFrame([data.dict()])
    # Get probability of class 1 (Flood)
    probability = models["flood"].predict_proba(df)[0][1]
    
    if probability < 0.3:
        risk_level = "Safe"
        alert = "Conditions are normal."
    elif 0.3 <= probability < 0.6:
        risk_level = "Warning"
        alert = "Be cautious. Monitor local news."
    else:
        risk_level = "Emergency"
        alert = "HIGH RISK! Evacuate immediately."
    
    return {
        "disaster_type": "flood",
        "risk_level": risk_level,
        "probability": float(probability),
        "alert": alert
    }

@app.post("/predict/earthquake")
def predict_earthquake(data: EarthquakeInput):
    if "earthquake" not in models:
        raise HTTPException(status_code=503, detail="Earthquake model not loaded")
        
    df = pd.DataFrame([data.dict()])
    probability = models["earthquake"].predict_proba(df)[0][1]
    
    # Earthquake probabilities are often lower/harder, but we'll use same logic for demo
    if probability < 0.3:
        risk_level = "Low"
        alert = "Seismic activity is stable."
    elif 0.3 <= probability < 0.7:
        risk_level = "Moderate"
        alert = "Potential tremors. Secure objects."
    else:
        risk_level = "Critical"
        alert = "MAJOR EARTHQUAKE DETECTED. DROP, COVER, HOLD ON."
    
    return {
        "disaster_type": "earthquake",
        "risk_level": risk_level,
        "probability": float(probability),
        "alert": alert
    }
