# Day 26 - Generators in Python

> Phase 1: Programming Foundation  
> Roadmap: AI/ML Engineer → GenAI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand what Generators are
- Learn why Generators are memory efficient
- Create Generators using `yield`
- Differentiate between `return` and `yield`
- Iterate over Generator objects
- Use Generator Expressions
- Build custom Generators
- Solve real-world problems using Generators
- Answer Generator interview questions confidently

---

# 📖 What is a Generator?

A **Generator** is a special type of function that produces values **one at a time**, instead of returning all values at once.

Unlike normal functions, a Generator **remembers its previous state** and continues execution from where it stopped.

Generators are created using the **`yield`** keyword.

---

# 🤔 Why Do We Need Generators?

Imagine you need numbers from **1 to 10,000,000**.

### Using a List

```python
numbers = [x for x in range(10000000)]
```

Problems:

- Uses huge memory
- Slower
- Stores all values at once

---

### Using a Generator

```python
numbers = (x for x in range(10000000))
```

Advantages:

- Uses very little memory
- Faster for large datasets
- Generates values only when needed

---

# Generator vs Normal Function

## Normal Function

```python
def numbers():
    return [1, 2, 3]
```

Returns everything at once.

---

## Generator Function

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Produces one value at a time.

---

# Understanding `yield`

`yield` pauses the function and remembers its current state.

```python
def demo():
    yield 1
    yield 2
    yield 3
```

---

# Creating Your First Generator

```python
def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output

```
1
2
3
```

---

# How `next()` Works

```python
def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output

```
10
20
30
```

---

# StopIteration Exception

```python
print(next(gen))
```

Output

```
StopIteration
```

because there are no more values.

---

# Iterating Over Generator

```python
def colors():
    yield "Red"
    yield "Blue"
    yield "Green"

for color in colors():
    print(color)
```

Output

```
Red
Blue
Green
```

---

# Generator with Loop

```python
def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)
```

Output

```
1
2
3
4
5
```

---

# Generator vs List

## List

```python
numbers = [x for x in range(5)]
print(numbers)
```

Output

```
[0, 1, 2, 3, 4]
```

---

## Generator

```python
numbers = (x for x in range(5))
print(numbers)
```

Output

```
<generator object>
```

---

# Generator Expression

Instead of

```python
def square():
    for i in range(5):
        yield i * i
```

Use

```python
squares = (x * x for x in range(5))

for value in squares:
    print(value)
```

Output

```
0
1
4
9
16
```

---

# Infinite Generator

```python
def infinite():
    num = 1

    while True:
        yield num
        num += 1
```

Usage

```python
gen = infinite()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output

```
1
2
3
```

---

# Fibonacci Generator

```python
def fibonacci(limit):

    a, b = 0, 1

    while a <= limit:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num)
```

Output

```
0
1
1
2
3
5
8
13
21
34
```

---

# Reading Large Files Using Generator

```python
def read_file(file_name):

    with open(file_name) as file:
        for line in file:
            yield line
```

Usage

```python
for line in read_file("data.txt"):
    print(line)
```

This avoids loading the whole file into memory.

---

# Real-World Use Cases

## Reading Large CSV Files

```python
def read_csv(file):

    with open(file) as f:
        for row in f:
            yield row
```

---

## API Pagination

```python
def fetch_pages():

    page = 1

    while True:
        yield f"Fetching Page {page}"
        page += 1
```

---

## Machine Learning

Generators are used for:

- Image batches
- Data loaders
- Training datasets

Example:

```python
from torch.utils.data import DataLoader
```

---

## Streaming Data

Used in:

- Chat Applications
- AI Systems
- Video Streaming
- Sensor Data

---

# Generator Advantages

- Memory Efficient
- Faster for huge datasets
- Lazy Evaluation
- Easy to iterate
- Ideal for AI pipelines

---

# Generator Disadvantages

- Cannot access elements using index
- Can iterate only once
- Harder to debug

---

# Mini Project

# Number Generator

```python
def even_numbers(limit):

    for i in range(limit):

        if i % 2 == 0:
            yield i

