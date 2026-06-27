# Day 17 - JSON Handling in Python

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand what JSON is and why it is widely used
- Read JSON data from files
- Write JSON data to files
- Convert Python objects to JSON
- Convert JSON into Python objects
- Work with nested JSON structures
- Pretty-print JSON data
- Handle JSON file exceptions
- Build a Configuration Loader project
- Answer JSON interview questions confidently

---

# 📖 Table of Contents

1. What is JSON?
2. Why JSON is Important
3. JSON Data Types
4. Python Dictionary vs JSON
5. The `json` Module
6. Reading JSON Files
7. Writing JSON Files
8. JSON Serialization
9. JSON Deserialization
10. Pretty Printing JSON
11. Working with Nested JSON
12. Handling JSON Exceptions
13. Practical Examples
14. Mini Project
15. Best Practices
16. Practice Questions
17. Interview Questions
18. Summary

---

# What is JSON?

**JSON** stands for **JavaScript Object Notation**.

It is a lightweight data-interchange format used to exchange data between applications, APIs, databases, and servers.

JSON is:

- Human-readable
- Lightweight
- Language-independent
- Easy to parse
- Easy to generate

---

# Why JSON is Important

Almost every modern application uses JSON.

Examples:

- REST APIs
- AI APIs (OpenAI, Gemini)
- Configuration Files
- Mobile Apps
- Web Applications
- Cloud Services
- Databases
- Machine Learning APIs

---

# Example JSON

```json
{
    "name": "John",
    "age": 22,
    "city": "New York",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}
```

---

# JSON Data Types

| JSON Type | Python Type |
|------------|-------------|
| Object | dict |
| Array | list |
| String | str |
| Number | int / float |
| Boolean | bool |
| Null | None |

---

# Python Dictionary vs JSON

## Python Dictionary

```python
student = {
    "name": "Alice",
    "age": 21
}
```

---

## JSON

```json
{
    "name": "Alice",
    "age": 21
}
```

Difference:

Python uses:

```python
True
False
None
```

JSON uses:

```json
true
false
null
```

---

# Importing the json Module

```python
import json
```

---

# JSON Serialization

Serialization means converting Python objects into JSON.

Python Object ➜ JSON

Use:

```python
json.dumps()
```

Example:

```python
import json

student = {
    "name": "Alice",
    "age": 20,
    "course": "BCA"
}

json_data = json.dumps(student)

print(json_data)
```

Output

```json
{"name": "Alice", "age": 20, "course": "BCA"}
```

---

# Pretty Printing JSON

```python
import json

student = {
    "name": "Alice",
    "age": 20,
    "skills": ["Python", "SQL"]
}

print(json.dumps(student, indent=4))
```

Output

```json
{
    "name": "Alice",
    "age": 20,
    "skills": [
        "Python",
        "SQL"
    ]
}
```

---

# JSON Deserialization

Converting JSON into Python object.

Use

```python
json.loads()
```

Example

```python
import json

data = '{"name":"John","age":21}'

student = json.loads(data)

print(student)

print(type(student))
```

Output

```text
{'name': 'John', 'age': 21}

<class 'dict'>
```

---

# Writing JSON to File

Use

```python
json.dump()
```

Example

```python
import json

student = {
    "name": "Alice",
    "age": 20,
    "course": "BCA"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")
```

Generated file

```json
{
    "name": "Alice",
    "age": 20,
    "course": "BCA"
}
```

---

# Reading JSON File

Use

```python
json.load()
```

Example

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

Output

```text
{'name': 'Alice', 'age': 20, 'course': 'BCA'}
```

---

# Working with Nested JSON

Example

```json
{
    "student": {
        "name": "John",
        "age": 22,
        "address": {
            "city": "Delhi",
            "state": "Delhi"
        }
    }
}
```

Python

```python
import json

with open("student.json") as file:
    data = json.load(file)

print(data["student"]["address"]["city"])
```

Output

```text
Delhi
```

---

# JSON Arrays

```json
[
    {
        "name": "Alice"
    },
    {
        "name": "Bob"
    }
]
```

Python

```python
import json

employees = [
    {"name": "Alice"},
    {"name": "Bob"},
    {"name": "Charlie"}
]

print(json.dumps(employees, indent=4))
```

---

# Updating JSON Data

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

student["age"] = 25

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

---

# Handling JSON Exceptions

```python
import json

try:
    with open("student.json") as file:
        data = json.load(file)

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON format.")
```

---

# Practical Example 1

## Save Student Details

```python
import json

student = {
    "name": input("Enter Name: "),
    "age": int(input("Enter Age: ")),
    "course": input("Enter Course: ")
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data Saved Successfully.")
```

---

# Practical Example 2

## Read Student Details

```python
import json

with open("student.json") as file:
    student = json.load(file)

print(student)
```

---

# Practical Example 3

## Add New Employee

```python
import json

employees = []

for i in range(3):

    name = input("Name: ")

    employees.append({
        "name": name
    })

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
```

---

# Mini Project

