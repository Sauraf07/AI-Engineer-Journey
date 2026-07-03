# Day 22 - Python Standard Libraries (`os`, `datetime`, `requests`)

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📚 Table of Contents

- Introduction
- Learning Objectives
- What are Python Standard Libraries?
- The `os` Module
- The `datetime` Module
- The `requests` Library
- Practical Examples
- Mini Project - File Organizer
- Practice Questions
- Interview Questions
- Best Practices
- Resources
- Assignment
- GitHub Commit Message
- Summary

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand Python Standard Libraries
- Work with files and directories using `os`
- Handle dates and times using `datetime`
- Make HTTP requests using `requests`
- Read API responses in JSON format
- Build a File Organizer
- Prepare for Python interview questions

---

# 📖 Introduction

Python comes with a rich collection of built-in libraries that help developers perform common tasks without writing everything from scratch.

Today, you'll learn three essential libraries:

- `os` → Work with operating system files and folders
- `datetime` → Work with dates and times
- `requests` → Fetch data from web APIs

These libraries are widely used in AI, Machine Learning, Automation, Web Development, and Data Engineering.

---

# 📦 Python Standard Libraries

A Python Standard Library is a collection of pre-written modules included with Python.

Instead of writing everything manually, you can import a library and use its functions.

Example:

```python
import os
import datetime
```

Third-party libraries (like `requests`) must be installed separately.

```bash
pip install requests
```

---

# 📂 The `os` Module

The `os` module allows interaction with the operating system.

## Why Use `os`?

- Create folders
- Delete files
- Rename files
- Navigate directories
- Get current working directory
- List files

---

## Importing `os`

```python
import os
```

---

## Current Working Directory

```python
import os

print(os.getcwd())
```

Output:

```text
C:\Users\YourName\Projects
```

---

## List Files

```python
import os

print(os.listdir())
```

Output:

```text
['main.py', 'notes.txt', 'image.png']
```

---

## Create Folder

```python
import os

os.mkdir("NewFolder")
```

---

## Rename Folder

```python
os.rename("NewFolder", "PythonFiles")
```

---

## Remove Folder

```python
os.rmdir("PythonFiles")
```

---

## Check File Exists

```python
import os

print(os.path.exists("main.py"))
```

---

## Get File Size

```python
import os

print(os.path.getsize("notes.txt"))
```

---

## Create File Path

```python
import os

path = os.path.join("Documents", "notes.txt")

print(path)
```

---

# 📅 The `datetime` Module

The `datetime` module helps work with dates and times.

Used in:

- AI logging
- Data analysis
- Banking
- Attendance systems
- Scheduling

---

## Import

```python
from datetime import datetime
```

---

## Current Date & Time

```python
from datetime import datetime

print(datetime.now())
```

---

## Current Date

```python
today = datetime.today()

print(today.date())
```

---

## Current Time

```python
print(datetime.now().time())
```

---

## Format Date

```python
today = datetime.now()

print(today.strftime("%d-%m-%Y"))
```

Output

```text
03-07-2026
```

---

## Format Time

```python
print(today.strftime("%H:%M:%S"))
```

---

## Extract Year

```python
print(today.year)
```

---

## Extract Month

```python
print(today.month)
```

---

## Extract Day

```python
print(today.day)
```

---

# 🌐 The `requests` Library

`requests` is one of the most popular Python libraries.

Used for:

- Calling APIs
- Fetching weather
- AI APIs
- OpenAI API
- Gemini API
- Hugging Face API

---

## Installation

```bash
pip install requests
```

---

## Import

```python
import requests
```

---

## GET Request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)
```

---

## JSON Response

```python
data = response.json()

print(data[0])
```

---

## Print Title

```python
print(data[0]["title"])
```

---

## POST Request

```python
import requests

data = {
    "name": "John"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data
)

