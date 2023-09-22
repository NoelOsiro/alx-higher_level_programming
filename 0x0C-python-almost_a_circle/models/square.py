#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square with new attributes.

        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg) if i < len(attrs) else None

        elif kwargs:
            for k, v in kwargs.items():
                if k in ("id", "size", "x", "y"):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)
