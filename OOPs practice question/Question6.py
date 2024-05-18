# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.balance = 0
        self.amount = amount

    def debit(self):
        print("Your account has been debited by", self.amount)

    def credit(self):
        print("Your account has been credited by", self.amount)

    def show_balance(self):
        print(self.balance)

name = input("Enter your name: ")
choice = input("Choose 1 to deposit money and 2 to withdraw")
customer1 = Bank('Alok', 0)
if choice == 1:
    amount = float(input("Enter the amount you want to deposit: "))
    if amount <0:
        print("betichod thik amount choose kar...")
    else:
        customer1.name = name
        customer1.amount = amount
        customer1.debit()

else:
    amount = float(input("Enter the amount to withdraw: "))
    if amount <0:
        print("betichod thik amount choose kar...")
    else:
        customer1.name = name
        customer1.amount = amount
        customer1.credit()