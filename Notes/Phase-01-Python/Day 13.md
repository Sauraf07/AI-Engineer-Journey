# Day 13 - Object-Oriented Programming (OOP) in Python (Part 1)

> Phase 1: Programming Foundation
>
> Roadmap: AI/ML Engineer → GenAI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand Object-Oriented Programming (OOP)
- Create Classes and Objects
- Use Constructors (`__init__`)
- Understand Instance Variables
- Create Methods
- Work with Multiple Objects
- Build Real-World OOP Applications
- Create a Student Management System
- Answer OOP Interview Questions confidently

---

# 📌 What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **Objects** and **Classes**.

Instead of writing everything in functions, OOP helps us model real-world entities.

Examples:

| Real World | OOP |
|------------|-----|
| Student | Student Class |
| Car | Car Class |
| Employee | Employee Class |
| Bank Account | BankAccount Class |

---

# Why OOP Matters

As applications grow larger, managing code becomes difficult.

OOP helps by providing:

✅ Reusability

✅ Maintainability

✅ Scalability

✅ Better Organization

✅ Real-World Modeling

---

# Real World Example

Imagine a College Management System.

Every student has:

- Name
- Age
- Course
- Roll Number

Instead of creating separate variables:

```python
student1_name = "John"
student1_age = 20

student2_name = "Mike"
student2_age = 21
```

We use OOP:

```python
class Student:
    pass
```

And create multiple student objects.

---

# What is a Class?

A Class is a blueprint for creating objects.

Think of it as a design or template.

Example:

```python
class Student:
    pass
```

Here:

```text
Student
```

is a class.

---

# What is an Object?

An Object is an instance of a class.

Example:

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

Here:

```text
student1
student2
```

are objects.

---

# Creating a Simple Class

```python
class Student:
    pass
```

Creating Object:

```python
student = Student()

print(student)
```

Output:

```text
<__main__.Student object at 0x000001>
```

---

# Class with Attributes

```python
class Student:
    name = "John"
    age = 20

student = Student()

print(student.name)
print(student.age)
```

Output:

```text
John
20
```

---

# Understanding Constructors

A Constructor initializes object data automatically.

Python Constructor:

```python
__init__()
```

runs automatically when an object is created.

---

# Constructor Syntax

```python
class Student:

    def __init__(self):
        print("Object Created")
```

Creating Object:

```python
student = Student()
```

Output:

```text
Object Created
```

---

# Understanding self

`self` refers to the current object.

Example:

```python
class Student:

    def __init__(self):
        print(self)
```

```python
student = Student()
```

Output:

```text
<__main__.Student object>
```

---

# Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

Creating Object:

```python
student = Student("John", 20)

print(student.name)
print(student.age)
```

Output:

```text
John
20
```

---

# Instance Variables

Variables belonging to an object are called Instance Variables.

Example:

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

Instance Variables:

```python
self.name
self.age
```

---

# Creating Multiple Objects

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

```python
student1 = Student("John", 20)
student2 = Student("Mike", 21)

print(student1.name)
print(student2.name)
```

Output:

```text
John
Mike
```

---

# Methods in Python Classes

Methods are functions inside a class.

Example:

```python
class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Name:", self.name)
```

Creating Object:

```python
student = Student("John")

student.display()
```

Output:

```text
Name: John
```

---

# Multiple Methods Example

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print(self.name)
        print(self.age)

    def greet(self):

        print("Welcome", self.name)
```

```python
student = Student("John", 20)

student.display()
student.greet()
```

---

# Practical Example 1

## Employee Class

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display(self):

        print("Name:", self.name)
        print("Salary:", self.salary)
```

```python
emp1 = Employee("Rahul", 50000)

emp1.display()
```

---

# Practical Example 2

## Car Class

```python
class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def show(self):

        print(self.brand, self.model)
```

```python
car1 = Car("Toyota", "Fortuner")

car1.show()
```

Output:

```text
Toyota Fortuner
```

---

# Practical Example 3

## Bank Account

