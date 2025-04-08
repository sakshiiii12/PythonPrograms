#Python program to read a CSV file.

file = open('demofile.csv','r')
data = file.read()
print(data)
file.close()
