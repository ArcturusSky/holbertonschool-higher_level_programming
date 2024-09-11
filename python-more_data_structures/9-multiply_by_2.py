#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    # For each value in "values"  * 2
    new_dict = {value: value * 2 for value in a_dictionary.values()}

    return new_dict
