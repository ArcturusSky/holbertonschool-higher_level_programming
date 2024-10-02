#!/usr/bin/python3
"""
Module to demonstrate creation of an object from a JSON file
"""


def load_from_json_file(filename):
    """
    Function that creates an object from JSON file
    """
    import json

    with open(filename, "r") as file:
        json_content = file.read()
        python_object = json.loads(json_content)
