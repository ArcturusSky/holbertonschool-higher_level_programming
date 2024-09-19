#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.
"""


class Rectangle:
    """
    Creating a class "Rectangle" to define a rectangle
    """

    def __init__(self, width=0, height=(0, 0)):
        """
        Initializes the rectangle with:

        - a private width attribute
        - a privtate height attribute
        """

        self.width = width
        self.height = height

# Getting and setting width before anything to allow checks first

    @property
    def width(self):
        """
        Getter for the private width attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private width attribute and checking errors.
        """

        # Check if value is a positive integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value     # Assign the validated value

# Getting and setting height before anything to allow checks first

    @property
    def height(self):
        """
        Getter for the private height attribute
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private height attribute and checking errors.
        """

        # Check if value is a positive integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

# Once all checks done in setters, pursuing with methods

#    def area(self):
#        """
#       Calculate and return the area of the rectangle
#        """

#        return self.width * self.height

#
#    def my_print(self):
#        """
#        Public instance method to "draw" the rectangle itself with "#"
#        and placing it in the stoudt with space and padding
#        """
#
#        # If empty only a empty line
#        if self.width == 0:
#            print("")
#
#        else:
#            if self.height[1] > 0:
#                for index in range(0, self.height[1]):
#                    print("")
#
#            for firstindex in range(0, self.width):
#                print(" " * self.height[0], end="")
#                for secondindex in range(0, self.width):
#                    print("#", end="")
#                print("")
#