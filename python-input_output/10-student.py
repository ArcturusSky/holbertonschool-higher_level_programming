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

    def to_json(self, attrs=None):
        """
        Public method to retrieves a dictionarys representation of
        student instance
        """

        # If list create empty dictionnary
        if isinstance(attrs, list):
            my_dict = dict()

            # Iterate trough attrs and check if match key of self.__dict__
            for word in attrs:
                if word in self.__dict__:
                    my_dict[word] = self.__dict__[word]

            return my_dict

        else:
            return self.__dict__
