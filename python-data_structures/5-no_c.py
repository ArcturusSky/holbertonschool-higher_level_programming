#!/usr/bin/python3
def no_c(my_string):
    new_string_list = list(my_string)
    rem_c = {"c", "C"}
    new_string_list = [item for item in new_string_list if item not in rem_c]
    new_string = ''.join(new_string_list)
    return new_string
