#!/usr/bin/python3
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    line_count = 0
    with open(filename) as file:
        for line in file:
            line_count += 1
    return line_count
