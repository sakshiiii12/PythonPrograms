#Python program to print the Fibonacci sequence up to n terms.

a = 0
b = 1
n = int(input("Enter the range:"))
for i in range(1,n+1):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
