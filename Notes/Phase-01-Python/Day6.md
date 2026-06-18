# Day 6 - Conditional Statements in Python

## 📌 Overview

Conditional statements allow a program to make decisions based on different conditions. They help control the flow of execution by running specific blocks of code only when certain conditions are met.

Think of it like real life:

- If it is raining, take an umbrella.
- If your age is 18 or above, you can vote.
- If your exam score is above 90, you get an A grade.

Python uses:

- `if`
- `elif`
- `else`

to implement decision-making.

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand conditional statements
- Use `if`, `elif`, and `else`
- Write decision-making programs
- Use comparison operators
- Use logical operators
- Build small real-world projects

---

# 🔹 Why Conditional Statements Matter

Conditional statements are used everywhere:

- Login Systems
- ATM Machines
- E-commerce Websites
- AI Applications
- Chatbots
- Recommendation Systems

Without conditions, programs cannot make decisions.

---

# 📚 Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning | Example |
|-----------|---------|---------|
| == | Equal To | x == y |
| != | Not Equal To | x != y |
| > | Greater Than | x > y |
| < | Less Than | x < y |
| >= | Greater Than or Equal To | x >= y |
| <= | Less Than or Equal To | x <= y |

### Example

```python
age = 20

print(age > 18)
```

### Output

```python
True
```

---

# 🔹 The if Statement

The `if` statement executes a block of code only if the condition is True.

### Syntax

```python
if condition:
    # code block
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```python
You are eligible to vote.
```

---

# 🔹 The if-else Statement

If the condition is True, the `if` block executes.

Otherwise, the `else` block executes.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### Output

```python
Not eligible to vote
```

---

# 🔹 The if-elif-else Statement

Used when there are multiple conditions.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```

### Output

```python
Grade B
```

---

# 🔹 Nested if Statements

An `if` statement inside another `if` statement.

### Example

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
```

### Output

```python
You can drive.
```

---

# 🔹 Logical Operators

Logical operators combine multiple conditions.

## AND Operator

Returns True if both conditions are True.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

## OR Operator

Returns True if at least one condition is True.

```python
age = 16
special_permission = True

if age >= 18 or special_permission:
    print("Access Granted")
```

---

## NOT Operator

Reverses the result.

```python
is_logged_in = False

if not is_logged_in:
    print("Please Login")
```

---

# 🧠 Real-World Example 1: Voting Eligibility Checker

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

# 🧠 Real-World Example 2: Grade Calculator

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
```

---

# 🧠 Real-World Example 3: Login System

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

---

# 🚀 Hands-On Exercises

### Beginner

1. Check if a number is positive or negative.
2. Check if a number is even or odd.
3. Check if a person can vote.
4. Find the largest of two numbers.
5. Find the smallest of two numbers.

### Intermediate

6. Grade Calculator
7. BMI Category Checker
8. Login System
9. ATM Withdrawal Validation
10. Age Category Checker

### Advanced

11. Electricity Bill Calculator
12. Tax Calculator
13. Scholarship Eligibility Checker
14. Movie Ticket Pricing System
15. Student Result Management System

---

# 💼 Mini Project: Grade Calculator

### Requirements

- Take marks as input.
- Display grade.
- Handle invalid marks.

### Solution

```python
marks = int(input("Enter Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
```

---

# 🎤 Python Interview Questions

## Basic Level

### 1. What is a conditional statement?

A conditional statement allows a program to make decisions based on conditions.

---

### 2. What are the conditional statements available in Python?

- if
- if-else
- if-elif-else
- Nested if

---

### 3. What is the difference between if and if-else?

`if` executes code only when the condition is True.

`if-else` provides an alternative block when the condition is False.

---

### 4. What does elif mean?

`elif` stands for "else if" and is used to check multiple conditions.

---

### 5. What happens if multiple conditions are True?

Python executes only the first matching condition.

---

## Intermediate Level

### 6. What is a nested if statement?

An if statement inside another if statement.

---

### 7. What are logical operators?

Operators used to combine conditions:

- and
- or
- not

---

### 8. Difference between == and = ?

`=` is an assignment operator.

```python
x = 5
```

`==` is a comparison operator.

```python
x == 5
```

---

### 9. What is short-circuit evaluation?

Python stops evaluating conditions once the final result is known.

Example:

```python
True or some_expensive_function()
```

The function will not execute.

---

### 10. Can we use multiple elif statements?

Yes.

```python
if condition1:
    pass
elif condition2:
    pass
elif condition3:
    pass
else:
    pass
```

---

# 📝 Key Takeaways

✅ Conditional statements help programs make decisions.

✅ Python provides:

- if
- if-else
- if-elif-else
- nested if

✅ Comparison operators return True or False.

✅ Logical operators help combine conditions.

✅ Conditional statements are heavily used in real-world applications like authentication systems, AI applications, recommendation systems, and automation tools.

---

# 📅 Progress

- [x] Learned Conditional Statements
- [x] Practiced if, elif, else
- [x] Built Voting Eligibility Checker
- [x] Built Grade Calculator
- [x] Solved Practice Problems

**Day 6 Completed ✅**