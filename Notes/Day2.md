# Day 2 - Python Data Types, Type Casting & Operators

## 📅 AI/ML Engineer Roadmap - Phase 1

Today I learned the fundamentals of Python Data Types, Type Casting, and Operators. These concepts are the building blocks of every Python program and are heavily used in Data Science, Machine Learning, and AI development.

---

# 📌 Topics Covered

## 1. Data Types in Python

Data types define the kind of value a variable can store.

### Integer (int)

```python
age = 21
print(age)
print(type(age))
```

Output:

```python
21
<class 'int'>
```

---

### Float (float)

```python
price = 99.99
print(type(price))
```

Output:

```python
<class 'float'>
```

---

### String (str)

```python
name = "Sauraf"
print(type(name))
```

Output:

```python
<class 'str'>
```

---

### Boolean (bool)

```python
is_student = True
print(type(is_student))
```

Output:

```python
<class 'bool'>
```

---

### Complex Number

```python
num = 3 + 5j
print(type(num))
```

Output:

```python
<class 'complex'>
```

---

# 📌 Type Casting

Type Casting means converting one data type into another.

## Integer to Float

```python
num = 10
result = float(num)

print(result)
print(type(result))
```

Output:

```python
10.0
<class 'float'>
```

---

## Float to Integer

```python
num = 10.99
result = int(num)

print(result)
```

Output:

```python
10
```

---

## Integer to String

```python
age = 21
text = str(age)

print(text)
print(type(text))
```

Output:

```python
21
<class 'str'>
```

---

## String to Integer

```python
number = "100"
result = int(number)

print(result)
print(type(result))
```

Output:

```python
100
<class 'int'>
```

---

# 📌 Operators in Python

Operators are used to perform operations on variables and values.

---

## Arithmetic Operators

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
```

Output:

```python
15
5
50
2.0
0
100000
2
```

---

## Comparison Operators

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Output:

```python
False
True
False
True
False
True
```

---

## Logical Operators

```python
x = True
y = False

print(x and y)
print(x or y)
print(not x)
```

Output:

```python
False
True
False
```

---

## Assignment Operators

```python
x = 10

x += 5
print(x)

x -= 2
print(x)
```

Output:

```python
15
13
```

---

# 🚀 Mini Project 1: Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

# 🚀 Mini Project 2: BMI Calculator

```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))
```

---

# 🚀 Mini Project 3: Temperature Converter

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
```

---

# 🎯 Practice Questions

### Easy

1. Create variables of different data types and print their types.
2. Convert an integer into a string.
3. Convert a string into an integer.
4. Find the square of a number.
5. Calculate the remainder using `%`.

### Medium

6. Create a simple calculator.
7. Calculate the area of a rectangle.
8. Calculate simple interest.
9. Convert Celsius to Fahrenheit.
10. Convert kilometers to miles.

---

# 💡 Interview Questions

### Q1. What are Python Data Types?

Data types define the type of value stored in a variable.

Examples:

- int
- float
- str
- bool
- complex

---

### Q2. What is Type Casting?

Type Casting is the process of converting one data type into another.

Example:

```python
num = "100"
print(int(num))
```

---

### Q3. Difference Between `=` and `==`?

| Operator | Meaning |
|-----------|----------|
| = | Assignment |
| == | Comparison |

Example:

```python
x = 10

print(x == 10)
```

---

### Q4. Difference Between `/` and `//`?

| Operator | Result |
|-----------|----------|
| / | Float Division |
| // | Floor Division |

Example:

```python
print(10 / 3)
print(10 // 3)
```

Output:

```python
3.3333
3
```

---

# 📚 Resources

### Documentation

https://docs.python.org/3/

### Practice Platforms

- HackerRank
- LeetCode
- CodeWars

### YouTube

- CodeWithHarry Python Course
- Corey Schafer Python Tutorials
- freeCodeCamp Python Full Course

---

# ✅ Day 2 Summary

Today I learned:

- Python Data Types
- Type Casting
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators

Projects Built:

- Calculator
- BMI Calculator
- Temperature Converter

Next Topic: Strings and String Operations 🚀