# Assignment 2.1

# Create a 10 line text file with some text of your choice. Write a Python to read first n lines of the file 
# and return the number of alphabetic (a-z A-Z) characters you read in for the n lines.
# : def read_count (filename: String, n: int) -> int:



def read_count (filename: str, n: int) -> int:
    strLines = ''
    with open(filename) as text:
        for line in range(n):
            strLines = strLines + text.readline()
        text.close()
    
    charCount = 0
    for words in strLines:
        if words.isalpha():
            charCount += 1
    
    return charCount

print (read_count('Assignment_2.1_Text.txt', 3))