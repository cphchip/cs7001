# Assignment 1.14

# Write a Python function to return the longest string of a list of strings. Display result after function 
# returns. 

# function: def longest_str (p1: list[str]) -> str:

# Test Cases:
#     Input: ['cat', 'car', 'fear', 'center']
#     Output: center

#     Input: ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
#     Output: shatter

def longest_str (p1: list) -> str:
    longestWordLength = 0 # Create 0 value variable to compare against which ensures first word will orver-write
    for i in p1: # Loop through each value provided in test cases
        if len(i) > longestWordLength: # if value is longer than check variable, replace with this value
            longestWord = i
            longestWordLength = len(i)
    return longestWord

wordList = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''] # Provided test case

print(longest_str(wordList)) # Call function in print statement
