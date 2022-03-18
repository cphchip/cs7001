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

userList = list(input("Enter your list of numbers: "))
userNumber = int(input("Enter the number of high numbers: "))
# print(userList)
compNumb = 0 
highList = []
counter = 0

highList = userList

for x in highList:
    for i in userList:
        if int(i) < int(x):
            highList.remove(x)


    # if len(highList) == 0:
    #     highList.append(i)
    # if int(userList(i)) > int(highList[0]):
    #     for x in highList:
    #         if userList(i) > highList(x):
    #             highList.append(i)
print(highList)

