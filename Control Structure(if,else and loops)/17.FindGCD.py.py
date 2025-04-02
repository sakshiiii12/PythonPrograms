#Python program to find the greatest common divisor (GCD) of two numbers.

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
gcd = 1
for i in range(1,num1+1):
    if((num1%i==0) and (num2%i==0)):
        gcd = i
print("The greatest common divisor(GCD) of two numbers is:",gcd)
