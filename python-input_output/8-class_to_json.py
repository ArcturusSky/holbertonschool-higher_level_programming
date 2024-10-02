#!/usr/bin/python3
"""
Module to serialize a class
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description of an object
    using simple data structures (list, dictionary, string, integer, 
    and boolean) for JSON serialization.

    Parameters:
    obj: The object to serialize.

    Returns:
    A dictionary representing the object's simple attributes.
    """

    return obj.__dict__
