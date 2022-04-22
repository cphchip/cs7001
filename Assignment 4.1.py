# Assignment 4.1
# The following adds two numbers and returns the result.
# def add(a,b):
# return a+b
# Use *args as parameter to return the sum of all numbers passed to the function.
# function: def add_nums(*args) ->Number:
# Beware of parameters that are not int or float
# IN: add_nums(3,4,5, 'foo', 6.2)
# OUT: 18.2

from tokenize import Number

def add_nums(*args) -> Number:
    sumNum = 0
    for n in args:
        if isinstance(n,int) or isinstance(n, float):
            sumNum = n + sumNum

    return sumNum

print(add_nums(3,4,5, 'foo', 6.2))
