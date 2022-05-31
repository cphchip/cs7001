# Assignment 1.10

def solve1(x : int, y : int) -> int: # Define function
    return (x + y) ** 2

# Prompt user for input
xIntercept = int(input("Please enter the 'x' intercept: "))
yIntercept = int(input("Please enter the 'y' intercept: "))

print(solve1(xIntercept, yIntercept)) # Call function in print statement w user input