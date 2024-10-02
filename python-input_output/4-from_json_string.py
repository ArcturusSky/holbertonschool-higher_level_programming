#!/usr/bin/python3
"""
Module to demonstration deserialization
"""


def from_json_string(my_str):
    """
    Function that returns an object (Python Data structure)
    represented by a JSON string.
    """

    import json

    python_data = json.loads(my_str)  # convert json data into python data
    return python_data
