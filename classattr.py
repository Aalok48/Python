class Person:
    name = "Anonymous"

    # def __init__(self, name):
    #     # self.name = name           # here we want to change the class attribute name but it cannot be done directly this way so we use
    #     self.__class__.name = name

# this can also be done using classmethod
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person() 
p1.changename("Alok karn")     
print(p1.name)
print(Person.name)
