#Demonstrate polymorphism by defining the method fuel_type in both car and electric car classes, but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# Create instances of the Car and ElectricCar classes
car1 = Car("Toyota", "Fortuner")
electric_car1 = ElectricCar("Tesla", "Model S", 100)

print(car1.fuel_type())
print(electric_car1.fuel_type())
