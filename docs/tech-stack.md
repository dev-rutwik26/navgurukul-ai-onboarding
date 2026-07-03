# Technology Stack Overview

This document explains each technology in our stack, why we use it, and where it fits in our architecture.

---

## 🏛️ Architecture Philosophy

> **Edge AI First.** We push computation to the client side wherever possible to minimize server costs and maximize accessibility for students on low-bandwidth, low-spec devices.

Our flagship product is a **Speech-to-Speech (STT/TTS) pipeline** that transcribes student speech, processes it with an AI model, and responds with synthesized audio — all running on devices with as little as 4GB of RAM.

---

## 🗺️ Full Stack Overview

| Domain | Technologies |
|---|---|
| **Frontend** | React |
| **Backend** | Python, FastAPI |
| **Databases** | Mixpanel, Firebase, MongoDB |
| **Cloud** | AWS |
| **AI & ML** | ONNX Runtime, Web Speech API, Whisper, Transformers, MediaPipe, TensorFlow Lite, WebGPU, WebAssembly, Hugging Face, LangChain, AI Agents |

---

## 🖥️ Frontend — React

**Why React?**
- Component-based architecture keeps our UI modular and testable
- Large ecosystem for audio/media handling
- Strong support for Web APIs (WebGPU, WebAssembly, Web Speech API)

**Our usage:**
- Speech input/output UI
- Real-time audio visualization
- Client-side ML model invocation via ONNX Runtime Web / WebAssembly

---

## ⚙️ Backend — Python + FastAPI

**Why FastAPI?**
- Native async support — critical for handling concurrent audio streams
- Automatic OpenAPI docs generation
- Pydantic validation keeps our data models strict and safe
- Python ecosystem gives us direct access to ML libraries

**Our usage:**
- API endpoints for model inference fallback (when client-side is insufficient)
- Data pipelines and preprocessing
- Integration with Firebase, MongoDB, and AWS services

---

## 🗄️ Databases

### Firebase
- **Use case:** Real-time data sync, authentication, and student session management
- Chosen for real-time capabilities and free tier for small-scale usage

### MongoDB
- **Use case:** Storing unstructured data — student transcripts, model outputs, session logs
- Flexible schema suits our rapidly evolving AI data formats

### Mixpanel
- **Use case:** Product analytics and user behavior tracking
- Helps us understand how students interact with the product to improve learning outcomes

---

## ☁️ Cloud — AWS

**Key services we use:**
- **S3** — Model weights storage, audio file storage
- **EC2/Lambda** — Backend API hosting
- **CloudFront** — CDN for static assets

---

## 🤖 AI & Machine Learning

### ONNX Runtime & ONNX Runtime Web
- **Role:** Run fine-tuned ML models in the browser or on edge devices without a server
- **Why:** Enables true client-side inference with cross-platform compatibility

### Web Speech API
- **Role:** Browser-native speech recognition — the first layer of our STT pipeline
- **Why:** Zero latency, no network cost, works offline

### Whisper (OpenAI)
- **Role:** High-accuracy speech-to-text for cases where Web Speech API falls short
- **Why:** Best-in-class accuracy, especially for Indian English accents

### Transformers (Hugging Face)
- **Role:** Fine-tuned NLP models for understanding student queries
- **Why:** Access to thousands of pretrained models; we fine-tune on our domain data

### TensorFlow Lite & MediaPipe
- **Role:** Lightweight ML inference on mobile and edge devices
- **Why:** Optimized for devices with 4-8GB RAM; MediaPipe provides ready-made vision/gesture pipelines

### WebGPU & WebAssembly
- **Role:** Hardware-accelerated ML inference directly in the browser
- **Why:** Dramatically speeds up client-side model execution on modern browsers

### LangChain & AI Agents
- **Role:** Orchestrating multi-step AI workflows and building conversational agents
- **Why:** Enables complex reasoning chains (e.g., "student asks a question → retrieve context → generate tutored response")

### Hugging Face Hub
- **Role:** Model storage, versioning, and discovery
- **Why:** Central registry for our fine-tuned model weights

---

## 🛠️ Project Management

| Tool | Purpose |
|---|---|
| **Notion** | Scrum board, sprint planning, task tracking, architectural decision records |
| **GitHub** | Version control, code review, CI/CD, issue tracking |
| **GitHub Issues** | Bug tracking and onboarding task management |
