#Build a Vehicle class and override its move() method in Car, Bike, and Truck subclasses. Call them polymorphically.
#(Covers: Runtime Polymorphism, Method Overriding, Superclass Reference)

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is riding")

class Truck(Vehicle):
    def move(self):
        print("Truck is hauling")

vehicles = [Car(), Bike(), Truck()]
for v in vehicles:
    v.move()
