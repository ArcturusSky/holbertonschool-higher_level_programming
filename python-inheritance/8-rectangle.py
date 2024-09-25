#!/usr/bin/python3
"""
Module that will define a subclass rectangle
that will inherite from BaseGeometry
to show use of sub and superclasses
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass that inherits all its methods from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Constructor method to init private attributes
        width and height
        """

        # Validate and assign width and height
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
