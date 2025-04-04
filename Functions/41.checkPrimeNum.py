#Python function to check if a number is prime.

def checkPrimeNum(num):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count = count + 1
    if(count==2):
            return True
    else:
        return False

num = int(input("Enter the number to check:"))
print("This number is a prime number:",checkPrimeNum(num))
