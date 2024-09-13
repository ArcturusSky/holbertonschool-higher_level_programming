#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string:            # Check if exist and/or empty
        return 0
    elif roman_string is None:
        return 0

    else:                           # Create a dic for roman values
        roman_dic = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
            }

        number = 0
        prev_value = 0

    # Reverse the Roman numeral string to simplify
    # the logic for adding/subtracting values
        reverse_string = reversed(roman_string)

        for char in reverse_string:
            value = roman_dic[char]     # Get the Roman value from dic

            if value < prev_value:      # Check if value less than previous
                number = number - value     # if less then substract it.
            else:
                number = number + value

            prev_value = value

        return number
