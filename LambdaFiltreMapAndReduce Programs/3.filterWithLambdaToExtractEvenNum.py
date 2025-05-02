#Use filter() and a lambda function to extract all even numbers from the list.
'''
Filters elements from an iterable based on a function that returns True or False.
Syntax: filter(function, iterable)
'''

nums = [5,8,15,2,9,12]
evenNum = list(filter(lambda x:x%2==0,nums))
print('The even numbers from the list is:',evenNum)
