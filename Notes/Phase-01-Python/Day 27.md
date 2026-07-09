# Day 27 - Decorators in Python

> **Phase 1: Programming Foundation**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📚 Table of Contents

* Introduction
* Learning Objectives
* What are Decorators?
* Why Decorators Matter
* Functions as First-Class Objects
* Nested Functions
* Returning Functions
* Basic Decorator
* Using `@` Syntax
* Decorators with Arguments
* `*args` and `**kwargs`
* Multiple Decorators
* Built-in Decorators
* Practical Examples
* Mini Project
* Best Practices
* Common Mistakes
* Interview Questions
* Practice Problems
* Summary
* GitHub Commit Message

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Understand what decorators are
* Learn why decorators are used
* Create your own decorators
* Use the `@decorator` syntax
* Pass arguments to decorators
* Decorate functions with any number of parameters
* Chain multiple decorators
* Understand built-in decorators
* Apply decorators in real-world applications
* Answer decorator interview questions confidently

---

# 📌 What are Decorators?

A **Decorator** is a special function that **adds extra functionality to another function without changing its original code**.

Think of a decorator as a wrapper around a function.

Instead of modifying the original function, we wrap it with additional behavior.

---

# 🤔 Why Do We Need Decorators?

Suppose you have multiple functions and want to:

* Log function calls
* Measure execution time
* Check user authentication
* Validate input
* Retry failed operations

Instead of repeating the same code in every function, decorators allow you to write that logic once and reuse it.

---

# Real-Life Example

Imagine ordering a pizza.

Base Pizza 🍕

You can decorate it with:

* Cheese
* Extra Sauce
* Mushrooms
* Olives

The pizza stays the same, but additional features are added.

Decorators work in exactly the same way.

---

# Functions are First-Class Objects

In Python:

* Functions can be stored in variables
* Functions can be passed as arguments
* Functions can be returned from other functions

Example:

```python
def greet():
    print("Hello")

message = greet

message()
```

Output:

```text
Hello
```

---

# Nested Functions

Functions can exist inside other functions.

```python
def outer():

    def inner():
        print("Inside Inner Function")

    inner()

outer()
```

Output:

```text
Inside Inner Function
```

---

# Returning Functions

```python
def outer():

    def inner():
        print("Hello")

    return inner

greet = outer()

greet()
```

Output

```text
Hello
```

---

# Creating Your First Decorator

```python
def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper
```

---

# Decorating a Function

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper


def greet():
    print("Hello")


greet = decorator(greet)

greet()
```

Output

```text
Before
Hello
After
```

---

# Using @ Syntax

Python provides a cleaner way.

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()
```

Output

```text
Before
Hello
After
```

---

# Decorators with Arguments

```python
def decorator(func):

    def wrapper(name):
        print("Welcome")

        func(name)

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("John")
```

Output

```text
Welcome
Hello John
```

---

# Using *args and **kwargs

Best practice:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper
```

---

# Example

```python
@decorator
def add(a, b):
    return a + b

print(add(10, 20))
```

Output

```text
Function Started
Function Finished
30
```

---

# Multiple Decorators

```python
def decorator1(func):

    def wrapper():
        print("Decorator 1")
        func()

    return wrapper


def decorator2(func):

    def wrapper():
        print("Decorator 2")
        func()

    return wrapper


@decorator1
@decorator2
def hello():
    print("Hello")


hello()
```

Output

```text
Decorator 1
Decorator 2
Hello
```

---

# Built-in Decorators

Python provides useful decorators.

## @staticmethod

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))
```

---

## @classmethod

```python
class Student:

    count = 0

    @classmethod
    def increase(cls):
        cls.count += 1

Student.increase()

print(Student.count)
```

---

## @property

```python
class Student:

    def __init__(self):
        self._age = 20

    @property
    def age(self):
        return self._age

student = Student()

print(student.age)
```

---

# Real-World Example 1

