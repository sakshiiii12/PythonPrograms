#Python program to capitalize the first letter of each word in a string.

str = input("Enter the string:")
print("String:",str)
strlist = str.split()
str1 = " "
for i in strlist:
    str1 = str1+i[0].upper()+i[1::]+" "
print("Capitalize the first letter of each word in a string.",str1)
