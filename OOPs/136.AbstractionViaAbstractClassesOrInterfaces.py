#Use abstraction by creating an abstract class Animal with an abstract method makeSound() and implement it in subclasses.
#(Covers: Abstraction via Abstract Classes or Interfaces)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()
