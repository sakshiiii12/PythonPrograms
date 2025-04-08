#Python program to merge two text files into one.

file1 = open('demofile.txt','r')
file2 = open('copy.txt','r')
file3 = open('mergedfile.txt','a')
file3.write(file1.read()+"\n")
file3.write(file2.read())
print("File Merged Successfully!")
file1.close()
file2.close()
file3.close()
