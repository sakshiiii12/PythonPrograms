#Write a python program for this pattern
'''
     *
    **
   ***
  ****
******
'''

for i in range(1,5+1):
    for j in range(1,5+1):
        if j <= 5 - i:
            print(" ",end=" ")
        else:
            print("*", end=" ")
    print()
