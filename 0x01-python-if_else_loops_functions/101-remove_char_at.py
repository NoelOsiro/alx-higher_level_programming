#!/usr/bin/python3
def remove_char_at(s, n):
    """
    Creates a copy of the string with the character at position n removed.

    :param s: The input string.
    :type s: str
    :param n: The position of the character to remove.
    :type n: int
    :return: The modified string with the character removed.
    :rtype: str
    """
    if n < 0 or n >= len(s):
        return s 
    return s[:n] + s[n + 1:]
