#Python program to check if a string contains only numbers.

def isNumeric(str):
    if not str:
        return False
    for char in str:
        if char < "0" or char > "9":
            return False
    return True

print(isNumeric("1234"))
print(isNumeric("sakshi1234"))
print(isNumeric(" "))
print(isNumeric("hello"))
