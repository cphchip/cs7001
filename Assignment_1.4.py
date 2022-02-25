val1 = int(input("Enter the value: "))
val2 = int(input("Enter the value: "))
val3 = int(input("Enter the value: "))

def sum1(n1:int, n2:int, n3:int) -> int:
    if n1 == n2 == n3:
        intCalc = n1 * n2 * n3
    else: 
        intCalc = n1 + n2 + n3
    return intCalc

print(sum1(val1, val2, val3))