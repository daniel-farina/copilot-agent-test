"""Tests for form_handler input validation."""

import pytest

from form_handler import (
    ValidationError,
    process_contact_form,
    process_contact_form_all_errors,
    validate_email,
    validate_message,
    validate_name,
)


# ---------------------------------------------------------------------------
# validate_name
# ---------------------------------------------------------------------------

class TestValidateName:
    def test_valid_name(self):
        assert validate_name("Alice") == "Alice"

    def test_strips_whitespace(self):
        assert validate_name("  Bob  ") == "Bob"

    def test_empty_string_raises(self):
        with pytest.raises(ValidationError) as exc_info:
            validate_name("")
        assert exc_info.value.field == "name"

    def test_whitespace_only_raises(self):
        with pytest.raises(ValidationError):
            validate_name("   ")

    def test_none_raises(self):
        with pytest.raises(ValidationError):
            validate_name(None)

    def test_name_too_long_raises(self):
        with pytest.raises(ValidationError) as exc_info:
            validate_name("A" * 101)
        assert "100" in exc_info.value.message

    def test_name_exactly_max_length_allowed(self):
        assert len(validate_name("A" * 100)) == 100


# ---------------------------------------------------------------------------
# validate_email
# ---------------------------------------------------------------------------

class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") == "user@example.com"

    def test_normalises_to_lowercase(self):
        assert validate_email("User@Example.COM") == "user@example.com"

    def test_strips_whitespace(self):
        assert validate_email("  user@example.com  ") == "user@example.com"

    def test_empty_string_raises(self):
        with pytest.raises(ValidationError) as exc_info:
            validate_email("")
        assert exc_info.value.field == "email"

    def test_none_raises(self):
        with pytest.raises(ValidationError):
            validate_email(None)

    def test_missing_at_sign_raises(self):
        with pytest.raises(ValidationError):
            validate_email("notanemail.com")

    def test_missing_domain_raises(self):
        with pytest.raises(ValidationError):
            validate_email("user@")

    def test_consecutive_dots_in_domain_raises(self):
        with pytest.raises(ValidationError):
            validate_email("user@domain..com")

    def test_multiple_at_signs_raises(self):
        with pytest.raises(ValidationError):
            validate_email("user@@domain.com")

    def test_email_too_long_raises(self):
        local = "a" * 245
        with pytest.raises(ValidationError) as exc_info:
            validate_email(f"{local}@example.com")
        assert "254" in exc_info.value.message


# ---------------------------------------------------------------------------
# validate_message
# ---------------------------------------------------------------------------

class TestValidateMessage:
    def test_valid_message(self):
        assert validate_message("Hello, world!") == "Hello, world!"

    def test_strips_whitespace(self):
        assert validate_message("  hi  ") == "hi"

    def test_empty_string_raises(self):
        with pytest.raises(ValidationError) as exc_info:
            validate_message("")
        assert exc_info.value.field == "message"

    def test_whitespace_only_raises(self):
        with pytest.raises(ValidationError):
            validate_message("   ")

    def test_none_raises(self):
        with pytest.raises(ValidationError):
            validate_message(None)

    def test_message_too_long_raises(self):
        with pytest.raises(ValidationError) as exc_info:
            validate_message("x" * 2001)
        assert "2000" in exc_info.value.message

    def test_message_exactly_max_length_allowed(self):
        assert len(validate_message("x" * 2000)) == 2000


# ---------------------------------------------------------------------------
# process_contact_form
# ---------------------------------------------------------------------------

class TestProcessContactForm:
    def test_valid_submission(self):
        data = {"name": "Alice", "email": "alice@example.com", "message": "Hi there"}
        result = process_contact_form(data)
        assert result == {"name": "Alice", "email": "alice@example.com", "message": "Hi there"}

    def test_raises_on_missing_name(self):
        data = {"name": "", "email": "alice@example.com", "message": "Hi"}
        with pytest.raises(ValidationError) as exc_info:
            process_contact_form(data)
        assert exc_info.value.field == "name"

    def test_raises_on_invalid_email(self):
        data = {"name": "Alice", "email": "bad-email", "message": "Hi"}
        with pytest.raises(ValidationError) as exc_info:
            process_contact_form(data)
        assert exc_info.value.field == "email"

    def test_raises_on_missing_message(self):
        data = {"name": "Alice", "email": "alice@example.com", "message": ""}
        with pytest.raises(ValidationError) as exc_info:
            process_contact_form(data)
        assert exc_info.value.field == "message"

    def test_raises_type_error_for_non_dict(self):
        with pytest.raises(TypeError):
            process_contact_form("not a dict")

    def test_raises_type_error_for_none(self):
        with pytest.raises(TypeError):
            process_contact_form(None)


# ---------------------------------------------------------------------------
# process_contact_form_all_errors
# ---------------------------------------------------------------------------

class TestProcessContactFormAllErrors:
    def test_valid_submission_returns_no_errors(self):
        data = {"name": "Bob", "email": "bob@example.com", "message": "Hello"}
        validated, errors = process_contact_form_all_errors(data)
        assert errors == {}
        assert validated["name"] == "Bob"

    def test_multiple_invalid_fields_returns_all_errors(self):
        data = {"name": "", "email": "bad", "message": ""}
        _, errors = process_contact_form_all_errors(data)
        assert "name" in errors
        assert "email" in errors
        assert "message" in errors

    def test_partial_errors(self):
        data = {"name": "Carol", "email": "bad-email", "message": "Hi"}
        validated, errors = process_contact_form_all_errors(data)
        assert "email" in errors
        assert "name" not in errors
        assert "message" not in errors
        assert validated.get("name") == "Carol"

    def test_raises_type_error_for_non_dict(self):
        with pytest.raises(TypeError):
            process_contact_form_all_errors(42)
