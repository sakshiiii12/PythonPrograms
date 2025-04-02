#Python program to remove duplicates from a list.  

list = [2,3,4,5,2,1,4,6,7,8,9,7,6,8,0]
li = []
for i in list:
    if i not in li:
        li.append(i)
print("Removing Duplicates From A list:",li)
