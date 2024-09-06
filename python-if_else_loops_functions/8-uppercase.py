#!/usr/bin/python3
def uppercase(str):
    upper_string = ""
    for char in str:
        ascii_numb = ord(char)
        if ascii_numb in range(97, 123):
            upper_string += chr(ascii_numb - 32)
        else:
            upper_string += char
    print("{}".format(upper_string))
