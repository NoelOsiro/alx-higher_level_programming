#!/usr/bin/python3
"""Module for the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)  # Call the constructor of the base class with the provided id.
        
        # Private instance attributes with public getters and setters.
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter methods for private attributes.
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    # Setter methods for private attributes.
    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
