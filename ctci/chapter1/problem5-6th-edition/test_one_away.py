"""
Tests for one_away
"""
import unittest
from .one_away import one_away_1, one_away_2


class TestOneAway(unittest.TestCase):

    def test_one_away_1(self):
        """
        Simple test for one_away_1
        """
        self.assertTrue(one_away_1('pale', 'ple'))
        self.assertTrue(one_away_1('pales', 'pale'))
        self.assertTrue(one_away_1('pale', 'bale'))
        self.assertFalse(one_away_1('pale', 'bake'))
        self.assertTrue(one_away_1('', 'e'))
        self.assertTrue(one_away_1('ppppaaaa', 'pppaaaa'))

    def test_one_away_2(self):
        """
        Simple test for one_away_2
        """
        self.assertTrue(one_away_2('pale', 'ple'))
        self.assertTrue(one_away_2('pales', 'pale'))
        self.assertTrue(one_away_2('pale', 'bale'))
        self.assertFalse(one_away_2('pale', 'bake'))
        self.assertTrue(one_away_2('', 'e'))
        self.assertTrue(one_away_2('ppppaaaa', 'pppaaaa'))
