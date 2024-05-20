class Car:
    car = {
        1: (1, 'Honda', 'Civic', 'Black', True),
        2: (2, 'Toyota', 'Corolla', 'White', True),
        3: (3, 'Hyundai', 'Elantra', 'Red', True),
        4: (4, 'Kia', 'Sorento', 'Blue', True),
        5: (5, 'Nissan', 'Altima', 'Silver', True),
    }

    def show_cars(self):
        for key, value in self.car.items():
            print(value)

    def rent_car(self, car_id):
        if car_id in self.car:
            if self.car[car_id][4]:
                self.car[car_id] = (*self.car[car_id][:4], False)
                print(f"Car {car_id} has been rented.")
            else:
                print(f"Car {car_id} is already rented.")
        else:
            print("Invalid car ID.")

    def return_car(self, car_id):
        if car_id in self.car:
            if not self.car[car_id][4]:
                self.car[car_id] = (*self.car[car_id][:4], True)
                print(f"Car {car_id} has been returned.")
            else:
                print(f"Car {car_id} is not rented.")
        else:
            print("Invalid car ID.")

    def calculate_rental_cost(self, car_id, days):
        if car_id in self.car:
            if not self.car[car_id][4]:
                rental_rate = 50  # Assuming a fixed rental rate of $50 per day
                total_cost = rental_rate * days
                print(f"Rental cost for Car {car_id} for {days} days: ${total_cost}")
            else:
                print(f"Car {car_id} is not rented.")
        else:
            print("Invalid car ID.")


if __name__ == '__main__':
    print("Welcome to the Car Rental System")
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    customer_id = input("Enter your ID: ")

    car_rental_system = Car()
    print("Welcome", name)
    print("Available Cars:")
    car_rental_system.show_cars()

    choice = int(input("Enter the index to book a car: "))
    car_rental_system.rent_car(choice)

    # Perform additional actions like returning a car and calculating rental cost as needed
    
