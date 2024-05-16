# function created in class is called method in python 

class Student:
    college_name = "Paschimanchal Campus"
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("Welcome to Paschimanchal Campus", self.name)

    def student_marks(self):
        print("Congratulations you got", self.marks, "marks")



s1=Student("Alok karn", 94)
print(s1.college_name)
print(s1.name)
print(s1.marks)
s1.welcome()
s1.student_marks()