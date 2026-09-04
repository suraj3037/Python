#Use a property decorator in car class to make the model attribute read only.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @staticmethod
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."

    @property
    def model(self):
        return self.__model
    
# Create an instance of the Car class
car1 = Car("Toyota", "Fortuner")
# Call the static method without creating an instance of the class
print(Car.general_description())

print("car model :", car1.model)