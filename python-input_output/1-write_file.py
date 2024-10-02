#!/usr/bin/python3
"""
Module to demonstrate writing with I/O
"""


def write_file(filename="", text=""):
    """
    Function that write a string
    to a text file in UTF8
    and return numbers of charaters
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
