# backend/api/routes.py
from fastapi import Request, APIRouter
from pydantic import BaseModel
from core.ats_engine import analyze_resume
from backend.llm.suggestions import enhance_suggestions
from backend.llm.rate_limiter import can_usage_llm
from backend.config import settings


router = APIRouter()


class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str
    use_llm: bool = False


@router.post("/analyze")
def analyze(payload: AnalyzeRequest, request: Request):
    result = analyze_resume(
        resume_text=payload.resume_text,
        jd_text=payload.job_description,
    )

    if payload.use_llm:
        client_id = getattr(request.client, "host", None) or "unknown"

        if can_usage_llm(client_id):
            # enhance_suggestions will internally respect settings.ENABLE_LLM
            result = enhance_suggestions(result)
        else:
            result["llm_error"] = "Daily AI limit reached"

    result["llm_enabled"] = payload.use_llm
    return result

