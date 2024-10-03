#!/usr/bin/python3
"""
Module to create a Pascal's Triangle without any helps
that's gonna be difficult because I don't know what a
Pascal's triangle is.
"""


def pascal_triangle(n):
    """
    Return a list of integers representing the Pascal's
    triangle of "n"
    """

    list_pascal_triangle = list()

    index = 0

    if n <= 0:
        return list_pascal_triangle
    else:
        for index in range(n):
            return (1)