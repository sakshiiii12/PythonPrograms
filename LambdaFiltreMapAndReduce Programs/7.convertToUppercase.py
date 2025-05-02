#Convert all strings in a list to uppercase using map() and lambda.

li =  ["a", "b", "c"]
uppercase = list(map(lambda x: x.upper(),li))
print("The uppercase strings are:",uppercase)
