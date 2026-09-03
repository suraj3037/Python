#create the electric car class that inherits from the car class and has an additional attribute battery_size, then create an instance of that class

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