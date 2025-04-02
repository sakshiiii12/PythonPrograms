#Python program to find the largest among three numbers. 

x = int(input("Enter the number to check:"))
y = int(input("Enter the number to check:"))
z = int(input("Enter the number to check:"))

if((x>y) and (x>z)):
    print("The largest among the three numbers is x")
elif((x<y) and (y>z)):
    print("The largest among the three numbers is y")
else:
    print("The largest among the three numbers is z")

