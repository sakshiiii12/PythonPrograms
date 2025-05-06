#Create two classes A and B with a method show(). Create a class C that inherits from both, and see which show() gets called.
#Concepts: Multiple Inheritance, MRO


class A:
    def show(self):
        print("My class is A")
    
class B:
    def show(self):
        print("My Class is B")

class C(A, B):
    pass

obj = C()
obj.show()
