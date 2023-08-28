#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    try:
        printed_count = 0
        for element in my_list:
            if printed_count < x:
                print(element,end='')
                printed_count += 1
            else:
                break
        print()
        return printed_count
    except:
        return printed_count
