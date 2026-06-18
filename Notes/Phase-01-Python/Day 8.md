# Day 8 - Python Functions 🚀

## Overview

Functions are one of the most important concepts in Python. They help us write reusable, organized, and efficient code. Instead of writing the same code multiple times, we can place it inside a function and call it whenever needed.

In real-world software development, functions are used everywhere—from simple calculations to complex AI/ML applications.

---

# What You Will Learn

- What are Functions?
- Why Functions are Important?
- Creating Functions
- Function Parameters
- Return Statement
- Default Parameters
- Keyword Arguments
- Variable Scope
- Built-in Functions
- Practical Examples
- Mini Project
- Interview Questions

---

# What is a Function?

A function is a block of reusable code that performs a specific task.

### Syntax

```python
def function_name():
    # code block
```

### Example

```python
def greet():
    print("Hello World!")

greet()
```

### Output

```text
Hello World!
```

---

# Why Use Functions?

Without functions:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With functions:

```python
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()
```

### Benefits

- Code Reusability
- Better Readability
- Easier Maintenance
- Reduced Errors
- Modular Programming

---

# Function with Parameters

Parameters allow us to pass data into functions.

### Example

```python
def greet(name):
    print(f"Hello {name}")

greet("Gaurav")
```

### Output

```text
Hello Gaurav
```

---

# Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Output

```text
30
```

---

# Return Statement

The return statement sends a value back from a function.

### Example

```python
def add(a, b):
    return a + b

result = add(5, 10)

print(result)
```

### Output

```text
15
```

---

# Difference Between print() and return

### Using print()

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

### Using return()

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# Default Parameters

Default values are used if no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Gaurav")
```

### Output

```text
Hello Guest
Hello Gaurav
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=20, name="Gaurav")
```

### Output

```text
Gaurav
20
```

---

# Variable Scope

## Local Variable

A variable created inside a function.

```python
def demo():
    x = 100
    print(x)

demo()
```

---

## Global Variable

A variable created outside a function.

```python
x = 500

def demo():
    print(x)

demo()
```

Output:

```text
500
```

---

# Built-in Functions

Python provides many built-in functions.

### Examples

```python
print()
len()
max()
min()
sum()
type()
input()
```

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

Output:

```text
3
30
10
60
```

---

# Real-World Example 1: Area of Rectangle

```python
def area(length, width):
    return length * width

result = area(10, 5)

print("Area:", result)
```

Output:

```text
Area: 50
```

---

# Real-World Example 2: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))
```

Output:

```text
77.0
```

---

# Real-World Example 3: Simple Calculator

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
```

Output:

```text
15
5
50
2.0
```

---

# Mini Project: Student Result Calculator

```python
def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

student_marks = [80, 75, 90, 85, 88]

result = calculate_percentage(student_marks)

print("Percentage:", result)
```

### Output

```text
Percentage: 83.6
```

---

# Practice Questions

## Easy

1. Create a function that prints your name.
2. Create a function that adds two numbers.
3. Create a function that finds the square of a number.
4. Create a function that checks whether a number is even or odd.
5. Create a function that finds the maximum of two numbers.

---

## Medium

1. Create a function that calculates the area of a circle.
2. Create a function that counts vowels in a string.
3. Create a function that checks palindrome strings.
4. Create a function that finds factorial using functions.
5. Create a function that calculates student grades.

---

## Challenge

Build a complete calculator using functions.

Operations:

- Addition
- Subtraction
- Multiplication
- Division
- Exit

---

# Interview Questions and Answers

## 1. What is a Function in Python?

A function is a reusable block of code that performs a specific task.

Example:

```python
def greet():
    print("Hello")
```

---

## 2. Why Do We Use Functions?

- Reusability
- Better Readability
- Reduced Code Duplication
- Easier Maintenance

---

## 3. Difference Between Parameter and Argument?

Parameter:

```python
def greet(name):
```

Argument:

```python
greet("Gaurav")
```

Here:

- name → Parameter
- Gaurav → Argument

---

## 4. What is the Return Statement?

The return statement sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b
```

---

## 5. Difference Between print() and return()?

| print() | return() |
|----------|----------|
| Displays output | Sends value back |
| Cannot be reused | Can be stored and reused |
| Used for debugging | Used in real applications |

---

## 6. What are Default Parameters?

Parameters that already have predefined values.

Example:

```python
def greet(name="Guest"):
    print(name)
```

---

## 7. What are Keyword Arguments?

Arguments passed using parameter names.

```python
student(age=20, name="Gaurav")
```

---

## 8. What is Variable Scope?

Scope defines where a variable can be accessed.

Types:

- Local Scope
- Global Scope

---

## 9. What are Built-in Functions?

Functions already provided by Python.

Examples:

```python
len()
max()
min()
sum()
type()
```

---

## 10. Can a Function Return Multiple Values?

Yes.

Example:

```python
def data():
    return 10, 20

a, b = data()
```

---

# Assignment

Build the following projects:

### Project 1

Student Grade Calculator

Features:

- Input Marks
- Calculate Percentage
- Display Grade

### Project 2

Simple Calculator

Features:

- Add
- Subtract
- Multiply
- Divide

### Project 3

Temperature Converter

Features:

- Celsius to Fahrenheit
- Fahrenheit to Celsius

---

# Day 8 Summary

Today you learned:

✅ Functions  
✅ Parameters  
✅ Arguments  
✅ Return Statement  
✅ Default Parameters  
✅ Keyword Arguments  
✅ Variable Scope  
✅ Built-in Functions  
✅ Real-World Examples  
✅ Mini Project  
✅ Interview Questions

---

### GitHub Repository Structure

```text
Day-08-Functions/
│
├── examples/
│   ├── basic_function.py
│   ├── parameters.py
│   ├── return_statement.py
│   ├── default_parameters.py
│
├── projects/
│   ├── calculator.py
│   ├── grade_calculator.py
│   ├── temperature_converter.py
│
└── README.md
```

### Next Topic

➡️ Day 9: Advanced Functions (*args, **kwargs, Lambda Functions)