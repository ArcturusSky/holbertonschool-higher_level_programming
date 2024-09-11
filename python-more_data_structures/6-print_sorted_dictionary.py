#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    keys = a_dictionary.keys()      # Retrieving each key
    orderering = list(keys)         # Converting to list
    orderering.sort                 # Ordering list

    for key in orderering:          # Print each key in ordered list
        print("{}: {}".format(key, a_dictionary[key]))
