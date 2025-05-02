#Given a list, use map() and lambda to create a new list where each element is doubled.
'''
Map:- Applies a function to each item in an iterable (like a list) and returns a new iterator.
Syntax:- map(function, iterable)
'''

nums = [1,2,3,4]
double_the_elements = list(map(lambda x:x*2,nums))
print(double_the_elements)
