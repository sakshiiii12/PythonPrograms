#Python program to find the longest word in a sentence.

str = "We are Learning python!"
strlist = str.split()
maxstr = ""
for i in strlist:
    if (len(maxstr)<len(i)):
        maxstr = i
print("The longest word in a sentence is:",maxstr)
