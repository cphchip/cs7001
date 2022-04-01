# Assignment 2.1

# Create a 10 line text file with some text of your choice. Write a Python to read first n lines of the file 
# and return the number of alphabetic (a-z A-Z) characters you read in for the n lines.
# : def read_count (filename: String, n: int) -> int:

with open('Assignment_2.1_Text.txt') as text:
    nLines = text.read()
    text.close()

nList = [nLines.split(' ')]
# nList = ['ably', 'abruptly', 'abecedary']
print (type(nList))

charCount = 0
counter = 0

for n in nList:
    while counter < len(n):
        # print (n[counter])
        if n[counter].isalpha(): 
            charCount += 1
        counter += 1
    counter = 0

print (charCount)