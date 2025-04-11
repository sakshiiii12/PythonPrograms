#Python program to merge two dictionaries.

dict1 = {'Name':'Ram Sharma','RollNo.':19,'Class':10}
dict2 = {'Math':89,'Science':92,'Sst':70}
dict3 = {}
for i in range(0,len(dict1)):
    dict3.update(dict1)
    dict3.update(dict2)
print("Merged Two Dictionaries:",dict3)
