'''Task 2: Vehicle Management System
Objective

Practice Polymorphism

Requirements

Create:

Vehicle
│
├── Car
├── Bike
└── Truck'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def calculate_mileage(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Fuel Type: {self.fuel_type}"

    def calculate_mileage(self):
        return 15  # Example mileage for a car
    
class Bike(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Engine Capacity: {self.engine_capacity}cc"

    def calculate_mileage(self):
        return 40  # Example mileage for a bike
    
class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Load Capacity: {self.load_capacity} tons"

    def calculate_mileage(self):
        return 8  # Example mileage for a truck
    
# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, "Petrol")
    bike = Bike("Yamaha", "R15", 2019, 155)
    truck = Truck("Volvo", "FH16", 2021, 20)

    vehicles = [car, bike, truck]

    for vehicle in vehicles:
        print(vehicle.get_details())
        print(f"Mileage: {vehicle.calculate_mileage()} km/l")
        print()
        