#Python program to copy the contents of one file to another.

file1 = open("demofile.txt","r")
file2 = open("copy.file.txt","w")
data = file1.read()
file2.write(data)
print("Content Copied Successfully!")
file1.close()
file2.close()  
