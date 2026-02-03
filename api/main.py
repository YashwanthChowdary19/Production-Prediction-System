from fastapi import FastAPI
from .schema import PredictionRequest, PredictionResponse
import numpy as np
import pandas as pd
import joblib
import os

app = FastAPI(title="Manufacturing Output Prediction API")

# -------------------------
# Load model & scaler
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models", "linear_regression_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

# -------------------------
# EXACT feature list used during training
# -------------------------
FEATURE_COLUMNS = list(scaler.feature_names_in_)

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    try:
        # Create empty input with correct order
        input_dict = {col: 0 for col in FEATURE_COLUMNS}

        # Fill values coming from request
        for key, value in data.dict().items():
            if key in input_dict:
                input_dict[key] = value

        # Create DataFrame WITH EXACT ORDER
        input_df = pd.DataFrame([input_dict], columns=FEATURE_COLUMNS)

        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)

        return {"parts_per_hour": float(prediction[0])}

    except Exception as e:
        print("🔥 PREDICTION ERROR:", e)
        raise e
