# Assignment 1.17

# 17: Write a Python function that takes a list of integers and returns True if all the integers are different 
# from each other, False otherwise. Display result after function returns.
# function: def all_different (p1: list[int]) -> bool:

# Input: [1,2,3,4,5,6] 
# Output: True

# Input: [1,2,4,4,5,6] 
# Output: False

userList = [1, 2, 4, 4, 5, 6]

bCheck = True
for i in userList:
    for x in userList:
        if i == x and userList.index(i) != userList.index(x):
            bCheck = False
            break
        else:
            bCheck = True


print (bCheck)