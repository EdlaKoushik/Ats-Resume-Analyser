# backend/llm/rate_limiter.py

#rate_limiter
from collections import defaultdict 
from datetime import date
from backend.config import settings


__llm_usage=defaultdict(lambda:{"count":0,"date":date.today()})


def can_use_llm(client_id:str) -> bool:
    today=date.today()
    record=__llm_usage[client_id]
    
    if record["date"]!=today:
        record["date"]=today
        record["count"]=0
    
    if record["count"]>=settings.MAX_LLM_CALLS_PER_DAY:
        return False
    
    record["count"]+=1
    return  True      

# compatibility alias for older import name
def can_usage_llm(client_id: str) -> bool:
    return can_use_llm(client_id)

