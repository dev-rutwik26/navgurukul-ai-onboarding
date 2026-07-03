# Exercise 03 — Git & GitHub Workflow Practice

## 🎯 Goal
Practise the **full NavGurukul Git workflow** — branching, committing, pushing, and opening a PR — exactly as you will every single day on the job.

---

## 📋 Tasks

Complete all tasks **in order**. Each task builds on the previous one.

---

### Task 1 — Set Up Your Branch

**Objective:** Create your personal development branch from `dev`.

```bash
# Fetch the latest state of the remote
git fetch --all

# Switch to the integration branch
git checkout dev

# Pull the latest changes
git pull origin dev

# Create YOUR personal branch (replace your_name)
git checkout -b dev/your_name
```

**✅ Done when:**
- [ ] You are on branch `dev/your_name` (check with `git branch`)
- [ ] Your branch is based on the latest `dev`

---

### Task 2 — Make Your First Commit

**Objective:** Add a file and commit it with a proper commit message.

1. Create a file at `exercises/03_git_practice/my_intro.md`
2. Add the following content (fill in your details):

```markdown
# My Introduction

**Name:** Your Full Name  
**Role:** Software Engineer — NavGurukul AI Team  
**GitHub:** @your_github_username  
**Start Date:** YYYY-MM-DD  

## What I'm excited to work on
<!-- Write 2-3 sentences about what interests you most about this role -->

## My strongest technical skill
<!-- One sentence -->

## Something I want to learn here
<!-- One sentence -->
```

3. Stage and commit:

```bash
git add exercises/03_git_practice/my_intro.md
git commit -m "docs: add intro for your_name"
```

**✅ Done when:**
- [ ] File exists at `exercises/03_git_practice/my_intro.md`
- [ ] Commit message follows the `type: description` format
- [ ] `git log --oneline -3` shows your commit

---

### Task 3 — Practice the Commit Loop

**Objective:** Make **3 separate, meaningful commits** (not one big commit).

Open `exercises/01_python_basics/task.py` and complete **only Section 1** (the first 3 functions). Make a separate commit for each function you complete:

```bash
# After completing reverse_words():
git add exercises/01_python_basics/task.py
git commit -m "feat: implement reverse_words in exercise 01"

# After completing count_vowels():
git add exercises/01_python_basics/task.py
git commit -m "feat: implement count_vowels in exercise 01"

# After completing remove_duplicates():
git add exercises/01_python_basics/task.py
git commit -m "feat: implement remove_duplicates in exercise 01"
```

**✅ Done when:**
- [ ] `git log --oneline -5` shows 3 separate commits for the 3 functions
- [ ] Each commit message clearly describes what was done
- [ ] `python exercises/01_python_basics/task.py` Section 1 assertions pass

---

### Task 4 — Push to Remote

**Objective:** Push your branch to GitHub.

```bash
git push origin dev/your_name
```

**✅ Done when:**
- [ ] Your branch appears on GitHub under the repository's branch list
- [ ] All your commits are visible on GitHub

---

### Task 5 — Open a Pull Request

**Objective:** Open a PR from `dev/your_name` → `dev`.

1. Go to the repository on GitHub
2. Click **"Compare & pull request"** (appears after you push)
3. Fill in the PR template completely:
   - Title: `[ONBOARDING] your_name — Git Practice Exercise`
   - Link this GitHub issue (or a Notion task if you have one)
   - Describe what you did in each commit
4. Assign **at least 1 reviewer**
5. Submit the PR

**✅ Done when:**
- [ ] PR is open on GitHub targeting `dev`
- [ ] PR template is fully filled in
- [ ] At least 1 reviewer is assigned
- [ ] CI checks are passing (green ✅)

---

### Task 6 — Review Someone Else's PR

**Objective:** Practice being a code reviewer.

1. Find a teammate's open PR on the repository
2. Read through their changes carefully
3. Leave **at least 2 constructive comments** (questions, suggestions, or approvals)
4. Either approve it or request changes with clear explanations

**✅ Done when:**
- [ ] You have left at least 2 comments on a teammate's PR
- [ ] Your review is either an Approval or a Request for Changes (not just "LGTM")

---

### Task 7 — Resolve a Merge Conflict (Bonus 🔴)

**Objective:** Practise resolving a merge conflict — an unavoidable real-world skill.

1. Your team lead will intentionally create a conflicting commit on `dev`
2. Sync your branch:

```bash
git fetch origin
git checkout dev/your_name
git merge origin/dev
```

3. Git will report a conflict. Open the conflicted file(s) and resolve them manually.
4. After resolving:

```bash
git add <resolved-files>
git commit -m "fix: resolve merge conflict with dev"
git push origin dev/your_name
```

**✅ Done when:**
- [ ] Conflict is resolved without losing any code
- [ ] `git log --oneline -5` shows the merge commit
- [ ] PR is updated on GitHub

---

## 📸 Evidence to Include in Your PR

- Screenshot of `git log --oneline` showing all your commits
- Screenshot of the open PR on GitHub
- Screenshot of the CI checks passing

---

## 🔑 Key Git Commands Reference

| Action | Command |
|---|---|
| See current branch | `git branch` |
| See last 10 commits | `git log --oneline -10` |
| See what's staged | `git status` |
| See unstaged changes | `git diff` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Sync with remote dev | `git fetch origin && git merge origin/dev` |
