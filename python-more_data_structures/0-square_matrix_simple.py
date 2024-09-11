#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []                         # Create a new empty matrix

    for row in matrix:                      # Iterate through each lines
        # Create a new line with square of each
        new_row = [num ** 2 for num in row]

        new_matrix.append(new_row)          # Append new row to the new matrix

    return new_matrix
