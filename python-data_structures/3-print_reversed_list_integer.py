#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for index in range(0, len(my_list)):
        print(my_list[index])
