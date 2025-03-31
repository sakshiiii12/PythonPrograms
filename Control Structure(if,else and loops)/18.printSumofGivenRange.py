#Python program to find whether a given number is Armstrong or not. 

num = int(input("Enter the number to check:"))
temp = num
total = 0
while num>0:
    rem = num%10
    total = total+rem*rem*rem
    num = int(num/10)
if(total==temp):
    print("Yes! Its an armstrong number")
else:
    print("No! Its not an armstrong number")
