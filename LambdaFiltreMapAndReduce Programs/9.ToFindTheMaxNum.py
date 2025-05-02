#Use reduce() and lambda to find the maximum number in a list.

from functools import reduce
li = [3, 8, 2, 10, 6]
max_num = reduce(lambda x , y: x if x > y else y, li)
print("The maximum number in a list is:",max_num)
