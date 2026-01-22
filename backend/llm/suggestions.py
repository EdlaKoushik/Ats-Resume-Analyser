# backend/llm/suggestions.py

#suggestions

import requests
from config import settings

OPENROUTER_URL="https://openrouter.ai/api/v1/chat/completions"

def enhance_suggestions(ml_output:dict)-> dict:
    
    """
    Uses LLM to rewrite ML suggestions in a more human-friendly way.
    If LLM is disabled or fails , return original ML output.
    """
    
    if not settings.ENABLE_LLM  or not settings.OPENROUTER_API_KEY:
        ml_output["llm_used"] = False
        ml_output["llm_error"] = "LLM disabled or API key missing"
        return  ml_output
    
    prompt=f"""

    You are an assistant,professional resume editor helping job seekers improve resumes.
    Given this ATS analysis:
    
    
    Rewrite the suggestions clearly,concise and professionally.
    present them in bullet points
    Rules:
    - Do NOT add new skills
    - Do NOT remove any skills
    - Do NOT change meaning
    - Do NOT change ATS score
    - Do NOT promise job selection
    Content to rewrite:
    {ml_output["ml_suggestions",""]}
    """
    
    headers={"Authorization":f"Bearer {settings.OPENROUTER_API_KEY}",
             "Content-Type":"application/json"
             }
    
    payload={
        "model":settings.LLM_MODEL,
        "messages":[{"role":"user","content":prompt}],
        "temperature":0.4
    }
    
    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        content = data.get("choices", [])[0].get("message", {}).get("content")

        ml_output["llm_suggestions"] = content
        ml_output["llm_used"] = True
        return ml_output

    except requests.HTTPError as e:
        ml_output["llm_used"] = False
        ml_output["llm_error"] = f"HTTPError: {e} - {getattr(e.response, 'text', '')}"
        return ml_output

    except Exception as e:
        ml_output["llm_used"] = False
        ml_output["llm_error"] = str(e)
        return ml_output