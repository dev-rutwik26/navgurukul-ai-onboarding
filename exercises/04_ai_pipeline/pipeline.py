"""
Exercise 04 — AI Pipeline Stub
================================
NavGurukul AI Engineering Onboarding

This exercise simulates our core Speech-to-Speech (STT/TTS) pipeline.
In production, this runs on 4GB RAM edge devices with real ONNX models.
Here, we use mock functions so you can focus on pipeline ARCHITECTURE.

Pipeline stages:
    Raw Audio → [STT] → Raw Text → [Normalize] → [NLP Response] → [TTS] → Audio Output

Instructions:
- Complete every function marked with # TODO:
- Run: python pipeline.py
- All assertions and demo output must work
- Focus on: modularity, single responsibility, clear docstrings

Submission:
- Branch: dev/your_name
- PR target: dev
- PR must include: terminal output screenshot
"""

from __future__ import annotations
import re
import time
from dataclasses import dataclass, field
from typing import Optional


# ─────────────────────────────────────────
# Data Models
# ─────────────────────────────────────────

@dataclass
class AudioChunk:
    """Represents a raw audio input chunk from the microphone."""
    data: bytes
    sample_rate: int = 16000
    duration_ms: int = 0


@dataclass
class Transcript:
    """The result of Speech-to-Text conversion."""
    text: str
    confidence: float  # 0.0 to 1.0
    language: str = "en"


@dataclass
class PipelineResult:
    """Final output of the full STT → NLP → TTS pipeline."""
    input_transcript: str
    normalized_text: str
    nlp_response: str
    audio_output: bytes
    processing_time_ms: float
    stages_log: list[str] = field(default_factory=list)


# ─────────────────────────────────────────
# SECTION 1: Mock Infrastructure
# (Simulates real models — do not modify)
# ─────────────────────────────────────────

def _mock_whisper_transcribe(audio: AudioChunk) -> tuple[str, float]:
    """
    Simulates Whisper STT model inference.
    Returns (transcript_text, confidence_score).
    Do NOT modify this function.
    """
    # In production: onnx_session.run(["output"], {"input": audio.data})
    mock_transcripts = {
        b"hello": ("hello how are you doing today", 0.95),
        b"question": ("can you explain what machine learning is", 0.89),
        b"math": ("what is the square root of one hundred and forty four", 0.92),
    }
    return mock_transcripts.get(audio.data, ("i need help with my studies", 0.78))


def _mock_tts_synthesize(text: str) -> bytes:
    """
    Simulates TTS model synthesis.
    Returns fake audio bytes. Do NOT modify this function.
    """
    # In production: tts_onnx_session.run(["audio"], {"text_input": text})
    return f"[AUDIO: {text[:50]}]".encode("utf-8")


def _mock_nlp_respond(text: str) -> str:
    """
    Simulates an NLP model generating a response.
    Do NOT modify this function.
    """
    responses = {
        "machine learning": "Machine learning is a branch of AI where systems learn from data.",
        "square root": "The square root of 144 is 12.",
        "studies": "I'm here to help! What subject would you like to work on?",
        "hello": "Hello! I'm your NavGurukul AI tutor. What would you like to learn today?",
    }
    for keyword, response in responses.items():
        if keyword in text:
            return response
    return "That's a great question! Let me help you understand that concept."


# ─────────────────────────────────────────
# SECTION 2: Pipeline Stages
# Each function = one stage of the pipeline
# ─────────────────────────────────────────

def transcribe_audio(audio: AudioChunk) -> Transcript:
    """
    Stage 1: Convert raw audio to text using the STT model.

    TODO:
    1. Validate that audio.data is not empty — raise ValueError if it is
    2. Call _mock_whisper_transcribe(audio) to get (text, confidence)
    3. Return a Transcript object with the results

    Args:
        audio: AudioChunk containing raw audio bytes

    Returns:
        Transcript with text and confidence score

    Raises:
        ValueError: If audio data is empty
    """
    # TODO: Implement
    pass


def normalize_text(transcript: Transcript) -> str:
    """
    Stage 2: Normalize the transcript for NLP processing.

    Steps to apply (in order):
    1. Strip leading/trailing whitespace
    2. Collapse multiple spaces to single space
    3. Convert to lowercase
    4. Remove filler words: ["um", "uh", "er", "like"]
    5. Strip again after filler word removal

    Args:
        transcript: The Transcript from stage 1

    Returns:
        Cleaned, normalized text string

    Raises:
        ValueError: If transcript.text is empty after normalization
    """
    # TODO: Implement
    # Hint: Use re.sub(r'\s+', ' ', text) to collapse spaces
    # Hint: re.sub(r'\b(um|uh|er|like)\b', '', text, flags=re.IGNORECASE)
    pass


def generate_response(normalized_text: str) -> str:
    """
    Stage 3: Generate a tutoring response for the student's query.

    TODO:
    1. Validate normalized_text is not empty or None
    2. Call _mock_nlp_respond(normalized_text) to get a response
    3. Ensure the response is not empty — raise RuntimeError if it is
    4. Return the response string

    Args:
        normalized_text: Clean text from stage 2

    Returns:
        NLP-generated response string
    """
    # TODO: Implement
    pass


