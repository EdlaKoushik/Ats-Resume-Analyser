# ATS Resume Analyser

A full-stack resume analysis tool demonstrating programmatic ATS-style scoring and role/skill matching: a FastAPI backend for analysis and a Vite + React frontend for providing resume text and job descriptions.

This repository is a monorepo with separate `backend/` and `frontend/` folders so the services can be deployed independently.

---

## Project structure
A high-level view of the repository and the purpose of key files/folders.

- `backend/` — FastAPI application and server-side logic
  - `backend/main.py` — FastAPI app (exports `app`)
  - `backend/requirements.txt` — Python dependencies
  - `backend/.env.example` — example environment variables for server
  - `backend/core/` — core ATS logic (skill extraction, vector scoring, templates)
  - `backend/data/` — canonical skill/role datasets used by the engine

- `frontend/` — Vite + React client
  - `frontend/package.json` — npm scripts and dependencies
  - `frontend/src/App.jsx` — main UI and analyze flow
  - `frontend/src/` — other React components and assets

- Root files
  - `.gitignore` — files/folders excluded from git
  - `.env.example` — top-level note about env usage
  - `README.md` — this file

---

## What this project does
- Extracts skills and relevant tokens from resume text and job descriptions.
- Computes similarity and scoring to estimate how well a resume matches a job description.
- Exposes a simple HTTP API for analysis (e.g., POST `/analyze` with resume text and job description).

---

## How to use (developer quick start)

### Prerequisites
- Python 3.11+
- Node.js 16+

### Run backend (development)
Open PowerShell in the project root and run:

```powershell
python -m venv .venv
& '.\.venv\Scripts\Activate.ps1'
pip install -r backend/requirements.txt
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Notes:
- For production, run the backend with an ASGI server such as Gunicorn + Uvicorn worker:
  `gunicorn -k uvicorn.workers.UvicornWorker backend.main:app --bind 0.0.0.0:$PORT`
- Configure environment variables needed by the backend in your host; do not commit secrets.

### Run frontend (development)
Open PowerShell in the `frontend` folder and run:

```powershell
cd frontend
npm install
npm run dev
```

Vite will print a local URL (usually `http://localhost:5173`). The frontend calls the backend API (check `frontend/src/App.jsx` for the exact endpoint); set `VITE_API_URL` when needed.

### Example API usage
The backend exposes a POST `/analyze` endpoint for scoring resume text against a job description.

JSON example:

```powershell
curl -X POST 'http://127.0.0.1:8000/analyze' -H 'Content-Type: application/json' -d '{"resume_text":"Experienced software engineer...","job_description":"Looking for a backend engineer with Python and FastAPI experience"}'
```

---

## Build for production
- Frontend build:

```powershell
cd frontend
npm install
npm run build
```

- Backend: configure environment variables on your host (Render/Heroku/etc) and run using an ASGI server as shown above.

---

## Suggested next improvements
- Add unit tests for `backend/core` functions (skill extraction, vector scoring).
- Add E2E tests for the analyze flow between frontend and backend.
- Add a small sample data page in the frontend for quick manual testing.

---

## License
- MIT

---

## Contact
- Add your contact link or GitHub profile if you want to publish it here.

If you want, I can commit and push this README change to the repository, or add a short tree-style file listing.
