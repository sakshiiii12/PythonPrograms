#Python function that accepts a list and returns a new list with unique elements.

def uniqueList(list1):
    return list(set(list1))

list1 = [1,2,3,3,4,5,6,7,2,5,7,10]
print("List:",list1)
print("A new list with unique elements:",uniqueList(list1))
