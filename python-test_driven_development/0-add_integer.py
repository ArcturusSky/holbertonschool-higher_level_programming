#!/usr/bin/python3

"""
This module provides a function for basic add operation.
"""


def add_integer(a, b=98):
    """
    This function adds two numbers together and return the result.

    Args:
        a: first number
        b: second number (default is 98)

    Return:
        sum of a and b

    Raises:
        TypeError: If a or b is not an integer or float.
    """

# Error if not int or float

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

# Error if infinite or -infinite

    if a == float('inf') or a == float('-inf'):
        raise OverflowError
    if b == float('inf') or b == float('-inf'):
        raise OverflowError


# Error if "NaN"

    if a != a:
        raise ValueError
    if b != b:
        raise ValueError

# If everything correct, cast in int

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
