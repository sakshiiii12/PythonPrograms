#Create a Car class with attributes (make, model, year) and a method to display details. Create objects for 2 cars.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)
car1.display()
car2.display()
