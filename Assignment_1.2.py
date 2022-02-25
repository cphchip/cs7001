
str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))
str3 = str(input("Enter third string: "))

userList = [str1, str2, str3]
listCount =  len(userList)

def get_last(mylist : list[str]) -> str:
     return mylist[listCount-1]

print (get_last(userList))