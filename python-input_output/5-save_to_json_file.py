#!/usr/bin/python3
"""
Module to demonstrate direct writing of an object (python data)
in the form of a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    with a Json representation
    """
    import json

    with open(filename, "w") as file:
        json_representation = json.dumps(my_obj)
        file.write(json_representation)
