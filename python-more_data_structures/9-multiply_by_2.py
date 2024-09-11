#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new_dict = a_dictionary.copy()

    # Assigning key to key and value to value
    for key, value in new_dict.items():
        # Iterate and double the value var
        value = value * 2
        new_dict.update({key: value})

    return new_dict
