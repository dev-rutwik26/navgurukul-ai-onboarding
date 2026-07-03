# Coding Standards & AI Assistance Policy

These standards exist to ensure our codebase stays maintainable, secure, and collaborative — especially important given the complexity of our AI pipelines and edge device constraints.

---

## 🏗️ General Coding Standards

### 1. Modularity

**Functions should do one thing and do it well.**

```python
# ❌ Bad — monolithic function doing everything
def handle_audio(audio_input):
    # transcribe
    raw_text = model.transcribe(audio_input)
    # clean
    cleaned = re.sub(r'\s+', ' ', raw_text)
    # translate
    translated = translate_api.translate(cleaned, target='en')
    # synthesize
    audio_output = tts_model.synthesize(translated)
    return audio_output

# ✅ Good — each function does one thing
def transcribe_audio(audio_input: bytes) -> str:
    """Convert raw audio bytes to text using Whisper."""
    return whisper_model.transcribe(audio_input)

def clean_transcript(raw_text: str) -> str:
    """Normalize whitespace and remove filler words."""
    return re.sub(r'\s+', ' ', raw_text).strip()

def translate_text(text: str, target_lang: str = 'en') -> str:
    """Translate text to the target language via the translation API."""
    return translate_api.translate(text, target=target_lang)

def synthesize_speech(text: str) -> bytes:
    """Convert text to audio using the fine-tuned TTS model."""
    return tts_model.synthesize(text)
```

**React:** Break complex components into focused sub-components. A component over 150 lines is a signal it should be split.

### 2. Commenting

**Comment the WHY, not the WHAT.**

```python
# ❌ Bad — restates the code
# Loop through items
for item in items:
    process(item)

# ✅ Good — explains the reasoning
# We process items sequentially (not in parallel) because the ONNX model
# is not thread-safe and crashes under concurrent access on 4GB RAM devices.
for item in items:
    process(item)
```

Always add docstrings to functions and classes:

```python
def load_onnx_model(model_path: str, memory_limit_mb: int = 512) -> ort.InferenceSession:
    """
    Load an ONNX model with a configurable memory limit.

    Uses lazy initialization to avoid pre-allocating the full model graph,
    which would exceed available RAM on 4GB edge devices.

    Args:
        model_path: Absolute path to the .onnx model file
        memory_limit_mb: Maximum memory allocation in MB (default: 512)

    Returns:
        An ONNX Runtime InferenceSession ready for inference

    Raises:
        FileNotFoundError: If the model file does not exist
        MemoryError: If the device does not have sufficient RAM
    """
```

### 3. Naming Conventions

| Context | Convention | Example |
|---|---|---|
| Python variables & functions | `snake_case` | `audio_buffer`, `load_model()` |
| Python classes | `PascalCase` | `STTPipeline`, `AudioProcessor` |
| React components | `PascalCase` | `VoiceInput`, `TranscriptDisplay` |
| React hooks | `camelCase` with `use` prefix | `useAudioStream`, `useModelInference` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_AUDIO_DURATION_MS`, `MODEL_PATH` |
| Files (React) | `PascalCase` | `VoiceInput.jsx`, `AudioProcessor.js` |
| Files (Python) | `snake_case` | `stt_pipeline.py`, `model_loader.py` |

### 4. Folder Structure

**React (Frontend)**

```
src/
├── components/          ← Reusable UI components
│   ├── VoiceInput/
│   │   ├── VoiceInput.jsx
│   │   ├── VoiceInput.css
│   │   └── index.js
├── hooks/               ← Custom React hooks
├── services/            ← API calls & external integrations
├── utils/               ← Pure utility functions
├── pages/               ← Page-level components
└── constants/           ← App-wide constants
```

**Python (Backend)**

```
app/
├── routes/              ← FastAPI route handlers
├── services/            ← Business logic
├── models/              ← Pydantic models & schemas
├── utils/               ← Utility functions
├── ml/                  ← ML model loading & inference
└── config.py            ← Environment configuration
```

---

## 🤖 AI-Assisted Development Policy

We actively encourage AI coding tools. The following rules are **non-negotiable**.

### The Rules

| Rule | Details |
|---|---|
| **Full Comprehension** | You are fully responsible for every line you commit. If you can't explain it, don't commit it. |
| **No Blind Copying** | Never copy-paste AI output without reviewing for: edge cases, security holes, and architecture fit |
| **Refactor for Modularity** | AI tends to generate long, monolithic functions. Always break them up |
| **Comments Are Still Required** | AI output rarely has good comments. Add them yourself |
| **Security Review** | AI output can contain subtle security vulnerabilities. Scrutinize any code handling auth, user data, or credentials |

### Prompting for Quality

Getting good AI output starts with good prompts. When using AI tools:

```
# ✅ Good prompt structure:
"Write a Python function that [specific task]. 
It should:
- Be modular and do only one thing
- Handle [specific edge case]
- Follow PEP 8
- Include a docstring
Our stack uses FastAPI and ONNX Runtime on 4GB RAM edge devices."

# ❌ Bad prompt:
"write code for audio processing"
```

---

## 🔒 Security Standards

- **No hardcoded credentials** — use environment variables, always
- **Validate all inputs** — never trust client-sent data
- **Use HTTPS** — all API calls must use HTTPS in production
- **Dependency audits** — run `npm audit` and `pip-audit` before major releases
- **CORS** — configure CORS explicitly; never use wildcard `*` in production

---

## ✅ Pre-Commit Self-Review Checklist

Before opening a PR, ask yourself:

- [ ] Does each function do one thing only?
- [ ] Have I explained the *why* in comments for complex logic?
- [ ] Have I removed all debug `console.log` / `print` statements?
- [ ] Are there any hardcoded values that should be constants or env vars?
- [ ] Have I checked my code for edge cases the AI might have missed?
- [ ] Is the code consistent with the existing patterns in the codebase?
