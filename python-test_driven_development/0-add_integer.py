#!/usr/bin/python3

"""
This module provides a function for basic add operation.
Adds two numbers together (with "b" = 98 by default)
Return: sum
"""


def add_integer(a, b=98):
    """
    This function adds two numbers together and return the result.
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
