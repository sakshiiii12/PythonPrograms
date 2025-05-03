#Demonstrate inheritance by creating a Person class and a Student class that inherits from it.
#(Covers: Inheritance, Method Overriding)

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}")

class Student(Person):
    def __init__(self, name, student_id, course):
        super().__init__(name)
        self.student_id = student_id
        self.course = course

    def greet(self):
        print(f"I'm {self.name}, and my ID is {self.student_id} and course is {self.course}")

p1 = Student("Sakshi Yadav", "s@1212", "Data Science")
p1.greet()
        
