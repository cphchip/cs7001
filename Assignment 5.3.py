# Assignment 5.3
# Write a function to divide two integers, n1 and n2 as n1/n2
# function: divide (n1: int, n2:int) -> Any:
# If n2 is passed as zero, catch the exception, display "Can't divide by Zero" and return None as the value 
# of the function.
# Do not use if statements – use Exceptions!

from typing import Any

def divide (n1: int, n2: int) -> Any:

    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print("Can't devide by Zero")
        return "None"

print(divide (12, 0))