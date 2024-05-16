class Student:
    def __init__(self, first_name, last_name):           # constructor always takes 'self' as a parameter
        self.first_name = first_name                     # here the fist_name and last_name are automatically created as object
        self.last_name = last_name                       # any other variable name can be used instead of self... using self name is not a must


s1 = Student("Alok", "karn")
print(s1.first_name)
print(s1.last_name)

# There are two types of constructors 
# 1. Default constructor

# def __init__(self):                           # default constructor donot take any parameters while parameterized constructor do take
#     pass
                                                # the constructor matching the number of parameters are called while creating an object
# 2. Parameterized constructor
# def __init__(self, name, faculty):
#     self.name = name
#     self.faculty = faculty