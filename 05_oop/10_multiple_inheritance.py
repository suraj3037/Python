#create two classes battery and engine and let the electric car class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_description(self):
        return "A battery is a device that stores energy and provides power to an electric vehicle."

class Engine:
    def engine_description(self):
        return "An engine is a machine that converts energy into mechanical motion, typically used in vehicles."

class ElectricCar(Battery, Engine):
    pass

# Create an instance of the ElectricCar class
electric_car1 = ElectricCar()
# Call methods from both parent classes
print(electric_car1.battery_description())
print(electric_car1.engine_description())