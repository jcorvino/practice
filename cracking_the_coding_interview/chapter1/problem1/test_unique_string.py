"""
Test cases for unique_string
"""
import unittest
from .unique_string import is_unique


class TestUniqueString(unittest.TestCase):
    def test_is_unique(self):
        """
        Simple test cases for is_unique function
        """
        self.assertTrue(is_unique('abcd'))
        self.assertFalse(is_unique('zzz'))
        self.assertFalse(is_unique('123.098670asdf'))
        self.assertTrue(is_unique('aA'))


