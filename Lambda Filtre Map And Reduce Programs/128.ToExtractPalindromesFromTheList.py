#Use filter() and lambda to extract palindromes from the list.

li = ["madam", "racecar", "apple", "level", "banana"]
palindromes = list(filter(lambda x : x == x[::-1], li))
print("The palindromes strings from the list are:",palindromes)
