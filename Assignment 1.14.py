# Assignment 1.14

def longest_str (p1: list) -> str:
    longestWordLength = 0 # Create 0 value variable to compare against which ensures first word will orver-write
    for i in p1: # Loop through each value provided in test cases
        if len(i) > longestWordLength: # if value is longer than check variable, replace with this value
            longestWord = i
            longestWordLength = len(i)
    return longestWord

wordList = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''] # Provided test case

print(longest_str(wordList)) # Call function in print statement
