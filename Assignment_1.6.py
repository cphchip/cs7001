# Assignment 1.6

userVal = str(input("Enter the letter: "))  # User is prompted to enter a letter

def is_vowel(n1:chr) -> bool:
    vList = ['a', 'e', 'i', 'o', 'u']
    for x in vList: # Loop through each vowel to determine if the user letter matches
        if x == n1:
            return True
    return False

print (is_vowel(userVal))   # Print statment calling the function with user input
