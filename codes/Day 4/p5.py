# Task 5: AI Engineer Challenge – Employee Database (Medium-Hard)
'''Create an empty employee database'''
employees = [
    ("Rahul", 50000),
    ("Amit", 60000),
    ("Priya", 75000),
    ("Neha", 80000)
]
print("Employee Database:")
for name, salary in employees:
    print(f"Name: {name}, Salary: {salary}")
def add_employee(name, salary):
    employees.append((name, salary))    
def remove_employee(name):
    for employee in employees:
        if employee[0] == name:
            employees.remove(employee)
            return
    print(f"{name} not found in employee database.")
def show_employees():
    print("Employee Database:")
    for name, salary in employees:
        print(f"Name: {name}, Salary: {salary}")
def total_employees():
    print("Total Number of Employees:", len(employees))
# Example usage
add_employee("Suresh", 55000)
show_employees()
total_employees()
remove_employee("Amit")
show_employees()
total_employees()
