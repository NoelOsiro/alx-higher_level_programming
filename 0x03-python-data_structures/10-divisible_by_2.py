#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for num in my_list:
        multiples.append(num % 2 == 0)
    return multiples
