#education_relevance_score.py
from typing import Tuple

EXPERIENCE_SIGNALS = {
    "code review",
    "debug",
    "testing",
    "documentation",
    "agile",
    "scrum",
    "collaboration",
    "team",
    "software development",
    "object oriented",
}


def experience_relevance_score(
    resume_text: str,
    jd_text: str
) -> Tuple[float, str]:

    resume = resume_text.lower()
    jd = jd_text.lower()

    jd_hits = {k for k in EXPERIENCE_SIGNALS if k in jd}
    resume_hits = {k for k in EXPERIENCE_SIGNALS if k in resume}

    if not jd_hits:
        return 0.7, "No strong experience signals required"

    overlap = resume_hits & jd_hits
    score = len(overlap) / len(jd_hits)

    if score >= 0.7:
        return score, "Experience aligns well with job responsibilities"
    if score >= 0.4:
        return score, "Partial experience alignment"
    return score, "Limited experience alignment"
