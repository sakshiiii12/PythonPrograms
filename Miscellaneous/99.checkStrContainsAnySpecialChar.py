#Python program to check if a string contains any special characters.

def contains_special_characters(str):
    for char in str:
        if not char.isalnum():
            return True
    return False

print(contains_special_characters("Hello123"))
print(contains_special_characters("Hello@123"))
print(contains_special_characters("123$%"))   
print(contains_special_characters("!@#$%^&*<>/")) 
print(contains_special_characters(" "))   
