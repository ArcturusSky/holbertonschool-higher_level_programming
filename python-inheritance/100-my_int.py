#!/usr/bin/python3
"""
Module for advanced task. Creating a new class int
"""


class MyInt(int):
    """
    New subclass from int BUT is rebel and exchanges operators
    == and !=
    """
    def __new__(cls, value=0):
        # Use __new__ to create an instance of int
        return super().__new__(cls, value)

    def __eq__(self, other):
        # Invert the behavior of equality
        return int(self) != int(other)

    def __ne__(self, other):
        # Invert the behavior of inequality
        return int(self) == int(other)