# Configuration Loader

## Objective

Create an application that reads application settings from a JSON file.

---

## config.json

```json
{
    "app_name": "AI Assistant",
    "version": "1.0",
    "theme": "dark",
    "language": "English",
    "database": {
        "host": "localhost",
        "port": 3306
    }
}
```

---

## main.py

```python
import json

try:

    with open("config.json") as file:
        config = json.load(file)

    print("Application Name :", config["app_name"])
    print("Version          :", config["version"])
    print("Theme            :", config["theme"])
    print("Language         :", config["language"])
    print("Database Host    :", config["database"]["host"])
    print("Database Port    :", config["database"]["port"])

except FileNotFoundError:
    print("Configuration file not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")
```

---

# Folder Structure

```text
Configuration-Loader/

│── config.json
│── main.py
│── README.md
```

---

# Best Practices

- Always use `with open()`
- Always use `indent=4`
- Handle exceptions
- Validate JSON before loading
- Use meaningful keys
- Keep JSON readable
- Avoid deeply nested structures when possible

---

# Practice Questions

## Easy

1. Convert dictionary to JSON.
2. Convert JSON string to dictionary.
3. Write JSON into a file.
4. Read JSON file.
5. Print JSON with indentation.

---

## Medium

6. Update JSON file.
7. Store multiple students.
8. Read nested JSON.
9. Create employee database.
10. Build configuration loader.

---

## Advanced

11. Merge two JSON files.
12. Validate JSON data.
13. Create JSON API response parser.
14. Build settings manager.
15. Build JSON-based inventory system.

---

# Real World Applications

- API Responses
- OpenAI API
- Gemini API
- REST APIs
- Mobile Apps
- Machine Learning Models
- Configuration Files
- Docker Configurations
- Kubernetes
- Cloud Services

---

# Interview Questions

## Beginner Level

### 1. What is JSON?

JSON (JavaScript Object Notation) is a lightweight data-interchange format used to exchange data between systems.

---

### 2. Why is JSON used?

Because it is lightweight, human-readable, language-independent, and easy to parse.

---

### 3. What is the difference between JSON and XML?

| JSON | XML |
|------|-----|
| Lightweight | Heavy |
| Faster | Slower |
| Easy to read | Verbose |
| Less storage | More storage |

---

### 4. What module is used for JSON in Python?

```python
import json
```

---

### 5. What does `json.dumps()` do?

Converts a Python object into a JSON string.

---

### 6. What does `json.loads()` do?

Converts a JSON string into a Python object.

---

### 7. What does `json.dump()` do?

Writes a Python object directly to a JSON file.

---

### 8. What does `json.load()` do?

Reads JSON data from a file and converts it into a Python object.

---

### 9. What is serialization?

Converting Python objects into JSON format.

---

### 10. What is deserialization?

Converting JSON data into Python objects.

---

# Intermediate Level

### 11. Why is JSON preferred over XML?

It is simpler, faster, and consumes less bandwidth.

---

### 12. Can JSON store comments?

No.

---

### 13. Can JSON have duplicate keys?

Technically allowed, but the last value usually overwrites previous ones during parsing.

---

### 14. What exception occurs when JSON is invalid?

```python
json.JSONDecodeError
```

---

### 15. Why use `indent=4`?

To make JSON human-readable.

---

# Advanced Level

### 16. How do APIs use JSON?

Servers send responses in JSON, and clients parse them into objects.

---

### 17. Why is JSON important in AI Engineering?

Most AI APIs (OpenAI, Gemini, Hugging Face, Anthropic, etc.) send and receive data in JSON.

---

### 18. What are nested JSON objects?

Objects containing other objects or arrays inside them.

---

### 19. What is the difference between `dump` and `dumps`?

| dump | dumps |
|------|--------|
| Writes to a file | Returns a JSON string |

---

### 20. What is the difference between `load` and `loads`?

| load | loads |
|------|---------|
| Reads from file | Reads from string |

---

# Common Mistakes

❌ Forgetting to import `json`

❌ Not handling exceptions

❌ Writing invalid JSON syntax

❌ Forgetting to close files (use `with open()`)

❌ Mixing Python data types with JSON types

---

# Day 17 Summary

Today you learned:

- What JSON is
- JSON syntax
- Serialization
- Deserialization
- Reading JSON files
- Writing JSON files
- Nested JSON
- JSON exceptions
- Configuration Loader Project
- Real-world applications
- Interview questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 17: Learned JSON Handling in Python and Built Configuration Loader"
git push origin main
```

---

# Repository Structure

```text
Day-17-JSON-Handling/
│
├── config.json
├── student.json
├── main.py
├── examples.py
└── README.md
```

---

# 🚀 What's Next?

**Day 18 – Python Problem Solving & Logic Building**

Topics:
- Algorithmic Thinking
- Pattern Problems
- String Challenges
- List Challenges
- Dictionary Challenges
- HackerRank & LeetCode Practice
- Time Complexity Basics
- 25+ Coding Problems
- Interview Coding Patterns