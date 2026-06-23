'''Day 14 Tasks – OOP Advanced
Task 1: Employee Management System
Objective

Practice:

Inheritance
Method Overriding
Encapsulation'''

class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name  # Encapsulation: private attribute
        self.__emp_id = emp_id  # Encapsulation: private attribute
        self.__salary = salary  # Encapsulation: private attribute

    def get_details(self):
        return f"Name: {self.__name}, ID: {self.__emp_id}, Salary: {self.__salary}"

    def calculate_bonus(self):
        return self.__salary * 0.10  # 10% bonus
    
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)  # Inheritance
        self.__department = department  # Encapsulation: private attribute

    def get_details(self):
        base_details = super().get_details()  # Method Overriding
        return f"{base_details}, Department: {self.__department}"

    def calculate_bonus(self):
        return self._Employee__salary * 0.20  # 20% bonus for managers
    
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)  # Inheritance
        self.__programming_language = programming_language  # Encapsulation: private attribute

    def get_details(self):
        base_details = super().get_details()  # Method Overriding
        return f"{base_details}, Programming Language: {self.__programming_language}"

    def calculate_bonus(self):
        return self._Employee__salary * 0.15  # 15% bonus for developers
    
class Designer(Employee):
    def __init__(self, name, emp_id, salary, design_tool):
        super().__init__(name, emp_id, salary)  # Inheritance
        self.__design_tool = design_tool  # Encapsulation: private attribute

    def get_details(self):
        base_details = super().get_details()  # Method Overriding
        return f"{base_details}, Design Tool: {self.__design_tool}"

    def calculate_bonus(self):
        return self._Employee__salary * 0.12  # 12% bonus for designers
    
# Example usage
if __name__ == "__main__":
    manager = Manager("Alice", 101, 80000, "HR")
    developer = Developer("Bob", 102, 70000, "Python")
    designer = Designer("Charlie", 103, 60000, "Photoshop")

    print(manager.get_details())
    print(f"Manager Bonus: {manager.calculate_bonus()}")

    print(developer.get_details())
    print(f"Developer Bonus: {developer.calculate_bonus()}")

    print(designer.get_details())
    print(f"Designer Bonus: {designer.calculate_bonus()}")