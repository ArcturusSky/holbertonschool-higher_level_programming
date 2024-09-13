#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length

    for index in range(0, list_length):

        try:
            new_list[index] = (my_list_1[index] / my_list_2[index])

        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")

    return new_list
