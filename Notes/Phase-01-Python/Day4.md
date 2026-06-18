# Day 4 - Lists and Tuples in Python 🐍

Welcome to **Day 4** of my Python Learning Journey.

Today I learned two of the most important data structures in Python:

- Lists
- Tuples

These are used to store multiple values in a single variable and are heavily used in Data Science, Machine Learning, Web Development, and Automation.

---

# 📚 Topics Covered

## 1. Lists

A list is an ordered, mutable (changeable) collection of items.

### Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

### Output

```python
['Apple', 'Banana', 'Mango']
```

---

## Accessing List Elements

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
```

### Output

```python
Apple
Banana
```

---

## Modifying a List

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

### Output

```python
['Apple', 'Orange', 'Mango']
```

---

## Adding Elements

### append()

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

### Output

```python
['Apple', 'Banana', 'Mango']
```

---

## Removing Elements

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

### Output

```python
['Apple', 'Mango']
```

---

## Useful List Methods

| Method | Description |
|----------|----------|
| append() | Add item |
| remove() | Remove item |
| insert() | Insert item |
| pop() | Remove by index |
| sort() | Sort list |
| reverse() | Reverse list |
| len() | Length of list |

---

# 2. Tuples

A tuple is an ordered, immutable (unchangeable) collection.

### Creating a Tuple

```python
colors = ("Red", "Green", "Blue")

print(colors)
```

### Output

```python
('Red', 'Green', 'Blue')
```

---

## Accessing Tuple Elements

```python
colors = ("Red", "Green", "Blue")

print(colors[0])
```

### Output

```python
Red
```

---

## Tuple Cannot Be Modified

```python
colors = ("Red", "Green", "Blue")

colors[1] = "Yellow"
```

### Output

```python
TypeError
```

Because tuples are immutable.

---

# List vs Tuple

| Feature | List | Tuple |
|----------|----------|----------|
| Ordered | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Faster | ❌ | ✅ |
| Syntax | [] | () |
| Can Modify | ✅ | ❌ |

---

# Real World Example

## Student Names Using List

```python
students = ["Rahul", "Amit", "Priya"]

students.append("Anjali")

print(students)
```

### Output

```python
['Rahul', 'Amit', 'Priya', 'Anjali']
```

---

## Days of Week Using Tuple

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days)
```

Since days never change, tuple is a better choice.

---

# Mini Project 1: Student Marks System

## Description

Store student marks in a list and calculate:

- Total Marks
- Average Marks
- Highest Marks
- Lowest Marks

### Code

```python
marks = [85, 90, 78, 92, 88]

total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
```

### Output

```python
Total Marks: 433
Average Marks: 86.6
Highest Marks: 92
Lowest Marks: 78
```

---

# Mini Project 2: Shopping Cart

## Description

Create a simple shopping cart using lists.

### Code

```python
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Shopping Cart:")
print(cart)
```

### Output

```python
Shopping Cart:
['Laptop', 'Mouse', 'Keyboard']
```

---

# Practice Questions

### Easy

1. Create a list of 5 fruits.
2. Print the first and last fruit.
3. Add a new fruit.
4. Remove a fruit.
5. Find length of list.

### Medium

6. Create a list of numbers.
7. Find largest number.
8. Find smallest number.
9. Calculate sum of all numbers.
10. Calculate average.

### Tuple Practice

11. Create a tuple of 5 colors.
12. Print second color.
13. Count number of items.
14. Try modifying tuple and observe error.

---

# Interview Questions

## What is a List?

A list is an ordered and mutable collection used to store multiple items.

---

## What is a Tuple?

A tuple is an ordered and immutable collection.

---

## Difference Between List and Tuple?

- Lists can be modified.
- Tuples cannot be modified.
- Tuples are faster and more memory efficient.

---

## When Should You Use Tuple?

Use tuples when data should not change, such as:

- Days of week
- Months
- Coordinates
- Configuration values

---

# Key Takeaways

✅ Lists are mutable and flexible

✅ Tuples are immutable and faster

✅ Lists use []

✅ Tuples use ()

✅ Learned list operations

✅ Built Student Marks System

✅ Built Shopping Cart Project

---

# Day 4 Progress

- [x] Learned Lists
- [x] Learned Tuples
- [x] Practiced List Methods
- [x] Built Student Marks System
- [x] Built Shopping Cart Project
- [x] Solved Practice Questions

## Connect With Me

I'm currently on a journey to become an AI/ML Engineer and sharing my daily learning progress.

⭐ Feel free to explore my repositories and follow my journey!  