def synthesize_audio(response_text: str) -> bytes:
    """
    Stage 4: Convert the NLP response text to audio.

    TODO:
    1. Validate response_text is not empty
    2. Call _mock_tts_synthesize(response_text) to get audio bytes
    3. Validate the returned bytes are not empty
    4. Return the audio bytes

    Args:
        response_text: The NLP response from stage 3

    Returns:
        Audio bytes ready to play to the student
    """
    # TODO: Implement
    pass


# ─────────────────────────────────────────
# SECTION 3: Pipeline Orchestrator
# Ties all stages together
# ─────────────────────────────────────────

def run_pipeline(audio: AudioChunk) -> PipelineResult:
    """
    Orchestrate the full Speech-to-Speech pipeline.

    Stages:
        AudioChunk → transcribe_audio() → normalize_text()
                  → generate_response() → synthesize_audio()
                  → PipelineResult

    TODO:
    1. Record start time using time.time()
    2. Run each stage in sequence, passing the output of each to the next
    3. Log each stage completion in a stages_log list
       e.g., stages_log.append("✅ Stage 1 [STT]: 'hello world' (confidence: 0.95)")
    4. Calculate processing_time_ms = (time.time() - start) * 1000
    5. Return a PipelineResult with all fields filled in

    Args:
        audio: Raw AudioChunk input

    Returns:
        PipelineResult with all intermediate and final values
    """
    # TODO: Implement this orchestrator
    stages_log = []
    pass


# ─────────────────────────────────────────
# SECTION 4: Batch Processing
# ─────────────────────────────────────────

def process_batch(audio_chunks: list[AudioChunk]) -> list[PipelineResult]:
    """
    Process multiple audio chunks through the pipeline sequentially.

    Important: Process one at a time (not parallel) — the ONNX model
    is NOT thread-safe on edge devices with limited RAM.

    TODO:
    1. Validate the input list is not empty
    2. For each chunk, call run_pipeline() and collect results
    3. Skip (and log a warning) any chunk that raises an exception
    4. Return the list of successful results

    Args:
        audio_chunks: List of AudioChunk objects to process

    Returns:
        List of PipelineResult for successfully processed chunks
    """
    # TODO: Implement
    pass


# ─────────────────────────────────────────
# Tests & Demo — DO NOT MODIFY
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("NavGurukul AI — STT/TTS Pipeline Exercise")
    print("=" * 60)

    # Test individual stages
    print("\n📋 Testing individual pipeline stages...")

    audio_hello = AudioChunk(data=b"hello", duration_ms=2000)
    audio_question = AudioChunk(data=b"question", duration_ms=3500)
    audio_math = AudioChunk(data=b"math", duration_ms=4000)

    # Stage 1
    transcript = transcribe_audio(audio_hello)
    assert isinstance(transcript, Transcript), "transcribe_audio must return a Transcript"
    assert transcript.confidence > 0, "Confidence should be > 0"
    print(f"✅ Stage 1 [STT]: '{transcript.text}' (confidence: {transcript.confidence})")

    # Stage 2
    normalized = normalize_text(transcript)
    assert isinstance(normalized, str), "normalize_text must return a str"
    assert normalized == normalized.lower(), "Output should be lowercase"
    print(f"✅ Stage 2 [Normalize]: '{normalized}'")

    # Stage 3
    response = generate_response(normalized)
    assert isinstance(response, str) and len(response) > 0, "generate_response must return non-empty str"
    print(f"✅ Stage 3 [NLP]: '{response}'")

    # Stage 4
    audio_out = synthesize_audio(response)
    assert isinstance(audio_out, bytes) and len(audio_out) > 0, "synthesize_audio must return non-empty bytes"
    print(f"✅ Stage 4 [TTS]: {len(audio_out)} bytes of audio")

    # Full pipeline
    print("\n🔄 Testing full pipeline...")
    result = run_pipeline(audio_question)
    assert isinstance(result, PipelineResult), "run_pipeline must return a PipelineResult"
    assert result.processing_time_ms > 0, "Processing time should be recorded"
    assert len(result.stages_log) == 4, "All 4 stages should be logged"
    print(f"✅ Full pipeline completed in {result.processing_time_ms:.2f}ms")
    print(f"   Input:    '{result.input_transcript}'")
    print(f"   Response: '{result.nlp_response}'")

    # Batch processing
    print("\n📦 Testing batch processing...")
    batch = [audio_hello, audio_question, audio_math]
    results = process_batch(batch)
    assert len(results) == 3, "All 3 chunks should be processed"
    print(f"✅ Batch processed {len(results)}/3 chunks successfully")

    # Edge case: empty audio
    print("\n⚠️  Testing edge cases...")
    try:
        transcribe_audio(AudioChunk(data=b""))
        print("❌ Should have raised ValueError for empty audio")
    except ValueError:
        print("✅ Correctly raised ValueError for empty audio")

    print("\n🎉 All tests passed! You're ready to open your PR.")
    print("\nStages log from full pipeline run:")
    for log_entry in result.stages_log:
        print(f"   {log_entry}")
