# Count Fours in a List

This is a simple Python script to count the number of occurrences of the number 4 in a list.

## Description

The script defines a function `countFours` which takes a list as an argument and prints the number of times the number 4 appears in that list. It then demonstrates the use of this function with a predefined list of integers.

## Usage

To use this script, simply copy the code into a Python file (e.g., `count_fours.py`) and run it.

## Code

```python
def countFours(list):
  print(list.count(4))

a = [2, 4, 2, 5, 8, 7, 4, 9, 6, 4, 3, 4]
countFours(a)
