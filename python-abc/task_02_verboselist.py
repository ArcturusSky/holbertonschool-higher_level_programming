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

        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """
        Method to remove an item but with verbose
        """

        if item not in self or item is None:
            return None

        else:
            super().remove(item)
            print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """
        Method to pop an item but with verbose
        """

        item = self[index]
        super().pop(index)
        print("Popped [{}] from the list.".format(item))
