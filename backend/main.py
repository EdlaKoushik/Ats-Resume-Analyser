# backend/main.py
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router


app = FastAPI(
    title="AI RESUME ATS Analyser",
    description="ATS-style resume analysis using ML (TF-IDF +cosine similarity)",
    version="1.0.0",
)

# Configure CORS so the frontend (Vite dev server) can make requests
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)