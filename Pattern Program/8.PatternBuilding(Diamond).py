#Write a python program for this pattern
'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *

'''

#Upper Half
for i in range(1,5+1):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

#Lower Half
for i in range(5,0,-1):
    for j in range(1,5+1):
        if j < 5 - i + 1:
            print(" ",end="")
        else:
            print("* ",end="")
    print()
