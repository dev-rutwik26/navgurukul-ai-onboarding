# Development Environment Setup

This guide walks you through getting your machine fully set up for NavGurukul AI development. Complete everything here **before your first standup**.

> 💡 If you get stuck at any step, ask for help immediately — don't spend more than 30 minutes blocked on a setup issue.

---

## ✅ Pre-Setup Checklist

Before you touch your machine, make sure you have:

- [ ] Your **NavGurukul company email** address
- [ ] Access to the team's **Notion workspace** (ask your team lead)
- [ ] An invitation to the **NavGurukul GitHub organization** (ask your team lead)

---

## 1. GitHub Account

1. Go to [github.com](https://github.com) and create an account using your **NavGurukul company email**
2. Enable **Two-Factor Authentication (2FA)** — this is required for organization membership
3. Share your GitHub username with your team lead to be added to the org
4. Accept the organization invitation from your email

---

## 2. IDE Setup

You may use any of the following IDEs:

| IDE | Download | Recommended for |
|---|---|---|
| **VS Code** | [code.visualstudio.com](https://code.visualstudio.com) | All-purpose |
| **Antigravity** | Via your team lead | AI-assisted development |
| **Claude Code** | [claude.ai/code](https://claude.ai/code) | AI-assisted development |

### Required VS Code Extensions

If using VS Code, install these extensions:

```
# Python
ms-python.python
ms-python.black-formatter
ms-python.pylint

# JavaScript / React
esbenp.prettier-vscode
dbaeumer.vscode-eslint
dsznajder.es7-react-js-snippets

# Git
eamodio.gitlens

# General
streetsidesoftware.code-spell-checker
```

Install all at once:

```bash
code --install-extension ms-python.python \
     ms-python.black-formatter \
     ms-python.pylint \
     esbenp.prettier-vscode \
     dbaeumer.vscode-eslint \
     dsznajder.es7-react-js-snippets \
     eamodio.gitlens \
     streetsidesoftware.code-spell-checker
```

---

## 3. Core Tools Installation

### Node.js (v18 LTS or higher)

```bash
# Option A: Direct install (recommended)
# Download from https://nodejs.org → choose LTS version

# Option B: Via nvm (allows multiple Node versions)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc  # or ~/.zshrc
nvm install 18
nvm use 18

# Verify
node --version  # Should be v18.x.x or higher
npm --version
```

### Python (v3.10 or higher)

```bash
# Option A: Direct install
# Download from https://python.org → Python 3.10+

# Option B: Via pyenv (recommended for managing versions)
curl https://pyenv.run | bash
pyenv install 3.10.14
pyenv global 3.10.14

# Verify
python3 --version  # Should be 3.10.x or higher
pip3 --version
```

### Git

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Verify
git --version

# Configure your identity (use your NavGurukul email)
git config --global user.name "Your Full Name"
git config --global user.email "yourname@navgurukul.org"
```

---

## 4. Python Environment Setup

Always use a virtual environment — never install packages globally.

```bash
# Create a virtual environment in your project
cd your-project-directory
python3 -m venv venv

# Activate it
source venv/bin/activate          # macOS / Linux
# or
.\venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

---

## 5. Repository Access

1. **Do not clone everything.** We have 10+ repositories.
2. Your team lead will tell you which repository/repositories your project uses.
3. Only clone what you need.

```bash
# Clone your assigned repository
git clone git@github.com:navgurukul/<repo-name>.git
cd <repo-name>

# Create your personal branch
git checkout dev
git checkout -b dev/your_name
```

---

## 6. Environment Variables

1. Every project has a `.env.example` file — **never a `.env` file committed to Git**.
2. Copy `.env.example` to `.env` and fill in your values.

```bash
cp .env.example .env
# Now edit .env with the actual values (get them from your team lead)
```

> ⚠️ **Never commit your `.env` file.** It contains secrets that must not touch version control.

---

## 7. Verify Your Setup

Run through this final check before your first standup:

```bash
# Git configured
git config --global user.name   # Should show your name
git config --global user.email  # Should show your NavGurukul email

# Node
node --version                  # v18+
npm --version                   # 9+

# Python
python3 --version               # 3.10+
pip3 --version

# Confirm you're on your personal branch
git branch                      # Should show dev/your_name as active
```

---

## 🆘 Troubleshooting

| Issue | Solution |
|---|---|
| `node: command not found` | Restart your terminal after installing Node |
| `python3: command not found` | Add Python to PATH; restart terminal |
| GitHub SSH key rejected | Generate and add SSH key: `ssh-keygen -t ed25519 -C "email"` then add to GitHub Settings → SSH Keys |
| Can't clone repo | Confirm you've been added to the GitHub org by your team lead |
| `.env` values not working | Check for typos; make sure no quotes around values unless required |

---

> **All set? Head over to the [Onboarding Checklist](../onboarding/checklist.md) for your next steps.**
