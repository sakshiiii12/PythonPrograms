#Create a Student class. Use a class method to set a class-level variable like school_name, and a static method to validate age.
#Concepts: Class vs Static methods

class Student:
    school_name = "Unknown"

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_school(cls, name):
        cls.school_name = name

    @staticmethod
    def is_valid_age(age):
        return 5 <= age <= 18

Student.set_school("J.K.G International School")
print(Student.school_name)
print(Student.is_valid_age(16))
        
