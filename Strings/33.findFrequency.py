#Python program to find the frequency of characters in a string.

str = input("Enter the string:")
print("String:",str)
templist = [ ]
for i in list(str):
    if i not in templist:
        print("Occurence of",i,"string:",str.count(i))
        templist.append(i)
