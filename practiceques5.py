# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that :
#      order1>order2 if price of order1>price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price>order2.price

order1 = Order("Chips", 20)

order2 = Order("Frooti", 25)

print(order1>order2) 