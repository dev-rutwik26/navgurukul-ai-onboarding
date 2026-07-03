# Week 3 Tasks — Independence

**Goal:** Tackle the advanced AI pipeline exercise, resolve a merge conflict, and demonstrate you can work independently on real sprint work.

---

## Day 1–3: AI Pipeline Exercise

### Task 3.1 — Complete Exercise 04 (AI Pipeline)
- Open [`exercises/04_ai_pipeline/pipeline.py`](../../exercises/04_ai_pipeline/pipeline.py)
- Complete all `# TODO:` sections across 4 pipeline stages + orchestrator + batch processor
- Run: `python exercises/04_ai_pipeline/pipeline.py`
- All assertions and demo output must work correctly
- **Acceptance criteria:**
  - [ ] `python pipeline.py` prints "🎉 All tests passed!"
  - [ ] Each pipeline stage is a separate, focused function (no monoliths)
  - [ ] Every function has a complete docstring
  - [ ] Edge cases are handled (empty input raises ValueError)
  - [ ] PR includes screenshot of terminal output

### Task 3.2 — Open PR for Exercise 04
- PR title: `[ONBOARDING] your_name — AI Pipeline Exercise`
- PR description must include:
  - Screenshot of terminal showing all tests passing
  - Your explanation of what each pipeline stage does (in your own words)
  - One thing about the architecture you'd improve in production
- **Acceptance:** PR reviewed and merged to `dev`

---

## Day 3: Merge Conflict Practice

### Task 3.3 — Resolve a Merge Conflict (Exercise 03, Task 7)
- Your team lead will create a conflicting commit on `dev`
- Sync your branch and resolve the conflict manually
- ```bash
  git fetch origin
  git merge origin/dev
  # resolve conflicts in editor
  git add .
  git commit -m "fix: resolve merge conflict with dev"
  git push origin dev/your_name
  ```
- **Acceptance:** Conflict resolved, no code lost, PR updated on GitHub

---

## Day 4–5: Sprint Contribution

### Task 3.4 — Complete Your First Real Sprint Task
- Continue work started in Week 2 Task 2.4
- Respond to all code review feedback on your PR
- Get it merged to `dev`
- **Acceptance:** PR merged, Notion task marked as done

### Task 3.5 — Contribute to Sprint Planning
- Attend the next sprint planning session
- Estimate at least 2 tasks (using story points or t-shirt sizes, as the team does)
- Volunteer for a task in the upcoming sprint
- **Acceptance:** Team lead confirms participation

---

## Onboarding Sign-Off

At the end of Week 3, your team lead will review the following with you:

| Criteria | Done? |
|---|---|
| All 3 coding exercises complete and merged | |
| At least 3 PRs merged to `dev` | |
| At least 2 teammates' PRs reviewed | |
| First real Notion task completed | |
| Participated in sprint planning | |
| Daily intentions shared in standup every day | |
| Can explain the branch hierarchy without notes | |
| Can explain our Edge AI architecture philosophy | |

> **Once all criteria are met, welcome to the team as a fully onboarded NavGurukul AI engineer!** 🎓🚀
