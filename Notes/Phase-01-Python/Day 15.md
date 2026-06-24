# Day 15 - File Handling in Python

> Phase 1: Programming Foundation
>
> Roadmap: AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand what file handling is
- Create, read, write, and append files
- Work with text files
- Use different file modes
- Use the `with` statement
- Handle file-related exceptions
- Build a Notes Management Application
- Answer File Handling interview questions confidently

---

# 📌 What is File Handling?

File Handling is the process of:

- Creating files
- Reading files
- Writing files
- Updating files
- Deleting files

It allows data to be stored permanently even after the program ends. File handling is essential for data persistence, logs, configuration files, datasets, and automation scripts. :contentReference[oaicite:0]{index=0}

---

# Why File Handling Matters

Without files:

❌ Data is lost when program stops

With files:

✅ Data remains stored permanently

Real-world applications use files for:

- User data
- Logs
- Reports
- Configurations
- Datasets
- Machine Learning data

---

# File Handling Workflow

```text
Open File
     ↓
Read / Write Data
     ↓
Close File
```

Python provides the built-in `open()` function for working with files. :contentReference[oaicite:1]{index=1}

---

# Opening a File

Syntax:

```python
file = open("filename.txt", "mode")
```

Example:

```python
file = open("notes.txt", "r")
```

---

# File Modes

| Mode | Description |
|--------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |
| r+ | Read and Write |

Python's common file modes include read (`r`), write (`w`), and append (`a`). :contentReference[oaicite:2]{index=2}

---

# Reading Files

---

## read()

Reads entire file.

```python
file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()
```

---

# Example

Suppose file contains:

```text
Hello
Welcome to Python
```

Output:

```text
Hello
Welcome to Python
```

---

# readline()

Reads one line at a time.

```python
file = open("notes.txt", "r")

line = file.readline()

print(line)

file.close()
```

---

# readlines()

Returns list of lines.

```python
file = open("notes.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

Output:

```python
['Hello\n', 'Welcome to Python\n']
```

---

# Writing Files

Used to create or overwrite a file.

```python
file = open("notes.txt", "w")

file.write("Hello Python")

file.close()
```

---

# Important

If file exists:

```python
"w"
```

will overwrite existing content. :contentReference[oaicite:3]{index=3}

---

# Appending Data

Append adds data without deleting existing content.

```python
file = open("notes.txt", "a")

file.write("\nNew Note Added")

file.close()
```

---

# Creating a New File

```python
file = open("newfile.txt", "x")

file.close()
```

---

# Using with Statement

Best Practice ✅

```python
with open("notes.txt", "r") as file:
    data = file.read()
    print(data)
```

Benefits:

- Automatically closes file
- Cleaner code
- Safer

The `with open(...)` pattern is considered the safest and most recommended way to work with files in Python. :contentReference[oaicite:4]{index=4}

---

# File Closing

Manual:

```python
file.close()
```

Automatic:

```python
with open(...)
```

---

# Checking File Position

tell()

```python
with open("notes.txt", "r") as file:

    print(file.tell())
```

Output:

```text
0
```

---

# Moving Cursor

seek()

```python
with open("notes.txt", "r") as file:

    file.seek(5)

    print(file.read())
```

---

# Example

File:

```text
Hello Python
```

Output:

```text
Python
```

---

# Handling File Exceptions

---

## File Not Found

```python
try:

    file = open("data.txt", "r")

except FileNotFoundError:

    print("File Not Found")
```

File-related exceptions such as `FileNotFoundError` should be handled to prevent application crashes. :contentReference[oaicite:5]{index=5}

---

# Complete Example

```python
try:

    with open("data.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File Not Found")

finally:

    print("Operation Completed")
```

---

# Writing Multiple Lines

```python
with open("notes.txt", "w") as file:

    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
```

---

# Reading File Line by Line

```python
with open("notes.txt", "r") as file:

    for line in file:

        print(line.strip())
