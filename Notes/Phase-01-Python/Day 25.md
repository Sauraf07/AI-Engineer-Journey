# Day 25 - List Comprehensions in Python

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📚 Table of Contents

- Introduction
- Learning Objectives
- What is List Comprehension?
- Why Use List Comprehensions?
- Syntax
- Basic Examples
- List Comprehension with Conditions
- Nested List Comprehensions
- Using Functions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Expressions
- Performance Comparison
- Best Practices
- Real-World Use Cases
- Mini Project
- Practice Problems
- Interview Questions
- Summary
- Resources

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand list comprehensions
- Write clean and concise Python code
- Replace traditional loops with comprehensions
- Apply filtering conditions
- Create nested comprehensions
- Understand dictionary and set comprehensions
- Learn generator expressions
- Improve code readability and performance

---

# 📌 What is a List Comprehension?

A **List Comprehension** is a concise way to create lists in Python using a single line of code.

Instead of writing multiple lines with a loop, you can generate a list more efficiently.

---

# Traditional Way

```python
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
```

### Output

```text
[0, 1, 2, 3, 4]
```

---

# Using List Comprehension

```python
numbers = [i for i in range(5)]

print(numbers)
```

### Output

```text
[0, 1, 2, 3, 4]
```

---

# Why Use List Comprehensions?

✅ Less code

✅ Faster execution

✅ Better readability

✅ Pythonic style

---

# Syntax

```python
new_list = [expression for item in iterable]
```

---

# Example 1: Squares of Numbers

Traditional:

```python
squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares)
```

Using List Comprehension:

```python
squares = [i * i for i in range(1, 6)]

print(squares)
```

Output

```text
[1, 4, 9, 16, 25]
```

---

# Example 2: Cube of Numbers

```python
cubes = [i ** 3 for i in range(1, 6)]

print(cubes)
```

Output

```text
[1, 8, 27, 64, 125]
```

---

# Example 3: Convert Strings to Uppercase

```python
names = ["alice", "bob", "john"]

uppercase = [name.upper() for name in names]

print(uppercase)
```

Output

```text
['ALICE', 'BOB', 'JOHN']
```

---

# List Comprehension with Conditions

Syntax

```python
[expression for item in iterable if condition]
```

---

# Example 4: Even Numbers

```python
even = [i for i in range(20) if i % 2 == 0]

print(even)
```

Output

```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

# Example 5: Odd Numbers

```python
odd = [i for i in range(20) if i % 2 != 0]

print(odd)
```

---

# Example 6: Numbers Greater Than 50

```python
numbers = [10, 25, 50, 60, 75, 90]

result = [num for num in numbers if num > 50]

print(result)
```

Output

```text
[60, 75, 90]
```

---

# If-Else in List Comprehension

Syntax

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

---

# Example 7

```python
numbers = [1, 2, 3, 4, 5]

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(labels)
```

Output

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Nested List Comprehensions

Example

```python
matrix = [[1,2],[3,4],[5,6]]

flatten = [item for row in matrix for item in row]

print(flatten)
```

Output

```text
[1, 2, 3, 4, 5, 6]
```

---

# Using Functions

```python
def square(x):
    return x*x

result = [square(i) for i in range(5)]

print(result)
```

---

# Dictionary Comprehension

Syntax

```python
{key:value for item in iterable}
```

Example

```python
numbers = {x: x*x for x in range(5)}

print(numbers)
```

Output

```text
{0:0,1:1,2:4,3:9,4:16}
```

---

# Set Comprehension

```python
numbers = {x*x for x in range(6)}

print(numbers)
```

---

# Generator Expression

Generator expressions are similar to list comprehensions but generate values one at a time.

```python
numbers = (x*x for x in range(5))

for i in numbers:
    print(i)
```

---

# List vs Generator

| Feature | List | Generator |
|----------|------|-----------|
| Memory | High | Low |
| Speed | Fast | Lazy Evaluation |
| Syntax | [] | () |

---

# Performance Comparison

Traditional Loop

```python
result = []

for i in range(100000):
    result.append(i)
