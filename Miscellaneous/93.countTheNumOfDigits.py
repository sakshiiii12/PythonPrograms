#Python program to count the number of digits in a number.

def countNumDigits(num):
    count = 0
    if(num == 0):
        return 1
    num = abs(num)
    while num>0:
        count = count + 1
        num //= 10
    return count

number = int(input("Enter the number:"))
print("The number of digits in a number is:",countNumDigits(number))
