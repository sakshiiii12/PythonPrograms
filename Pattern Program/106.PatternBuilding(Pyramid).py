#Write a python program for this pattern
'''
     *
    * *
   * * *
  * * * *
 * * * * *
'''

for i in range(1,6):
    for k in range(5,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
