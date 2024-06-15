# Circle Area Calculator

This is a simple Python script to calculate and print the area of a circle given its radius.

## Description

The script defines a function `area` which takes the radius of a circle as an argument and prints the calculated area using the formula \( \pi \times \text{radius}^2 \). The script prompts the user to input the radius of the circle and then uses the `area` function to display the result.

## Code

```python
import math

def area(radius):
  print(math.pi * float(radius) * float(radius))

rad = input("Enter the radius of the circle: ")
area(rad)
