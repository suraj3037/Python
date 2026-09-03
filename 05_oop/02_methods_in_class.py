#Add method to a car class that displays the full name of the car(brand and model)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Create an instance of the Car class
car1 = Car("Toyota", "Fortuner")
print(car1.full_name())