# Day 14 - Object-Oriented Programming (OOP) in Python (Part 2)

> Phase 1: Programming Foundation  
> Roadmap: AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand advanced OOP concepts
- Understand Inheritance
- Understand Polymorphism
- Understand Encapsulation
- Understand Abstraction
- Apply OOP principles in real-world applications
- Build scalable and reusable code
- Solve OOP interview questions confidently

---

# 📌 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects and classes.

OOP helps developers:

- Reuse code
- Reduce duplication
- Improve maintainability
- Build scalable applications

---

# The Four Pillars of OOP

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction

These are the most important OOP concepts asked in interviews.

---

# 1️⃣ Inheritance

## What is Inheritance?

Inheritance allows one class to acquire properties and methods from another class.

### Benefits

- Code Reusability
- Easy Maintenance
- Faster Development

---

## Parent Class

```python
class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
```

---

## Child Class

```python
class Student(Person):

    def study(self):
        print(self.name, "is studying")
```

---

## Using Inheritance

```python
student = Student("John")

student.display()
student.study()
```

### Output

```text
Name: John
John is studying
```

---

# Types of Inheritance

## Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

## Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

## Hierarchical Inheritance

```python
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

---

## Multiple Inheritance

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

# Method Overriding

Child class modifies parent class method.

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

## Example

```python
dog = Dog()
dog.sound()
```

### Output

```text
Bark
```

---

# super() Function

Used to access parent class methods.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
```

---

# 2️⃣ Polymorphism

## What is Polymorphism?

Polymorphism means:

> One interface, many forms.

Different objects can use the same method name but behave differently.

---

## Example

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")
```

---

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

### Output

```text
Bark
Meow
```

---

# Real World Example

```python
class Payment:

    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")
```

---

```python
payments = [CreditCard(), UPI()]

for payment in payments:
    payment.pay()
```

---

# Method Overloading in Python

Python does not support traditional method overloading.

Instead use default arguments.

```python
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c
```

---

# 3️⃣ Encapsulation

## What is Encapsulation?

Encapsulation means:

> Wrapping data and methods together and restricting direct access.

---

# Why Encapsulation?

- Data Protection
- Security
- Better Control

---

# Public Variable

```python
class Student:

    def __init__(self):
        self.name = "John"
```

---

# Protected Variable

```python
class Student:

    def __init__(self):
        self._name = "John"
```

Convention only.

---

# Private Variable

```python
class Student:

    def __init__(self):
        self.__name = "John"
```

Cannot be directly accessed.

---

# Example

```python
student = Student()

print(student.__name)
```

### Output

```text
AttributeError
```

---

# Getter and Setter

```python
class Student:

    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```

---

## Using Getter and Setter

```python
student = Student()

student.set_name("John")

print(student.get_name())
```

---

# 4️⃣ Abstraction

## What is Abstraction?

Abstraction hides implementation details and shows only essential features.

---

# Real Life Example

Car Driver:

- Knows accelerator
- Knows brake

Doesn't know engine internals

---

# Abstract Class

Python provides:

```python
from abc import ABC, abstractmethod
```

---

## Example

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

## Child Class

```python
class Car(Vehicle):

    def start(self):
        print("Car Started")
```

---

## Using Abstract Class

```python
car = Car()

car.start()
```

### Output

```text
Car Started
```

---

# Why Abstraction?

- Simplifies code
- Hides complexity
- Improves security
- Better architecture

---

# Real World OOP Example

## Banking System

```python
from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SavingsAccount(Account):

    def withdraw(self):
        print("Money Withdrawn")
```

---

# Mini Project

# Employee Management System

---

## Requirements

- Add Employee
- Display Employee
- Use Inheritance
- Use Encapsulation
- Use Polymorphism

---

## Solution

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)


class Developer(Employee):

    def display(self):
        print("Developer Details")
        super().display()


class Manager(Employee):

    def display(self):
        print("Manager Details")
        super().display()


employees = [
    Developer("John", 50000),
    Manager("Alice", 80000)
]

for employee in employees:
    employee.display()
    print()
```

---

