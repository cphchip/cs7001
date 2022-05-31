# Assignment 1.15

def split_str (s:str) -> list:
    userStrList = [] # Create an empty variable list to hold the result
    if ' ' not in s and ',' not in s: # The first case checks if spaces and commas are not in the string
        for i in s: 
            userStrList.append(i) # In this case for each letter in the string add it individually to the list
        userStrList = userStrList[::-1] # Reverse the order of the list
    elif ',' in s: # Handles splitting the string if there is a comma
        userStrList = [s.split(',')]
    else: # Final case handles splitting the string if there is a space
        userStrList = [s.split(' ')]

    return userStrList

userString = str(input("Enter your string: ")) # Prompt user for string input
print(split_str(userString))