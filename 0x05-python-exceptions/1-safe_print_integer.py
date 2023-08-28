#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except (TypeError, ValueError):
        return (False)
