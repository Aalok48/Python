# Write a Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

class Person:
    def __init__(self, name, country, dob) -> None:
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        age = 2024 - int(self.dob )
        print("Hello", self.name,".You live in", self.country, "and your age is", age)

name = input("Enter your name: ")
country = input("Enter your country: ")
dob = input("Enter your dob(the year when you were born in AD): ")

person1 = Person(name, country, dob)
person1.calculate_age()