'''Task 3: Employee Salary Calculator
Requirements

Create an Employee class.

Attributes
emp_id
name
basic_salary
Methods
calculate_hra()
calculate_da()
calculate_total_salary()'''
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def clalculate_hra(self):
        return self.basic_salary * 0.2  # HRA is 20% of basic salary
    
    def calculate_da(self):
        return self.basic_salary * 0.1  # DA is 10% of basic salary
    
    def calculate_total_salary(self):
        hra = self.clalculate_hra()
        da = self.calculate_da()
        total_salary = self.basic_salary + hra + da
        return total_salary
    
# Example usage
employee1 = Employee(101, "Bob", 50000)
print(f"Employee ID: {employee1.emp_id}")
print(f"Name: {employee1.name}")
print(f"Basic Salary: ${employee1.basic_salary}")
print(f"HRA: ${employee1.clalculate_hra()}")
print(f"DA: ${employee1.calculate_da()}")
print(f"Total Salary: ${employee1.calculate_total_salary()}")
