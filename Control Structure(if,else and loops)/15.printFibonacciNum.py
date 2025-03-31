#Python program to check if a year is a leap year.

year = int(input("Enter the year to check:"))
if(year%4==0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")
