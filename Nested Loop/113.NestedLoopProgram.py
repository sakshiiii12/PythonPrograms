#Write a python program for this pattern
'''
1
23
456
78910
11121314
'''

c=1
for i in range(1,6):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    print()
