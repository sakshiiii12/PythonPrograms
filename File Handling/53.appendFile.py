#Python program to append text to a file.

file = open("demofile.txt","a")
data = file.write("\nWe are praticing file handling programming questions.")
print(data)
file.close()
