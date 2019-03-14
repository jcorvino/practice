"""
Test cases for zero_matrix
"""
import unittest
from .zero_matrix import zero_matrix


class TestZeroMatrix(unittest.TestCase):

    def test_zero_matrix(self):
        """
        Simple test cases for zero_matrix function
        """
        # Test case
        matrix1 = [[1, 2, 3], [4, 0, 6]]
        matrix2 = [[1, 1], [2, 3]]
        self.assertListEqual(zero_matrix(matrix1), [[1, 0, 3], [0, 0, 0]])
        self.assertListEqual(zero_matrix(matrix2), matrix2)

