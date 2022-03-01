userList = ['foo', 'bar', 99.3]
strOut = ""

for i in userList:
    if type(i) == str:
        strTemp = i
    else:
        i = str(i)
        strTemp = i
    strOut = strOut + strTemp

print(strOut)