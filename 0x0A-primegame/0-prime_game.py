#!/usr/bin/python3
"""Module with that determines the prime numbers within a given range"""


def is_prime(n):
    """function Checking if a number is prime
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """

    primeNums = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNums.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNums


def isWinner(x, nums):
    """Determines the winner of each round
    Args:
        x (num) = The number of rounds
        nums (list)= array of n for each round
    Returns:
        str: ame of the player that won the most rounds or None"""

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_remaining = n + 1

        # Count prime numbers remaining
        for i in range(2, n + 1):
            if is_prime(i):
                primes_remaining -= 1

        # Determine the winner of the round
        if primes_remaining % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
