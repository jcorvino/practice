"""
Tests for string_compression
"""
import unittest
from .string_compression import string_compressor


class TestStringCompression(unittest.TestCase):

    def test_string_compressor(self):
        """
        Simple test cases for string_compressor
        """

        self.assertEqual(string_compressor('abc'), 'abc')
        self.assertEqual(string_compressor('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_compressor("this string can't be compressed :("), "this string can't be compressed :(")

