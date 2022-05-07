# Assignment 1.3
# Write a Python function that accepts an integer (n) and computes the value of n+nn+nnn. Display 
# result after function returns.
# function: def mult1(n : int) -> int:
# IN: 5
# OUT: 615

value = int(input("Enter the value: ")) # Prompt user for value

def mult1(n : int) -> int:
    return n + n * 11 + n * 111 # Perform calculation
     
print(mult1(value)) # Call function using user input