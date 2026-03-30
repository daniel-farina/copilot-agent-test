"""Utility functions for the copilot-agent-test project."""


def hello_world() -> str:
    """Return a hello world greeting string."""
    return "Hello, World!"


def reverse_string(s: str) -> str:
    """Return the reverse of a string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome (case-insensitive, ignoring spaces)."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    normalized = s.lower().replace(" ", "")
    return normalized == normalized[::-1]


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp a numeric value between minimum and maximum (inclusive)."""
    if minimum > maximum:
        raise ValueError("minimum must not be greater than maximum")
    return max(minimum, min(value, maximum))


def flatten(nested: list) -> list:
    """Recursively flatten a nested list into a single flat list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def count_words(text: str) -> int:
    """Return the number of words in a string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())


def unique(items: list) -> list:
    """Return a list with duplicates removed, preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
