# 🚀 Day 5 — OOPs in Python (Object-Oriented Programming)

## 🎯 Goal of Day 5

Today’s goal is to understand how real-world things are represented in code.

This is VERY important because:

* AI Applications
* Backend Systems
* APIs
* Frameworks
* LangChain
* Agent Systems

…all use OOP concepts heavily.

---

# 📚 Topics To Learn Today

---

# 1️⃣ What is OOP?

Object-Oriented Programming (OOP) is a way to structure code using:

* Classes
* Objects

---

## 🧠 Real-Life Example

```bash id="t9n7wo"
Car = Class
BMW Car = Object
```

---

# 2️⃣ Class and Object

Learn:

* How to create a class
* How to create objects

---

## Example

```python id="8gwq3m"
class Student:
    name = "Sauraf"

s1 = Student()
print(s1.name)
```

---

## Understand

* `Student` → Class
* `s1` → Object

---

# 3️⃣ Constructor (`__init__`)

Learn how objects get initialized automatically.

---

## Example

```python id="k0jlwm"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sauraf", 20)

print(s1.name)
print(s1.age)
```

---

## Understand

* `self`
* Constructor
* Instance Variables

---

# 4️⃣ Instance Variables vs Class Variables

Learn the difference between:

* Variables inside constructor
* Variables shared by all objects

---

## Example

```python id="g7p6o1"
class Student:
    college = "BCA College"

    def __init__(self, name):
        self.name = name
```

---

# 5️⃣ Methods in Class

Methods are functions inside classes.

---

## Example

```python id="f4kg0f"
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s1 = Student("Sauraf")
s1.greet()
```

---

# 6️⃣ Encapsulation

Learn:

* Hiding internal data
* Private variables

Basic understanding is enough for now.

---

## Example

```python id="8v4g8k"
class Bank:
    def __init__(self):
        self.__balance = 1000
```

---

# 7️⃣ Inheritance (VERY IMPORTANT)

One class can inherit another class.

---

## Example

```python id="g34woj"
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
```

---

## Understand

* Parent Class
* Child Class

---

# 8️⃣ Polymorphism (Basic Only)

Same function behaves differently.

---

## Example

```python id="h6m67q"
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
```

---

# 💻 Practice Tasks (Must Do)

---

# 🟢 Easy Tasks

## Task 1 — Create a Car Class

Create:

* Brand
* Model
* Display Function

---

## Task 2 — Create a Mobile Class

Create:

* Brand
* Price
* Display Function

---

## Task 3 — Create a Student Class

Features:

* Name
* Marks
* Display Function

---

# 🟡 Medium Tasks

---

# 🏦 Task 1 — Bank System

Create methods:

```python id="v4vr6u"
deposit()
withdraw()
check_balance()
```

---

## Concepts Used

* Class
* Object
* Methods
* Constructor

---

# 👨‍💼 Task 2 — Employee Management System

Features:

* Add Employee
* Show Employee Details

---

# 🚀 Mini Project (Important)

# 📚 Library Management System

---

## Features

* Add Book
* Issue Book
* Return Book
* Show Available Books

---

## This Project Will Strengthen

* Classes
* Objects
* Methods
* Lists
* Logic Building

---

# 📚 Resources To Learn

---

# 🎥 YouTube

* CodeWithHarry — OOP Python
* Corey Schafer — OOP Playlist

---

# 📖 Documentation

* Python Classes Docs

---

# 📂 Day 5 Assignment

You must upload on GitHub:

* 3 Practice Programs
* Bank System Project
* README Explaining Concepts Learned

---

# ✅ Output Expected By End Of Day

By tonight you should be able to:

* ✅ Create Classes
* ✅ Create Objects
* ✅ Use Constructors
* ✅ Write Methods
* ✅ Understand Inheritance
* ✅ Build Small OOP Projects

---

# 🧠 Why OOP Matters for AI Engineering

Most modern AI systems are built using OOP concepts.

Examples:

* LangChain
* FastAPI
* AI Agents
* Backend APIs
* Frameworks
* Automation Systems

Understanding OOP now will make advanced AI development much easier later.

---

# 📂 Suggested GitHub Folder Structure

```bash id="4e8o4m"
Day-05-OOP-Python/
│
├── car_class.py
├── mobile_class.py
├── student_class.py
├── bank_system.py
├── employee_management.py
├── library_management_system.py
└── README.md
```

---

# ✅ End of Day 5 Checklist

* [ ] Learned OOP Basics
* [ ] Created Classes and Objects
* [ ] Used Constructors
* [ ] Created Methods
* [ ] Learned Inheritance
* [ ] Practiced Encapsulation
* [ ] Built Bank System
* [ ] Built Library Management System
* [ ] Uploaded Everything to GitHub

---

# 🚀 Keep Going

Strong OOP skills = Strong Developer Foundation.

And strong foundations create strong AI Engineers 🔥
