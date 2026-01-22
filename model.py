import os
import joblib
import pandas as pd

# -----------------------------
# Resolve base directory
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "credit_risk_logistic_pipeline.pkl"
)

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Prediction function
# -----------------------------
def predict_default_probability(input_data: dict) -> float:
    """
    Predict probability of credit card default
    """
    input_df = pd.DataFrame([input_data])
    return model.predict_proba(input_df)[0][1]
