'''Task 2: Student Information System using **kwargs
Objective

Create a function that accepts student details dynamically.'''
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
student_info(name="Alice", age=20, grade="A")
student_info(name="Bob", age=22, grade="B", major="Computer Science")