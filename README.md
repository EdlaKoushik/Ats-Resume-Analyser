# AI Resume Analyser

Minimal instructions to run, test, and push this repository to GitHub.

Folders
- `backend/` - FastAPI backend
- `frontend/frontend/` - Vite + React frontend

Quick start (local)
1. From project root, create and activate a Python venv:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
& '.\.venv\Scripts\Activate.ps1'
```

2. Install backend requirements (generate `requirements.txt` if missing):

```powershell
# If you haven't generated it yet, create from your venv:
# pip freeze > requirements.txt
pip install -r requirements.txt
```

3. Start backend (from project root):

```powershell
cd backend
python -m uvicorn backend.main:app --reload --port 8000
```

4. Start frontend (in a separate terminal):

```powershell
cd frontend/frontend
npm install
npm run dev
```

Environment variables
- Copy `backend/.env.example` to `backend/.env` and fill values before running in production.

Preparing to push
1. Make any final changes.
2. Stage and commit:

```powershell
git add .
git commit -m "Prepare repo for GitHub"
```

3. Add remote and push:

```powershell
git remote add origin git@github.com:<your-user>/<your-repo>.git
git push -u origin main
```

CI / Deployment
- A simple GitHub Actions workflow is included at `.github/workflows/ci.yml` that will run on push and attempt a backend/ frontend build.

Notes
- Keep secrets (API keys) out of the repo. Use GitHub Secrets for CI/deploy.
- Update `requirements.txt` by running `pip freeze > requirements.txt` from the activated venv.
