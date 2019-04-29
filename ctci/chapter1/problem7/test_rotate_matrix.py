"""
Test cases for rotate_matrix
"""
import unittest
from copy import deepcopy
from .rotate_matrix import rotate_matrix


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix(self):
        """
        Simple test cases for rotate_matrix function
        """
        # Simple 2x2 and 3x3 cases
        mat1 = [(1, 2), (3, 4)]
        mat2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        mat1_single_rotation = [(3, 1), (4, 2)]
        mat2_single_rotation = [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

        # Test a single rotation
        self.assertListEqual(rotate_matrix(mat1), mat1_single_rotation)
        self.assertListEqual(rotate_matrix(mat2), mat2_single_rotation)

        # Test 4 rotations returns the original matrix
        mat2_rotated = deepcopy(mat2)
        for i in range(4):
            mat2_rotated = rotate_matrix(mat2_rotated)
        self.assertListEqual(mat2_rotated, mat2)
