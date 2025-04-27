#Write a python program for this pattern
'''
*       *
* *     * *
* * *   * * *
* * * * * * *
* * * * * * *
* * *   * * *
* *     * *
*       *
'''

n = 4

# Upper half
for i in range(1, n+1):  
    for j in range(1, n+1): 
        if j <= i:
            print('* ', end='')  
        else:
            print('  ', end='') 
    for j in range(1, n+1):  
        if j <= n-i:
            print('  ', end='')  
        else:
            print('* ', end='')  
    print()

# Lower half
for i in range(n, 0, -1):  
    for j in range(1, n+1):  
        if j <= i:
            print('* ', end='') 
        else:
            print('  ', end='')  
    for j in range(1, n+1):  
        if j <= n-i:
            print('  ', end='')  
        else:
            print('* ', end='')
    print()

