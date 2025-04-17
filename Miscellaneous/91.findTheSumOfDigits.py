#Python program to find the sum of digits of a number.

def findSumOfDigits(num):
    sum_of_digits = 0
    for i in range(1,num+1):
        rem = num%10
        sum_of_digits = rem + sum_of_digits
        num = num // 10
    return sum_of_digits

number = int(input("Enter the number:"))
print("The sum of digits of a number is:",findSumOfDigits(number))
