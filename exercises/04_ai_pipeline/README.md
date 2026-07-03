# Exercise 04 — AI Pipeline Stub

## 🎯 Goal
Understand and extend a simplified version of our **Speech-to-Speech (STT/TTS) pipeline** — the core of NavGurukul's product. You'll work with ONNX Runtime, audio processing, and modular pipeline design.

## 📋 Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Open `pipeline.py` and complete every `# TODO:` section
3. Run: `python pipeline.py` — all assertions and demo output must work
4. Commit and open a PR to `dev`

## ✅ Acceptance Criteria
- [ ] All `# TODO:` items completed
- [ ] `python pipeline.py` runs without errors
- [ ] Each pipeline stage is a **separate function** (no monoliths)
- [ ] Every function has a docstring
- [ ] Pipeline handles edge cases: empty input, None values
- [ ] PR opened against `dev` with screenshot of terminal output

## ⚠️ Note on ONNX Model
This exercise uses a **mock ONNX inference function** so you don't need to download actual model weights. Focus on the pipeline architecture, not the model itself.

## 💡 Hints
- Think of the pipeline as a series of transformations: `audio → text → response → audio`
- Each stage should be independently testable
- Read [our tech stack doc](../../docs/tech-stack.md) for context on why we use ONNX
