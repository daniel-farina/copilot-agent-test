"""Form handler with input validation and error handling."""

import re

# RFC 5321/5322-inspired pattern: local-part@domain.tld
# Rejects consecutive dots, missing TLD, and multiple @ signs.
_EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}$"
)


class ValidationError(Exception):
    """Raised when form input fails validation."""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


def validate_name(name):
    """Validate a name field.

    Args:
        name: The name value to validate.

    Returns:
        The stripped name string.

    Raises:
        ValidationError: If the name is missing or too long.
    """
    if not name or not str(name).strip():
        raise ValidationError("name", "Name is required")
    name = str(name).strip()
    if len(name) > 100:
        raise ValidationError("name", "Name must be 100 characters or fewer")
    return name


def validate_email(email):
    """Validate an email address field.

    Args:
        email: The email value to validate.

    Returns:
        The normalised (lowercased, stripped) email string.

    Raises:
        ValidationError: If the email is missing or has an invalid format.
    """
    if not email or not str(email).strip():
        raise ValidationError("email", "Email is required")
    email = str(email).strip().lower()
    if not _EMAIL_RE.match(email):
        raise ValidationError("email", "Email address is not valid")
    if len(email) > 254:
        raise ValidationError("email", "Email must be 254 characters or fewer")
    return email


def validate_message(message):
    """Validate a free-text message field.

    Args:
        message: The message value to validate.

    Returns:
        The stripped message string.

    Raises:
        ValidationError: If the message is missing or too long.
    """
    if not message or not str(message).strip():
        raise ValidationError("message", "Message is required")
    message = str(message).strip()
    if len(message) > 2000:
        raise ValidationError("message", "Message must be 2000 characters or fewer")
    return message


def process_contact_form(data):
    """Process and validate a contact-form submission.

    Args:
        data: A dict-like object containing the form fields
              ``name``, ``email``, and ``message``.

    Returns:
        A dict with the validated and normalised form values::

            {"name": ..., "email": ..., "message": ...}

    Raises:
        ValidationError: On the first field that fails validation.
        TypeError: If *data* is not a mapping.
    """
    if not isinstance(data, dict):
        raise TypeError("Form data must be a dictionary")

    validated = {}
    validated["name"] = validate_name(data.get("name"))
    validated["email"] = validate_email(data.get("email"))
    validated["message"] = validate_message(data.get("message"))
    return validated


def process_contact_form_all_errors(data):
    """Process a contact-form submission and collect all validation errors.

    Unlike :func:`process_contact_form`, this function does not stop at the
    first invalid field; instead it gathers every error and returns them
    together.

    Args:
        data: A dict-like object containing the form fields.

    Returns:
        A tuple ``(validated, errors)`` where *validated* is a dict of
        successfully validated fields and *errors* is a dict mapping field
        names to error messages.  If *errors* is empty the submission is
        valid.

    Raises:
        TypeError: If *data* is not a mapping.
    """
    if not isinstance(data, dict):
        raise TypeError("Form data must be a dictionary")

    validators = {
        "name": validate_name,
        "email": validate_email,
        "message": validate_message,
    }

    validated = {}
    errors = {}

    for field, validator in validators.items():
        try:
            validated[field] = validator(data.get(field))
        except ValidationError as exc:
            errors[exc.field] = exc.message

    return validated, errors
