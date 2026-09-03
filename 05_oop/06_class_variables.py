#Add class variable to a car that keeps the track of number of cars created

class Car:
    total_cars = 0  # class variable to keep track of the number of cars created
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1  # increment the class variable when a new car is created

# Create instances of the Car class
car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")

print(f"Total cars created: {Car.total_cars}")