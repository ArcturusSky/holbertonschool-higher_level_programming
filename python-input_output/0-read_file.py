#!/usr/bin/python3
"""
Module to test simple input/ouput command
"""


def read_file(filename=""):
    """
    Function to read a file
    print content
    and  automatically close it.
    """

    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content)
