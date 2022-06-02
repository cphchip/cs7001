﻿# Assignment 1.7

from typing import Any

userList = ['foo', 'bar', False, 99.3, True]

def make_strl(mylist:list) -> str:
    strOut = "" # Create an empty String variable to contain the final string
    for i in mylist:    # Check if each item in the user's list is a string
        if type(i) == str:
            strTemp = i # If True store the value in a temporary variable
        else:
            i = str(i)  # If False convert the value to string and add to temporary variable
            strTemp = i
        strOut = strOut + strTemp   # Create the final string by adding the temporary variable value
    return strOut

print(make_strl(userList))  # Use print to call the function with user values