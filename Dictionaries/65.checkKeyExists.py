#Python program to check if a key exists in a dictionary.

dict = {"name": "Arjun", "age": 21, "course": "Computer Science"}
keys = input("Enter the keys to check:")
if(keys in dict):
    print("Yes! this key exists in a dictionary")
else:
    print("No! this key do not exists in a dictionary")
