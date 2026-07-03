# Exercise 02 — FastAPI Endpoint Design

## 🎯 Goal
Build a minimal but well-structured **FastAPI backend** following NavGurukul's clean architecture standards. This mirrors how our real backend services are structured.

## 📋 Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Open `main.py` and complete every `# TODO:` section
3. Run the server: `uvicorn main:app --reload`
4. Test your endpoints at `http://localhost:8000/docs` (auto-generated Swagger UI)
5. All endpoints must return correct responses as described in the task
6. Commit and open a PR to `dev`

## ✅ Acceptance Criteria
- [ ] Server starts without errors
- [ ] All endpoints return the correct response shapes
- [ ] Input validation works (FastAPI returns 422 for invalid inputs)
- [ ] Each route has a proper docstring / description
- [ ] Code is split into logical sections (routes, models, utils)
- [ ] Environment config uses `.env` — no hardcoded values
- [ ] PR is opened against `dev`

## 💡 Hints
- Use Pydantic `BaseModel` for request/response schemas
- Use `HTTPException` to return proper error responses
- Check `http://localhost:8000/docs` — FastAPI generates Swagger docs automatically
