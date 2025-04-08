#Python program to open a file and read its contents.

file = open("demofile.txt","r")
data = file.read()
print(data)
file.close()
