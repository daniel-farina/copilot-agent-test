"""Utility functions with structured logging for tracing function calls in production."""

import logging
import functools
import time

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure structured logging with a consistent format."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )


def log_call(func):
    """Decorator that logs function entry, exit, and elapsed time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("function=%s event=call args=%r kwargs=%r", func.__name__, args, kwargs)
        start = time.monotonic()
        try:
            result = func(*args, **kwargs)
            elapsed = time.monotonic() - start
            logger.info("function=%s event=return elapsed=%.6f", func.__name__, elapsed)
            return result
        except Exception as exc:
            elapsed = time.monotonic() - start
            logger.error(
                "function=%s event=error elapsed=%.6f error=%r",
                func.__name__,
                elapsed,
                exc,
            )
            raise
    return wrapper


@log_call
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


@log_call
def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


@log_call
def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


@log_call
def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers. Raises ValueError on division by zero.

    Note: only exact zero is guarded; near-zero values may still cause numerical
    instability and should be validated by the caller when precision matters.
    """
    if b == 0.0:
        raise ValueError("Division by zero is not allowed")
    return a / b


@log_call
def format_message(template: str, **kwargs) -> str:
    """Return a formatted string from a template and keyword arguments."""
    return template.format(**kwargs)
