# Assignment 1.18: 
# Write a Python function to remove the duplicate elements of a given list of integers such that each 
# element appear only once. Return the new list. Display result after function returns.

# function: def remove_dups (p1: List[int) -> List[int]:
# 
# Input: [1,2,3,4,5,6] 
# Output: [1,2,3,4,5,6] 
# 
# Input: [1,2,3,4,4,5,5, 6] 
# Output: [1,2,3,4,5,6] 

userList = [1,2,3,4,4,5,5,6] 

# print (userList)

def remove_dups (p1: list) -> list[int]:
    newSet = set(p1)

    return list(newSet)

print(remove_dups(userList))

