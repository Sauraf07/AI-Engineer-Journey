'''Task 2: Student Marks Recorder
Objective

Store student data in a file.

Features
Add Student
View Students
Calculate Average Marks
Example Data
Rahul,85
Aman,92
Priya,78
Concepts Used
split(",")
strip()
readlines()
Bonus

Find:

Highest Marks
Lowest Marks'''

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Marks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        with open("students.txt", "a") as file:
            file.write(f"{name},{marks}\n")
        print("Student added successfully!")
        
    elif choice == '2':
        try:
            with open("students.txt", "r") as file:
                students = file.readlines()
                if students:
                    print("Student Records:")
                    for idx, student in enumerate(students, start=1):
                        name, marks = student.strip().split(",")
                        print(f"{idx}. {name} - {marks}")
                else:
                    print("No student records found.")
        except FileNotFoundError:
            print("No student records found.")
            
    elif choice == '3':
        try:
            with open("students.txt", "r") as file:
                students = file.readlines()
                if students:
                    total_marks = 0
                    count = 0
                    for student in students:
                        _, marks = student.strip().split(",")
                        total_marks += int(marks)
                        count += 1
                    average_marks = total_marks / count
                    print(f"Average Marks: {average_marks:.2f}")
                else:
                    print("No student records found.")
        except FileNotFoundError:
            print("No student records found.")
            
    elif choice == '4':
        print("Exiting the Student Marks Recorder. Goodbye!")

        