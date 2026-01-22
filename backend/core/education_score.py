from typing import Tuple

UG_KEYWORDS = {
    "btech", "b.tech", "bachelor", "undergraduate", "ug",
    "computer science", "engineering", "cse", "information technology"
}

PG_KEYWORDS = {
    "mtech", "m.tech", "master", "postgraduate", "pg"
}


def education_score(resume_text: str, jd_text: str) -> Tuple[float, str]:
    resume = resume_text.lower()
    jd = jd_text.lower()

    requires_ug = any(k in jd for k in ["graduate", "bachelor", "ug"])
    requires_pg = any(k in jd for k in ["postgraduate", "master", "pg"])

    has_ug = any(k in resume for k in UG_KEYWORDS)
    has_pg = any(k in resume for k in PG_KEYWORDS)

    if requires_pg:
        if has_pg:
            return 1.0, "Postgraduate requirement satisfied"
        if has_ug:
            return 0.6, "Undergraduate detected where postgraduate preferred"
        return 0.0, "Postgraduate qualification not found"

    if requires_ug:
        if has_ug or has_pg:
            return 1.0, "Undergraduate requirement satisfied"
        return 0.0, "Undergraduate qualification not found"

    return 0.8, "No strict education requirement in job description"
