import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    print("NO OPENROUTER_API_KEY in environment")
    raise SystemExit(1)

URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
PAYLOAD = {
    "model": os.getenv("LLM_MODEL", "deepseek/deepseek-chat"),
    "messages": [{"role": "user", "content": "Rewrite this professionally: Add AWS and Docker to skills."}],
    "temperature": 0.3,
}

print('Sending request to OpenRouter...')
resp = requests.post(URL, headers=HEADERS, json=PAYLOAD, timeout=15)
print('Status:', resp.status_code)
try:
    print('Body:', resp.json())
except Exception:
    print('Raw body:', resp.text)
