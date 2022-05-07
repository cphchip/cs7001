# 4. Write a Python function to calculate and return the sum of three given numbers. If the values are 
# equal then return three times of their sum.
# function: def sum1(n1: int, n2:int, n3: int) -> int:
# IN: 2,2,2
# OUT: 18
# IN: 2,3,4
# OUT: 9

val1 = int(input("Enter the value: ")) # Prompt user for values
val2 = int(input("Enter the value: "))
val3 = int(input("Enter the value: "))

def sum1(n1:int, n2:int, n3:int) -> int:
    if n1 == n2 == n3:
        return (n1 + n2 + n3) * 3 # Return 3 times the number's sum if they are equal
    else: 
        return n1 + n2 + n3 # Return sum if they are anything but equal

print(sum1(val1, val2, val3))