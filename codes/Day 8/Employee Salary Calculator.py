'''Challenge Task (Recommended)
Employee Salary Calculator

Create functions:

calculate_hra()
calculate_da()
calculate_tax()
calculate_net_salary()'''
def calculate_hra(basic_salary):
    return basic_salary * 0.2
def calculate_da(basic_salary):
    return basic_salary * 0.1
def calculate_tax(gross_salary):
    return gross_salary * 0.1
def calculate_net_salary(basic_salary):
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    gross_salary = basic_salary + hra + da
    tax = calculate_tax(gross_salary)
    return gross_salary - tax
# Example usage:
basic_salary = 50000
net_salary = calculate_net_salary(basic_salary)
print(f"The net salary is: {net_salary}")
