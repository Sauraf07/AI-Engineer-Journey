'''Task 5: Mini Project — Student Result System
Requirements

Create a Student class.

Attributes
name
roll_no
marks1
marks2
marks3
Methods
calculate_total()
calculate_average()
calculate_grade()
display_result()'''

class Student:
    def __init__(self, name, roll_no, marks1, marks2, marks3):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3
    
    def calculate_average(self):
        total = self.calculate_total()
        return total / 3
    
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    def display_result(self):
        total = self.calculate_total()
        average = self.calculate_average()
        grade = self.calculate_grade()
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks1}, {self.marks2}, {self.marks3}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
# Example usage
student1 = Student("Alice", "101", 85, 92, 78)
student1.display_result()

