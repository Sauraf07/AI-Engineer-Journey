# Day 9 – Advanced Functions in Python (`*args`, `**kwargs`, Lambda Functions)

> Part of My AI/ML & Generative AI Engineering Journey 🚀

---

# 📌 Day 9 Goals

By the end of this lesson, you will be able to:

- Understand Python Functions deeply
- Use `*args` for variable positional arguments
- Use `**kwargs` for variable keyword arguments
- Create anonymous functions using `lambda`
- Know when to use normal functions vs lambda functions
- Solve real-world problems using advanced functions
- Answer common Python interview questions

---

# Why Learn Advanced Functions?

Functions are one of the most important concepts in Python.

In real-world applications, functions help:

- Reduce code duplication
- Improve code readability
- Improve code reusability
- Organize large projects
- Build scalable applications

Advanced functions are heavily used in:

- Data Science
- Machine Learning
- Backend Development
- Automation Scripts
- APIs
- AI Engineering

---

# 1. Functions Recap

A function is a block of reusable code that performs a specific task.

## Syntax

```python
def greet():
    print("Hello World")
```

## Example

```python
def greet():
    print("Welcome to Python")

greet()
```

### Output

```text
Welcome to Python
```

---

# 2. Function with Parameters

Parameters allow functions to accept input values.

## Example

```python
def greet(name):
    print("Hello", name)

greet("Sauraf")
```

### Output

```text
Hello Sauraf
```

---

# 3. Function with Return Value

Functions can return values using the `return` keyword.

## Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Output

```text
30
```

---

# 4. What is *args?

Sometimes we don't know how many arguments will be passed to a function.

Python provides `*args`.

`*args` allows multiple positional arguments.

---

## Example 1

```python
def numbers(*args):
    print(args)

numbers(1, 2, 3, 4)
```

### Output

```text
(1, 2, 3, 4)
```

Notice:

`args` becomes a tuple.

---

## Example 2

```python
def total(*args):
    return sum(args)

print(total(10, 20))
print(total(10, 20, 30))
print(total(10, 20, 30, 40))
```

### Output

```text
30
60
100
```

---

# Real-Life Example of *args

Imagine a shopping cart.

Different customers buy different numbers of items.

```python
def cart_total(*prices):
    return sum(prices)

print(cart_total(100, 200))
print(cart_total(100, 200, 300))
```

### Output

```text
300
600
```

---

# 5. What is **kwargs?

`**kwargs` allows multiple keyword arguments.

It stores data in dictionary format.

---

## Example

```python
def student(**kwargs):
    print(kwargs)

student(
    name="Sauraf",
    age=21,
    city="Indore"
)
```

### Output

```python
{
    'name': 'Sauraf',
    'age': 21,
    'city': 'Indore'
}
```

---

# Accessing kwargs Values

```python
def student(**kwargs):

    for key, value in kwargs.items():
        print(key, value)

student(
    name="Sauraf",
    age=21,
    city="Indore"
)
```

### Output

```text
name Sauraf
age 21
city Indore
```

---

# Real-Life Example of kwargs

User registration form:

```python
def register_user(**user):

    print("User Details")

    for key, value in user.items():
        print(key, value)

register_user(
    username="sauraf123",
    email="abc@gmail.com",
    city="Indore"
)
```

---

# Difference Between *args and **kwargs

| Feature | *args | **kwargs |
|----------|--------|---------|
| Stores Data As | Tuple | Dictionary |
| Accepts | Positional Arguments | Keyword Arguments |
| Symbol | * | ** |
| Example | 10,20,30 | name="John" |

---

# Using *args and **kwargs Together

```python
def display(*args, **kwargs):

    print("Args:", args)
    print("Kwargs:", kwargs)

display(
    10,
    20,
    30,
    name="Sauraf",
    city="Indore"
)
```

### Output

```python
Args: (10, 20, 30)

Kwargs: {
    'name': 'Sauraf',
    'city': 'Indore'
}
```

---

# 6. Lambda Functions

A lambda function is a small anonymous function.

Anonymous means:

No function name.

---

## Normal Function

