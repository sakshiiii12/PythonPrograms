#Python program to print all even numbers between 1 and 50.  

even_num = []
for i in range(1,51):
    if (i%2==0):
        even_num.append(i)
print("Even Numbers Between 1 to 50 is:",even_num)
