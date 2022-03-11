# Assignment 1.15

# 15. Write a Python function to split a given string (s) into a List of strings if there is a space in s, 
# otherwise split on commas if there is a comma, otherwise return a list of the string characters in reverse 
# order. Display result after function returns. 

# function: def split_str (s: String) -> List[str]:
# Test Cases:
# Input: 'abc de xyz'
# Output: ['abc', 'de', 'xyz']
#  
# Input: 'xyz w k'
# Output: ['abc', 'de', 'xyz']

# Input: 'bogus'
# Output: ['s', 'u', 'g', 'o', 'b']

userString = str(input("Enter your string: "))

strLength = len(userString)

print(userString[::-1])