#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
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


if __name__ == "__main__":
    unittest.main()
