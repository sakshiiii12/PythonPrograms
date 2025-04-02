#Python program to find the intersection of two lists.    

list1 = [32,41,12,45,67,98,78]
list2 = [12,34,67,45,78,56,49]
list3 = []
for i in list1:
    for j in list2:
        if(i==j):
            list3.append(i)
            list2.remove(i)
print("The Intersection of two lists:",list3)
