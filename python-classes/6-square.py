#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.
"""


class Square:
    """
    Creating a class "Square" to define a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with:

        - a private size attribute
        - a privtate position attribute
        """

        self.size = size
        self.position = position

# Getting and setting size before anything to allow checks first

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

        # Check if value is a positive integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value     # Assign the validated value

# Getting and setting position before anything to allow checks first

    @property
    def position(self):
        """
        Getter for the private position attribute
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the private position attribute and checking errors.
        """

        # Check if correct tuple
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if right amount of integers
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if value are int
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if positive tuple
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

# Once all checks done in setters, pursuing with methods

    def area(self):
        """
        Calculate and return the area of the square
        """

        return self.size * self.size

    def my_print(self):
        """
        Public instance method to "draw" the square itself with "#"
        and placing it in the stoudt with space and padding
        """

        # If empty only a empty line
        if self.size == 0:
            print("")

        else:
            if self.position[1] > 0:
                for index in range(0, self.position[1]):
                    print("")

            for firstindex in range(0, self.size):
                print(" " * self.position[0], end="")
                for secondindex in range(0, self.size):
                    print("#", end="")
                print("")
