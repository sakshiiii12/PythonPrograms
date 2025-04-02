#Python program to count the number of occurrences of an element in a list.

list = [23,45,67,90,87,67,9,45,10,90,90]
count = 0
n = int(input("Enter the number to check the occurrences:"))
for i in list:
    if(i==n):
        count = count + 1
print("The number of occurrences of an element in a list:",count)
