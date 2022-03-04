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
from asyncio.windows_events import NULL


userList1 = ["White", "Black", "Red"]
userList2 = ["Red", "Green"]

def extract1(color_list_1 : list, color_list_2: list) -> set:
    mySet = set()
    for i in color_list_1:
        for x in color_list_2:
            if i != x: 
                if i in mySet == False:
                    mySet.add(i)
                else:
                    if len(mySet) == 0:
                        mySet.add(i)
    return mySet

print(extract1(userList1, userList2))