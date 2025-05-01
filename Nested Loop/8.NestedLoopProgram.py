#Write a python program for this pattern
'''
        1 
      2  3 
    4  5  6 
  7  8  9 10 
11 12 13 14 15
'''
n = 5
num = 1
for i in range(1, n + 1):
    print(' ' * (n - i) * 2, end='')  # Center spacing
    for j in range(i):
        print(f"{num:2}", end=' ')
        num += 1
    print()

