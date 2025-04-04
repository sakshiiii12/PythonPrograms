#Write a function that returns the greatest common divisor (GCD) of two numbers.

def GCD(num1,num2):
    gcd = 1
    for i in range(1,num1+1):
        if((num1%i==0) and (num2%i==0)):
            gcd = i
    return gcd

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
print("The greatest common divisor (GCD) of two numbers is:",GCD(num1,num2))
