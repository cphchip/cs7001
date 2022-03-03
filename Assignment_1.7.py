from typing import Any


userList = ['foo', 'bar', False, 99.3, True]

def make_strl(mylist:list) -> str:
    strOut = ""
    for i in mylist:
        if type(i) == str:
            strTemp = i
        else:
            i = str(i)
            strTemp = i
        strOut = strOut + strTemp
    return strOut

print(make_strl(userList))