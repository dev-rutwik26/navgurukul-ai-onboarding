# Week 1 Tasks — Foundation & First PR

**Goal:** Get fully set up, understand the codebase, and open your first Pull Request.

---

## Day 1–2: Setup & Orientation

### Task 1.1 — Complete Environment Setup
- Follow the [Environment Setup Guide](../../docs/environment-setup.md) end-to-end
- **Deliverable:** Run `node --version`, `python3 --version`, and `git config --global user.email` and share the output in your standup
- **Acceptance:** All three return correct values

### Task 1.2 — Read Core Docs
Read these in order (mark each done in [checklist.md](../checklist.md)):
- [ ] [Engineering Handbook](../../docs/handbook.md)
- [ ] [Git Workflow](../../docs/git-workflow.md)
- [ ] [Coding Standards](../../docs/coding-standards.md)
- [ ] [Tech Stack](../../docs/tech-stack.md)
- **Acceptance:** You can explain the branch hierarchy and commit message format to your team lead without looking

### Task 1.3 — Create Your Branch
```bash
git checkout dev
git pull origin dev
git checkout -b dev/your_name
git push -u origin dev/your_name
```
- **Acceptance:** Your branch appears on GitHub

---

## Day 3–4: Python Exercise

### Task 1.4 — Complete Exercise 01 (Python Basics)
- Open [`exercises/01_python_basics/task.py`](../../exercises/01_python_basics/task.py)
- Complete **all sections** (1–4 including bonus)
- Run `python exercises/01_python_basics/task.py` — all assertions must pass
- Make **one commit per function** with a proper commit message
- **Acceptance:** `python task.py` prints "🎉 All tests passed!"

---

## Day 4–5: Git Practice & First PR

### Task 1.5 — Complete Exercise 03 (Git Practice) Tasks 1–5
- Follow [`exercises/03_git_practice/README.md`](../../exercises/03_git_practice/README.md)
- Create `my_intro.md`, make 3+ commits, push, open a PR
- **Acceptance:** PR is open on GitHub targeting `dev`, CI is green ✅

### Task 1.6 — Open Your First Real PR
- Combine your Exercise 01 and Exercise 03 work
- Open a single PR titled: `[ONBOARDING] your_name — Week 1 Exercises`
- Fill in the full PR template including:
  - What each commit does
  - Screenshot of `python task.py` output (all tests passing)
  - `git log --oneline` screenshot
- Assign your team lead as reviewer
- **Acceptance:** PR merged to `dev` by end of Week 1

---

## Week 1 Summary Standup

At your **end-of-week standup**, share:
1. What you completed this week
2. What was harder than expected
3. One question you still have about the codebase or workflow
