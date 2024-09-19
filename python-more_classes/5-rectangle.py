#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.
"""


class Rectangle:
    """
    Creating a class "Rectangle" to define a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with:

        - a private height attribute
        - a privtate width attribute
        """

        self.height = height
        self.width = width

# Getting and setting width before anything to allow checks first

    @property
    def width(self):
        """
        Getter for the private width attribute
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

        self.__width = value

# Getting and setting height before anything to allow checks first

    @property
    def height(self):
        """
        Getter for the private height attribute.
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

        self.__height = value     # Assign the validated value

# Once all checks done in setters, pursuing with methods

    def area(self):
        """

        Calculate and return the area of the rectangle

        """

        return self.height * self.width

    def perimeter(self):
        """

        Calculate and return the perimeter of the rectangle

        """
        if self.height == 0 or self.width == 0:
            return 0
        else:

            return (self.height * 2) + (self.width * 2)

    def my_print(self):
        """
        Public instance method to "draw" the rectangle itself with "#"
        and placing it in the stoudt with space and padding
        """

        # If empty only a empty line
        if self.height == 0 or self.width == 0:
            print("")

        else:
            for rowindex in range(0, self.height):
                for columndindex in range(0, self.width):
                    print("#", end="")
                print("")

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'
        """

        # If either width or height is 0, return an empty string
        if self.width == 0 or self.height == 0:
            return ""

        # Create a list of strings, each representing a row of the rectangle
        string_rec = []
        for row in range(self.width):
            for columndindex in range(0, self.height):
                string_rec.append("#" * self.width)

        # Join the rows with newline characters and return the resulting string
            return "\n".join(string_rec)

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        del self
        print("Bye rectangle...")
