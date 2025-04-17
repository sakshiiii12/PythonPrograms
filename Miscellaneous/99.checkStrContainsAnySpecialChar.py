#Python program to check if a string contains any special characters.

def contains_special_characters(str):
    for char in str:
        if not char.isalnum():
            return True
    return False

print("Is string contains any special characters:",contains_special_characters("Hello123"))
print("Is string contains any special characters:",contains_special_characters("Hello@123"))
print("Is string contains any special characters:",contains_special_characters("123$%"))   
print("Is string contains any special characters:",contains_special_characters("!@#$%^&*<>/")) 
print("Is string contains any special characters:",contains_special_characters(" "))   
