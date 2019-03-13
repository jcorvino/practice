"""
Problem 1.7: Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""
# NOTE: Assumes rotation is clockwise
# Ex: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def rotate_matrix(mat):
    """
    Rotates an N x N matrix by 90 degrees clockwise.
    Time complexity = O(N**2)

    :param [[int]] mat: N x N matrix of integers
    :return [[int]]: rotated matrix (90 deg clockwise)
    """

    return list(zip(*mat[::-1]))
