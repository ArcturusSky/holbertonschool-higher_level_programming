#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)

    if length == 0:                     # Check if empty string
        first_char = None

    else:
        first_char = sentence[0]        # Extract first char

    my_tuple = (length, first_char)     # Create tuple
    return my_tuple
