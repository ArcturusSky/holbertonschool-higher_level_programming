#!/usr/bin/python3
"""
Module to create a student and retrieves a
dictionary representation
of a student instance
"""


class Student:
    """
    Class to create a simple student with simple attributes
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor method to init attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method to retrieves a dictionarys representation of
        student instance
        """

        return self.__dict__
