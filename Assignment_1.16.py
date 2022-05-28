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

userList = list(input("Enter your list of numbers: ")) # Prompt user for list of numbers
userNumber = int(input("Enter the number of high numbers: ")) # Prompt user for quantity of high numbers to return

def largest_k(mylist: list, knum: int) -> list:
    for i in mylist: # Checks each item in the list to verify they are digits
        if i.isdigit() == False:
            mylist.remove(i) # Remove items that if they are not digits

    mylist = [int(i) for i in mylist] # Forces each item in the list to be an integer

    highList = [] # Establish an empty list variable to return the result
    c = 0 # Counter variable
    while c < knum: # While loop to ensures user designated quantity of values is returned 
        maxValue = 0 # Establish a max value for comparison as 0 to ensure it'll be overwritten for positive numbers
        for i in mylist:
            if maxValue < i: # Compares max value to current value
                maxValue = i  # Reassigns max value to current value if current value is higher
        c += 1 # Counter advance
        highList.append(maxValue) # Adds the values to list to return to user
        mylist.remove(maxValue) # Ensures same result isn't returned more than once
        
    return highList

print(largest_k(userList, userNumber))
