#!/usr/bin/python3
def lookup(obj):
    """
    Function to return a list of available attributes
    and methods of an object
    """

    attribute_list = dir(obj)
    return attribute_list
