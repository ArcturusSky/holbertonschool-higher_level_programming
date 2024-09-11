#!/usr/bin/python3
def best_score(a_dictionary):

    # Check if empty. Warning "None" check if exactly None.
    if not a_dictionary:
        return None
    else:

        # return the key corresponding to max
        return max(a_dictionary, key=a_dictionary.get)
