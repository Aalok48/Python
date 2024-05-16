# Parent class | Base class
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

# child class of "Car" and parent class of "Fortuner" | First derived class
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

# child class of ToyotaCar | last derived class
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.type)
car1.start()