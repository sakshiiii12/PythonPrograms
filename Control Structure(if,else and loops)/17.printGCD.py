#Python program to print the sum of all numbers in a given range. 

start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range:"))
sum = 0
for i in range(start,end+1):
    sum = sum + i
print("The sum of all numbers in a given range are:",sum)
