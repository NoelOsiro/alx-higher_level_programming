#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints and returns the last digit of a number.

    :param number: The input number.
    :type number: int
    :return: The last digit of the input number.
    :rtype: int
    """
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
