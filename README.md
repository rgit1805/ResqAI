# ResQ-AI: AI-Driven Disaster Readiness & Response Platform

## 📌 Project Overview
ResQ-AI is a full-stack disaster management solution designed to predict natural disasters, assess risks, and manage resources efficiently. It utilizes **Machine Learning (Random Forest & Logistic Regression)** for accurate predictions and features a modern **Glassmorphism UI** for an intuitive user experience.

## ✨ Key Features
- **🤖 AI Disaster Prediction**: Predicts Floods and Earthquakes based on environmental data.
- **📊 Real-time Risk Assessment**: Classifies risk into Safe, Warning, and Emergency levels.
- **🌍 Interactive Live Map**: Visualizes high-risk zones using dynamic mapping.
- **🏥 Resource Management**: Locates nearest hospitals and shelters.
- **💎 Glassmorphism Design**: Premium, aesthetic UI with frosted glass effects.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript (Fetch API), Leaflet.js
- **Backend**: Python, FastAPI
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Data**: Synthetic datasets generated for training concepts.

## 🚀 Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. **Train Models**:
   ```bash
   python ml_training/train_models.py
   ```

3. **Run API**:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

4. **Launch UI**:
   - Open `frontend/index.html` in your web browser.

## 🔮 Future Enhancements
- Integration with live weather APIs (OpenWeatherMap).
- User authentication for admin access.
- SMS/Email automated alerts (Twilio/SendGrid).

---
*Created for ResQMind*
