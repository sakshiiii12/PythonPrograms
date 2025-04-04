#Python function to find the maximum of three numbers.

def maxNum(list):
    return max(list)

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))

print("The maximum of three numbers:",maxNum([num1,num2,num3]))
