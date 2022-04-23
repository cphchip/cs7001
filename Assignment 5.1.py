# Assignment 5.1: Objects and Exceptions
# 1. Write a Python class named Rectangle. Pass in length and width to the constructor. 
# Write a method which will compute the area of a rectangle. 

class Rectangle():

    def calcArea(self, length, width):
        area = length * width
        return area

rect1 = Rectangle()

thisArea = rect1.calcArea(5, 3)
print(thisArea)