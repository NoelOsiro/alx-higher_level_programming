#!/usr/bin/python3
"""Defines unittests for rectangle.py.

Unittest classes:
    TestRectangle - line 12
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

if __name__ == "__main__":
    unittest.main()
