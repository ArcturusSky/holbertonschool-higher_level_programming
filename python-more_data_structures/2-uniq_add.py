#!/usr/bin/python3
def uniq_add(my_list=[]):

    remove_dup = set(my_list)
    total = 0
    for num in remove_dup:
        total += num

    return total
