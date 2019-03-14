"""
Problem 1.8: Write an algorithm such that if an element in an M x N matrix is 0, then the entire row and column are 0.
"""


def zero_matrix(mat):
    """
    Takes an MxN matrix and if an element is zero, then it sets the element's row and column to 0.
    Time complexity = O(M*N)

    :param [[int]] mat: MxN matrix
    :return [[int]]: zeroed MxN matrix
    """
    zero_column_index = []

    # zero out the rows
    for i, row in enumerate(mat[:]):
        try:
            j = row.index(0)
        except ValueError:
            pass
        else:
            zero_column_index.append(j)
            mat[i] = [0] * len(row)

    # zero out the columns
    for j in zero_column_index:
        for i in range(len(mat)):
            mat[i][j] = 0
    return mat

