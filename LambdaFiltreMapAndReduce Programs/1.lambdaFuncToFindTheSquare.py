#Write a lambda function to compute the square of a number
'''
Lambda:- Creates small, one-line functions without giving them a name using def.
Syntax:- lambda arguments: expression
'''

square = lambda val:val*val
result = square
print("The square of a number is:",result(7))
