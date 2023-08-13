#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    forbidden_chars = {'c', 'C'}
    copy = [x for x in my_string if x not in forbidden_chars]
    return "".join(copy)
