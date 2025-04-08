#Python program to read a file line by line.

file = open("demofile.txt","r")
for lines in file.readlines():
    print(lines)
file.close()
