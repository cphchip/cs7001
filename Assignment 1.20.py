# Assignment 1.20
# Write a Python function to capture the vowels from each string in a list of strings and return a list 
# with only the vowels from each string. Display result after function returns.

# Note: y counts as a vowel only when at the end of the word.

# function: def grades_to_letter (p1: list[str]) -> List[str]:

# Input: ['w3resource', 'Python', 'Java', 'C++']
# Output: ['eoue', 'o', 'aa', '']

# Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
# Output: ['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

wordList = ['w3resource', 'Python', 'Java', 'C++']
vowelList = ['a', 'e', 'i', 'o','u','y']



# print('C++' in wordList)

newList = []
# for i in wordList:
#     for x in vowelList:
filter(lambda vowel: 'a' in wordList, wordList)
# newList.append()
print(wordList)

