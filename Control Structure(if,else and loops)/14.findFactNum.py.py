#Python program to calculate the factorial of a number.

num = int(input("Enter the number to calculate the factorial:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("Factorial of a given number is:",fact)
