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

def is_ith(p1 : list) -> bool:
    for i in ithList:
        if ithList.count(i) == ithList[i]:
            check = True
    return check

ithList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]

print(is_ith(ithList))