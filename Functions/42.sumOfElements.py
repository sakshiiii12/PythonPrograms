#Python function to calculate the sum of all elements in a list.

def sumOfList(li):
    sum = 0
    for i in li:
        sum = sum + i
    return sum

list = [1,2,3,4,5,6,7,8,9,10]
print("The sum of all elements in a list:",sumOfList(list))
