#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = my_list.copy()           # Create a coopy to avoid mod original

    for index in range(len(new_list)):  # Iteration

        if new_list[index] == search:   # Search and replace
            new_list[index] = replace

    return new_list
