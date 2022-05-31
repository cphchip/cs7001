# Assignment 1.17

userList = [1, 2, 3, 4, 5, 1]

def all_different (p1: list) -> bool:
# Function forces user values from a list to a set. 
# Sets don't allow duplicates so if the length is different some numbers were inherently the same
    if len(p1) != len(set(p1)): 
        return False
    else:
        return True

print (all_different(userList))