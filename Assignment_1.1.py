import math

def get_area(radius : float) -> str:
    return radius ** 2 * math.pi

radius_val = float(input("Enter the radius: "))
area = get_area(radius_val)
print("The area is: ")
print(area)