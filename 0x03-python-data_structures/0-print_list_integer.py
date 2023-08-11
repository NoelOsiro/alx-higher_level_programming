#!/usr/bin/python3
def print_list_integer(my_list=None):
    """
    Prints all integers in the given list.
    Args:
        my_list (list): List of integers to print.
    """
    if my_list is None:
        my_list = []

    for num in my_list:
        print("{:d}".format(num))
