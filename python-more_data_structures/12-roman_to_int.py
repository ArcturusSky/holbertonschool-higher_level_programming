#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string:            # Check if exist and/or empty
        return 0

    else:                           # Create a dic for roman values
        roman_dic = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
            }

        number = 0
        prev_value = 0

    # Reverse the Roman numeral string to process it from right to left
    for char in reversed(roman_string):
        value = roman_dic[char]  # Get the Roman value from the dictionary

        # Subtract value if it is smaller than the previous value
        if value < prev_value:
            number -= value
        else:
            number += value

        # Update prev_value to the current value
        prev_value = value

    return number
