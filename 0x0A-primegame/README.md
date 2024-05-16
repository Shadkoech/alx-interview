# Prime Game


## Overview
This project involves solving a competitive game scenario where two players (say Maria and Ben) strategically remove prime numbers and their multiples from a set of consecutive integers. The goal is to determine the winner of each round based on optimal play strategies.

## Problem statement
Maria and Ben are engaged in a game where they play multiple rounds. In each round, they are given a set of consecutive integers starting from 1 up to a certain limit 
𝑛. The players take turns choosing a prime number from the set and removing that number along with its multiples from the set. The player who cannot make a move loses the game.

- The task is to implement the isWinner(x, nums) function, where 𝑥 represents the number of rounds played, and nums is an array containing the limits 𝑛 for each round. The function should determine the winner of each round, assuming Maria always plays first and both players play optimally. It should return the name of the player who won the most rounds, or None if the winner cannot be determined

## Approach
In order to solve this problem, a good understanding of prime numbers, game thery as well as algorithmic optimization is required. Applying efficient algorithm for identifying prime numbers within a given range such as Eratosthenes is very important. Also concepts such as dynamic programming, memoization techniques are also key for creating an optimal solution for multiple rounds of the game. 

## Case example
In the first round, with 𝑛=4, Maria picks the prime number 2 and removes 2 and its multiples, leaving 1 and 3. Ben then picks 3, leaving only 1. Since there are no prime numbers left for Maria to choose, Ben wins the round.

In the second round, with 𝑛=5, Maria picks 2 and removes 2 and 4, leaving 1, 3, and 5. Ben picks 3, removing 3 and leaving 1 and 5. Maria then picks 5, leaving only 1 for Ben. Maria wins this round.

In the third round, with 𝑛=1, there are no prime numbers for Maria to choose, so Ben wins automatically.
- Therefore, the winner of the most rounds is Ben.

## Task
Files

    - 0-prime_game.py, main_0.py
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

- Prototype: def isWinner(x, nums)
- where x is the number of rounds and nums is an array of n
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return None
- You can assume n and x will not be larger than 10000
- You cannot import any packages in this task
Example:
x = 3, nums = [4, 5, 1]


First round: 4

- Maria picks 2 and removes 2, 4, leaving 1, 3
- Ben picks 3 and removes 3, leaving 1
- Ben wins because there are no prime numbers left for Maria to choose


Second round: 5

- Maria picks 2 and removes 2, 4, leaving 1, 3, 5
- Ben picks 3 and removes 3, leaving 1, 5
- Maria picks 5 and removes 5, leaving 1
- Maria wins because there are no prime numbers left for Ben to choose


Third round: 1

- Ben wins because there are no prime numbers for Maria to choose