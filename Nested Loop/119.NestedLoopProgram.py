#Write a python program for this pattern
'''
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1
'''

def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

n = 5
for i in range(n):
    print(' ' * (n - i), end='')  # Centering the row
    for j in range(i + 1):
        value = factorial(i) // (factorial(j) * factorial(i - j))
        print(value, end=' ')
    print()

