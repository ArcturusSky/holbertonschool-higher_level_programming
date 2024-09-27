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

        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        next_item = next(self.iterator)
        return next_item