```

List Comprehension

```python
result = [i for i in range(100000)]
```

List comprehensions are generally faster and more concise.

---

# Best Practices

✅ Keep comprehensions simple

✅ Use meaningful variable names

✅ Avoid deeply nested comprehensions

✅ Use generators for large datasets

---

# Real-World Use Cases

## Data Cleaning

```python
names = [" Alice ", " Bob ", " John "]

clean = [name.strip() for name in names]

print(clean)
```

---

## Machine Learning

Normalize data

```python
values = [20,40,60]

normalized = [x/100 for x in values]

print(normalized)
```

---

## File Processing

```python
lines = [line.strip() for line in open("data.txt")]
```

---

## API Response

```python
users = [
    {"name":"Alice"},
    {"name":"Bob"}
]

names = [user["name"] for user in users]
```

---

# Mini Project

## Student Grade Analyzer

Requirements

- Store marks
- Calculate grades
- Separate passed students
- Find toppers

```python
marks = [90,45,75,30,88,66]

passed = [m for m in marks if m >= 40]

grades = ["A" if m>=80 else
          "B" if m>=60 else
          "C" if m>=40 else
          "Fail"
          for m in marks]

print("Passed:", passed)
print("Grades:", grades)
```

---

# Practice Questions

## Easy

1. Create a list of squares.
2. Create cube numbers.
3. Convert names to uppercase.
4. Extract vowels.
5. Reverse strings.

---

## Medium

6. Filter even numbers.
7. Filter prime numbers.
8. Flatten nested lists.
9. Remove duplicates.
10. Create multiplication table.

---

## Advanced

11. Build matrix transpose.
12. Generate Pascal Triangle.
13. Build Sudoku grid.
14. Data normalization.
15. Parse JSON data.

---

# Interview Questions

## Beginner

### 1. What is List Comprehension?

A concise way to create lists in Python.

---

### 2. Why use List Comprehensions?

They reduce code, improve readability, and are generally faster.

---

### 3. Syntax of List Comprehension?

```python
[expression for item in iterable]
```

---

### 4. Can we use conditions?

Yes.

```python
[x for x in range(10) if x % 2 == 0]
```

---

### 5. Difference between append() and List Comprehension?

List comprehensions create the entire list in one expression, while `append()` adds elements one by one.

---

## Intermediate

### 6. Can List Comprehensions be nested?

Yes.

---

### 7. Difference between List Comprehension and Generator Expression?

Generators use less memory because they produce values lazily.

---

### 8. Can functions be called inside List Comprehensions?

Yes.

---

### 9. When should you avoid List Comprehensions?

When the logic becomes too complex or unreadable.

---

### 10. Are List Comprehensions faster?

In most cases, yes.

---

## Advanced

### 11. What is lazy evaluation?

Producing values only when needed.

---

### 12. Difference between Dictionary and List Comprehensions?

Dictionary comprehensions create key-value pairs.

---

### 13. Explain Generator Expressions.

Generator expressions return an iterator instead of a list.

---

### 14. What is memory optimization?

Using generators for large datasets to reduce memory usage.

---

### 15. Why are List Comprehensions important in AI/ML?

They are widely used for:

- Data preprocessing
- Feature engineering
- Data transformation
- Cleaning datasets
- Preparing model inputs

---

# 📖 Resources

## Official Documentation

- https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

## Free Resources

- freeCodeCamp Python Course
- Python Official Tutorial
- Real Python

## Books

- Python Crash Course
- Automate the Boring Stuff with Python

---

# 📝 Day 25 Summary

Today you learned:

- List Comprehensions
- Conditional Comprehensions
- Nested Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Expressions
- Performance Optimization
- Real-world Applications
- Student Grade Analyzer Project
- Python Interview Questions

---

# 🚀 GitHub Commit Message

```bash
git add .
git commit -m "Day 25: Mastered Python List Comprehensions with Projects and Interview Questions"
git push origin main
```

---

# ⭐ Next Day

**Day 26 - Generators and Iterators in Python**

Topics:
- Iterators
- `iter()`
- `next()`
- Generators
- `yield`
- Lazy Evaluation
- Memory Optimization
- Generator vs List
- Real-world Applications
- Projects
- Interview Questions

---

## ⭐ If you found this helpful, consider giving this repository a star!