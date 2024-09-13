#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length

    for index in range(0, list_length):

        try:
            new_list[index] = my_list_1[index] / my_list_2[index]

        except IndexError:
            print("out of range")
            new_list[index] = 0

        except ZeroDivisionError:
            print("division by 0")
            new_list[index] = 0

        except TypeError:
            print("wrong type")
            new_list[index] = 0
        
        finally:
            if len(new_list) <= index:
                new_list.append(0)

    return new_list
