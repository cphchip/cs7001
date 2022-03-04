#   Assignment 9

# 9. Write a Python function that will return true if the two given integer values are equal or the absolute 
# value of their sum or difference is 5.
# function: def addem (n1 : int, n2: int]) -> bool:
    # IN: 4,4
    # OUT: True

    # IN: 3,2
    # OUT: True
    
    # IN: 23,27
    # OUT: True
        # Not sure how they think this is True?
    
    # IN: 29,27
    # OUT: True
        # Not sure how they think this is True?
    
    # IN: 23,67
    # OUT: False

numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

def addem (n1: int, n2: int) -> bool:
    if n1 == n2 or abs(n1 - n2 == 5) or abs(n1 + n2) == 5:
        return True
    else:
        return False

print(addem(numb1, numb2))