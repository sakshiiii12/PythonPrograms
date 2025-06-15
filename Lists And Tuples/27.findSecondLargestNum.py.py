#Python program to find the second largest number in a list.  

list = [32,41,12,45,67,98,78]
for i in list:
    list.sort(reverse=True)
print("Second Largest Number In A List:",list[1])
