# Day 16 - Working with CSV Files in Python

> Phase 1: Programming Foundation  
> Roadmap: AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand CSV files
- Read CSV files using Python
- Write data to CSV files
- Use csv.reader()
- Use csv.writer()
- Use DictReader()
- Use DictWriter()
- Handle CSV file exceptions
- Build a Student Result Management System
- Answer CSV interview questions confidently

---

# 📌 What is a CSV File?

CSV stands for:

**Comma Separated Values**

A CSV file is a plain text file used to store tabular data.

Example:

```csv
id,name,age
1,John,20
2,Alice,21
3,Bob,22
```

CSV files are commonly used for:

- Data Analysis
- Machine Learning
- Data Migration
- Excel Data Exchange
- Database Import/Export

Python provides a built-in `csv` module to read and write CSV files easily. :contentReference[oaicite:0]{index=0}

---

# Why CSV Files Matter

In AI and Data Science:

- Most datasets are provided as CSV files
- Pandas reads CSV files
- Machine Learning models often train on CSV datasets
- Data engineers exchange data using CSV

Examples:

- Student Data
- Sales Data
- Employee Records
- Customer Information
- Stock Market Data

---

# CSV Module

Python provides a built-in module:

```python
import csv
```

The csv module allows:

- Reading CSV files
- Writing CSV files
- Reading dictionaries
- Writing dictionaries

:contentReference[oaicite:1]{index=1}

---

# Creating a CSV File

Example:

```csv
student.csv
```

```csv
id,name,course
1,John,Python
2,Alice,AI
3,Bob,Data Science
```

---

# Reading CSV Files

## csv.reader()

```python
import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### Output

```text
['id', 'name', 'course']
['1', 'John', 'Python']
['2', 'Alice', 'AI']
['3', 'Bob', 'Data Science']
```

The `csv.reader()` method reads rows as lists. :contentReference[oaicite:2]{index=2}

---

# Skipping Header Row

```python
import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

### Output

```text
['1', 'John', 'Python']
['2', 'Alice', 'AI']
['3', 'Bob', 'Data Science']
```

---

# Accessing Individual Columns

```python
import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print("Name:", row[1])
```

### Output

```text
Name: John
Name: Alice
Name: Bob
```

---

# Writing CSV Files

## csv.writer()

```python
import csv

with open("employee.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Department"])

    writer.writerow([1, "John", "HR"])

    writer.writerow([2, "Alice", "IT"])
```

This creates:

```csv
ID,Name,Department
1,John,HR
2,Alice,IT
```

:contentReference[oaicite:3]{index=3}

---

# Writing Multiple Rows

```python
import csv

data = [
    ["ID", "Name", "Course"],
    [1, "John", "Python"],
    [2, "Alice", "AI"],
    [3, "Bob", "ML"]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(data)
```

---

# DictReader()

Reads CSV rows as dictionaries.

Example CSV:

```csv
name,age,course
John,20,Python
Alice,21,AI
```

---

## Example

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

### Output

```python
{
 'name': 'John',
 'age': '20',
 'course': 'Python'
}
```

`DictReader` uses the first row as keys. :contentReference[oaicite:4]{index=4}

---

# Access Dictionary Values

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Output:

```text
John
Alice
```

---

# DictWriter()

Writes dictionaries to CSV files.

```python
import csv

with open("employees.csv", "w", newline="") as file:

    fields = ["name", "department"]

    writer = csv.DictWriter(
        file,
        fieldnames=fields
    )

    writer.writeheader()

    writer.writerow({
        "name": "John",
        "department": "HR"
    })

    writer.writerow({
        "name": "Alice",
        "department": "IT"
    })
```

:contentReference[oaicite:5]{index=5}

---

# Appending Data to CSV

```python
import csv

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([4, "David", "ML"])
```

Mode:

```python
"a"
```

means Append.

---

# Handling CSV Exceptions

```python
import csv

try:

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:

    print("File not found")
```

---

# Real World Example

# Employee Records

```csv
id,name,salary
1,John,50000
2,Alice,60000
3,Bob,70000
```

Read and calculate total salary.

```python
import csv

total = 0

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["salary"])

print(total)
```

---

# Mini Project

# Student Result Management System

---

# Requirements

