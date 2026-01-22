# backend/core/score_level.py
#score_level

def get_score_level(score: float) -> str:
    if score < 0.5:
        return "low"
    elif score <0.7:
        return "medium"
    else:
        return "high"