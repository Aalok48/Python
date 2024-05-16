# dunder function is an example of polymorphism

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real,"i +",self.imag,"j")

    # Example of dunder functions
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

complex1 = Complex(5, 8)
complex1.show_number()

complex2 = Complex(1, 2)
complex2.show_number()

num3 = complex1 + complex2
num3.show_number()