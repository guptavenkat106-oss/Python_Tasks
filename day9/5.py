class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def display(self):
        print("Car Brand:", self.brand)
        print("Speed:", self.speed)
        print("----------------------")

class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)
        print("Speed:", self.speed)
        print("----------------------")

car1 = Car("Toyota", 120)
bike1 = Bike("Yamha", 80)

car1.display()
bike1.display()


        
