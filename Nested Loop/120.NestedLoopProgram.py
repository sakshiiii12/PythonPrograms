#Write a python program for this pattern
'''
0
909
89098
789087
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321
'''

s = '0'
for i in range(10,0,-1):
    if(i!=10):
      s = str(i)+s+str(i)
    print(s)
