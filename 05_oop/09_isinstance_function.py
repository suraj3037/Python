#Demonstrate the use of isinstance() function to check if an object is an instance of a class or a subclass thereof.

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create an instance of the ElectricCar class
electric_car1 = ElectricCar("Tesla", "Model S", 100)
print(electric_car1.full_name())
print(electric_car1.battery_size)

# Check if electric_car1 is an instance of ElectricCar
print(isinstance(electric_car1, ElectricCar))  # Output: True
# Check if electric_car1 is an instance of car
print(isinstance(electric_car1, car))  # Output: True