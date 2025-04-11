#Python program to create a dictionary from two lists.

list1 = ['apple','banana','mango','grapes','litchi']
list2 = [22,45,33,76,56]
dict = {}
for i in range(0,len(list1)):
    dict.update({list1[i]:list2[i]})
print("New Dictionary:",dict)
