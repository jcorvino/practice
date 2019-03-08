"""
Test cases for unique_string
"""
import unittest
from .unique_string import is_unique_1, is_unique_2


class TestUniqueString(unittest.TestCase):
    def test_is_unique_1(self):
        """
        Simple test cases for is_unique_1 function
        """
        self.assertTrue(is_unique_1('abcd'))
        self.assertFalse(is_unique_1('zzz'))
        self.assertFalse(is_unique_1('123.098670asdf'))
        self.assertTrue(is_unique_1('a'))
        self.assertTrue(is_unique_1(''))

    def test_is_unique_2(self):
        """
        Simple test cases for is_unique_2 function
        """
        self.assertTrue(is_unique_2('abcd'))
        self.assertFalse(is_unique_2('zzz'))
        self.assertFalse(is_unique_2('123.098670asdf'))
        self.assertTrue(is_unique_2('a'))
        self.assertTrue(is_unique_2(''))


