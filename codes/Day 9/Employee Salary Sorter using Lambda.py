'''Task 3: Employee Salary Sorter using Lambda
Objective

Sort employee salaries in ascending order.'''
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 60000},
    {"name": "Bob", "salary": 55000}
]

sorted_employees = sorted(employees, key=lambda x: x["salary"])
for emp in sorted_employees:
    print(f"{emp['name']}: {emp['salary']}")