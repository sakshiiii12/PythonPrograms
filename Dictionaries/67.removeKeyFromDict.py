#Python program to remove a key from a dictionary.

dict = {1:2, 2:4, 3:6, 4:8, 5:10, 6:12}
keys = int(input("Enter the key to delete:"))
if(dict.get(keys)!=None):
    del dict[keys]
    print("Deleted Done",dict)
else:
    print("Key Not Found!")
