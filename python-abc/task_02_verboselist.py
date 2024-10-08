#!/usr/bin/env python3
"""
Module to demonstrate extending python built-in
"""


class VerboseList(list):
    """
    Class that inherits from list to desponstrate the possibility
    of extending built-in.
    """

    def append(self, item):
        """
        Method to append an item but with verbose
        """

        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Method to extend the but with verbose
        """

        size = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(size))

    def remove(self, item):
        """
        Method to remove an item but with verbose
        """

        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Method to pop an item but with verbose
        """

        item = self[index]
        print("Popped [{}] from the list.".format(item))
        super().pop(index)
