# Assignment 1.8

userList1 = ["White", "Black", "Red"]
userList2 = ["Red", "Green"]

# Syntax as written in the instructions "color_list_1 : List[str]" doesn't seem to work, but simply "list" is ok
def extract1(color_list_1 : list, color_list_2 : list) -> set:  
    mySet = set()   # Create an empty set variable to hold the final result
    for i in color_list_1:  # Check each item in userList1 against userList2
        if i not in color_list_2 and i not in mySet:
            mySet.add(i)    # If item from color_list_1 is not in color_list_2 and not previously added to mySet, add it
    return mySet

print(extract1(userList1, userList2))   # Print function result with user values