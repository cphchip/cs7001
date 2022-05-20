# Assignment 1.11
# Write a Python function to solve (x + y)^(x + y). Display result after function returns.
# function: def solve1(x : int, y: int]) -> int:
# IN: 4,3 (for x and y)
# OUT: 823543


def solve1(x : int, y : int) -> int:
    return (x + y) ** (x + y)

# Prompt the user for inputs
xInt = int(input("Please enter the x intercept: "))
yInt = int(input("Please enter the y intercept: "))

print(solve1(xInt, yInt)) # Call function in print statement with user inputs