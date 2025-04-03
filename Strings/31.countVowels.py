#Python program to count the number of vowels in a string.

str = input("Enter the string:")
count = 0
for i in str:
    if(i in 'AEIOUaeiou'):
        count = count + 1
print("The number of vowels in a string:",count)
