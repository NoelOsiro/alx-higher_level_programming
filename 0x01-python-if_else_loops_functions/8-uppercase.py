#!/usr/bin/python3
def uppercase(Str):
    """
    Prints the input string in uppercase followed by a new line.

    :param Str: The input string.
    :type Str: str
    """
    for char in Str:
        uppercase_char = chr(ord(char) - ord('a') + ord('A')) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end="")
    print()
