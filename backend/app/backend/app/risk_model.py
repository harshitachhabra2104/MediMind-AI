"""
A placeholder lightweight risk estimator.
Replace with a trained model for better accuracy.
"""

def estimate_risk(age: int, symptoms: list, chronic_conditions: list) -> dict:
    score = 0
    # basic scoring rules (demo)
    high_risk_symptoms = ["shortness of breath", "chest pain", "confusion"]
    for s in symptoms:
        s_low = s.lower()
        if any(hr in s_low for hr in high_risk_symptoms):
            score += 3
        elif len(s_low) > 0:
            score += 1
    if age and age > 60:
        score += 2
    if chronic_conditions:
        score += len(chronic_conditions)

    # scale to level
    if score >= 6:
        level = "High"
    elif score >= 3:
        level = "Medium"
    else:
        level = "Low"

    return {"score": score, "level": level}