print(response.json())
```

---

## Response Status Codes

| Code | Meaning |
|--------|----------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# 💻 Mini Project

# File Organizer

## Objective

Automatically organize files into folders.

Example

```
Downloads/

photo.png
notes.pdf
movie.mp4
song.mp3
```

After execution

```
Downloads/

Images/
Videos/
PDFs/
Music/
```

---

## Sample Solution

```python
import os
import shutil

folder = "Downloads"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    if file.endswith(".png"):
        os.makedirs("Images", exist_ok=True)
        shutil.move(path, "Images")

    elif file.endswith(".pdf"):
        os.makedirs("PDFs", exist_ok=True)
        shutil.move(path, "PDFs")
```

---

# 📝 Practice Questions

### Easy

1. Print current directory
2. Create folder
3. Rename folder
4. Delete folder
5. Print current date

---

### Medium

6. Print file size
7. Print formatted date
8. Fetch JSON from API
9. Print API status code
10. Build date formatter

---

### Advanced

11. File Organizer
12. Weather API App
13. News API App
14. Currency Converter
15. API Logger

---

# 🎤 Interview Questions

## Beginner

### 1. What is the `os` module?

Used for interacting with the operating system.

---

### 2. What does `os.getcwd()` do?

Returns the current working directory.

---

### 3. Difference between `os.mkdir()` and `os.makedirs()`?

`mkdir()` creates one directory.

`makedirs()` creates nested directories.

---

### 4. What is `datetime.now()`?

Returns current date and time.

---

### 5. What is `strftime()`?

Formats dates into readable strings.

---

### 6. Why use `requests`?

To communicate with web servers and APIs.

---

### 7. What is an API?

Application Programming Interface that allows software to communicate.

---

### 8. Difference between GET and POST?

GET retrieves data.

POST sends data.

---

### 9. What is JSON?

JavaScript Object Notation used for data exchange.

---

### 10. What does `response.json()` do?

Converts JSON response into a Python dictionary or list.

---

## Intermediate

### 11. Explain HTTP Status Codes.

- 200 Success
- 404 Not Found
- 500 Server Error

---

### 12. Why use APIs in AI?

To communicate with LLMs like OpenAI and Gemini.

---

### 13. Difference between JSON and Dictionary?

JSON is a text format.

Dictionary is a Python object.

---

### 14. What is REST API?

An API that follows REST architecture using HTTP methods.

---

### 15. Which HTTP methods do you know?

- GET
- POST
- PUT
- PATCH
- DELETE

---

# ⭐ Best Practices

- Always handle exceptions while making API calls.
- Check HTTP status codes.
- Use meaningful variable names.
- Keep API keys secure.
- Avoid hardcoding file paths.
- Organize code into functions.

---

# 📚 Resources

## Official Documentation

- Python `os` Module: https://docs.python.org/3/library/os.html
- Python `datetime`: https://docs.python.org/3/library/datetime.html
- Requests Library: https://requests.readthedocs.io/

## Free Resources

- freeCodeCamp Python Course
- W3Schools Python
- Real Python

---

# 🏆 Assignment

Build a **Smart File Organizer** that:

- Organizes Images
- Organizes PDFs
- Organizes Videos
- Organizes Music
- Prints Summary Report
- Uses `os` module
- Uses Functions

Bonus:

- Add date-based folders using `datetime`.

---

# 📌 Day 22 Summary

Today you learned:

- Python Standard Libraries
- `os`
- `datetime`
- `requests`
- API Basics
- HTTP Methods
- JSON Responses
- File Organizer Project

---

# 🚀 GitHub Commit Message

```bash
git add .
git commit -m "Day 22: Learned Python Standard Libraries (os, datetime, requests) and built a File Organizer"
git push origin main
```

---

# ⏭️ Next Day

## Day 23 - Working with REST APIs

Topics:

- API Fundamentals
- HTTP Methods
- REST Architecture
- API Authentication
- API Parameters
- JSON Parsing
- Error Handling
- Build a Weather Application using a Public API