from fastapi import Request, APIRouter
from pydantic import BaseModel
import time

from core.ats_engine import analyze_resume
from llm.suggestions import enhance_suggestions
from llm.rate_limiter import can_usage_llm
from config import settings

router = APIRouter()

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str
    use_llm: bool = False

@router.post("/analyze")
def analyze(payload: AnalyzeRequest, request: Request):
    print("✅ /analyze HIT")
    start = time.time()

    result = analyze_resume(
        resume_text=payload.resume_text,
        jd_text=payload.job_description,
    )

    print("✅ analyze_resume done in", time.time() - start, "seconds")

    if payload.use_llm:
        client_id = getattr(request.client, "host", None) or "unknown"

        if can_usage_llm(client_id):
            print("🤖 LLM enhancement started")
            result = enhance_suggestions(result)
            print("🤖 LLM enhancement finished")
        else:
            result["llm_error"] = "Daily AI limit reached"

    result["llm_enabled"] = payload.use_llm
    return result
