#  Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
#  Implement subclasses for different shapes like circle, triangle, and square.

class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print("The area of the circle having radius", self.radius, "is ", 3.14 * pow(self.radius, 2))

    def calculate_perimeter(self):
        print("The perimeter of the circle having radius", self.radius, "is", 2 * 3.14 * self.radius)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        print("The area of the rectangle having base", self.base, "and breadth", self.height, "is", self.base * self.height * 0.5)

    def calculate_perimeter(self):
        print("I am too bored to write the code for the perimeter of triangle!!!")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        print("The area of the rectangle having length", self.length, "and breadth", self.breadth, "is", self.length * self.breadth)

    def calculate_perimeter(self):
        print("The perimeter of the rectangle having length", self.length, "and breadth", self.breadth, "is", 2 * (self.length + self.breadth))

radius = 7
circle = Circle(radius)
circle.calculate_area()
circle.calculate_perimeter()

base = 7
height = 5
triangle = Triangle(base, height)
triangle.calculate_area()
triangle.calculate_perimeter()

length = 5
breadth = 4
rectangle = Rectangle(length, breadth)
rectangle.calculate_area()
rectangle.calculate_perimeter()