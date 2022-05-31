# Assignment 1.18: 

userList = [1,2,3,4,4,5,5,6] 

# print (userList)

def remove_dups (p1: list) -> list[int]:
    newSet = set(p1)

    return list(newSet)

print(remove_dups(userList))

