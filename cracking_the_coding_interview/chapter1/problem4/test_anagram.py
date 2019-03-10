"""
Test cases for anagram
"""
import unittest
from .anagram import is_anagram


class TestAnagram(unittest.TestCase):

    def test_is_anagram(self):
        """
        Simple test cases for is_anagram function
        """
        # Basic Cases
        self.assertTrue(is_anagram('restful', 'fluster'))
        self.assertFalse(is_anagram("What's an anagram?", "I don't know"))

        # Edge cases (empty strings)
        self.assertTrue(is_anagram('', ''))
        self.assertFalse(is_anagram('', 'abc'))
        self.assertFalse(is_anagram('abc', ''))

        # Cases w/ ignore
        self.assertFalse(is_anagram('tom marvolo riddle', 'i am lord voldemort'))
        self.assertTrue(is_anagram('tom marvolo riddle', 'i am lord voldemort', ignore=' '))
        self.assertTrue(is_anagram('restful', 'ful', ignore='rest'))
