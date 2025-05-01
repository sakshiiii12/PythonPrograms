#Write a python program for this pattern
'''
1
01
010
1010
10101
'''

c=3
for i in range(1,6):
    for j in range(1,i+1):
        print(c%2,end=" ")
        c=c+1
    print()
