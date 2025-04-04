#Write a function to check if a number is a perfect square.

def checkPerfectSquare(num):
    if num < 0:
        return False
    i = 0
    while i*i<=num:
        if(i*i==num):
            return True
        i = i + 1
    return False

num = int(input("Enter the number to check:"))
print("This number is a perfect square:",checkPerfectSquare(num))
