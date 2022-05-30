# Assignment 1.20
# Write a Python function to capture the vowels from each string in a list of strings and return a list 
# with only the vowels from each string. Display result after function returns.

# Note: y counts as a vowel only when at the end of the word.

# function: def grades_to_letter (p1: list[str]) -> List[str]:

# Input: ['w3resource', 'Python', 'Java', 'C++']
# Output: ['eoue', 'o', 'aa', '']

# Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
# Output: ['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

wordList = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']

def vowelFinder (p1: list) -> list:
    vResult = [] # Empty list to hold returned values
    vString = '' # Variable to hold temporary values to append to the list
    counter = 0

    for i in p1: # Loop through each item in the list 'P1'
        while counter < len(i): # Use counter value to step through each letter of each item
            # Use if statements to add vowels to temporary variables
            if i[counter] == 'a':
                vString = vString + 'a'
            elif i[counter] == 'e':
                vString = vString + 'e'
            elif i[counter] == 'i':
                vString = vString + 'i'
            elif i[counter] == 'o':
                vString = vString + 'o'
            elif i[counter] == 'u':
                vString = vString + 'u'
            elif i[counter] == 'y' and len(i)-1 == counter:
                vString = vString + 'y'
            counter += 1
        counter = 0 # Reset the letter counter for the next list item
        vResult.append(vString) # Add the new strings of vowels to the returned list
        vString = '' # Reset the temporary string variable

    return vResult  

print(vowelFinder(wordList)) # Call function in print statement