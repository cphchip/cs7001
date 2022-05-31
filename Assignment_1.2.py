# Assignment 1.2

# Get strings input by the user
str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))
str3 = str(input("Enter third string: "))

userList = [str1, str2, str3] # Create a list of the strings

def get_last(mylist : list[str]) -> str:
     return mylist[len(mylist)-1]  # Using the length of the list return the last value accounting for 0 index

print (get_last(userList)) # Print result using function