# OOP Comparison Table

| Concept | Purpose |
|----------|----------|
| Inheritance | Reuse code |
| Polymorphism | One interface many forms |
| Encapsulation | Protect data |
| Abstraction | Hide implementation |

---

# Practice Questions

## Easy

1. Create a Person class and Student class using inheritance.
2. Create a Vehicle class and Car class.
3. Override a method in child class.
4. Use super() function.
5. Create a protected variable.

---

## Medium

6. Create BankAccount using encapsulation.
7. Create Employee hierarchy.
8. Create Shape polymorphism example.
9. Implement getter and setter.
10. Create abstract Vehicle class.

---

## Advanced

11. Build Library Management System.
12. Build Student Management System.
13. Build ATM System.
14. Build Hospital Management System.
15. Build Employee Management System.

---

# Interview Questions

# Beginner Level

## 1. What is OOP?

OOP is a programming paradigm that organizes code using classes and objects.

---

## 2. What are the four pillars of OOP?

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction

---

## 3. What is Inheritance?

Inheritance allows one class to acquire properties and methods from another class.

---

## 4. What is Polymorphism?

Polymorphism means one interface can have multiple implementations.

---

## 5. What is Encapsulation?

Encapsulation wraps data and methods together while restricting direct access.

---

## 6. What is Abstraction?

Abstraction hides implementation details and exposes only essential features.

---

## 7. What is Method Overriding?

A child class provides its own implementation of a parent class method.

---

## 8. What is super()?

super() is used to access parent class methods and constructors.

---

## 9. Difference between Class and Object?

| Class | Object |
|---------|---------|
| Blueprint | Real instance |
| Defines structure | Uses structure |

---

## 10. Why use OOP?

- Reusability
- Scalability
- Maintainability
- Security

---

# Intermediate Level

## 11. Difference between Inheritance and Composition?

Inheritance creates an "is-a" relationship.

Composition creates a "has-a" relationship.

---

## 12. What is Multiple Inheritance?

A class inherits from multiple parent classes.

---

## 13. What is Method Resolution Order (MRO)?

The order Python follows to find methods in inheritance hierarchy.

---

## 14. What is Name Mangling?

Python changes private variable names internally.

Example:

```python
self.__name
```

becomes

```python
self._ClassName__name
```

---

## 15. What are Getter and Setter methods?

Methods used to access and modify private data safely.

---

# Advanced Level

## 16. What is an Abstract Class?

A class that cannot be instantiated and contains abstract methods.

---

## 17. What is an Abstract Method?

A method declared but not implemented in parent class.

---

## 18. Difference between Abstraction and Encapsulation?

| Abstraction | Encapsulation |
|-------------|---------------|
| Hides complexity | Hides data |
| Design level | Implementation level |

---

## 19. Why is OOP important for large applications?

Because it provides:

- Modular code
- Reusability
- Maintainability
- Scalability

---

## 20. Which OOP pillar is most important?

All four pillars work together to create robust software systems.

---

# Real Interview Questions

### Q1: Explain the four pillars of OOP with examples.

### Q2: What is the difference between method overloading and overriding?

### Q3: How does Python implement encapsulation?

### Q4: What is MRO in Python?

### Q5: Explain abstraction using a real-world example.

### Q6: What is the purpose of abstract classes?

### Q7: Difference between protected and private variables?

### Q8: What is the diamond problem?

### Q9: What is polymorphism in Python?

### Q10: Explain super() with example.

---

# Day 14 Summary

Today you learned:

✅ Inheritance

✅ Types of Inheritance

✅ Method Overriding

✅ super()

✅ Polymorphism

✅ Encapsulation

✅ Getter and Setter

✅ Private Variables

✅ Abstraction

✅ Abstract Classes

✅ Employee Management System Project

✅ OOP Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 14: Mastered Advanced OOP Concepts in Python"
git push origin main
```

---

# 🚀 Next Day

**Day 15: File Handling in Python**

Topics:

- Opening Files
- Reading Files
- Writing Files
- Appending Files
- File Modes
- Working with Text Files
- Notes Management Project