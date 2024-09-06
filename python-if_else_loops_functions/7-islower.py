#!/usr/bin/python3
def islower(c):
    ascii = ord(c)
    if ascii in range(97, 123):
        return True
    else:
        return False
