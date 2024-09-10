#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:           # Check if empty list
        return None

    my_list.sort()                  # Order list by size
    return my_list[-1]              # Return last one
