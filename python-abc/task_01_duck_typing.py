#!/usr/bin/env python3
"""
Module to demonstrate ducktyping and abstract base classes in Python.

This module defines an abstract Shape class and two concrete subclasses,
Circle and Rectangle. It also includes a function to demonstrate ducktyping.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    This class defines the interface for all shapes, requiring
    implementations of area and perimeter calculations.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        This method must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        This method must be implemented by all subclasses.
        """
        pass

class Circle(Shape):
    """
    Concrete class representing a circle.

    This class implements the Shape interface for a circle.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius * self.radius)
    
    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return math.pi * (self.radius * 2)

class Rectangle(Shape):
    """
    Concrete class representing a rectangle.

    This class implements the Shape interface for a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return (self.width * 2) + (self.height * 2)

def shape_info(any_argument):
    """
    Print the area and perimeter of any shape object.

    This function demonstrates ducktyping by working with any object
    that has area() and perimeter() methods, regardless of its actual class.

    Args:
        any_argument (Shape): Any object that implements area() and perimeter() methods.
    """
    area = any_argument.area()
    perimeter = any_argument.perimeter()

    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
