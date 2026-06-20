# Day 11 – Python Modules & Packages

> Part of AI/ML Engineer Roadmap – Phase 1: Programming Foundation

---

# 🎯 Learning Objectives

By the end of Day 11, you will be able to:

- Understand what Python modules are
- Import and use built-in modules
- Create custom modules
- Understand packages in Python
- Use the `math`, `random`, `datetime`, and `os` modules
- Organize Python code professionally
- Build a Random Password Generator project
- Answer common Python module interview questions

---

# 📌 What is a Module?

A module is a Python file containing variables, functions, and classes that can be reused in other programs.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

You can use it in another file:

```python
import calculator

result = calculator.add(5, 3)
print(result)
```

Output:

```text
8
```

---

# Why Modules Matter

Without modules:

```python
# Everything in one file
```

With modules:

```python
project/
│
├── main.py
├── database.py
├── auth.py
├── utils.py
```

Benefits:

- Reusability
- Better organization
- Easy maintenance
- Cleaner code
- Industry standard practice

---

# Types of Modules

## 1. Built-in Modules

Provided by Python.

Examples:

- math
- random
- datetime
- os
- sys
- json

---

## 2. User Defined Modules

Created by developers.

Example:

```python
# greetings.py

def hello():
    print("Hello World")
```

Import:

```python
import greetings

greetings.hello()
```

---

# Importing Modules

---

## Import Entire Module

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

## Import Specific Function

```python
from math import sqrt

print(sqrt(49))
```

Output:

```text
7.0
```

---

## Import Multiple Functions

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))
```

Output:

```text
4.0
120
```

---

## Import with Alias

```python
import math as m

print(m.pi)
```

Output:

```text
3.141592653589793
```

---

# The Math Module

Used for mathematical operations.

Import:

```python
import math
```

---

## Square Root

```python
print(math.sqrt(64))
```

Output:

```text
8.0
```

---

## Power

```python
print(math.pow(2, 3))
```

Output:

```text
8.0
```

---

## Pi Value

```python
print(math.pi)
```

Output:

```text
3.141592653589793
```

---

## Factorial

```python
print(math.factorial(5))
```

Output:

```text
120
```

---

# The Random Module

Used for generating random values.

Import:

```python
import random
```

---

## Random Number

```python
print(random.randint(1, 10))
```

Output:

```text
7
```

(Random every time)

---

## Random Choice

```python
colors = ["red", "blue", "green"]

print(random.choice(colors))
```

Output:

```text
blue
```

---

## Shuffle List

```python
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

Output:

```text
[3, 1, 5, 2, 4]
```

(Random order)

---

# The Datetime Module

Used for date and time operations.

Import:

```python
from datetime import datetime
```

---

## Current Date and Time

```python
now = datetime.now()

print(now)
```

Output:

```text
2026-06-20 10:30:15
```

---

## Current Date

```python
print(now.date())
```

Output:

```text
2026-06-20
```

---

## Current Time

```python
print(now.time())
```

Output:

```text
10:30:15
```

---

# The OS Module

Used for interacting with the operating system.

Import:

```python
import os
```

---

## Current Working Directory

```python
print(os.getcwd())
```

Output:

```text
C:/Users/Student
```

---

## List Files

```python
print(os.listdir())
```

Output:

```text
['main.py', 'notes.txt']
```

---

## Create Folder

```python
os.mkdir("test_folder")
```

---

# Creating Your Own Module

---

## Step 1

Create file:

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

## Step 2

Create another file:

```python
# main.py

import calculator

print(calculator.add(10, 5))
```

Output:

```text
15
```

---

# Packages in Python

A package is a collection of modules.

Example:

```text
project/
│
├── package/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
│
└── main.py
```

---

# Difference Between Module and Package

| Module | Package |
|----------|----------|
| Single Python file | Collection of modules |
| .py file | Directory |
| Contains functions/classes | Contains modules |

Example:

```text
calculator.py
```

Module

Example:

```text
utils/
    calculator.py
    database.py
```

Package

---

# Best Practices

✅ Use meaningful module names

```python
database.py
auth.py
```

---

✅ Avoid large files

Bad:

```python
5000 lines in one file
```

Good:

```python
auth.py
database.py
utils.py
```

---

✅ Reuse code

Don't copy-paste functions repeatedly.

Use modules.

---

# Mini Project: Random Password Generator

---

## Problem Statement

Generate secure random passwords using:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

---

## Solution

```python
import random
import string

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:")
print(password)
```

---

## Sample Output

```text
Enter password length: 12

Generated Password:
aD@7k#P9!xLm
```

---

# Practice Questions

## Easy

1. Import math module and find square root of 144.
2. Generate random number between 1 and 100.
3. Print current date.
4. Print current working directory.
5. Create a custom module.

---

## Medium

1. Dice Simulator
2. OTP Generator
3. Random Quote Generator
4. Birthday Countdown
5. Number Guessing Game using modules

---

# Interview Questions

## Beginner Level

### 1. What is a Python module?

A module is a Python file containing reusable code such as functions, variables, and classes.

---

### 2. Why are modules used?

- Reusability
- Organization
- Maintainability
- Code sharing

---

### 3. What is the difference between a module and a package?

| Module | Package |
|----------|----------|
| Single file | Collection of modules |

---

### 4. How do you import a module?

```python
import math
```

---

### 5. How do you import a specific function?

```python
from math import sqrt
```

---

### 6. What is aliasing?

```python
import numpy as np
```

Using a shorter name for a module.

---

### 7. What are built-in modules?

Modules provided by Python.

Examples:

- math
- random
- os
- datetime

---

### 8. What is the purpose of __init__.py?

It tells Python that a directory should be treated as a package.

---

### 9. What is sys.path?

A list of directories Python searches when importing modules.

---

### 10. What happens if Python cannot find a module?

It raises:

```python
ModuleNotFoundError
```

---

# Advanced Interview Questions

### 11. Difference between import and from import?

```python
import math
math.sqrt(25)
```

vs

```python
from math import sqrt
sqrt(25)
```

---

### 12. What is namespace in Python?

A namespace is a container that maps names to objects.

---

### 13. What is module caching?

Python loads a module once and stores it in memory for future use.

---

### 14. How can you reload a module?

```python
import importlib

importlib.reload(module_name)
```

---

### 15. Explain circular imports.

When two modules import each other causing dependency issues.

Example:

```python
a.py imports b.py
b.py imports a.py
```

---

# Day 11 Assignment

Build and upload the following:

### Project 1

Random Password Generator

---

### Project 2

OTP Generator

Features:

- Generate 6-digit OTP
- Generate 4-digit OTP
- Regenerate OTP

---

### Project 3

Custom Calculator Module

Files:

```text
calculator_project/
│
├── calculator.py
└── main.py
```

Functions:

- add()
- subtract()
- multiply()
- divide()

---

# GitHub Repository Structure

```text
Day-11-Python-Modules/
│
├── random_password_generator.py
├── otp_generator.py
├── calculator.py
├── main.py
└── README.md
```

---

# Day 11 Completion Checklist

- [ ] Understand modules
- [ ] Understand packages
- [ ] Use math module
- [ ] Use random module
- [ ] Use datetime module
- [ ] Use os module
- [ ] Create custom module
- [ ] Complete password generator project
- [ ] Solve practice questions
- [ ] Upload code to GitHub

---

# Next Day

➡️ Day 12: Exception Handling (try, except, finally, custom exceptions, real-world error handling, and production-grade Python practices)