for number in even_numbers(20):
    print(number)
```

Output

```
0
2
4
6
8
10
12
14
16
18
```

---

# Practice Questions

## Easy

1. Create generator from 1 to 10
2. Print squares using generator
3. Print cubes using generator
4. Print even numbers
5. Print odd numbers

---

## Medium

6. Fibonacci Generator
7. Prime Number Generator
8. Reverse Number Generator
9. Alphabet Generator
10. Infinite Counter

---

## Advanced

11. File Reader Generator
12. CSV Generator
13. API Data Generator
14. Batch Data Generator
15. Image Loader Generator

---

# Interview Questions

## Beginner Level

### 1. What is a Generator?

A Generator is a function that returns values one at a time using `yield`.

---

### 2. Why are Generators used?

To save memory and improve performance.

---

### 3. Which keyword creates a Generator?

```
yield
```

---

### 4. Difference between `return` and `yield`?

| return | yield |
|---------|--------|
| Ends function | Pauses function |
| Returns one value | Returns multiple values over time |

---

### 5. What does `next()` do?

Returns the next value from a Generator.

---

### 6. What happens after Generator finishes?

Raises

```
StopIteration
```

---

### 7. Can a Generator have multiple `yield` statements?

Yes.

---

### 8. Is a Generator iterable?

Yes.

---

### 9. Can we loop over a Generator?

Yes.

---

### 10. Is Generator memory efficient?

Yes.

---

# Intermediate Level

### 11. Generator vs List?

Generators use lazy evaluation.

Lists store all elements.

---

### 12. What is lazy evaluation?

Values are created only when required.

---

### 13. Generator Expression vs List Comprehension?

```
(x for x in range(5))
```

vs

```
[x for x in range(5)]
```

---

### 14. Can Generators be reused?

No.

Once exhausted, they must be recreated.

---

### 15. Where are Generators commonly used?

- AI
- Machine Learning
- Data Science
- APIs
- Streaming
- Large File Processing

---

# Advanced Interview Questions

### 16. How do Generators improve performance?

By avoiding unnecessary memory allocation.

---

### 17. Explain lazy loading.

Data is generated only when requested.

---

### 18. Why are Generators important in AI?

Large datasets cannot fit into memory.

Generators load data batch-by-batch.

---

### 19. Difference between Iterator and Generator?

Generator automatically creates an iterator.

---

### 20. What is the biggest advantage of Generators?

Efficient memory usage.

---

# Best Practices

✅ Use Generators for large datasets

✅ Use `yield` instead of creating huge lists

✅ Use Generator Expressions when possible

✅ Prefer Generators for file processing

✅ Use Generators in ML pipelines

---

# Day 26 Summary

Today you learned:

- What are Generators
- Why use Generators
- `yield` keyword
- `next()` function
- Generator Expressions
- Infinite Generators
- Fibonacci Generator
- Reading files with Generators
- Real-world applications
- Interview questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 26: Learned Python Generators and Built Memory-Efficient Programs"
git push origin main
```

---

# 🚀 Next Day

**Day 27: Decorators in Python**

Topics:

- Functions as Objects
- Nested Functions
- Closures
- Decorators
- `@decorator` Syntax
- Multiple Decorators
- Practical Examples
- Logging Decorator Project
- Interview Questions

---

# 📚 Resources

## Official Documentation

- https://docs.python.org/3/reference/expressions.html#yieldexpr
- https://docs.python.org/3/howto/functional.html

## Free Resources

- freeCodeCamp Python Course
- Corey Schafer - Python Generators
- Python Docs

## Practice Platforms

- LeetCode
- HackerRank
- Codewars

---

⭐ If you found this repository helpful, consider giving it a **Star** and follow along for the complete **365-Day AI/ML + GenAI + Agentic AI Roadmap**!