# Student Management System:
# Create a Student class with attributes like name, ID, and grades.
# Implement methods for adding, removing, and updating grades, as well as calculating the student's average grade.

import random

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.grades = {
            'math': 0,
            'physics': 0,
            'chemistry': 0,
            'biology': 0,
            'english': 0
        }
    
    def get_grades(self):
        self.grades['math'] = float(input("Enter the marks of mathematics: "))
        self.grades['physics'] = float(input("Enter the marks of Physics: "))
        self.grades['chemistry'] = float(input("Enter the marks of Chemistry: "))
        self.grades['biology'] = float(input("Enter the marks of Biology: "))
        self.grades['english'] = float(input("Enter the marks of English: "))

    def calculate_average_grade(self):
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

    def display_student_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.ID)
        print("Grades:", self.grades)
        print("Average Grade:", self.calculate_average_grade())

if __name__ == '__main__':
    name = input("Enter your name: ")
    ID = random.randint(100, 199)
    student = Student(name, ID)
    student.get_grades()
    student.display_student_info()
    