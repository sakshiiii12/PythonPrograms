#Python program that raises an exception if the input is not a number.

try:
    num1 = int(input("Enter the number:"))
    num2 = int(input("Enter the number:"))
    sum = num1 + num2
except:
    print("Error:In the variable only numeric data are allowed not string data type")
else:
    print(f"The sum of two number is {sum}")
