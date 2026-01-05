from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("recovery_model.pkl")

@app.post("/predict")
def predict(data: dict):
    features = np.array([[
        data["amount_due"],
        data["days_overdue"],
        data["customer_risk_score"],
        data["past_recovery_rate"]
    ]])

    # Raw probability
    raw_prob = model.predict_proba(features)[0][1]

    # Clamp probability (enterprise best practice)
    recovery_prob = min(max(raw_prob, 0.05), 0.95)

    # Priority score
    priority_score = (
        0.4 * (data["amount_due"] / 50000) +
        0.3 * (data["days_overdue"] / 180) +
        0.3 * (1 - recovery_prob)
    )

    # Priority level
    if priority_score > 0.7:
        priority_level = "HIGH"
    elif priority_score > 0.4:
        priority_level = "MEDIUM"
    else:
        priority_level = "LOW"

    return {
        "recovery_probability": round(recovery_prob, 2),
        "priority_score": round(priority_score, 2),
        "priority_level": priority_level
    }
