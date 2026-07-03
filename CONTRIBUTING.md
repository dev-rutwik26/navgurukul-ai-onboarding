# Contributing to NavGurukul AI Projects

This guide defines the standards every engineer must follow when contributing code. These are not suggestions — they are team agreements that protect code quality, security, and collaboration.

---

## 🌿 Branching Strategy

Our branching hierarchy is **strictly hierarchical** to protect the production environment.

```
main
 └── release
      └── dev
           └── dev/<your_name>
```

| Branch | Purpose |
|---|---|
| `main` | Production — always stable and deployable |
| `release` | Pre-production QA and validation |
| `dev` | Integration branch — all features merge here first |
| `dev/<your_name>` | **Your personal workspace** — all daily work happens here |

### Rules
- **All work** must be done inside `dev/<your_name>`.
- **Never push directly to `main`, `release`, or `dev`.**
- When ready, open a PR from `dev/<your_name>` → `dev`.
- Team leads handle `dev` → `release` → `main` promotions.

---

## ✍️ Commit Standards

Commit messages are the historical record of our software. Write them as if explaining to a future engineer who has no context.

### Format

```
<type>: <short summary>

[Optional body explaining the WHY, not just the WHAT]
[Optional: Notion task link]
```

### Types

| Type | When to use |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring without behavior change |
| `test` | Adding or updating tests |
| `chore` | Tooling, deps, config changes |
| `perf` | Performance improvements |

### Good Examples

```
feat: add ONNX model loader with memory optimization for edge devices

Reduces RAM footprint by 40% by lazy-loading model layers.
Notion: https://notion.so/navgurukul/task-id-123
```

```
fix: resolve Web Speech API desync on low-memory devices

The STT pipeline was not correctly clearing audio buffers on mobile.
Added explicit cleanup in the onend handler.
```

### Bad Examples ❌

```
fixed stuff
update
WIP
asdfgh
```

---

## 🚫 The "Must NEVER Do" List

Violation of these rules is grounds for immediate code reversal and a team discussion.

| Rule | Reason |
|---|---|
| ❌ Never commit secrets (API keys, credentials, `.env` files) | Security breach risk |
| ❌ Never push directly to `main` | Bypasses all quality gates |
| ❌ Never force-push shared branches (`dev`, `release`, `main`) | Destroys shared history |
| ❌ Never rewrite merged history | Breaks teammates' local repos |
| ❌ Never commit `node_modules/` | Massive repo bloat |
| ❌ Never commit `.env` files | Use `.env.example` instead |

---

## 📬 Pull Request Process

### Before Opening a PR

- [ ] My branch is up-to-date with `dev` (`git pull origin dev`)
- [ ] I have tested my changes locally
- [ ] I have added/updated comments for complex logic
- [ ] I have added a `.env.example` entry for any new environment variables
- [ ] My PR is **small and focused** on one concern

### PR Requirements

| Requirement | Standard |
|---|---|
| **Minimum reviewers** | 1 peer reviewer — **required**, no exceptions |
| **Self-approval** | Prohibited — you cannot merge your own PR |
| **UI changes** | Must include screenshots or a screen recording in the PR description |
| **Task tracking** | Every PR **must** be linked to the corresponding Notion task |
| **PR size** | Prefer small, focused PRs. Large PRs will be asked to be split. |

### PR Description Template

Use the [Pull Request Template](./.github/PULL_REQUEST_TEMPLATE.md) — it loads automatically when you open a PR.

### Code Review Etiquette

- **As an author:** Be open to feedback. Don't take comments personally.
- **As a reviewer:** Be specific and constructive. Explain *why* you're requesting a change.
- **Resolve all comments** before merging (or explicitly mark them as won't-fix with a reason).
- **Approve promptly** — don't leave PRs blocked for more than 24 hours without communication.

---

## 🤖 AI-Assisted Development Policy

We actively encourage AI coding tools (Claude Code, Antigravity, Copilot). The following rules apply:

1. **Full Comprehension** — You are responsible for every line you commit. Understand what the AI generated.
2. **Review for Edge Cases** — AI can miss edge cases, security vulnerabilities, and architecture constraints.
3. **Refactor for Modularity** — AI often generates monolithic blocks. Break them into focused functions.
4. **Never Blind-Copy** — Always review, adapt, and validate AI output against our standards.

---

## 🙋 Questions?

If you're unsure about any of these standards, ask in the team channel or raise it in standup. We'd rather answer a question than fix a production incident.
