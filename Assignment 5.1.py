# Assignment 5.1: Objects and Exceptions
# 1. Write a Python class named Rectangle. Pass in length and width to the constructor. 
# Write a method which will compute the area of a rectangle. 

from typing import NoReturn


class Rectangle():
    def __init__(area, length, width):
        area.length = length
        area.width = width

    def calcArea(area):
        print('The area is: ' area.length * area.width)

# print(Rectangle(5, 3))
a = Rectangle(5, 3)
a.calcArea