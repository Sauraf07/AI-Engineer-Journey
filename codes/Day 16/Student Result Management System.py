'''Task 1: Student Result Management System ⭐
Objective

Create a program to manage student records stored in a CSV file.

CSV Structure
RollNo,Name,Math,Science,English
101,Alice,85,90,88
102,Bob,78,81,75
Features
Add Student
View All Students
Search Student by Roll Number
Update Marks
Delete Student
Calculate Total Marks
Calculate Percentage
Display Grade (A/B/C/D/F)
Concepts Covered
csv.reader()
csv.writer()
File Handling
Lists
Loops
Functions
Bonus

Sort students by percentage.'''

import csv
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, math, science, english])
    
    print(f"Student {name} added successfully!")

add_student()

def view_all_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student(roll_no):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll_no:
                print(f"Student Found: {row}")
                return
    print("Student not found.")

def update_marks(roll_no):
    with open('students.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == roll_no:
            print(f"Current Marks: Math: {row[2]}, Science: {row[3]}, English: {row[4]}")
            row[2] = input("Enter new Math Marks: ")
            row[3] = input("Enter new Science Marks: ")
            row[4] = input("Enter new English Marks: ")
            reader[i] = row
            break
    else:
        print("Student not found.")
        return
    
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Marks for Roll Number {roll_no} updated successfully!")

def delete_student(roll_no):
    with open('students.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == roll_no:
            del reader[i]
            break
    else:
        print("Student not found.")
        return
    
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Student with Roll Number {roll_no} deleted successfully!")
    
    