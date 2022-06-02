# Assignment 1.9

# Get number inputs from the user
numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

def addem (n1: int, n2: int) -> bool:
    if n1 == n2 or abs(n1 - n2) == 5 or abs(n1 + n2) == 5: # Perform comparision
        return True
    else:
        return False

print(addem(numb1, numb2)) # Print statement calling the function