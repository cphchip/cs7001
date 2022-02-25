value = int(input("Enter the value: "))

def mult1(n : int) -> int:
    intCalc = n + n * 11 + n * 111
    return intCalc

print(mult1(value))