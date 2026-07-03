"""
Exercise 02 — FastAPI Endpoint Design
=======================================
NavGurukul AI Engineering Onboarding

Instructions:
- Complete every section marked with # TODO:
- Run the server: uvicorn main:app --reload
- Test at: http://localhost:8000/docs
- All endpoints must match the expected response shapes described below

Submission:
- Branch: dev/your_name
- PR target: dev
- PR must include: a screenshot of /docs showing your working endpoints
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import re
from datetime import datetime

# ─────────────────────────────────────────
# App initialization
# ─────────────────────────────────────────

app = FastAPI(
    title="NavGurukul Student API",
    description="A practice API for managing students and their learning sessions.",
    version="1.0.0",
)

# ─────────────────────────────────────────
# In-memory "database" (no real DB needed)
# ─────────────────────────────────────────

# This acts as our fake database for this exercise.
# In production, this would be a MongoDB collection.
students_db: dict[str, dict] = {}
sessions_db: list[dict] = []


# ─────────────────────────────────────────
# SECTION 1: Pydantic Models
# Define request/response schemas here
# ─────────────────────────────────────────

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    # TODO: Add the following fields with appropriate types and validation:
    #   - name: str (required, min length 2)
    #   - email: str (required)
    #   - grade: int (required, must be between 1 and 12)
    #   - language: str (optional, default = "English")
    #
    # Hint: Use Field(min_length=2) and Field(ge=1, le=12) for validation
    pass


class StudentResponse(BaseModel):
    """Schema for returning student data."""
    # TODO: Add fields:
    #   - student_id: str
    #   - name: str
    #   - email: str
    #   - grade: int
    #   - language: str
    #   - created_at: str
    pass


class SessionCreate(BaseModel):
    """Schema for logging a learning session."""
    # TODO: Add fields:
    #   - student_id: str
    #   - duration_minutes: int (must be > 0)
    #   - subject: str
    #   - notes: Optional[str] (default None)
    pass


class SessionResponse(BaseModel):
    """Schema for returning session data."""
    # TODO: Add fields matching SessionCreate, plus:
    #   - session_id: str
    #   - logged_at: str
    pass


# ─────────────────────────────────────────
# SECTION 2: Utility Functions
# Keep business logic out of route handlers
# ─────────────────────────────────────────

def generate_student_id(name: str) -> str:
    """
    Generate a simple student ID from the student's name.
    Format: first 3 letters of name (uppercase) + timestamp digits

    Example: "Priya Sharma" -> "PRI1720000000"
    """
    # TODO: Implement this function
    # Hint: Use name[:3].upper() and str(int(datetime.now().timestamp()))
    pass


def is_valid_email(email: str) -> bool:
    """
    Validate that an email address has a basic valid format.
    Returns True if valid, False otherwise.

    Example:
        is_valid_email("priya@navgurukul.org") -> True
        is_valid_email("not-an-email") -> False
    """
    # TODO: Implement using re.match with a simple email regex
    # Hint: r'^[\w\.-]+@[\w\.-]+\.\w+$'
    pass


# ─────────────────────────────────────────
# SECTION 3: API Routes
# ─────────────────────────────────────────

@app.get("/", summary="Health check")
def root():
    """
    Health check endpoint.

    TODO: Return a JSON response:
        {"status": "ok", "message": "NavGurukul Student API is running"}
    """
    # TODO: Implement
    pass


@app.post("/students", response_model=StudentResponse, status_code=201, summary="Register a student")
def create_student(student: StudentCreate):
    """
    Register a new student.

    TODO:
    1. Validate the email using is_valid_email() — raise HTTPException 400 if invalid
    2. Check if a student with the same email already exists — raise 409 if so
    3. Generate a student_id using generate_student_id()
    4. Store the student in students_db (keyed by student_id)
    5. Return the created student as StudentResponse

    Hint: HTTPException(status_code=400, detail="Invalid email format")
    """
    # TODO: Implement
    pass


@app.get("/students", summary="List all students")
def list_students(grade: Optional[int] = Query(None, ge=1, le=12)):
    """
    List all registered students.

    If `grade` query parameter is provided, filter by that grade.

    TODO:
    1. If grade is provided, return only students matching that grade
    2. Otherwise return all students
    3. Return as a list

    Example: GET /students?grade=10
    """
    # TODO: Implement
    pass


@app.get("/students/{student_id}", response_model=StudentResponse, summary="Get student by ID")
def get_student(student_id: str):
    """
    Retrieve a single student by their ID.

    TODO:
    1. Look up the student_id in students_db
    2. If not found, raise HTTPException 404
    3. Return the student data
    """
    # TODO: Implement
    pass


@app.delete("/students/{student_id}", status_code=204, summary="Delete a student")
def delete_student(student_id: str):
    """
    Delete a student by their ID.

    TODO:
    1. Check if student exists — raise 404 if not
    2. Remove from students_db
    3. Return None (FastAPI will send 204 No Content)
    """
    # TODO: Implement
    pass


@app.post("/sessions", response_model=SessionResponse, status_code=201, summary="Log a learning session")
def create_session(session: SessionCreate):
    """
    Log a new learning session for a student.

    TODO:
    1. Verify the student_id exists in students_db — raise 404 if not
    2. Generate a session_id (you can use f"SES{len(sessions_db)+1:04d}")
    3. Add the session to sessions_db
    4. Return the session as SessionResponse
    """
    # TODO: Implement
    pass


@app.get("/students/{student_id}/sessions", summary="Get sessions for a student")
def get_student_sessions(student_id: str):
    """
    Get all learning sessions for a specific student.

    TODO:
    1. Verify student exists — raise 404 if not
    2. Filter sessions_db for sessions matching student_id
    3. Return the list of sessions
    """
    # TODO: Implement
    pass


@app.get("/stats", summary="Get overall statistics")
def get_stats():
    """
    Return overall platform statistics.

    TODO: Return a dict with:
        - total_students: int
        - total_sessions: int
        - avg_session_duration_minutes: float (0.0 if no sessions)
        - most_common_subject: str or None
    """
    # TODO: Implement
    # Hint: Use a Counter from collections for most_common_subject
    pass
