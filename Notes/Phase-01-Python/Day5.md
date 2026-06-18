# Day 5 - Python Dictionaries and Sets

> Part of my AI/ML & Generative AI Engineering Journey 🚀

## 📅 Day 5 Goals

Today I learned two powerful Python data structures:

- Dictionaries (`dict`)
- Sets (`set`)

These data structures are widely used in real-world applications such as databases, APIs, machine learning, data processing, and AI systems.

---

# 📖 Dictionary in Python

A dictionary is a collection of key-value pairs.

### Syntax

```python
student = {
    "name": "Saurav",
    "age": 21,
    "course": "BCA"
}
```

### Accessing Values

```python
student = {
    "name": "Saurav",
    "age": 21
}

print(student["name"])
```

### Output

```python
Saurav
```

---

## Adding New Items

```python
student = {
    "name": "Saurav"
}

student["city"] = "Indore"

print(student)
```

### Output

```python
{'name': 'Saurav', 'city': 'Indore'}
```

---

## Updating Values

```python
student["city"] = "Bhopal"
```

---

## Removing Items

```python
student.pop("city")
```

---

## Useful Dictionary Methods

| Method | Description |
|----------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Safely gets value |
| pop() | Removes item |

### Example

```python
student = {
    "name": "Saurav",
    "age": 21
}

print(student.keys())
print(student.values())
```

---

# 🎯 Real-Life Example

Imagine a student record system.

```python
student = {
    "id": 101,
    "name": "Saurav",
    "course": "BCA",
    "marks": 89
}

print(student)
```

---

# 📖 Sets in Python

A set is an unordered collection of unique values.

### Syntax

```python
numbers = {1, 2, 3, 4}
```

---

## Why Use Sets?

Sets automatically remove duplicate values.

### Example

```python
numbers = {1, 2, 3, 3, 4, 4, 5}

print(numbers)
```

### Output

```python
{1, 2, 3, 4, 5}
```

---

## Adding Elements

```python
numbers.add(10)
```

---

## Removing Elements

```python
numbers.remove(2)
```

---

## Useful Set Methods

| Method | Description |
|----------|-------------|
| add() | Adds item |
| remove() | Removes item |
| union() | Combines sets |
| intersection() | Common values |
| difference() | Unique values |

---

## Union Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

### Output

```python
{1, 2, 3, 4, 5}
```

---

## Intersection Example

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

### Output

```python
{2, 3}
```

---

# 🛠 Project 1: Phonebook Application

### Problem Statement

Create a simple phonebook using dictionaries.

### Solution

```python
phonebook = {}

phonebook["Rahul"] = "9876543210"
phonebook["Amit"] = "9123456789"

print(phonebook)
```

### Output

```python
{
    'Rahul': '9876543210',
    'Amit': '9123456789'
}
```

---

# 🛠 Project 2: Word Frequency Counter

### Problem Statement

Count how many times each word appears.

### Solution

```python
text = "python is easy and python is powerful"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

### Output

```python
{
    'python': 2,
    'is': 2,
    'easy': 1,
    'and': 1,
    'powerful': 1
}
```

---

# 💡 Interview Questions

### 1. What is a Dictionary?

A dictionary is a collection of key-value pairs.

---

### 2. Are Dictionary Keys Unique?

Yes.

Duplicate keys are not allowed.

---

### 3. What is the Difference Between List and Dictionary?

| List | Dictionary |
|--------|------------|
| Uses index | Uses key |
| Ordered | Key-value structure |
| Faster for sequential data | Faster for lookups |

---

### 4. What is a Set?

A set is an unordered collection of unique values.

---

### 5. Why Use Sets?

To remove duplicates and perform mathematical operations like union and intersection.

---

# 🧠 Practice Questions

### Easy

1. Create a dictionary of your personal information.
2. Add a new key-value pair.
3. Update an existing value.
4. Remove a key.
5. Print all keys.

### Medium

6. Count vowels in a string.
7. Create a student marks system.
8. Find duplicate elements using sets.
9. Merge two dictionaries.
10. Find common elements between two lists using sets.

---

# 🎯 Day 5 Assignment

Build:

### 1. Student Record System

Features:

- Add Student
- Update Student
- Delete Student
- View Student

---

### 2. Contact Book

Features:

- Add Contact
- Search Contact
- Delete Contact
- Show All Contacts

---

# 📚 Resources

### Official Documentation

- https://docs.python.org/3/tutorial/datastructures.html

### Practice Platforms

- LeetCode
- HackerRank
- GeeksforGeeks

---

# ✅ Day 5 Summary

Today I learned:

- Dictionaries
- Dictionary Methods
- Sets
- Set Operations
- Phonebook Application
- Word Frequency Counter

These concepts are fundamental for Data Analysis, Machine Learning, APIs, and Generative AI applications.

---

## 🚀 Next Day

Day 6: Conditional Statements (`if`, `elif`, `else`) and Decision Making in Python.

#Python #100DaysOfCode #AIEngineer #MachineLearning #GenerativeAI #PythonProgramming #LearningInPublic #GitHub