```python
def square(x):
    return x * x

print(square(5))
```

### Output

```text
25
```

---

## Lambda Version

```python
square = lambda x: x * x

print(square(5))
```

### Output

```text
25
```

---

# Lambda Function Syntax

```python
lambda arguments : expression
```

---

# Example 1

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```text
30
```

---

# Example 2

```python
multiply = lambda a, b: a * b

print(multiply(5, 6))
```

### Output

```text
30
```

---

# Example 3

Finding Larger Number

```python
largest = lambda a, b: a if a > b else b

print(largest(50, 100))
```

### Output

```text
100
```

---

# 7. Lambda with map()

Used to transform data.

## Example

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(
        lambda x: x*x,
        numbers
    )
)

print(squares)
```

### Output

```text
[1, 4, 9, 16, 25]
```

---

# 8. Lambda with filter()

Used to filter data.

## Example

```python
numbers = [1,2,3,4,5,6]

even = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(even)
```

### Output

```text
[2, 4, 6]
```

---

# 9. Lambda with sorted()

```python
students = [

    ("Rahul", 80),
    ("Aman", 95),
    ("Sauraf", 90)

]

students.sort(
    key=lambda x: x[1]
)

print(students)
```

### Output

```python
[
 ('Rahul', 80),
 ('Sauraf', 90),
 ('Aman', 95)
]
```

---

# Mini Project: Student Marks Analyzer

```python
def average(*marks):

    return sum(marks) / len(marks)

print(
    average(
        85,
        90,
        95,
        80
    )
)
```

### Output

```text
87.5
```

---

# Practice Questions

## Easy

1. Create a function that accepts unlimited numbers and returns their sum.
2. Create a function using kwargs to store employee information.
3. Create a lambda function for square.
4. Create a lambda function for cube.
5. Find largest of two numbers using lambda.

---

## Intermediate

6. Use map() with lambda to double all numbers.
7. Use filter() with lambda to find odd numbers.
8. Sort a list of tuples using lambda.
9. Build a student result calculator using args.
10. Build a registration form using kwargs.

---

# Interview Questions

## Beginner Level

### 1. What is a function?

A reusable block of code that performs a specific task.

---

### 2. What is the difference between parameter and argument?

Parameter → Variable in function definition.

Argument → Actual value passed to function.

---

### 3. What is return keyword?

Used to send a value back from a function.

---

### 4. What is *args?

Allows a function to accept multiple positional arguments.

---

### 5. What is **kwargs?

Allows a function to accept multiple keyword arguments.

---

### 6. What data type does args use?

Tuple.

---

### 7. What data type does kwargs use?

Dictionary.

---

### 8. What is a lambda function?

A small anonymous one-line function.

---

### 9. Why use lambda functions?

For short and simple operations.

---

### 10. Difference between function and method?

Function:
```python
print()
```

Method:
```python
name.upper()
```

---

# Frequently Asked Interview Questions

### Explain *args with example.

### Explain **kwargs with example.

### Difference between args and kwargs.

### What is lambda function?

### When should lambda be avoided?

### Can lambda contain multiple expressions?

Answer:
No.

### Difference between lambda and normal function.

### Why is lambda used with map() and filter()?

### What is anonymous function?

### Explain positional and keyword arguments.

---

# Day 9 Assignment

Build:

### Project 1

Student Result Analyzer

Features:

- Accept unlimited marks using args
- Calculate average
- Find highest marks

---

### Project 2

Employee Registration System

Features:

- Use kwargs
- Store employee details
- Display formatted output

---

### Project 3

Lambda Practice Suite

Create lambda functions for:

- Square
- Cube
- Addition
- Multiplication
- Largest Number

---

# Day 9 Summary

Today I Learned:

- Functions
- Return Values
- *args
- **kwargs
- Lambda Functions
- map()
- filter()
- sorted()
- Real-world use cases of advanced functions

These concepts are heavily used in:

- Machine Learning
- Data Science
- Backend Development
- FastAPI
- AI Engineering
- Generative AI Applications

✅ Day 9 Completed
🚀 Moving Towards AI/ML Engineer Roadmap