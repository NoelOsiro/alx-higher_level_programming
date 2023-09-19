#!/usr/bin/python3
"""Module for the Base class."""


class Base:
    """Base class for managing id attribute in future classes."""

    # Private class attribute to keep track of the number of objects.
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique id.

        Args:
            id (int, optional): The id to assign to the instance. Defaults to None.

        Note:
            If id is provided, it will be assigned to the instance.
            If id is not provided, __nb_objects will be incremented, and
            the new value will be assigned to the instance as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
