#Create a Vector class and overload + and str() so you can add vectors and print them cleanly.
#Concepts: Dunder Methods (__add__, __str__)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1 + v2)
