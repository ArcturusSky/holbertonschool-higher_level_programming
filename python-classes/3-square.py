#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.

"""


class Square:
    """
    Creating a class "Square" to define a square
    """
    def __init__(self, size=0):
        """
        Initializes the square with a private size attribute
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate and return the area of the square
        """
        self.area = self.__size * self.__size   # storing area value

        return self.area
