# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

'''Link to the questions :- https://www.w3resource.com/python-exercises/oop/ '''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = math.pi * pow(self.radius, 2)
        print("The area of the circle with radius", self.radius, "is", round(area, 3))

    def Perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("The perimeter of the circle with radius", self.radius, "is", round(perimeter, 3))

radius = int(input("Enter the radius of the circle: "))
circle1 = Circle(radius)
circle1.Area()
circle1.Perimeter()