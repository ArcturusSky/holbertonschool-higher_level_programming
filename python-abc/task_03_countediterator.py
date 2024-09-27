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
        try:
            next_item = next(self.iterator)
            self.counter += 1
            return next_item
        except StopIteration:
            raise StopIteration("End of iterator reached.")

    def get_count(self):
        """ Method that returns number of items returnes"""
        return self.counter


# Test code to run when module is executed as a script
if __name__ == "__main__":
    test_counter = [1, 2, 4, 8, 16]
    counted = CountedIterator(test_counter)

    try:
        while True:
            item = next(counted)
            print(f"Got {item}, total {counted.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
