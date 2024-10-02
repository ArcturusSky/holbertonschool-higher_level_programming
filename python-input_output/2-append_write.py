#!/usr/bin/python3
"""
Module to demonstrate appending to a file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    encodes in UTF8 and returns the number of characters added.
    """

    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
        return len(text)
