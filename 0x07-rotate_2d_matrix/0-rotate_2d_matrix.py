#!/usr/bin/python3
"""Module that transposes a given matrix"""


def rotate_2d_matrix(matrix):
    """function that rotates 2D matrix by 90 degrees clockwise
    Args:
        matrix (list of lists): The matrix to transpose """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