```

Reading large files line-by-line is more memory efficient than reading the entire file at once. :contentReference[oaicite:6]{index=6}

---

# Mini Project

# Notes Management System

---

# Requirements

- Add Notes
- View Notes
- Store Notes in File
- Exit Program

---

# Solution

```python
while True:

    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose Option: ")

    if choice == "1":

        note = input("Enter Note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note Saved")

    elif choice == "2":

        try:

            with open("notes.txt", "r") as file:

                print("\nYour Notes:")
                print(file.read())

        except FileNotFoundError:

            print("No Notes Found")

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid Choice")
```

---

# Practice Questions

## Easy

1. Create a text file.
2. Write data into a file.
3. Read data from file.
4. Append data into file.
5. Use with statement.

---

## Medium

6. Create Notes App.
7. Create Student Record File.
8. Read line by line.
9. Use seek().
10. Use tell().

---

## Advanced

11. Create Log Management System.
12. Create Attendance System.
13. Create Expense Tracker using files.
14. Create File Search Utility.
15. Build CLI Note Taking Application.

---

# Real World Use Cases

---

## Application Logs

```python
with open("app.log", "a") as file:
    file.write("User Logged In\n")
```

---

## Saving User Data

```python
with open("users.txt", "a") as file:
    file.write(username)
```

---

## Machine Learning Dataset Loading

```python
with open("dataset.csv", "r") as file:
    data = file.read()
```

Machine learning and data processing workflows frequently rely on reading structured data from files such as CSVs and text files. :contentReference[oaicite:7]{index=7}

---

# Interview Questions

# Beginner Level

## 1. What is File Handling?

File Handling is the process of reading, writing, creating, and managing files.

---

## 2. Why is File Handling important?

It helps store data permanently.

---

## 3. What is open()?

A built-in Python function used to open files.

---

## 4. What is the default file mode?

```python
r
```

(Read Mode)

---

## 5. Difference between read() and readline()?

| read() | readline() |
|----------|------------|
| Entire file | One line |

---

## 6. What is write()?

Used to write data to file.

---

## 7. What is append mode?

Adds data without removing existing content.

---

## 8. What is close()?

Used to close opened files.

---

## 9. Why use with statement?

Automatically closes files.

---

## 10. What happens if file doesn't exist in read mode?

```python
FileNotFoundError
```

---

# Intermediate Level

## 11. Difference between write() and writelines()?

| write() | writelines() |
|-----------|-------------|
| Single string | Multiple strings |

---

## 12. What does seek() do?

Moves file cursor position.

---

## 13. What does tell() do?

Returns current cursor position.

---

## 14. Difference between w and a mode?

| w | a |
|-----|-----|
| Overwrites | Adds data |

---

## 15. Difference between text and binary files?

| Text File | Binary File |
|------------|-------------|
| Human Readable | Machine Readable |

---

# Advanced Level

## 16. Why is with statement preferred?

Because it automatically manages file closing and resource cleanup. :contentReference[oaicite:8]{index=8}

---

## 17. How do you handle file exceptions?

Using:

```python
try
except
```

---

## 18. What is FileNotFoundError?

Occurs when file does not exist.

---

## 19. How do you read large files efficiently?

Read line by line using:

```python
for line in file:
```

:contentReference[oaicite:9]{index=9}

---

## 20. What are best practices in File Handling?

- Use with statement
- Close files properly
- Handle exceptions
- Use correct file modes
- Validate file paths

---

# Real Interview Questions

### Q1: Explain Python file modes.

### Q2: Difference between read(), readline(), and readlines()?

### Q3: Why is with open() preferred?

### Q4: What is seek() and tell()?

### Q5: Difference between write and append?

### Q6: How do you handle missing files?

### Q7: Explain FileNotFoundError.

### Q8: What are binary files?

### Q9: How would you process a large file?

### Q10: What are best practices for file handling?

---

# Day 15 Summary

Today you learned:

✅ File Handling Basics

✅ Opening Files

✅ Reading Files

✅ Writing Files

✅ Appending Files

✅ File Modes

✅ with Statement

✅ seek()

✅ tell()

✅ Exception Handling

✅ Notes Management Project

✅ Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 15: Learned Python File Handling and Built Notes Management System"
git push origin main
```

---

# 🚀 Next Day

**Day 16: Working with CSV Files**

Topics:

- CSV Files
- csv Module
- Reading CSV
- Writing CSV
- Student Record Management System
- CSV Interview Questions