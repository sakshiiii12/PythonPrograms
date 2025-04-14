#Python program to handle file not found errors.

try:
    file = open("demofile.txt","r")
    data = file.read()
except Exception as e:
    print("Error! File Not Found Error")
else:
    print(data)
