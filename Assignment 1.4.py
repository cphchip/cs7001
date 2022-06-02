# Assignment 1.4

val1 = int(input("Enter the value: ")) # Prompt user for values
val2 = int(input("Enter the value: "))
val3 = int(input("Enter the value: "))

def sum1(n1:int, n2:int, n3:int) -> int:
    if n1 == n2 == n3:
        return (n1 + n2 + n3) * 3 # Return 3 times the number's sum if they are equal
    else: 
        return n1 + n2 + n3 # Return sum if they are anything but equal

print(sum1(val1, val2, val3))