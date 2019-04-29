"""
Test cases for string_rotation
"""
import unittest
from .string_rotation import string_rotation


class TestStringRotation(unittest.TestCase):

    def test_string_rotation(self):
        """
        Simple test cases for string_rotation function
        """
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(string_rotation(s1, s2))  # proper rotation
        self.assertTrue(string_rotation(s1, s1))  # same string
        self.assertFalse(string_rotation(s1, 'waterbottles'))  # different len
        self.assertFalse(string_rotation(s1, 'samelen1234'))  # not a rotation
        self.assertTrue(string_rotation('', ''))  # empty case
