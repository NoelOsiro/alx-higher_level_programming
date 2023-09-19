#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 14
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_auto_id_assignment(self):
        """Test that Base automatically assigns a unique ID."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_auto_id_increment(self):
        """Test that Base automatically assigns IDs incrementally."""
        # Create multiple Base instances without specifying an ID.
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b2.id + 1, b3.id)

    def test_custom_id_assignment(self):
        """Test that Base saves the ID passed as an argument."""
        # Create a Base instance with a specific ID (e.g., 89).
        b = Base(89)

        # Check if the instance has the ID passed as an argument.
        self.assertEqual(b.id, 89)

    def test_base_constructor_with_id(self):
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    def test_base_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = '[{"id": 1,"width": 10, "height": 7,'
        s2 = '  "x": 2, "y": 8}, {"id": 2, "width": 2, '
        s3 = '"height": 4, "x": 0, "y": 0}]'
        json_str = Rectangle.to_json_string(
            [r1.to_dictionary(),
             r2.to_dictionary()])
        self.assertTrue(isinstance(json_str, str))
        self.assertEqual(json_str, s1 + s2 + s3)

    def test_from_json_string(self):
        s1 = '[{"id": 1,"width": 10, "height": 7,'
        s2 = '  "x": 2, "y": 8}, {"id": 2, "width": 2, '
        s3 = '"height": 4, "x": 0, "y": 0}]'
        json_str = s1 + s2 + s3
        json_list = Rectangle.from_json_string(json_str)
        self.assertTrue(isinstance(json_list, list))
        self.assertEqual(len(json_list), 2)
        self.assertTrue(isinstance(json_list[0], dict))
        self.assertEqual(json_list[0]['width'], 10)

    def test_save_to_file_and_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, 10)
        self.assertEqual(loaded_rectangles[1].height, 4)

    def test_create_method(self):
        r_dict = {
            'id': 5,
            'width': 3,
            'height': 4,
            'x': 1,
            'y': 2}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.x, 1)

    def test_save_to_file_csv_and_load_from_file_csv(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(loaded_squares[0].size, 5)
        self.assertEqual(loaded_squares[1].y, 1)

    def test_draw_method(self):
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(5)
        self.assertIsNone(Base.draw([r1], [s1]))


if __name__ == "__main__":
    unittest.main()
