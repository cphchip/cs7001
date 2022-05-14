# Assignment 1.8
# Write a Python function to print out a set containing all the colors from color_list_1 which are not
# present in color_list_2. Display result after function returns.
# function: def extract1(color_list_1 : List[str], color_list_2: List[str] -> set:
# IN: 
#   color_list_1 = ["White", "Black", "Red"]
#   color_list_2 = ["Red", "Green"]
# OUT: {'Black', 'White'}

# Note I have trouble with the syntax on some of these assignments
# Python doesn't seem to like List[str], but list is ok
    # if i in mySet == False or len(mySet) == 0:  First condition doesn't work with this syntax, why?
    # if i not in mySet or len(mySet) == 0: # This one works fine???


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