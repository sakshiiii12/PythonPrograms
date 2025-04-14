#Python program that handles a type error.

try:
     num = input("Enter the number:")
     print(num+5)
except TypeError:
     print("Error invalid input")

