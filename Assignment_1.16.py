# Assignment_1.16
# Write a Python function to find the largest k numbers from a given list of ints. Display result after 
# function returns. 

# function: def largest_k (mylist: List[int], knum: int) -> List[int]:

# Test Cases:
# Input: [1,2,3,4,5,6] , 3
# Output: [6,5,4]

# Input: [1,2,3,4,5,6] , 0
# Output: [ ]

# Input: [1,2,3,'z',5,6] , 2
# Output: [6,5]

from collections import UserString


userList = list(input("Enter your list of numbers: "))
userNumber = int(input("Enter the number of high numbers: "))

def largest_k(mylist: list, knum: int) -> list:
    highList = []

    maxValue = 0
    c = 0

    while c < knum:
        for i in mylist:
            if int(maxValue) < int(i):
                maxValue = i
        c += 1
        highList.append(maxValue)
        mylist.remove(maxValue)
        maxValue = 0
        
    return highList

print(largest_k(userList, userNumber))
