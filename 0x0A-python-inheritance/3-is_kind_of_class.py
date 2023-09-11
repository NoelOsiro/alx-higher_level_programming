#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
