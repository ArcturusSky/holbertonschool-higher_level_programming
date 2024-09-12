#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:                                 # Handle empty list
        return 0

    else:
        weight_tot = 0
        multi_tot = 0

        for tuple in my_list:                       # Going through list
            score, weight = tuple
            # Unpacking tuple

            weight_tot = weight_tot + weight
            # Saving Sum weight for last div

            multi = score * weight
            # Result multi current tuple

            multi_tot = multi_tot + multi
            # Saving Sum score for last div

        average = multi_tot / weight_tot            # Calcul average

        return average
