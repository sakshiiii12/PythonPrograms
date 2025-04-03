#Python program to remove all spaces from a string.

str = input("Enter the string:")
print("String:",str)
strlist = str.split()
str1 = " "
for i in strlist:
    str1=str1+i
print("Remove all spaces from a string:",str1)
