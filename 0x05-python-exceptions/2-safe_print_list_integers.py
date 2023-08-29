#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    printed_count = 0
    for element in my_list:
        if printed_count < x:
            try:
                formatted_element = "{:d}".format(element)
                print(formatted_element, end="")
                printed_count += 1
            except (ValueError, TypeError):
                pass
        else:
            break
    print()
    return printed_count
