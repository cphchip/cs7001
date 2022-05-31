# Assignment 1.11

def solve1(x : int, y : int) -> int:
    return (x + y) ** (x + y)

# Prompt the user for inputs
xInt = int(input("Please enter the x intercept: "))
yInt = int(input("Please enter the y intercept: "))

print(solve1(xInt, yInt)) # Call function in print statement with user inputs