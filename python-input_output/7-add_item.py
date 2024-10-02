#!/usr/bin/python3
"""
Script to adds all arguments into a python list and then save
them in a file into JSON representation.
"""

if __name__ == "__main__":

    save_to_js_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_js_file = __import__('6-load_from_json_file').load_from_json_file
    import sys
    import os

    filename_json = "add_item.json"

    if os.path.exists(filename_json):
        python_list = load_from_js_file(filename_json)
    else:
        python_list = []

    # Add directly each argument since it's sliced
    python_list.extend(sys.argv[1:])

    save_to_js_file(python_list, "add_item.json")
