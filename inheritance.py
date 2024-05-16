# Parent class
class Car:        
    color = "BLUE"    
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def accelerate():
        print("Car accelerating")

    @staticmethod
    def stop():
        print("Car stopped...")

# Child class
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.name)
print(car1.color)
car1.start()
car1.accelerate()
car1.stop()


# types of inheritance
# single inheritance = single parent class and single child class the above example is an example of single inheritance
# multilevel inheritance = multiple parent class and single child class 
