#Python program to update the value of a key in a dictionary.

dict = {1:2, 2:4, 3:6, 4:8, 5:10}
keys = int(input("Enter the key:"))
if(dict.get(keys)!=None):
    values = int(input("Enter the value to update:"))
    dict.update({keys:values})
    print("Updated Done:",dict)
else:
    print("Invalid Number")
