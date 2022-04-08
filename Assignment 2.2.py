# Assignment 2.2
# Write a Python to write each element of a list to a file, line by line. Pass in the list and filename as 
# parameters. 
# : def list_to_file (mylist: List, filename: String) -> None:
# Test with the list: [2,4,6,8,10,33] and with the list ['foo', 'bar', 'baz', 'bop'


def list_to_file (mylist: list, filename: str) -> None:
    file1 = open(filename, "w")
    for element in mylist:
        file1.writelines(str(element))
        file1.writelines('\n')
    file1.close()

    return

list_to_file ([2,4,6,8,10,33], 'Assignment_2.2_Writing.txt')