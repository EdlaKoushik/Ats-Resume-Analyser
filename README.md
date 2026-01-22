# ATS Resume Analyzer

A full-stack ATS-style resume analysis application that evaluates how well a resume matches a given job description.  
The system uses a FastAPI backend to perform text analysis and scoring, and a Vite + React frontend for user interaction.

This project is designed to demonstrate **backend development, machine-learning based text analysis, API design, and deployment** in a clean and production-ready manner.

---

## Project Overview

The ATS Resume Analyzer helps simulate how an Applicant Tracking System (ATS) evaluates resumes.

It:
- Accepts resume text and job description as input
- Extracts skills and important keywords
- Computes similarity between resume and job description
- Generates an ATS match score
- Provides matched skills, missing skills, and improvement suggestions

---

## Application Workflow

1. User enters resume text and job description in the frontend UI  
2. Frontend sends a POST request to the backend API  
3. Backend processes the input by:
   - Cleaning and preprocessing text
   - Extracting relevant skills
   - Vectorizing text using TF-IDF
   - Calculating similarity using cosine similarity
   - Applying rule-based scoring for education and experience
4. Backend returns structured analysis results
5. Frontend displays ATS score and suggestions to the user  

---

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- Fetch API

### Backend
- FastAPI
- Python
- Scikit-learn
- NumPy

### Deployment
- Frontend deployed on **Vercel**
- Backend deployed on **Render**

---

## Project Structure

.
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ frontend/
│ ├─ package.json
│ ├─ vite.config.js
│ ├─ public/
│ └─ src/
│ ├─ App.jsx
│ ├─ index.jsx
│ ├─ index.css
│ ├─ components/
│ │ └─ ... (UI components)
│ └─ assets/
│ └─ ...
└─ backend/
├─ main.py # FastAPI app (exports app)
├─ requirements.txt # Backend dependencies
├─ .env.example
├─ api/
│ └─ routes.py
├─ core/
│ ├─ ats_engine.py
│ ├─ suggestion_engine.py
│ ├─ skill_extractor.py
│ ├─ vectorizer.py
│ ├─ similarity.py
│ ├─ preprocessing.py
│ ├─ missing_skills.py
│ └─ score_level.py
├─ llm/
│ ├─ suggestions.py
│ └─ rate_limiter.py
└─ data/
├─ skills_db.py
└─ skill_meta.py


---

## API Reference

### POST `/analyze`

Analyzes resume text against a job description.

**Request Body**
```json
{
  "resume_text": "Experienced software engineer with Python and FastAPI",
  "job_description": "Looking for a backend engineer with Python",
  "use_llm": false
}
Response

{
  "ats_score": 77.04,
  "level": "high",
  "matched_skills": ["python"],
  "missing_skills": [],
  "education_note": "No strict education requirement in job description",
  "experience_note": "No strong experience signals required",
  "ml_suggestions": {
    "skills": "Your listed skills closely match the job description.",
    "experience": "Describe responsibilities and outcomes in projects or internships.",
    "projects": "Highlight projects that demonstrate real development workflows."
  }
}
Local Development Setup
Prerequisites
Python 3.11 or higher

Node.js 16 or higher

Run Backend (Development)
From the project root:

python -m venv .venv
& ".\.venv\Scripts\Activate.ps1"
pip install -r backend/requirements.txt
python -m uvicorn backend.main:app --reload --port 8000
Backend will be available at:

http://127.0.0.1:8000
Run Frontend (Development)
cd frontend
npm install
npm run dev
Frontend will be available at:

http://localhost:5173
Ensure the frontend API URL points to the backend endpoint.

Production Deployment
Backend
Run using an ASGI server such as Gunicorn with Uvicorn worker

gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
Frontend
npm run build
Deploy the build output to a static hosting service such as Vercel.

Key Highlights
End-to-end full-stack application

Real ML-based text similarity (TF-IDF + cosine similarity)

Clean API design with FastAPI

Production-ready deployment configuration

Modular and maintainable project structure

Future Enhancements
Resume PDF upload and parsing

Authentication and user dashboards

Resume history tracking

Improved skill taxonomy

Advanced ML or LLM-based feedback

License
MIT License

Author
Kaushik Edla
GitHub: https://github.com/EdlaKoushik
LinkedIn: https://www.linkedin.com/in/koushik-edla-46a7b6309/
