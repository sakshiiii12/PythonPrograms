#Python function to reverse a string.

def reverseStr(str):
    return str[::-1]

str = input("Enter the string:")
print("String:",str)
print("Reverse String:",reverseStr(str))
