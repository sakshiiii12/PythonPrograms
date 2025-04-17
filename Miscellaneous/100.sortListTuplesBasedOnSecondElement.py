#Python program to sort a list of tuples based on the second element.

tuples = [(1,4),(2,1),(3,7),(4,3),(5,9),(6,10)]
tuples.sort(key = lambda x:x[1])
print("Sorted list of tuples based on the second element:",tuples)
