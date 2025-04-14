#Python program to catch and handle a value error.

try:
     age = int(input("Enter the age:"))
     print(f"The person age is {age}")

except ValueError:
     print("Error! Invalid Input")

finally:
     print("Program Completed")
