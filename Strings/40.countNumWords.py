#Python program to count the number of words in a string.

str = input("Enter the string to count:")
count = 0
for i in str:
    count = count + 1
print("The number of words in a string:",count)
