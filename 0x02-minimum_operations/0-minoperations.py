#!/usr/bin/python3
"""
Python module that calculates the fewest number of operations needed
to result in a given number of desired characters """


def minOperations(n):
    """
    Calculates fewest number of operations needed to result in exactly
    n H characters in the file.
    Args:
        n (int): The desired number of H characters in the file.
    Returns:
        min number of operations needed or 0 if n is impossible to achieve"""

    min_ops = 0
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        while n % i == 0:
            n = n / i
            min_ops += i
    return min_ops
