# backend/config.py
#config.py
import os

class Settings:
    # App
    APP_NAME = "AI Resume ATS Analyzer"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    # LLM toggle
    ENABLE_LLM = os.getenv("ENABLE_LLM", "false").lower() == "true"

    # OpenRouter / DeepSeek
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    LLM_MODEL = os.getenv("LLM_MODEL", "deepseek/deepseek-chat")

    # Rate limiting
    MAX_LLM_CALLS_PER_DAY = int(os.getenv("MAX_LLM_CALLS_PER_DAY", "5"))
    

settings = Settings()
# Temporary debug output to verify env loading for LLM during development.
# print("LLM ENABLED:", settings.ENABLE_LLM)
# print("OPENROUTER KEY PRESENT:", bool(settings.OPENROUTER_API_KEY))
