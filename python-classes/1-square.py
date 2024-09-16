#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.

"""


class Square:
    """
    Creating a class "Square" to define a square
    """
    def __init__(self, size):
        """
        Initializes the square with a private size attribute
        """
        self.__size = size
