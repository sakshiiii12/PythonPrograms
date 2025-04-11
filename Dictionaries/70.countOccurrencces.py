#Python program to count the occurrences of each element in a list using a dictionary.

elements = ['apple', 'banana', 'apple', 'mango', 'banana', 'grapes', 'apple', 'mango', 'mango']
count_dict = {}
for item in elements:
     count_dict[item] = count_dict.get(item, 0) + 1
print("Element occurrences:", count_dict)
