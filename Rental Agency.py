class Vehicle:
    def __init__(self, cars, bus):
        self.cars = cars
        self.bus = bus

    def vehicles_available(self):
        print(f"Available cars: {self.cars}")
        print(f"Available buses: {self.bus}")

class Rental_Agency(Vehicle):
    def __init__(self, cars, bus):
        super().__init__(cars, bus)

    def rental_period(self, days):
        self.days = days
        print(f"Rental period is {self.days} days")

    def display_car_rent(self):
        print(f"The available cars are {self.cars} with a rent of 25 Rs per day at Star Agency.")

    def display_bus_rent(self):
        print(f"The available buses are {self.bus} with a rent of 50 Rs per day at Royal Agency.")


class Rental_Transaction(Rental_Agency):
    def __init__(self, cars, bus):
        super().__init__(cars, bus)

    def customer_booking(self, num_of_vehicles, days, vehicle_type):
        rent_price = 0
        if vehicle_type == 1:
            rent_price = num_of_vehicles * days * 25
            print(f"Your order for {num_of_vehicles} cars at Star Agency is booked. Please pay Rs {rent_price}.")
        elif vehicle_type == 2:
            rent_price = num_of_vehicles * days * 50
            print(f"Your order for {num_of_vehicles} buses at Royal Agency is booked. Please pay Rs {rent_price}.")
        else:
            print("Invalid vehicle type selected.")

if __name__ == "__main__":
    rental_agency = Rental_Transaction(cars=200, bus=100)

    while True:
        print("\n1. For renting car")
        print("2. For renting bus")
        print("3. For exit")
       
        choice = int(input("Enter your choice: "))
       
        if choice == 1:
            rental_agency.display_car_rent()
           
            num_of_cars = int(input("Enter number of cars you want to rent: "))
            days = int(input("Enter the number of days you want to rent: "))
            rental_agency.customer_booking(num_of_cars, days, 1)
           
        elif choice == 2:
            rental_agency.display_bus_rent()
           
            num_of_buses = int(input("Enter number of buses you want to rent: "))
            days = int(input("Enter the number of days you want to rent: "))
            rental_agency.customer_booking(num_of_buses, days, 2)
           
        elif choice == 3:
            print("Exiting")
            break
       
        else:
            print("Invalid choice. Please try again.")
