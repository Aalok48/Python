class Shopping_cart:
    def __init__(self, items, price):
        self.items = items
        self.price = price
        self.cart = {}

    def add_items(self):
        self.cart[self.items] = self.price

    def show_cart(self):
        print("Your cart:")
        for item, price in self.cart.items():
            print(f"{item}: ${price:.2f}")

    def remove_items(self):
        item = input("Enter the name of the item to remove: ")
        if item in self.cart:
            del self.cart[item]
            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} is not in the cart.")

    def calculate_price(self):
        total = 0
        for price in self.cart.values():
            total += price
        return total

if __name__ == "__main__":
    shopping = True
    customer = Shopping_cart("", 0)
    while shopping:
        item = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        customer.items = item
        customer.price = price
        customer.add_items()
        customer.show_cart()
        choice = input("Enter 1 to remove an item or 2 to continue: ")
        if choice == '1':
            customer.remove_items()
        shopping_status = input("Enter 'Y' to continue shopping or 'N' to stop: ")
        if shopping_status.upper() != 'Y':
            shopping = False

    total_price = customer.calculate_price()
    print(f"Total price: ${total_price:.2f}")
