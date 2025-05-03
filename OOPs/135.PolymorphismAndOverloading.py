#Demonstrate method overloading by creating a Calculator class with multiple add() methods.
#(Covers: Polymorphism - Overloading; note: overloading depends on language support)

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
