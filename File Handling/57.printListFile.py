#Python program to write a list of numbers to a text file.

file = open('copy.txt','w')
st = ""
for i in range(1,101):
    st=st+str(i)+"\n"
file.write(st)
print("File Written Succesfully")
file.close()
