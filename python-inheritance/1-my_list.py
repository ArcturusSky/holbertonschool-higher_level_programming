#!/usr/bin/python3
"""
Module retrieve a list from inherited list and sort
it in ascending order
"""


class MyList(list):
    """
    Class that inherits from "list"
    """

    def print_sorted(self):
        """
        Function that prints the list but in ascending order
        """

        print(sorted(self))
