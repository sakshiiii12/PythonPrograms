#Python program to convert a decimal number to hexadecimal.

def convertDecToHexdec(num):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while num>0:
        rem = num%16
        hexadecimal = hex_digits[rem] + hexadecimal
        num = int(num//16)
    return hexadecimal

print(convertDecToHexdec(740))
