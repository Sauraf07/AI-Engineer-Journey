'''Challenge Task (Recommended)

Build a College Management System with:

Classes
Student
Teacher
Course
Features
Add Student
Add Teacher
Assign Course
Display Details'''

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

class Course:
    def __init__(self, course_id, course_name, teacher):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher

    def display_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")

# Example usage
teacher1 = Teacher(1, "Dr. Smith", "Mathematics")
course1 = Course(101, "Calculus", teacher1)
student1 = Student(1, "Alice", 20, course1.course_name)
teacher1.display_info()
course1.display_info()
student1.display_info()
