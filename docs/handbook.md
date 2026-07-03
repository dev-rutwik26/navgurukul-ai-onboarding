# Engineering Onboarding Handbook

## NavGurukul AI Engineering Team

> Welcome to the NavGurukul Engineering Team. We build AI-driven products designed to help underprivileged students learn effectively and accessibly. Our engineering philosophy is centered around creating high-performance, low-cost solutions, which is why our architecture heavily leverages **Edge AI**, allowing models to run on small devices with 4–8 GB of minimum RAM.
>
> This handbook is your definitive guide to our technical practices, version control standards, and daily workflows. Please read through this carefully to ensure a seamless integration into our Agile development environment.

---

## 1. Engineering Philosophy & Work Culture

We operate on **Agile principles**. Communication, transparency, and collaboration are the bedrock of our success. As an engineer at NavGurukul, you are expected to follow these cultural practices:

| Practice | Expectation |
|---|---|
| **Share Daily Intentions** | Before starting work, share your daily goals and the features you'll be working on with the team |
| **Communicate Blockers Early** | Don't wait until end-of-day or sprint review. If you're stuck, ask for help immediately |
| **Keep Pull Requests Small** | Small, focused PRs are easier to review, test, and merge. Avoid monolithic changes |
| **Ask Questions** | Whenever uncertain about an implementation detail or architectural decision, ask |
| **Document Decisions** | Important architectural decisions must be documented for future reference |
| **Collaborate** | Prefer pair programming and collaboration over working in isolation |

---

## 2. Technology Stack

Our stack is uniquely tailored to **minimize server costs** by pushing computation to the client side wherever possible. Our main product features a Speech-to-Speech (STT/TTS) pipeline utilizing the Web Speech API and fine-tuned models.

| Domain | Technologies |
|---|---|
| **Frontend (Client-Side)** | React |
| **Backend** | Python, FastAPI |
| **Databases** | Mixpanel, Firebase, MongoDB |
| **Cloud Infrastructure** | AWS |
| **AI & Machine Learning** | ONNX Runtime, Web Speech API, Fine-tuned TTS, Edge AI, Whisper, Transformers, MediaPipe, TensorFlow Lite, WebGPU, WebAssembly, Hugging Face, LangChain, AI Agents |
| **Project Management** | Notion (Scrum Control), GitHub (Version Control) |

📖 [Full tech stack overview →](./tech-stack.md)

---

## 3. Development Environment Setup

To get started on Day 1, complete the following setup steps:

1. **GitHub Account:** Create a GitHub account using your official NavGurukul company email address.
2. **IDE Selection:** You are free to use VS Code, Antigravity, or Claude Code. Ensure your IDE is configured with standard linting and formatting plugins for React and Python.
3. **Repository Access:** We maintain 10+ active repositories. Do not clone everything. You will be granted access to, and should only clone, the specific repositories required for your allocated project.

📖 [Detailed environment setup guide →](./environment-setup.md)

---

## 4. Git Workflow & Branching Strategy

Our branching strategy is **strictly hierarchical** to protect the production environment and ensure thorough testing at multiple levels.

### The Branch Hierarchy

| Branch | Purpose |
|---|---|
| `main` | The production branch — always stable and deployable |
| `release` | Used exclusively for pre-production testing and QA validation |
| `dev` | The integration branch — all feature branches merge here first |
| `dev/<developer_name>` | Your personal workspace — all daily work happens here |

### The Standard Workflow

```
main
 └── release
      └── dev
           └── dev/<developer_name>
```

📖 [Full Git workflow guide →](./git-workflow.md)

---

## 5. Commit Standards & Rules

Commit messages act as the **historical record** of our software. They must be clear, concise, and provide enough context for future debugging.

- **Clarity:** Write messages that clearly state _what_ was changed and _why_. Example: `"Update ONNX model loader to reduce memory footprint on edge devices."`
- **Context:** Link commits to Notion tasks where applicable.

### The "Must NEVER Do" List

Security and repo hygiene are non-negotiable.

| Rule | Reason |
|---|---|
| ❌ Never commit secrets | API keys, AWS credentials, database URIs, or passwords must never touch version control |
| ❌ Never push directly to `main` | All code must go through the PR review process |
| ❌ Never force-push shared branches | Do not use `git push -f` on `dev`, `release`, or `main` |
| ❌ Never rewrite merged history | Once history is shared, it is immutable |
| ❌ Never commit `node_modules` | Ensure your `.gitignore` is correctly configured |
| ❌ Never commit `.env` files | Provide a `.env.example` file instead |

---

## 6. Pull Requests & Code Reviews

Code is read far more often than it is written. Our PR process is designed to ensure transparency, knowledge sharing, and high code quality.

| PR Requirement | Policy / Standard |
|---|---|
| **Minimum Reviewers** | 1 Peer Reviewer is strictly required |
| **Self-Approval** | Prohibited — you cannot merge your own PR without peer approval |
| **Visual Proof (UI Work)** | All frontend UI changes MUST include screenshots or a video |
| **Task Tracking** | Every PR MUST be linked to the corresponding Notion task |

---

## 7. Coding Standards & AI Assistance

### General Standards

- **Modularity:** Keep code as modular as possible. Functions should do one thing and do it well. Break down complex React components and FastAPI routes.
- **Commenting:** Add comprehensive comments. Because we work with complex AI pipelines and edge constraints, explaining the _"why"_ behind a block of code is critical.
- **World Standards:** Adhere to global best practices for folder structures, naming conventions, SOLID principles, and clean architecture.

### AI-Assisted Development Policy

We actively encourage the use of AI coding assistants (Claude Code, Antigravity, Copilot) to accelerate development. However:

1. **Full Comprehension:** You are fully responsible for the code you commit. You must understand how the AI-generated code works.
2. **Review & Implementation:** Never blind-copy AI output. Review it for edge cases, security vulnerabilities, and architecture requirements.
3. **Maintainability:** AI tends to write monolithic blocks if not prompted correctly. Refactor generated code to meet our modularity and commenting standards.

---

## 8. Git Cheat Sheet

| Action | Command |
|---|---|
| Sync your local repository | `git fetch --all` |
| Switch to the dev branch | `git checkout dev` |
| Pull latest dev updates | `git pull origin dev` |
| Create your personal branch | `git checkout -b dev/your_name` |
| Stage all changes | `git add .` |
| Commit changes | `git commit -m "Clear descriptive message"` |
| Push to remote | `git push origin dev/your_name` |

---

> **Welcome aboard! We are excited to see the impact you will make in helping students learn through accessible AI.** 🎓
