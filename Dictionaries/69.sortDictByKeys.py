#Python program to sort a dictionary by its keys.

dict1 = {'Peas':50, 'Onion':70, 'Cabbage':100, 'Tomoato':90, 'Gralic':70}
sorted_dict = dict(sorted(dict1.items()))
print("Dictionary sorted by keys:",sorted_dict)
