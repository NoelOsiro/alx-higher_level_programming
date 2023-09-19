#!/usr/bin/python3
"""Defines unittests for rectangle.py.

Unittest classes:
    TestRectangle - line 10
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        r = Rectangle(10, 20, 30, 40, 1)

        # Check if private attributes are correctly set.
        self.assertEqual(r._Base__nb_objects, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 1)

    def test_getters_and_setters(self):
        """Test getters and setters for private attributes."""
        r = Rectangle(10, 20, 30, 40, 1)

        # Test getters
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 1)

        # Test setters
        r.width = 50
        r.height = 60
        r.x = 70
        r.y = 80
        r.id = 2

        self.assertEqual(r.width, 50)
        self.assertEqual(r.height, 60)
        self.assertEqual(r.x, 70)
        self.assertEqual(r.y, 80)
        self.assertEqual(r.id, 2)

    def test_area(self):
        """Test the area method of the Rectangle class."""
        r = Rectangle(5, 10, 0, 0, 1)
        self.assertEqual(r.area(), 50)

    def display(self):
        """Display the rectangle by printing it with '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance.

        Args:
            *args: Variable-length positional arguments in the following order:
                - 1st argument: id attribute
                - 2nd argument: width attribute
                - 3rd argument: height attribute
                - 4th argument: x attribute
                - 5th argument: y attribute
            **kwargs: Variable-length keyword arguments, where each key represents an attribute to update.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


if __name__ == "__main__":
    unittest.main()
