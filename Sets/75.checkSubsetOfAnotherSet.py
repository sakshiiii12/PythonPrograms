#Python program to check if a set is a subset of another set.

set1 = {1,2}
set2 = {1,2,3}
subset = set1.issubset(set2)
print(subset) #True

set1 = {1,2,3}
set2 = {4,5,6}
subset = set1.issubset(set2)
print(subset) #False
