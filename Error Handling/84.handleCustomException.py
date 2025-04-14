#Python program to raise a custom exception.

class MyCustomError(Exception):
     pass 

try:
     value = int(input("Enter a number: "))

     if value < 0:
         raise MyCustomError  

     print("You entered:", value)

except MyCustomError:
     print("Custom Exception: Negative numbers are not allowed!")
except ValueError:
     print("Invalid input! Please enter a valid number.")

