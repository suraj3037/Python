#create a car class with atributes brand and model, then create a instance of that class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create an instance of the Car class

car1= Car("Toyota", "Fortuner")

print(f"Car Brand: {car1.brand}, Car Model: {car1.model}")