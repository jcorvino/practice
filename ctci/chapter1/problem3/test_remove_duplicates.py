"""
Test cases for remove_duplicates
"""
import unittest
from .remove_duplicates import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        """
        Simple test cases for remove_duplicates function
        """
        self.assertEqual(remove_duplicates('ababc'), 'abc')
        self.assertEqual(remove_duplicates(''), '')
        self.assertEqual(remove_duplicates('z'), 'z')
        self.assertEqual(remove_duplicates('no duplicates'), 'no duplicates')
        self.assertEqual(remove_duplicates('this is a string'), 'this arng')
        self.assertEqual(remove_duplicates('aaaabbbbccccdeeeacbca'), 'abcde')
