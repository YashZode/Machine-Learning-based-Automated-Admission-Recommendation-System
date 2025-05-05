# --------------------------------------------
# File: predict_admission.py
# Description: Predicts chance of admission using a trained Linear Regression model
# --------------------------------------------

import os
import joblib
import numpy as np

# Load model
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/admit_model.pkl"))
model = joblib.load(model_path)

def predict_admission_chance(
    gre_score,
    toefl_score,
    university_rating,
    sop_score,
    lor_score,
    cgpa,
    research
):
    """
    Predict admission probability using trained Linear Regression model.

    Args:
        gre_score (float): GRE score
        toefl_score (float): TOEFL score
        university_rating (int): Rating of the university (1 to 5)
        sop_score (float): SOP strength (1.0 to 5.0)
        lor_score (float): LOR strength (1.0 to 5.0)
        cgpa (float): CGPA (0 to 10)
        research (int): 0 or 1 indicating research experience

    Returns:
        dict: Contains predicted admission chance (0-100%) and classification
    """
    features = np.array([
        gre_score,
        toefl_score,
        university_rating,
        sop_score,
        lor_score,
        cgpa,
        research
    ]).reshape(1, -1)

    prediction = model.predict(features)[0] * 100
    label = "High" if prediction > 75 else "Moderate" if prediction > 50 else "Low"

    return {
        "admit_chance": round(prediction, 2),
        "classification": label
    }
