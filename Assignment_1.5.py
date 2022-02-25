userVal = int(input("What is the value: "))

def even_odd(n1:int) -> int:
    if userVal % 2 > 0:
        outVal = 1
    else:
        outVal = 0
    return outVal

print (even_odd(userVal))