# 8. Write a Python function to print out a set containing all the colors from color_list_1 which are not
# present in color_list_2. Display result after function returns.
# function: def extract1(color_list_1 : List[str], color_list_2: List[str] -> set:
# IN: 
#   color_list_1 = ["White", "Black", "Red"]
#   pwdcolor_list_2 = ["Red", "Green"]
# OUT: {'Black', 'White'}

# Note I have trouble with the syntax on some of these assignments
# Python doesn't seem to like List[str], but list is ok

from ast import And


userList1 = ["White", "Black", "Red"]
userList2 = ["Red", "Green"]

# testStr = "goat"
# myTestSet = set()
# myTestSet.add(testStr)
# # print(testStr in myTestSet)
# bCheck = testStr in myTestSet

# if testStr in myTestSet == False:
#     print("yes")
# else:
#     print('no')

def extract1(color_list_1 : list, color_list_2: list) -> set:
    mySet = set()
    for i in color_list_1:
        for x in color_list_2:
            if i != x: 
                # if i in mySet == False or len(mySet) == 0:  First condition doesn't work with this syntax, why?
                if i not in mySet or len(mySet) == 0: # This one works fine???
                    mySet.add(i)
    return mySet

print(extract1(userList1, userList2))