- Add Student
- View Students
- Save Data in CSV
- Read Data from CSV
- Handle Exceptions

---

# Project Solution

```python
import csv

FILE_NAME = "students.csv"


def add_student():

    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([name, marks])

    print("Student Added Successfully")


def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            print("\nStudent Records\n")

            for row in reader:
                print(row)

    except FileNotFoundError:

        print("No Records Found")


while True:

    print("\n===== Student Result System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")
```

---

# Practice Questions

## Easy

1. Create a CSV file manually.
2. Read CSV using csv.reader().
3. Print all rows.
4. Print specific columns.
5. Write data into CSV.

---

## Medium

6. Add employee records.
7. Create attendance system.
8. Append new records.
9. Read data using DictReader.
10. Write dictionaries using DictWriter.

---

## Advanced

11. Student Management System.
12. Inventory Management System.
13. Sales Report Generator.
14. Employee Payroll System.
15. CSV Data Analytics Tool.

---

# Common CSV Methods

| Method | Purpose |
|----------|----------|
| csv.reader() | Read CSV |
| csv.writer() | Write CSV |
| writerow() | Write single row |
| writerows() | Write multiple rows |
| DictReader() | Read as dictionary |
| DictWriter() | Write dictionary |
| writeheader() | Write header row |

---

# Interview Questions

## Beginner Level

### 1. What is a CSV file?

A CSV (Comma Separated Values) file stores tabular data in plain text format.

---

### 2. Why are CSV files used?

Because they are lightweight, easy to read, and supported by Excel, databases, and programming languages. :contentReference[oaicite:6]{index=6}

---

### 3. Which module is used to work with CSV files?

```python
import csv
```

---

### 4. What does csv.reader() do?

Reads CSV file rows as lists.

---

### 5. What does csv.writer() do?

Writes data into CSV files.

---

### 6. What is DictReader()?

Reads rows as dictionaries.

---

### 7. What is DictWriter()?

Writes dictionaries into CSV files.

---

### 8. Difference between reader and DictReader?

| reader() | DictReader() |
|-----------|-------------|
| Returns List | Returns Dictionary |

---

### 9. Why use newline="" while writing CSV?

Prevents extra blank lines.

---

### 10. What is writerows()?

Used to write multiple rows at once.

---

# Intermediate Level

### 11. Difference between CSV and Excel?

| CSV | Excel |
|------|------|
| Plain Text | Spreadsheet Format |
| Lightweight | Heavy |
| Faster | Rich Features |

---

### 12. How to append data to CSV?

```python
open(file, "a")
```

---

### 13. How to skip header row?

```python
next(reader)
```

---

### 14. How to handle missing CSV files?

```python
try:
except FileNotFoundError:
```

---

### 15. Why is CSV important in Data Science?

Most datasets are distributed in CSV format and can be loaded directly into tools like Pandas. :contentReference[oaicite:7]{index=7}

---

# Advanced Level

### 16. What are the limitations of CSV?

- No relationships
- No data types
- No security
- No indexing

CSV is simple but lacks database-like features. :contentReference[oaicite:8]{index=8}

---

### 17. Difference between CSV and Database?

| CSV | Database |
|------|-----------|
| File Based | Server Based |
| No Relationships | Relationships |
| Small Data | Large Data |

---

### 18. What is a CSV dialect?

A set of formatting rules used by the csv module. :contentReference[oaicite:9]{index=9}

---

### 19. How does Python handle large CSV files?

By reading rows one at a time instead of loading everything into memory.

---

### 20. Why learn CSV before Pandas?

Because Pandas internally works with CSV datasets very frequently, and understanding CSV fundamentals makes data analysis easier.

---

# Day 16 Summary

Today you learned:

✅ CSV Files

✅ csv Module

✅ csv.reader()

✅ csv.writer()

✅ DictReader()

✅ DictWriter()

✅ Reading CSV Files

✅ Writing CSV Files

✅ Appending Data

✅ Exception Handling

✅ Student Result Management System

✅ CSV Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 16: Learned CSV File Handling and Built Student Result Management System"
git push origin main
```

---

# 🚀 Next Day

**Day 17: Working with JSON Files in Python**

Topics:

- JSON Basics
- json Module
- json.load()
- json.dump()
- Reading JSON
- Writing JSON
- Configuration Management Project
- JSON Interview Questions