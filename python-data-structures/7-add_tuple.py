#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:                # Check if enough item  in tuple
        my_lista = list(tuple_a)        # Convert to list to be mutable

        while len(my_lista) < 2:        # Append 0 until correct len
            my_lista.append(0)

        tuple_a = tuple([my_lista[0], my_lista[1]]) # Convert back to tuple

    if len(tuple_b) < 2:                # Same for tuple_b
        my_listb = list(tuple_b)        

        while len(my_listb) < 2:
            my_listb.append(0)

        for index in range (0, 1):
            if my_listb[index] == None:
                my_listb[index] = 0

        tuple_b = tuple([my_listb[0], my_listb[1]]) # Convert back to tuple
    
    # Unpack into var, add each, convert back to tuple
    a1, b1 = tuple_a
    a2, b2 = tuple_b
    a = a1 + a2
    b = b1 + b2
    tuple_ab = (a, b)
    return tuple_ab
