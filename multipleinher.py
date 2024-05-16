# one derived class has multiple base class

# Base 1 class
class A:  
    var1 = "Welcome to class A"

# Base 2 class
class B:
    var2 = "Welcome to class B"

# Derived class having properties of both class A and B
class C(A, B):
    var3 = "Welcome to class C"

object1 = C()
print(object1.var1)
print(object1.var2)
print(object1.var3)