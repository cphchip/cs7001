# Assignment 3.6
# Write a Python function to count the elements in a list until an element is a tuple.
# function: def count1 (p1: List ) -> int:
# IN: [2, 'foo', 3.4737, (4,5), 'zzz']
# OUT: 3

userList = [2, 'foo', 3.4737, (4,5), 'zzz']

def count1 (p1: list) -> int:
    counter = 0
    for item in p1:
        if type(item) != tuple:
            counter += 1
        else:
            break
    
    return counter

print (count1(userList))