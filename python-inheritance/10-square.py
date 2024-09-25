#!/usr/bin/python3
"""
Module that will define a subclass Square
that will inherite from the subclass Rectangle
to show use of chain inheritance
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass that inherits all its methods from the subclasse
    Rectangle
    """

    def __init__(self, size):
        """
        Constructor method to init private attributes
        width and height
        """

        # Validate and assign size
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method that retrive the area method inherited from
        Rectangle
        """

        return self.__size * self.__size

    def __str__(self):
        """
        Method to return the rectangle description in the format:
        [Rectangle] <size>/<size>
        """

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
