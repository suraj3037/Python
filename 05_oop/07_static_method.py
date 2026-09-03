#Add a static method to a car class and display the general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."

# Create an instance of the Car class
car1 = Car("Toyota", "Fortuner")
# Call the static method without creating an instance of the class
print(Car.general_description())