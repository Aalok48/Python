# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, operator1, operator2):
        self.operator1 = operator1
        self.operator2 = operator2

    def add(self):
        sum = int(self.operator1) + int(self.operator2)
        print("The sum of", self.operator1, "&", self.operator2, "is", sum)

    def substract(self):
        diff = int(self.operator1) - int(self.operator2)
        print("The difference of", self.operator1, "&", self.operator2, "is", diff)

    def multiply(self):
        mul = int(self.operator1) * int(self.operator2)
        print("The product of", self.operator1, "&", self.operator2, "is", mul)

    def division(self):
        div = int(self.operator1) / int(self.operator2)
        print("The division of", self.operator1, "&", self.operator2, "is", div)

    def modulo(self):
        mod = int(self.operator1) % int(self.operator2)
        print("The dividend of", self.operator1, "&", self.operator2, "is", mod)

operator1 = int(input("Enter first number: "))
operator2 = int(input("Enter second number: "))

calc = Calculator(operator1, operator2)
calc.add()
calc.substract()
calc.multiply()
calc.division()
calc.modulo()