## Logging Decorator

```python
def logger(func):

    def wrapper(*args, **kwargs):

        print("Function Executed")

        return func(*args, **kwargs)

    return wrapper


@logger
def login():

    print("User Logged In")


login()
```

---

# Real-World Example 2

## Execution Time Decorator

```python
import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


@timer
def task():

    for i in range(1000000):
        pass

task()
```

---

# Real-World Example 3

## Authentication Decorator

```python
is_logged_in = True

def authenticate(func):

    def wrapper():

        if is_logged_in:
            func()
        else:
            print("Access Denied")

    return wrapper


@authenticate
def dashboard():
    print("Welcome to Dashboard")

dashboard()
```

---

# Mini Project

## Function Call Logger

### Features

* Log every function execution
* Display function name
* Display arguments
* Display returned value

```python
def logger(func):

    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")
        print("Arguments:", args)

        result = func(*args, **kwargs)

        print("Returned:", result)

        return result

    return wrapper


@logger
def multiply(a, b):
    return a * b


multiply(5, 8)
```

---

# Best Practices

* Use decorators for reusable functionality.
* Keep decorators simple and focused.
* Use `*args` and `**kwargs` for flexibility.
* Preserve function metadata with `functools.wraps`.
* Avoid excessive decorator nesting.

---

# Common Mistakes

❌ Forgetting to return the wrapper function

❌ Forgetting to call the original function

❌ Not handling function arguments

❌ Losing original function metadata

---

# Practice Problems

### Easy

1. Create a decorator that prints "Welcome".
2. Create a decorator that prints function name.
3. Decorate a calculator function.
4. Decorate a greeting function.
5. Decorate a multiplication function.

---

### Medium

6. Execution time decorator.
7. Authentication decorator.
8. Logging decorator.
9. Input validation decorator.
10. Retry decorator.

---

### Advanced

11. Decorator with parameters.
12. Multiple decorators.
13. API request logger.
14. Database connection decorator.
15. Exception handling decorator.

---

# Interview Questions

## Beginner

### 1. What is a decorator?

A decorator is a function that adds extra functionality to another function without modifying its original code.

---

### 2. Why are decorators used?

To reuse common functionality like logging, authentication, timing, caching, and validation.

---

### 3. What does the `@` symbol do?

It is syntactic sugar for applying a decorator to a function.

---

### 4. Can decorators accept arguments?

Yes.

---

### 5. Why use `*args` and `**kwargs` in decorators?

To support functions with any number of positional and keyword arguments.

---

## Intermediate

### 6. What are built-in decorators?

Examples include:

* `@staticmethod`
* `@classmethod`
* `@property`

---

### 7. How do multiple decorators execute?

They execute from the bottom decorator upward.

---

### 8. What is `functools.wraps`?

It preserves the original function's metadata, such as its name and documentation.

---

### 9. What are common use cases?

* Authentication
* Logging
* Timing
* Caching
* Validation
* Authorization

---

### 10. Can classes be used as decorators?

Yes, by implementing the `__call__()` method.

---

# Assignment

Build a **Simple Authentication System** using decorators.

### Requirements

* Login check
* Admin check
* Logging
* Error handling
* Multiple users

---

# 🎯 Day 27 Summary

Today you learned:

* Decorators
* Wrapper Functions
* `@` Syntax
* Decorators with Arguments
* `*args` and `**kwargs`
* Multiple Decorators
* Built-in Decorators
* Logging
* Authentication
* Execution Time Measurement
* Real-World Use Cases

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 27: Learned Python Decorators with Real-World Examples and Mini Project"
git push origin main
```

---

# 🚀 Next Day

**Day 28 – Virtual Environments & Package Management**

Topics:

* What is a Virtual Environment?
* Creating a Virtual Environment
* Activating and Deactivating `venv`
* Installing Packages with `pip`
* Managing Dependencies
* `requirements.txt`
* Building Reproducible Python Projects
