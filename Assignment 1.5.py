# Assignment 1.5

userVal = int(input("What is the value: ")) # Prompt user for value

def even_odd(n1:int) -> int:
    if userVal % 2 > 0: # Determine if value is even or odd using modulo operator, return appropriate value
        return 1
    else:
        return 0
    # return outVal

print (even_odd(userVal)) # Call function using the user's input value

