#Write a python program for this pattern
'''
0
10
101
0101
01010
'''

c=2
for i in range(1,6):
    for j in range(1,i+1):
        print(c%2,end=" ")
        c=c+1
    print()
