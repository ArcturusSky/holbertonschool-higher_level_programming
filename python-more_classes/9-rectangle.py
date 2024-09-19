#!/usr/bin/python3
"""
This module provides the first step into creating
and understanding classes.
"""


class Rectangle:
    """
    Creating a class "Rectangle" to define a rectangle
    """
    number_of_instances = 0     # Class attribute
    print_symbol = "#"          # Class attribute for string reprensetation

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with:

        - a private height attribute
        - a privtate width attribute
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        print_symbol = Rectangle.print_symbol

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
                    print(self.print_symbol, end="")
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
                string_rec.append(str(self.print_symbol) * self.width)

        # Join the rows with newline characters and return the resulting string
            return "\n".join(string_rec)

# Return the official representation to know what fonction it is
# here it's "Rectancle(2, 4)" if "2" and "4" were the parameters

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval
        """
        return "Rectangle({}, {})".format(self.width, self.height)

# DESTRUCTOR #

    def __del__(self):
        """
        Delete the current instance and free its memory + update counter
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# Static method to compare the area of rectangle instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle base on the area
        """

        # Check if parameters are instance of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Comparing areas of each instance
        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

# Class method to create a square rectangle

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with square features
        """

        return cls(size, size)
