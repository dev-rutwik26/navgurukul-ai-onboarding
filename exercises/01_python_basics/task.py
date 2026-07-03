"""
Exercise 01 — Python Basics & Clean Code
=========================================
NavGurukul AI Engineering Onboarding

Instructions:
- Complete every function marked with # TODO:
- Do NOT change function signatures
- Add a proper docstring to every function
- Run this file: `python task.py`
- All assert statements at the bottom must pass

Submission:
- Branch: dev/your_name
- PR target: dev
- PR must include: what you learned + any edge cases you found
"""

# ─────────────────────────────────────────
# SECTION 1: List & String Operations
# ─────────────────────────────────────────

def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.

    Example:
        reverse_words("hello world") -> "world hello"
        reverse_words("NavGurukul AI team") -> "team AI NavGurukul"
    """
    # TODO: Implement this function
    # Hint: str.split() and list slicing or reversed() will help
    pass


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Should be case-insensitive.

    Example:
        count_vowels("NavGurukul") -> 4
        count_vowels("HELLO") -> 2
    """
    # TODO: Implement this function
    # Hint: Use a set for O(1) lookup. Consider text.lower()
    pass


def remove_duplicates(items: list) -> list:
    """
    Remove duplicates from a list while preserving the original order.

    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
        remove_duplicates(["a", "b", "a", "c"]) -> ["a", "b", "c"]
    """
    # TODO: Implement this function
    # Hint: A regular set() won't preserve order. Think carefully.
    pass


# ─────────────────────────────────────────
# SECTION 2: Data Processing
# (Relevant to processing student data)
# ─────────────────────────────────────────

def calculate_average(scores: list[float]) -> float:
    """
    Calculate the average of a list of scores.
    Return 0.0 if the list is empty.

    Example:
        calculate_average([80, 90, 70, 85]) -> 81.25
        calculate_average([]) -> 0.0
    """
    # TODO: Implement this function
    # Hint: Handle the empty list edge case first
    pass


def find_top_students(student_scores: dict[str, float], top_n: int) -> list[str]:
    """
    Return the names of the top N students by score, sorted descending.

    Args:
        student_scores: A dict mapping student name -> score
        top_n: How many top students to return

    Example:
        find_top_students({"Priya": 92, "Rahul": 85, "Anita": 97}, 2)
        -> ["Anita", "Priya"]
    """
    # TODO: Implement this function
    # Hint: sorted() with a key and reverse=True, then slice
    pass


def group_by_grade(student_scores: dict[str, float]) -> dict[str, list[str]]:
    """
    Group students into grade buckets based on their score.

    Grade boundaries:
        A: score >= 90
        B: score >= 75
        C: score >= 60
        F: score < 60

    Args:
        student_scores: A dict mapping student name -> score

    Example:
        group_by_grade({"Priya": 92, "Rahul": 72, "Anita": 55})
        -> {"A": ["Priya"], "B": [], "C": ["Rahul"], "F": ["Anita"]}
    """
    # TODO: Implement this function
    # Hint: Initialize all grade keys first, then loop through students
    pass


# ─────────────────────────────────────────
# SECTION 3: Text Processing
# (Relevant to our STT/NLP pipeline)
# ─────────────────────────────────────────

def normalize_transcript(raw_text: str) -> str:
    """
    Clean and normalize a speech transcript.

    Steps to apply (in order):
        1. Strip leading/trailing whitespace
        2. Collapse multiple spaces into a single space
        3. Convert to lowercase
        4. Remove common filler words: ["um", "uh", "like", "you know"]

    Example:
        normalize_transcript("  Um  hello   UH  how  are   you  ")
        -> "hello how are you"
    """
    # TODO: Implement this function
    # Hint: import re — re.sub(r'\s+', ' ', text) collapses whitespace
    import re
    FILLER_WORDS = {"um", "uh", "like", "you know"}
    pass


def word_frequency(text: str) -> dict[str, int]:
    """
    Count the frequency of each word in the text.
    Should be case-insensitive and ignore punctuation.

    Example:
        word_frequency("Hello hello world")
        -> {"hello": 2, "world": 1}
    """
    # TODO: Implement this function
    # Hint: import re — use re.findall(r'\b\w+\b', text.lower())
    import re
    pass


# ─────────────────────────────────────────
# SECTION 4: Bonus Challenge
# ─────────────────────────────────────────

def chunk_list(items: list, chunk_size: int) -> list[list]:
    """
    Split a list into chunks of a given size.
    The last chunk may be smaller than chunk_size.

    Example:
        chunk_list([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
        chunk_list([], 3) -> []
    """
    # TODO: Implement this function
    # Hint: Use a list comprehension with range(0, len(items), chunk_size)
    pass


def flatten(nested: list) -> list:
    """
    Flatten a one-level nested list into a flat list.

    Example:
        flatten([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
        flatten([[], [1], [2, 3]]) -> [1, 2, 3]
    """
    # TODO: Implement this function using a list comprehension
    pass


# ─────────────────────────────────────────
# Tests — DO NOT MODIFY
# Run: python task.py
# All assertions must pass for the exercise to be complete
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("Running Exercise 01 tests...\n")

    # Section 1
    assert reverse_words("hello world") == "world hello", "reverse_words failed"
    assert reverse_words("NavGurukul AI team") == "team AI NavGurukul", "reverse_words failed"
    assert count_vowels("NavGurukul") == 4, "count_vowels failed"
    assert count_vowels("HELLO") == 2, "count_vowels failed"
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4], "remove_duplicates failed"
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"], "remove_duplicates failed"
    print("✅ Section 1 passed")

    # Section 2
    assert calculate_average([80, 90, 70, 85]) == 81.25, "calculate_average failed"
    assert calculate_average([]) == 0.0, "calculate_average empty case failed"
    assert find_top_students({"Priya": 92, "Rahul": 85, "Anita": 97}, 2) == ["Anita", "Priya"], "find_top_students failed"
    grades = group_by_grade({"Priya": 92, "Rahul": 72, "Anita": 55})
    assert grades["A"] == ["Priya"], "group_by_grade A failed"
    assert grades["C"] == ["Rahul"], "group_by_grade C failed"
    assert grades["F"] == ["Anita"], "group_by_grade F failed"
    print("✅ Section 2 passed")

    # Section 3
    assert normalize_transcript("  Um  hello   UH  how  are   you  ") == "hello how are you", "normalize_transcript failed"
    freq = word_frequency("Hello hello world")
    assert freq["hello"] == 2, "word_frequency failed"
    assert freq["world"] == 1, "word_frequency failed"
    print("✅ Section 3 passed")

    # Section 4 (Bonus)
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]], "chunk_list failed"
    assert chunk_list([], 3) == [], "chunk_list empty case failed"
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5], "flatten failed"
    print("✅ Section 4 (Bonus) passed")

    print("\n🎉 All tests passed! You're ready to open your PR.")
