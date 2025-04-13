#Python program to handle division by zero. 

try:
    numerator = int(input("Enter the numerator:"))
    denominator = int(input("Enter the denominator:"))
    result = numerator/denominator
except Exception as e:
     print("Error: Divsion by zero is not allowed")
else:
   print(f"The result is {result}")
