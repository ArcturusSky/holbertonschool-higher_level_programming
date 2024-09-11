#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string:
        return 0
    elif roman_string is None:
        return 0
    else:

        roman_dic = {
            "I": 1, "II": 2, "III": 3, "IV": 4,
            "V": 5, "VI": 6, "VII": 7, "VII": 8,
            "IX": 9, "X": 10, "L": 50, "C": 100, "D": 500
            }
        number = 0
        for key in roman_dic:
            if roman_string == key:
                number = number + roman_dic[key]

                return number
