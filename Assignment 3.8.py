# Assignment 3.8
# Write a Python function to check if a given value is present in a set or not. 
# function: def set1 (s1: Set, val: ANY ) -> bool:
# IN: (3,9,11,1,'fiji'), 1
# OUT: True

def set1 (s1: set, val: any) -> bool:
    # bTest = False
    for v in s1:
        if v == val:
            bTest = True
            break
        else:
            bTest = False
    
    return bTest

print(set1 ((3,9,11,1,'fiji'), 1))