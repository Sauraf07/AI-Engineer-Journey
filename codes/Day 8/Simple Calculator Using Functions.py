'''Task 1: Simple Calculator Using Functions

Concepts Covered:

Function definition
Parameters
Return values

Requirements:
Create functions for:

Addition
Subtraction
Multiplication
Division'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
# Example usage:
num1 = 10
num2 = 5
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
