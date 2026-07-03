# Git Workflow & Branching Strategy

This document is the definitive reference for how we use Git at NavGurukul AI. Follow this exactly — our branching strategy protects the production environment and ensures every line of code is tested before it reaches students.

---

## 🌿 Branch Hierarchy

```
main
 └── release
      └── dev
           └── dev/<developer_name>
```

| Branch | Stability | Who merges to it? | Purpose |
|---|---|---|---|
| `main` | 🟢 Production | Team Lead only | Always deployable — what students use |
| `release` | 🟡 Staging | Team Lead | Pre-production QA, final validation |
| `dev` | 🟠 Integration | PR from `dev/*` | Developer-level testing, all features land here |
| `dev/<your_name>` | 🔴 Personal | You | Your daily sandbox — features, fixes, experiments |

> **Rule:** Your work lives in `dev/<your_name>`. You never touch `main`, `release`, or `dev` directly.

---

## 🔄 Daily Workflow

### Starting a new task

```bash
# 1. Fetch all remote changes
git fetch --all

# 2. Switch to the integration branch
git checkout dev

# 3. Pull the latest changes
git pull origin dev

# 4. Create (or switch to) your personal branch
git checkout -b dev/your_name
# or if already exists:
git checkout dev/your_name
git merge dev  # bring in latest dev changes
```

### Working on your task

```bash
# Stage specific files (preferred over git add .)
git add src/components/STTPipeline.jsx

# Or stage everything (use with care)
git add .

# Commit with a clear, descriptive message
git commit -m "feat: add memory-efficient ONNX loader for 4GB edge devices"

# Push to your personal remote branch
git push origin dev/your_name
```

### Submitting for review

1. Go to GitHub and open a **Pull Request** from `dev/your_name` → `dev`
2. Fill in the [PR template](../.github/PULL_REQUEST_TEMPLATE.md)
3. Link your Notion task
4. Assign at least 1 reviewer
5. Add screenshots if it's a UI change
6. Wait for approval — **do not merge your own PR**

---

## ✍️ Commit Message Format

```
<type>: <short imperative summary (max 72 chars)>

[Optional body — explain WHY, not what]
[Notion task: https://notion.so/navgurukul/task-id]
```

### Commit Types

| Type | Usage |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Code restructuring, no behaviour change |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `chore` | Tooling, deps, config |

### Examples ✅

```bash
git commit -m "feat: add lazy-loading to ONNX model for reduced RAM on edge devices"
git commit -m "fix: resolve STT desync crash on low-memory mobile devices"
git commit -m "docs: update Git workflow guide with rebase instructions"
git commit -m "refactor: split STTPipeline into AudioCapture and ModelInference modules"
```

### Bad Examples ❌

```bash
git commit -m "update"
git commit -m "fix stuff"
git commit -m "WIP"
git commit -m "asdfgh"
```

---

## 🚫 Absolute Rules

| Rule | Why |
|---|---|
| ❌ Never `git push -f` on `dev`, `release`, or `main` | Destroys shared history |
| ❌ Never push directly to `main` or `release` | Bypasses all quality gates |
| ❌ Never rewrite history that has been shared | Breaks teammates' repos |
| ❌ Never commit `.env` or secrets | Permanent security risk even if "deleted" later |

---

## 🛠️ Cheat Sheet

| Action | Command |
|---|---|
| Fetch all remote changes | `git fetch --all` |
| See all branches | `git branch -a` |
| Switch branch | `git checkout <branch>` |
| Create & switch branch | `git checkout -b dev/your_name` |
| Pull latest from dev | `git pull origin dev` |
| Stage all changes | `git add .` |
| Stage specific file | `git add path/to/file` |
| Commit | `git commit -m "type: message"` |
| Push | `git push origin dev/your_name` |
| Check status | `git status` |
| See recent commits | `git log --oneline -10` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| See diff | `git diff` |
| Stash uncommitted changes | `git stash` |
| Pop stash | `git stash pop` |

---

## 🔁 Keeping Your Branch Up to Date

If `dev` has moved ahead while you were working:

```bash
# Option 1: Merge (simpler, creates a merge commit)
git checkout dev/your_name
git fetch origin
git merge origin/dev

# Option 2: Rebase (cleaner history — preferred)
git checkout dev/your_name
git fetch origin
git rebase origin/dev
```

> **Note:** Only rebase your own personal branch — never rebase shared branches.
