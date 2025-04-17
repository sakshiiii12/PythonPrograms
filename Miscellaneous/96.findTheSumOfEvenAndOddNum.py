#Python program to find the sum of even and odd numbers in a list separately.

list = [1,2,3,4,5,6,7,8,9,10]
sum_of_Even = 0
sum_of_Odd = 0
for i in list:
    if (i%2==0):
        sum_of_Even = sum_of_Even + i
    else:
        sum_of_Odd = sum_of_Odd + i

print("The sum of even numbers from a list is:",sum_of_Even)
print("The sun of odd numbers from a list is:",sum_of_Odd)
        
