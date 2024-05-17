# Define a Circle class to create a circle with radius r using the constructor
# Define an Area() method of the class which calculates the area of the circle
# Defind a Perimeter() method of the class which allows you to calculate the perimeter of the circle
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