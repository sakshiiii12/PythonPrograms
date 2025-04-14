#Python program to catch an index out of range exception.

try:
     list = [1,2,3,4,5]
     print("Index of list:",list[7])
except IndexError:
     print("Error!catch an index out of range exception")
finally:
     print("Excecution Completed!")
