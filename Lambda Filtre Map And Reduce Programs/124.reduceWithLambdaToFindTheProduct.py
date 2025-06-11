#Use reduce() and lambda to compute the product of all elements in the list.
'''
Reduce:- Collapse list into a single result
Syntax: from functools import reduce
        reduce(function, iterable)
'''

from functools import reduce
nums = [1,2,3,4,5]
product_elements = reduce(lambda x,y:x*y,nums)
print("The product of all elements in the list is:",product_elements)
