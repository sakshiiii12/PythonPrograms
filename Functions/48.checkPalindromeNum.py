#Write a function to check if a number is a palindrome.

def checkPalindromeNum(num):
    if(str(num)==str(num)[::-1]):
        return True
    else:
        return False

num = int(input("Enter the number to check:"))
print("This number is a palindrome number:",checkPalindromeNum(num))
