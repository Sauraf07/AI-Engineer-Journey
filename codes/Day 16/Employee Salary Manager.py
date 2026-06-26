'''Task 2: Employee Salary Manager
Objective

Store employee details in a CSV file and calculate salary information.

CSV Structure
EmployeeID,Name,Department,BasicSalary
1001,Rahul,IT,50000
1002,Anjali,HR,45000
Features
Add Employee
Update Salary
Search Employee
Delete Employee
Calculate HRA (20%)
Calculate DA (10%)
Calculate Net Salary
Bonus

Generate the highest-paid employee report.'''

import csv


def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    basic_salary = float(input("Enter Basic Salary: "))
    
    with open('employees.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, name, department, basic_salary])
    
    print(f"Employee {name} added successfully!")

def update_salary(employee_id): 
    with open('employees.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == employee_id:
            print(f"Current Salary: {row[3]}")
            new_salary = float(input("Enter new salary: "))
            row[3] = new_salary
            reader[i] = row
            break
    else:
        print("Employee not found.")
        return
    
    with open('employees.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Salary for Employee {employee_id} updated successfully!")

def search_employee(employee_id):
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == employee_id:
                print(f"Employee Found: {row}")
                return
    print("Employee not found.")

def delete_employee(employee_id):
    with open('employees.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == employee_id:
            del reader[i]
            break
    else:
        print("Employee not found.")
        return
    
    with open('employees.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Employee {employee_id} deleted successfully!")

def calculate_salary(employee_id):  
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == employee_id:
                basic_salary = float(row[3])
                hra = 0.2 * basic_salary
                da = 0.1 * basic_salary
                net_salary = basic_salary + hra + da
                print(f"Salary Details for Employee {employee_id}:")
                print(f"Basic Salary: {basic_salary}")
                print(f"HRA (20%): {hra}")
                print(f"DA (10%): {da}")
                print(f"Net Salary: {net_salary}")
                return
    print("Employee not found.")

def highest_paid_employee():
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        highest_salary = 0
        highest_paid = None
        for row in reader:
            salary = float(row[3])
            if salary > highest_salary:
                highest_salary = salary
                highest_paid = row
        if highest_paid:
            print(f"Highest Paid Employee: {highest_paid}")
        else:
            print("No employees found.")

