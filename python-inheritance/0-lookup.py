#!/usr/bin/python3
"""
This module defines a function called lookup
"""


def lookup(obj):
    """
    Function to return a list of available attributes
    and methods of an object
    """

    attribute_list = dir(obj)
    return attribute_list
