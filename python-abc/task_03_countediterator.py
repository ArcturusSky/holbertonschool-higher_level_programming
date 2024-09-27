#!/usr/bin/env python3
"""
Module to understand modification of built-in, here
iterator.
"""


class CountedIterator():
    """
    Class that will extends the buil-in iterator obtained from
    the iter function
    """

    def __init__(self, iterator):
        """
        Method that initialise iterator and countr
        """

        self.iterator = iter(iterator)
        self.counter = 0

    def __next__(self):
        """
        Method that returns the next item and count
        """
        self.counter += 1
        next_item = next(self.iterator)
        return next_item

    def get_count(self):
        """ Method that returns number of items returnes"""
        return self.counter


