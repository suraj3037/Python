#create car class to encapsulate the brand attribute, making it private and provide getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model

    def get_brand(self):
        return self.__brand
# Create an instance of the Car class
car1 = Car("Toyota", "Fortuner")
print(car1.get_brand())