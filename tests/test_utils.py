"""Unit tests for the utils.py module."""

import pytest
from utils import (
    hello_world,
    reverse_string,
    is_palindrome,
    clamp,
    flatten,
    count_words,
    unique,
)


# ---------------------------------------------------------------------------
# hello_world
# ---------------------------------------------------------------------------

class TestHelloWorld:
    def test_returns_string(self):
        assert isinstance(hello_world(), str)

    def test_expected_value(self):
        assert hello_world() == "Hello, World!"


# ---------------------------------------------------------------------------
# reverse_string
# ---------------------------------------------------------------------------

class TestReverseString:
    def test_basic_reversal(self):
        assert reverse_string("hello") == "olleh"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("a") == "a"

    def test_palindrome_unchanged(self):
        assert reverse_string("racecar") == "racecar"

    def test_type_error_on_non_string(self):
        with pytest.raises(TypeError):
            reverse_string(123)


# ---------------------------------------------------------------------------
# is_palindrome
# ---------------------------------------------------------------------------

class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("RaceCar") is True

    def test_ignores_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_character(self):
        assert is_palindrome("x") is True

    def test_type_error_on_non_string(self):
        with pytest.raises(TypeError):
            is_palindrome(42)


# ---------------------------------------------------------------------------
# clamp
# ---------------------------------------------------------------------------

class TestClamp:
    def test_value_within_range(self):
        assert clamp(5, 1, 10) == 5

    def test_value_below_minimum(self):
        assert clamp(-3, 0, 10) == 0

    def test_value_above_maximum(self):
        assert clamp(15, 0, 10) == 10

    def test_value_at_minimum(self):
        assert clamp(0, 0, 10) == 0

    def test_value_at_maximum(self):
        assert clamp(10, 0, 10) == 10

    def test_float_values(self):
        assert clamp(1.5, 1.0, 2.0) == 1.5

    def test_invalid_range_raises(self):
        with pytest.raises(ValueError):
            clamp(5, 10, 0)


# ---------------------------------------------------------------------------
# flatten
# ---------------------------------------------------------------------------

class TestFlatten:
    def test_already_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_one_level_nested(self):
        assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_mixed_types(self):
        assert flatten([1, "a", [2, "b"]]) == [1, "a", 2, "b"]

    def test_nested_empty_lists(self):
        assert flatten([[], [1, []], [2]]) == [1, 2]


# ---------------------------------------------------------------------------
# count_words
# ---------------------------------------------------------------------------

class TestCountWords:
    def test_simple_sentence(self):
        assert count_words("hello world") == 2

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_empty_string(self):
        assert count_words("") == 0

    def test_extra_whitespace(self):
        assert count_words("  foo   bar  ") == 2

    def test_type_error_on_non_string(self):
        with pytest.raises(TypeError):
            count_words(99)


# ---------------------------------------------------------------------------
# unique
# ---------------------------------------------------------------------------

class TestUnique:
    def test_removes_duplicates(self):
        assert unique([1, 2, 2, 3]) == [1, 2, 3]

    def test_preserves_order(self):
        assert unique([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_empty_list(self):
        assert unique([]) == []

    def test_no_duplicates(self):
        assert unique([1, 2, 3]) == [1, 2, 3]

    def test_all_same(self):
        assert unique([5, 5, 5]) == [5]

    def test_mixed_types(self):
        assert unique([1, "a", 1, "a"]) == [1, "a"]
