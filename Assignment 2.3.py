# Assignment 2.3
# Create two text files. Write a function to append the contents of the first file to the second file. Pass 
# the two filenames as parameters. Display the contents of filename2, the appended file, after the 
# function returns.

# function: def append_file (filename1: String, filename2: String) -> None:


def append_file (filename1: str, filename2: str) -> None:
    readFile = open(filename1)
    readFileWords = readFile.readlines()

    writeFile = open(filename2, 'a')
    writeFile.writelines(readFileWords)

    readFile.close()
    writeFile.close()

    return

append_file ('2.3_file_read.txt', '2.3_file_write.txt')

displayFile = open('2.3_file_write.txt')
display = displayFile.read()

print(display)
