import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Ensure models directory exists
# Get directory of this script: .../ml_training
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Models should be in .../backend/models
MODEL_DIR = os.path.join(BASE_DIR, "..", "backend", "models")
os.makedirs(MODEL_DIR, exist_ok=True)

def train_flood_model():
    print("Training Flood Prediction Model...")
    # Synthetic Data: Rainfall (mm), Humidity (%), River Level (m) -> Flood Risk (0: No, 1: Yes)
    np.random.seed(42)
    data_size = 1000
    
    rainfall = np.random.uniform(0, 500, data_size)
    humidity = np.random.uniform(30, 100, data_size)
    river_level = np.random.uniform(0, 15, data_size)
    
    # Logic: High rainfall + High river level = Flood
    flood_risk = []
    for r, h, l in zip(rainfall, humidity, river_level):
        if r > 300 and l > 10:
            flood_risk.append(1)
        elif r > 200 and l > 8 and h > 80:
            flood_risk.append(1)
        else:
            flood_risk.append(0)
            
    df = pd.DataFrame({
        'rainfall': rainfall,
        'humidity': humidity,
        'river_level': river_level,
        'flood': flood_risk
    })
    
    X = df[['rainfall', 'humidity', 'river_level']]
    y = df['flood']
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    # Evaluate
    accuracy = model.score(X, y)
    print(f"Flood Model Accuracy: {accuracy:.2f}")
    
    joblib.dump(model, os.path.join(MODEL_DIR, 'flood_model.pkl'))
    print("Saved flood_model.pkl")

def train_earthquake_model():
    print("\nTraining Earthquake Prediction Model...")
    # Synthetic Data: Magnitude, Depth (km) -> Risk Level (0: Low, 1: High)
    np.random.seed(42)
    data_size = 1000
    
    magnitude = np.random.uniform(2, 9, data_size)
    depth = np.random.uniform(5, 700, data_size)
    
    # Logic: High magnitude + Shallow depth = High Risk
    eq_risk = []
    for m, d in zip(magnitude, depth):
        if m > 6.0:
            eq_risk.append(1)
        elif m > 5.0 and d < 50:
            eq_risk.append(1)
        else:
            eq_risk.append(0)
            
    df = pd.DataFrame({
        'magnitude': magnitude,
        'depth': depth,
        'risk': eq_risk
    })
    
    X = df[['magnitude', 'depth']]
    y = df['risk']
    
    model = LogisticRegression()
    model.fit(X, y)
    
    accuracy = model.score(X, y)
    print(f"Earthquake Model Accuracy: {accuracy:.2f}")
    
    joblib.dump(model, os.path.join(MODEL_DIR, 'earthquake_model.pkl'))
    print("Saved earthquake_model.pkl")

if __name__ == "__main__":
    train_flood_model()
    train_earthquake_model()
