# Lockboxes

## Overview

This project aims to implement an algorithm in Python to solve the Lockboxes problem. The task involves determining whether all the boxes in a set of locked boxes can be opened, given that each box may contain keys to other boxes.


## Key concepts
- This project aims to implement an algorithm in Python to solve the Lockboxes problem. The task involves determining whether all the boxes in a set of locked boxes can be opened, given that each box may contain keys to other boxes.
- Algorithmic Complexity: Awareness of time and space complexity aids in crafting efficient algorithms.
- Recursion: Some solutions may require a recursive approach
- Set Operations: Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.

## Task: 0. Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
	* There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
