"""
Test cases for reverse_string
"""
import unittest
from .reverse_cstring import reverse_cstring


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        """
        Simple test cases for reverse_cstring function
        """
        self.assertEqual(reverse_cstring('abcd0'), 'dcba0')
        self.assertEqual(reverse_cstring('zzz0'), 'zzz0')
        self.assertEqual(reverse_cstring('0'), '0')
        self.assertRaises(Exception, reverse_cstring, '')  # no null char


