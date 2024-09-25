#!/usr/bin/python3
"""
Module to check if object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """

    if not type(obj) is a_class and isinstance(obj, a_class):
        return True
    else:
        return False
