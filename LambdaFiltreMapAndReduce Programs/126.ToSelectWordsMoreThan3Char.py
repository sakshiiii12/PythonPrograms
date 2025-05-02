#Given a list, use filter() and lambda to select words with more than 3 characters.

words = ["apple", "x", "pear", "kiwi", "plum"]
print(list(filter(lambda  word : len(word)>3 ,words)))
