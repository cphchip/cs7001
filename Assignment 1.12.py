# Assignment 1.12

# Write a Python function to compute the distance between the two points (x1, y1) and (x2, y2). Each 
# point is provided as a tuple of two ints. Display result after function returns. 
# function: def solve1(p1: tuple[int], p2: tuple[int]) -> int:

# IN: (2,5), (6,8)
# OUT: 5

import math
def solve1(p1 : tuple, p2 : tuple) -> int:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = int(input("Enter x intercept 1: "))
y1 = int(input("Enter y intercept 1: "))
x2 = int(input("Enter x intercept 2: "))
y2 = int(input("Enter y intercept 2: "))

point1 = x1, y1
point2 = x2, y2

print(solve1(point1, point2))