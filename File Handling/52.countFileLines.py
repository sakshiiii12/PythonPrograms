#Python program to count the number of lines in a text file.

file = open("demofile.txt",'rb')
data = file.readlines()
print("The number of lines in a text file:",len(data))
file.close()
