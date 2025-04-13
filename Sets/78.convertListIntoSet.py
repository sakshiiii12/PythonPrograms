#Python program to convert a list into a set.

list = [1,2,3,4,5,6,7,8,9,10]
print("List:",list)
set = set()
for i in list:
     set.add(i)
print(set)
print(type(set))
