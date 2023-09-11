#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: List of attributes and methods.
    """
    return dir(obj)
