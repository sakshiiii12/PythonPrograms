#Python function that returns the factorial of a number.

def factNum(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

num = int(input("Enter the number:"))
print("The factorial of a number:",factNum(num))
