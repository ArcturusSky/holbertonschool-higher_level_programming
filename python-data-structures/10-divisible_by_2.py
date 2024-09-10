#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = my_list[:]               # Create shallow copy my_list

    for index in range(len(my_list)):   # Iterate in lists

        if my_list[index] % 2 == 0:     # Check if divisible by 2
            new_list[index] = True

        else:
            new_list[index] = False

    return new_list
