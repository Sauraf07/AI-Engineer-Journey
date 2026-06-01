# 🚀 Day 3 — Python Collections + Git Basics

## 🎯 Goal of Day 3

Today’s goal is to:

* Learn how Python stores multiple values
* Understand the most used data structures
* Start thinking like a programmer
* Learn basic Git workflow

⚡ These topics are VERY important because AI applications heavily use:

* Lists
* Dictionaries
* Loops
* Structured Data

---

# 📚 Topics To Learn Today

---

# 1️⃣ Lists in Python

Lists are used to store multiple items.

---

## Example

```python id="h7lq3x"
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
```

---

## Learn

* Indexing
* Slicing
* `append()`
* `remove()`
* `pop()`
* `sort()`

---

## Practice

```python id="rlkq4x"
numbers = [5, 2, 9, 1]

numbers.append(10)
numbers.sort()

print(numbers)
```

---

# 2️⃣ Tuples

Tuples are immutable (cannot be changed).

---

## Example

```python id="y2c7gt"
colors = ("red", "blue", "green")

print(colors[1])
```

---

## Learn

* Tuple packing
* Tuple unpacking
* Difference between list and tuple

---

# 3️⃣ Sets

Sets store unique values only.

---

## Example

```python id="4f9xqb"
nums = {1, 2, 3, 3, 4}

print(nums)
```

---

## Output

```bash id="3vx8p2"
{1, 2, 3, 4}
```

---

## Learn

* `add()`
* `remove()`
* Union
* Intersection

---

## Example

```python id="5g81xv"
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
```

---

# 4️⃣ Dictionaries (MOST IMPORTANT)

Dictionaries are used everywhere in AI and APIs.

They store data in key-value pairs.

---

## Example

```python id="9zk4qy"
student = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
```

---

## Learn

* `keys()`
* `values()`
* `items()`
* `update()`
* `pop()`

---

## Practice

```python id="w6ap4q"
employee = {
    "name": "Aman",
    "salary": 25000
}

employee["salary"] = 30000

print(employee)
```

---

# 5️⃣ Nested Data Structures

Very important for JSON and API handling.

---

## Example

```python id="nk8t2j"
students = [
    {"name": "Rahul", "marks": 80},
    {"name": "Aman", "marks": 90}
]

print(students[0]["name"])
```

---

## Used Heavily In

* APIs
* AI Responses
* Databases
* Vector Search Results

---

# 6️⃣ Git & GitHub Basics

---

## Learn

* What is Git?
* What is GitHub?
* Why developers use version control

---

## Git Commands To Learn

```bash id="kz6d1t"
git init
git status
git add .
git commit -m "first commit"
git push
```

---

## Install Git

Download from:

* Git Official Website

---

## GitHub Learning Resources

* GitHub Docs
* GitHub Skills

---

# 💻 Day 3 Practice Tasks

---

# 🟢 Task 1 — List Program

Create a list of 5 numbers:

* Add a new number
* Remove one number
* Sort the list

---

# 🟢 Task 2 — Dictionary Program

Create a student dictionary:

* Name
* Age
* Marks
* Course

---

## Then

* Update marks
* Print all keys
* Print all values

---

# 🟢 Task 3 — Set Program

Create two sets and:

* Find union
* Find intersection

---

# 🟢 Task 4 — Mini Student Management System

Store 3 students using dictionaries inside a list.

---

## Example

```python id="6jtw4m"
students = [
    {"name": "Rahul", "marks": 80},
    {"name": "Aman", "marks": 90}
]
```

---

## Print

* All student names
* Highest marks

---

# 🔥 Challenge Task (IMPORTANT)

# 📞 Contact Book CLI App

---

## Features

* Add Contact
* Search Contact
* Delete Contact
* Show All Contacts

---

## Use

* Dictionary
* Loops
* Functions

---

# 🧠 Mini Revision Questions

1. Difference between list and tuple?
2. Why are sets useful?
3. What is a dictionary?
4. What is mutable vs immutable?
5. How do you access dictionary values?
6. What is indexing?
7. Why do we use Git?

---

# 🎯 End-of-Day Goal

By the end of Day 3, you should:

* Comfortably use Python collections
* Understand structured data
* Push code to GitHub
* Create small logic-based programs

---

# 📂 What To Upload on GitHub Today

Create folder:

```bash id="n8q2wh"
Day-03-Python-Collections
```

---

## Inside It

* List programs
* Tuple programs
* Set programs
* Dictionary programs
* Contact Book CLI App
* README.md

---

# 📝 README Example

```md id="xbh3gv"
# Day 3 - Python Collections + Git Basics

## Topics Covered
- Lists
- Tuples
- Sets
- Dictionaries
- Git Basics

## Projects
- Student Management System
- Contact Book CLI App
```

---

# 🧠 Important Concept for AI Career

Modern AI systems work heavily with structured data.

Examples:

* JSON Responses
* API Data
* Embeddings Metadata
* AI Model Outputs
* Vector Database Results

Most of these are handled using:

* Lists
* Dictionaries
* Nested Data Structures

⚡ Mastering collections will make learning AI frameworks much easier later.

---

# ✅ End of Day 3 Checklist

* [ ] Learned Lists
* [ ] Learned Tuples
* [ ] Learned Sets
* [ ] Learned Dictionaries
* [ ] Practiced Nested Data Structures
* [ ] Learned Basic Git Commands
* [ ] Completed Practice Tasks
* [ ] Built Contact Book CLI App
* [ ] Uploaded Code to GitHub

---

# 🚀 Keep Going

The better your programming fundamentals become, the easier advanced AI engineering will feel later 🔥
