# Assignment 1.6
# Write a Python function to test whether a passed letter is a vowel or not. Return True or False. Display 
# result after function returns. Python does not have a char datatype so simply pass in a string of length 1. 
# function: def is_vowel (n1: char) -> bool:
# IN: a
# OUT: True
# IN: z
# OUT: False


userVal = str(input("Enter the letter: "))  # User is prompted to enter a letter

def is_vowel(n1:chr) -> bool:
    vList = ['a', 'e', 'i', 'o', 'u']
    for x in vList: # Loop through each vowel to determine if the user letter matches
        if x == n1:
            return True
    return False

print (is_vowel(userVal))   # Print statment calling the function with user input
