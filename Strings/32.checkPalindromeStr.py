#Python program to check if a string is a palindrome.

str = input("Enter the string to check:")
if (str == str[::-1]):
    print("Yes! This string is a palindrome string")
else:
    print("No! This string is not a palindrome string")
