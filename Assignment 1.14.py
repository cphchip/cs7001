# Assignment 1.14

# Write a Python function to return the longest string of a list of strings. Display result after function 
# returns. 

# function: def longest_str (p1: list[str]) -> str:

# Test Cases:
#     Input: ['cat', 'car', 'fear', 'center']
#     Output: center

#     Input: ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
#     Output: shatter

wordList = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# print (len(wordList[3]))
longestWordLength = 0
for i in wordList:
    # wordLength = 
    if len(i) > longestWordLength:
        longestWord = i

print(longestWord)
