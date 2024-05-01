# 0x08. Making Change

## Introduction
The project "Change comes from within" has the objective of handling a given problem by making changes using dynamic programming and greedy algorithms. The challenge is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations.

## Problem description
Given a pile of coins with distinct values, and a total amount to be made up, the objective is to find the minimum number of coins required to reach that amount. For instance, if you have coins of values [1, 2, 5] and need to make up a total of 11, the optimal solution would involve using three coins: two coins of value 5 and one coin of value 1.

However, there are complexities to consider. What if the coin denominations at your disposal are not just [1, 2, 5], but rather a diverse array like [1, 3, 4, 9]? Herein lies the crux of the challenge – devising an algorithm that not only determines the fewest coins needed but does so optimally across various sets of coin denominations.

## Significance of this problem
This problem showcases the use of greedy algorithms to swiftly arrive at solutions and the efficacy of dynamic programming in handling complex scenarios. It finds everyday applications in:
- Vending machine operation algorithm
- Currency exchange systems
- Coin exchange and balances in banks

## Concepts Needed
* Greedy Algorithms
* Dynamic Programming
* Algorithmic Complexity
* Problem-Solving Strategies
* Python Programming

## Objectives
- Implement a solution to the coin change problem using both greedy algorithms and dynamic programming.
- Understand the principles behind greedy algorithms and dynamic programming.
- Analyze the trade-offs between efficiency and optimality in algorithmic solutions.
- Enhance problem-solving skills by tackling real-world challenges in a structured manner.

## Task
Files:

    - 0-making_change.py, 0-main.py

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
    * If total is 0 or less, return 0
    * If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task
