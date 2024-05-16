# Create a class that names and marks of 3 subjects as arguements in constructor then create a method to print the average

class Marks:
    def __init__(self, maths, science, nepali):
        self.maths=maths
        self.science=science
        self.nepali=nepali

    # staticmethod
    # method that don't use the self method (works at class level)

    @staticmethod
    def hello():
        print("Hello there this is static method")

    def average(self):
        avg = (self.maths+self.science+self.nepali)/3
        print("Hello there your average marks is", avg)
    
maths_marks=int(input("Enter your maths marks: "))
science_marks=int(input("Enter your maths science: "))
nepali_marks=int(input("Enter your maths nepali: "))
s1=Marks(maths_marks, science_marks, nepali_marks)
s1.hello()
s1.average()