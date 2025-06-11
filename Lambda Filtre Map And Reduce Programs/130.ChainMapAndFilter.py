#Given list, use map() and filter() with lambda to:
#  First filter even numbers
#  Then square each of them
#  Return the final list


nums = [1, 2, 3, 4, 5, 6]
even_squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print("The final list is:",even_squared)
