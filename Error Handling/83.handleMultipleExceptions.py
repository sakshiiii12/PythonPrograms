#Python program to catch multiple exceptions.

try:
     num1 = int(input("Enter the number:"))
     num2 = int(input("Enter the number:"))
     sum = num1+num2
     print(f"The sum of two number is {sum}")
except Exception as e:
     print("Error:The data is not a numeric data type")
try:
     n = int(input("Enter the number:"))
     d = int(input("Enter the number:"))
     r = n/d
     print(f"The final result of divsion are {r}")
except Exception as e:
     print("Error:Its a zero divsion error")
