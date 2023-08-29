#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
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
