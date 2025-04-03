#Python program to check if two strings are anagrams.

str1 = input("Enter the string1:")
str2 = input("Enter the string2:")
if(sorted(str1)==sorted(str2)):
    print("Yes! This string is an anagrams string")
else:
    print("No! This string is not an anagrams string")
