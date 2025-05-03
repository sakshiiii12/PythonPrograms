#Create a base class Shape with a method area(). Derive classes like Rectangle, Circle, etc., and override area().
#(Covers: Polymorphism - Method Overriding)

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s*self.s

shapes = [Rectangle(5,6), Circle(2), Square(4)]
for s in shapes:
    print(s.area())
        
