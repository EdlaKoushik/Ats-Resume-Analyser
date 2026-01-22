# backend/main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="AI RESUME ATS Analyser",
    description="ATS-style resume analysis using ML (TF-IDF + cosine similarity)",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ats-resume-analyser-jxoo.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- System / Health Endpoints ----

@app.get("/")
def root():
    return {"service": "AI Resume ATS Analyzer"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

# ---- Feature Routes ----
app.include_router(router)
