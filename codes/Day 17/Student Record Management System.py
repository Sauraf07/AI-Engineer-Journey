'''Task 1: Student Record Management System ⭐ (Beginner)
Objective

Learn CRUD (Create, Read, Update, Delete) operations with JSON.

Requirements

Create a file:

students.json
Features
Add Student
View All Students
Search Student by ID
Update Student
Delete Student
Concepts Covered
json.load()
json.dump()
Lists of Dictionaries
File Handling
CRUD Operations
Bonus
Validate duplicate IDs
Sort students by name'''

import json


def create_student_record(student_id, name, age, grade):
    student_data = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(student_data)
    
    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)

def view_all_students():
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            for student in data:
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("No student records found.")

def search_student_by_id(student_id):
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            for student in data:
                if student['id'] == student_id:
                    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

def update_student(student_id, name=None, age=None, grade=None):    
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            for student in data:
                if student['id'] == student_id:
                    if name:
                        student['name'] = name
                    if age:
                        student['age'] = age
                    if grade:
                        student['grade'] = grade
                    with open('students.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    print("Student record updated.")
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

def delete_student(student_id):
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            new_data = [student for student in data if student['id'] != student_id]
            if len(new_data) == len(data):
                print("Student not found.")
                return
            with open('students.json', 'w') as file:
                json.dump(new_data, file, indent=4)
            print("Student record deleted.")
    except FileNotFoundError:
        print("No student records found.")

def main(): 
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            create_student_record(student_id, name, age, grade)
        
        elif choice == '2':
            view_all_students()
        
        elif choice == '3':
            student_id = input("Enter Student ID to search: ")
            search_student_by_id(student_id)
        
        elif choice == '4':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            age = input("Enter new Age (leave blank to keep unchanged): ")
            grade = input("Enter new Grade (leave blank to keep unchanged): ")
            update_student(student_id, name if name else None, age if age else None, grade if grade else None)
        
        elif choice == '5':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()