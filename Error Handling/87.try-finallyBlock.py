#Python program that uses a try-finally block.

try:
     num = int(input("Enter a number: "))
     result = 10 / num  
     print("Result:", result)
except ZeroDivisionError:
     print("Error! Cannot divide by zero.")
except ValueError:
     print("Invalid input! Please enter a valid number.")
finally:
     print("Excecution Completed")
