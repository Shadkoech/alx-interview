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

    if n <= 1:
        return 0

    # Initializing variables
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = i  # Initialize with worst case

        # Check all possible lengths of substrings
        for j in range(2, i):
            if i % j == 0:
                # If j divides i, we repeat a substring to form i characters
                min_ops[i] = min(min_ops[i], min_ops[j] + (i // j))

    return min_ops[n]
