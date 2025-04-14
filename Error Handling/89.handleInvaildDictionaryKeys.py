#Python program to handle invalid dictionary keys.

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

try:
     name = input("Enter the student's name: ") 
     grade = student_grades[name] 
     print(f"{name}'s grade is: {grade}")

except KeyError:
     print("Error! The entered name is not found in the dictionary.")