```python
class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def display(self):

        print("Balance:", self.balance)
```

```python
account = BankAccount("John", 1000)

account.deposit(500)

account.display()
```

Output:

```text
Balance: 1500
```

---

# Mini Project

# Student Management System

---

## Requirements

- Add Student
- Display Student
- Store Name
- Store Age
- Store Course

---

## Solution

```python
class Student:

    def __init__(self, name, age, course):

        self.name = name
        self.age = age
        self.course = course

    def display(self):

        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


students = []

while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Choose Option: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = Student(name, age, course)

        students.append(student)

        print("Student Added Successfully")

    elif choice == "2":

        for student in students:
            student.display()

    elif choice == "3":

        print("Goodbye")
        break

    else:
        print("Invalid Choice")
```

---

# Practice Questions

## Easy

1. Create a Student class.
2. Create an Employee class.
3. Create a Car class.
4. Create a Book class.
5. Create a Mobile class.

---

## Medium

6. Create a Bank Account class.
7. Create a Product class.
8. Create a Movie class.
9. Create a Library System.
10. Create a Hospital Management System.

---

## Advanced

11. Create Inventory System.
12. Create Student Management System.
13. Create Hotel Booking System.
14. Create Banking System.
15. Create Shopping Cart System.

---

# Real World Use Cases

## E-Commerce

```text
Product Class
Customer Class
Order Class
```

---

## Banking

```text
Account Class
Transaction Class
Customer Class
```

---

## School Management

```text
Student Class
Teacher Class
Course Class
```

---

## Hospital Management

```text
Doctor Class
Patient Class
Appointment Class
```

---

# Interview Questions

# Beginner Level

### 1. What is OOP?

OOP (Object-Oriented Programming) is a programming paradigm based on classes and objects.

---

### 2. What is a Class?

A blueprint used to create objects.

---

### 3. What is an Object?

An instance of a class.

---

### 4. What is Constructor?

A special method automatically called when an object is created.

```python
def __init__(self):
```

---

### 5. What is self?

Represents the current object.

---

### 6. Why do we use self?

To access instance variables and methods.

---

### 7. What are Instance Variables?

Variables that belong to an object.

Example:

```python
self.name
```

---

### 8. Can a class have multiple objects?

Yes.

---

### 9. Can an object access class methods?

Yes.

Example:

```python
student.display()
```

---

### 10. What is a Method?

A function inside a class.

---

# Intermediate Level

### 11. Difference between Class and Object?

| Class | Object |
|---------|---------|
| Blueprint | Instance |
| Template | Real Entity |

---

### 12. Difference between Function and Method?

| Function | Method |
|-----------|---------|
| Independent | Inside Class |

---

### 13. What happens when object is created?

Constructor executes automatically.

---

### 14. Can we create object without constructor?

Yes.

---

### 15. Can a constructor return value?

No.

---

# Advanced Level

### 16. Can a class have multiple constructors?

Python does not support multiple constructors directly.

---

### 17. What is Object Instantiation?

Creating an object from a class.

---

### 18. What is Namespace?

Area where variables are stored and managed.

---

### 19. What are Object Attributes?

Variables belonging to an object.

---

### 20. Why is OOP important?

Because it improves:

- Reusability
- Scalability
- Maintainability
- Code Organization

---

# OOP Best Practices

✅ Use meaningful class names

✅ Use constructors for initialization

✅ Keep methods focused

✅ Follow Single Responsibility Principle

✅ Create reusable classes

✅ Avoid unnecessary global variables

---

# Day 13 Summary

Today you learned:

- Object-Oriented Programming
- Classes
- Objects
- Constructors
- self keyword
- Instance Variables
- Methods
- Creating Multiple Objects
- Student Management System Project
- OOP Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 13: Learned OOP Basics, Classes, Objects and Student Management System"
git push origin main
```

---

# 🚀 Next Day

## Day 14: OOP Part 2

Topics:

- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Method Overriding
- Method Resolution Order (MRO)
- Real World OOP Projects