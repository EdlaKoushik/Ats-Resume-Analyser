from backend.data.skills_db import SKILLS
from backend.core.preprocessing import clean_text

# ─────────────────────────────────────────
# Implicit → Explicit skill expansion
# ─────────────────────────────────────────
IMPLICIT_SKILLS = {
    "code review": {"testing", "debugging"},
    "software testing": {"testing"},
    "collaboratively": {"teamwork", "collaboration"},
    "problem solving": {"problem-solving"},
    "object oriented": {"oop"},
    "documentation": {"documentation"},
}

def extract_skills(text: str) -> set:
    """
    Extract valid skills from raw text using a controlled vocabulary
    + implicit skill expansion (ATS-style).
    """

    text_lower = text.lower()
    tokens = clean_text(text)

    found_skills = {token for token in tokens if token in SKILLS}

    # ── Implicit skill expansion ───────────
    for phrase, implied_skills in IMPLICIT_SKILLS.items():
        if phrase in text_lower:
            found_skills.update(
                skill for skill in implied_skills if skill in SKILLS
            )

    return found_skills
