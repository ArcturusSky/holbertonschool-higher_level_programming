#!/usr/bin/python3
def no_c(my_string):
    new_string_list = list(my_string)
    values_to_remove = {"c", "C"}
    new_string_list = [item for item in new_string_list if item not in values_to_remove]
    new_string = ''.join(new_string_list)
    return new_string
