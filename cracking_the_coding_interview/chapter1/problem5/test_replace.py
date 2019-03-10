"""
Test cases for replace
"""
import unittest
from .replace import replace


class TestReplace(unittest.TestCase):

    def test_replace(self):
        """
        Simple test cases for replace function
        """
        self.assertEqual(replace('this is a test'), 'this%20is%20a%20test')
        self.assertEqual(replace('another\ttest\n'), 'another\ttest\n')
