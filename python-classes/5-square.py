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

        self.size = size      # Check for error moved to setter

    def area(self):
        """
        Calculate and return the area of the square
        """

        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter for the private size attribute.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private size attribute and checking errors.
        """

        if not isinstance(value, int):      # Check validation error
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value     # Assign the validated value

    def my_print(self):
        """
        Public instance method to "draw" the square itself with #
        """

        if self.__size == 0:
            print("")
        else:
            for firstindex in range(0, self.__size):
                for secondindex in range(0, self.__size):
                    print("#", end="")
                print("")
