#!/usr/bin/python3
"""
Module that generates Pascal's triangle
"""


def pascal_triangle(n):
    """ A function that creates a Pascal's triable of dimension n
    Args:
        n represent the  number of rows of Pascal's triangle
    Returns:
        List of integers representing the Pascal's triangle
        Returns an empty list if n <= 0
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)

    return triangle
