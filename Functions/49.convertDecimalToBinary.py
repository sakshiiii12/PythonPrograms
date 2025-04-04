#Write a function to convert a decimal number to binary.

def convertDecToBin(num):
    binary = ""
    while num>0:
        rem = num%2
        binary = str(rem) + binary
        num = int(num/2)
    return binary

num = float(input("Enter the number to convert:"))
print("A decimal number into binary is:",convertDecToBin(num))
