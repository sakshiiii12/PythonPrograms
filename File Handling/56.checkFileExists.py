#Python program to check if a file exists. 

import os
file = "file.txt"
if(os.path.exists(file)):
     print("File Exist")
else:
    print("File Doesn't Exist")
