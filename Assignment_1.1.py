# Assignment 1.1
# 
# Write a Python function which accepts the radius of a circle and returns the area. Display area after 
# function returns.
# function: def get_area(radius : float)-> float:
# Input: 1.1
# Output: 3.8013271108436504

import math

def get_area(radius : float) -> str:
    return radius ** 2 * math.pi

# Ask User to input radius
radius_val = float(input("Enter the radius: "))

# Get the area by running function with user input and display 
print("The area is: ", get_area(radius_val))