#Create a class Temperature that stores temperature in Celsius, but allows getting/setting in Fahrenheit.
#Concepts: @property, Encapsulation

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, f):
        self._celsius = (f - 32) * 5/9

temp = Temperature(0)
print(temp.fahrenheit)
temp.fahrenheit = 212
print(temp._celsius)
