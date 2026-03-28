def greet(name):
    """Return a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting string addressed to the given name.
    """
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def is_even(number):
    """Check whether a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0


def factorial(n):
    """Compute the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
