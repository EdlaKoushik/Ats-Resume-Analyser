from core.vectorizer import vectorize_texts
from core.similarity import cosine_similarity_score
from core.skill_extractor import extract_skills
from core.score_level import get_score_level
from core.suggestion_engine import generate_suggestions

from core.education_score import education_score
from core.experience_relevance_score import experience_relevance_score
from core.role_weights import ROLE_WEIGHTS

from llm.suggestions import enhance_suggestions
from llm.rate_limiter import can_use_llm


def analyze_resume(
    resume_text: str,
    jd_text: str,
    role_level: str = "junior",
    use_llm: bool = False
) -> dict:

    resume_vec, jd_vec = vectorize_texts(resume_text, jd_text)
    similarity_score = cosine_similarity_score(resume_vec, jd_vec)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = resume_skills & jd_skills
    missing_skills = jd_skills - resume_skills

    skill_score = len(matched_skills) / max(len(jd_skills), 1)

    edu_score, edu_reason = education_score(resume_text, jd_text)
    exp_score, exp_reason = experience_relevance_score(resume_text, jd_text)

    weights = ROLE_WEIGHTS.get(role_level, ROLE_WEIGHTS["junior"])

    final_score = (
        weights["skills"] * skill_score +
        weights["education"] * edu_score +
        weights["experience"] * exp_score +
        weights["similarity"] * similarity_score
    )

    final_score = round(final_score * 100, 2)

    ml_suggestions = generate_suggestions(
        missing_skills=sorted(missing_skills),
        matched_skills=sorted(matched_skills),
        role=None
    )

    if use_llm and can_use_llm("default-user"):
        ml_output = {
            "ats_score": final_score,
            "ml_suggestions": ml_suggestions
        }
        ml_output = enhance_suggestions(ml_output)
        ml_suggestions = ml_output.get("ml_suggestions", ml_suggestions)

    return {
        "ats_score": final_score,
        "level": get_score_level(final_score / 100),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "education_note": edu_reason,
        "experience_note": exp_reason,
        "ml_suggestions": ml_suggestions,
    }
