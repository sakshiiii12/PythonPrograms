#Build a ShapeFactory that returns objects of Circle, Rectangle, or Square based on input.
#Concepts: Design Pattern – Factory

class Circle:
    def draw(self):
        print("Drawing Circle")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            return ValueError("Unknown Shape")

shape = ShapeFactory.get_shape("circle")
shape.draw()
