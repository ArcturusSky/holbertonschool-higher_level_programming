#!/usr/bin/python3
"""
Module that hold the BaseGeometry class and
will hold its methods and potential subclasses
"""


class BaseGeometry:
    """
    Class that will hold several methods and potential
    subclasses about geometry.
    """

    def area(self):
        """
        Will probably be used to def area later
        for now only raise exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value and raise errors if not correct
        """

        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
