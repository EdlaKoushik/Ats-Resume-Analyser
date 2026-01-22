#suggesion_engine.py
from typing import Dict, List, Optional
from data.skill_meta import SKILL_META
from core.role_templates import ROLE_TEMPLATES


def generate_suggestions(
    *,
    missing_skills: List[str],
    matched_skills: List[str],
    role: Optional[str] = None
) -> Dict[str, str]:

    suggestions: Dict[str, str] = {}

    # Skills
    if missing_skills:
        explained = []
        for skill in missing_skills[:6]:
            meta = SKILL_META.get(skill)
            explained.append(
                f"{skill} ({meta['why']})" if meta else skill
            )

        suggestions["skills"] = (
            "👉🏿The job description references skills not clearly shown in your resume. "
            "If you have practical exposure, consider including: "
            + ", ".join(explained)
        )
    else:
        suggestions["skills"] = (
            "👉🏿Your listed skills closely match the job description."
        )

    role_data = ROLE_TEMPLATES.get(role) if role else None

    if role_data:
        suggestions["experience"] = role_data["experience"]
        suggestions["projects"] = role_data["projects"]
    else:
        suggestions["experience"] = (
            "👉🏿Describe your responsibilities and outcomes in internships or projects, "
            "highlighting debugging, testing, and collaboration."
        )
        suggestions["projects"] = (
            "👉🏿Highlight projects that reflect real software development workflows "
            "and problem-solving scenarios."
        )

    return suggestions
