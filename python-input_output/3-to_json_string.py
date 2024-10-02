#!/usr/bin/python3
"""
Module to demonstration serialization
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of an object (string here)
    """

    import json

    json_data = json.dumps(my_obj)  # convert python data in json
    return json_data
