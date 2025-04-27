#Write a python program for this pattern
'''
* * * * *
* * * *
* * *
* *
*
'''

for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()
