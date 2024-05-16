# Create Account class with two attributes - balance and account no.
# Create methods for debit, credit & printing the balance
import time

class Account:
    
    def __init__(self, balance):
        self.account_balance = balance

    def debit_account(self, debit_amount, account):
        if self.account_balance<debit_amount:
            print("Insufficient balance to debit")
        else:
            self.account_balance = self.account_balance-debit_amount
            print("Account debited by", debit_amount, "from account number", account)

    def credit_account(self, credit_amount, account):
        self.account_balance = self.account_balance+credit_amount
        print("Account credited by", credit_amount, "in account number", account)

    def show_balance(self):
        print("Current balance is", self.account_balance)

customer1 = Account(0)
print("Hello, there...")
time.sleep(1.5)
choice = int(input("Click 1 for depit 2 for credit 3 for printing the balance"))
if choice == 1:
    balance = int(input("Enter amount to debit: "))
    customer1.debit_account(balance, 13124)

elif choice ==2:
    balance = int(input("Enter amount to credit: "))
    customer1.credit_account(balance, 13124)

else:
    customer1.show_balance()