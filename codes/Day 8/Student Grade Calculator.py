'''Task 2: Student Grade Calculator

Concepts Covered:

Functions
Conditional Statements

Requirements:
Create a function:'''
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Example usage:
student_score = 85
grade = calculate_grade(student_score)
print(f"The student's grade is: {grade}")
