#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    all_print = 0
    for index in range(0, x):
        try:
            element = (my_list[index])
            print("{:d}".format(element), end="")

        except IndexError:
            break

        all_print = all_print + 1

    print()
    return all_print
