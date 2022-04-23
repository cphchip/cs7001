# Assignment 5.2
# Write a Python class named Circle constructed by a radius.
# Write two methods which will compute the area and the perimeter of a circle. 

from cmath import pi


class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius
        pass

    def circArea(self):
        area = self.radius**2 * pi
        return area

    def circPerimeter(self):
        perimeter = self.radius * pi * 2
        return perimeter

thisCirc = Circle(5)

print("The area is: " , thisCirc.circArea())
print("The circumference is: " , thisCirc.circPerimeter())

