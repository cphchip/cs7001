# Assignemnt 3.7
# Write a Python function to compute the sum of all the elements of each tuple stored inside a list of 
# tuples. 
# function: def tup1 (p1: List ) -> List:
# IN: [(1, 2), (2, 3), (3, 4)]
# 3
# OUT: [3, 5, 7]
# Original list of tuples:

def tup1 (p1: list) -> list:
    newList = []
    for t in p1:
        newList.append(t[0] + t[1])

    return newList

print(tup1([(1, 2), (2, 3), (3, 4)]))