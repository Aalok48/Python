class Account:
    def __init__(self, account_no, account_password):
        self.account_no = account_no
        self.__account_password = account_password

    def reset_password(self):
        print(self.__account_password)

acc1 = Account("1234", "alookk")
# in this way the object is public ie. the information inside the class can be accessed outside the class

print(acc1.account_no)

# to prevent this the object can be made private by using two underscode 
# print(acc1.__account_password)   # now the __account_password is made private and cannot be accessed outside the class

acc1.reset_password()


# similarly a method or function can also be made private using "__"
# def __reset_password(self):
#     print(self.__account_password)