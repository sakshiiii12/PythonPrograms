#Python program to find the square root of a number without using built-in functions.

def findSqroot(num):
    if num < 0:
        return "Invalid Input"
    a = num
    while a*a > num:
        a = (a+num/a) //2
    return a

number = int(input("Enter the number:"))
print("The square root of a number is:",findSqroot(number))
