#Python program to count the occurrences of a word in a text file.

myfile = open('demofile.txt','r')
target = "file"
data = myfile.read()
data = data.lower()
target = target.lower()
count = data.split().count(target)
print(f"{target} is exist {count} times in this file!")
myfile.close()
