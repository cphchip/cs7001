# Assignment 1.13

# Write a Python that takes a list of integers and returns True if the ith integer occurs i times and 
# returns False if not. Display result after function returns. 
# function: def is_ith (p1: list[int]) -> bool:

# Test Cases:
    # Input: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    # Output: True

    # Input: [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    # Output: False
    
    # Input: [1, 2, 2, 3, 3, 3]
    # Output: True

# Variable for test cases
ithList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]

def is_ith(p1 : list) -> bool:
    bList = []  # Create an empty list that will hold bool values
    for i in ithList: # Loop through each value in the test case
        if ithList.count(i) == i: # Count quantity of occurrences of value and check if it matches value
            bList.append(True)
        else:
            bList.append(False)
    return all(bList) #Use all() function to verify if every value in bList is true to return correct result

print(is_ith(ithList)) # Call function in print statement