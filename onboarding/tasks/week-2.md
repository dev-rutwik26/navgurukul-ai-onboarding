# Week 2 Tasks — First Real Contribution

**Goal:** Build the FastAPI exercise, review a teammate's PR, and pick up your first real task from the sprint board.

---

## Day 1–3: FastAPI Exercise

### Task 2.1 — Complete Exercise 02 (FastAPI Basics)
- Open [`exercises/02_fastapi_basics/main.py`](../../exercises/02_fastapi_basics/main.py)
- Install deps: `pip install -r exercises/02_fastapi_basics/requirements.txt`
- Complete all `# TODO:` sections
- Run: `uvicorn main:app --reload` from the `02_fastapi_basics/` folder
- Verify all endpoints at `http://localhost:8000/docs`
- **Acceptance criteria:**
  - [ ] `POST /students` creates a student and validates email
  - [ ] `GET /students?grade=10` filters by grade correctly
  - [ ] `GET /students/{id}` returns 404 for unknown IDs
  - [ ] `DELETE /students/{id}` removes the student
  - [ ] `POST /sessions` requires a valid student_id
  - [ ] `GET /stats` returns correct counts and averages
  - [ ] PR includes screenshot of `/docs` with all endpoints visible

### Task 2.2 — Open PR for Exercise 02
- Branch: `dev/your_name` (same branch, new commits)
- PR title: `[ONBOARDING] your_name — FastAPI Exercise`
- Include in PR description:
  - Screenshot of `/docs` Swagger UI
  - What was the trickiest part to implement and why
- **Acceptance:** PR reviewed and merged to `dev`

---

## Day 3–4: Code Review Practice

### Task 2.3 — Review a Teammate's PR (Exercise 03, Task 6)
- Find an open PR from a teammate on GitHub
- Leave **at least 2 specific, constructive comments**:
  - Point out something you learned from their code
  - Suggest one improvement (with a reason, not just "change this")
- Either approve or request changes
- **Acceptance:** Review submitted on GitHub (not just "LGTM")

---

## Day 4–5: First Sprint Task

### Task 2.4 — Pick Up Your First Real Notion Task
- Go to the Notion sprint board with your team lead
- Pick a task labeled **"good first task"** or **"onboarding"**
- Create a new branch for it: `git checkout -b dev/your_name` (you're already there)
- Work on it, commit with proper messages, open a PR
- **Acceptance:** PR opened, linked to Notion task, reviewer assigned

---

## Week 2 Standup Checklist

At your **end-of-week standup**, share:
1. What features/endpoints you built in Exercise 02
2. What feedback you gave in your code review and what you learned
3. Status of your first real Notion task
4. Any architectural questions that came up
