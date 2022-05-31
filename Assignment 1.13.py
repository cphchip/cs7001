# Assignment 1.13

# Variable for test cases
ithList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]

def is_ith(p1 : list) -> bool:
    bList = []  # Create an empty list that will hold bool values
    for i in ithList: # Loop through each value in the test case
        if ithList.count(i) == i: # Count quantity of occurrences of value and check if it matches value
            bList.append(True)
        else:
            bList.append(False)
    return all(bList) #Use all() function to verify if every value in bList is true to return correct result

print(is_ith(ithList)) # Call function in print statement