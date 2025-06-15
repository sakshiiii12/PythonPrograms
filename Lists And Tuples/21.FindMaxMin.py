#Python program to find the maximum and minimum numbers in a list.      

list = [34,67,89,56,90,66,93,45,20,31]
max = list[0]
min = list[0]
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i
print("The maximum number from a list is:",max)
print("The minimum number from a list is:",min)
