#Write a python program for this pattern
'''
A
AB
ABC
ABCD
ABCDE
'''

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
