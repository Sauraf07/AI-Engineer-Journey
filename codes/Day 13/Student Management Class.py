'''Task 1: Student Management Class
Requirements

Create a Student class with:

student_id
name
age
course
Methods
display_info()'''
class Student:
    def __init__(self,id,name,age,course):
        self.student_id = id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

# Example usage
student1 = Student(1, "Alice", 20, "Computer Science")
student1.display_info()
    