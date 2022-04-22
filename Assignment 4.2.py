# Assignment 4.2
# Use **kwargs to print the names and the values of all parameters passed in.
# function foo2 (a, **kwargs) -> NoReturn :
# IN: foo2(99, c=3, d=8)
# Prints:
# a is 99
# c is 3
# d is 8

# from multiprocessing.sharedctypes import Value
from typing import NoReturn


def foo2 (a, **kwargs) -> NoReturn:
    print("a is %s" %a)
    for key, value in kwargs.items():
        print("%s is %s" %(key, value))

foo2(99, c=3, d=8)
