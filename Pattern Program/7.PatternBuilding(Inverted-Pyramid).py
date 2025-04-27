#Write a python program for this pattern
'''
* * * * *
 * * * *
  * * *
   * *
    *
'''

for i in range(5,0,-1):
    for j in range(1,5+1):
        if j < 5 - i + 1:
            print(' ',end="")
        else:
            print("* ",end="")
    print()
