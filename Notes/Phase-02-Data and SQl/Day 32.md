# Day 32 - SQL Fundamentals & Database Basics (Section A)

> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📌 Table of Contents

1. Introduction
2. Learning Objectives
3. What is Data?
4. What is Information?
5. Data vs Information
6. What is a Database?
7. Why Do We Need Databases?
8. Real-Life Examples of Databases
9. What is DBMS?
10. Advantages of DBMS
11. Limitations of File System
12. File System vs DBMS
13. What is RDBMS?
14. Features of RDBMS
15. DBMS vs RDBMS
16. Why AI Engineers Must Learn SQL
17. SQL vs MySQL vs PostgreSQL
18. Popular Database Systems
19. Database Terminologies
20. Real-World AI Use Cases
21. Summary

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what data actually is.
- Understand how databases work.
- Differentiate DBMS and RDBMS.
- Know why SQL is essential for AI Engineers.
- Understand SQL, MySQL, and PostgreSQL.
- Understand where databases are used in real life.
- Prepare for SQL interview fundamentals.

---

# 🚀 Introduction

Imagine Instagram.

Every second:

- Millions of users log in.
- Millions of photos are uploaded.
- Millions of likes are added.
- Millions of comments are written.

Where is all this information stored?

Certainly **not inside Python variables**.

It is stored inside **Databases**.

Every AI application also needs databases.

For example:

- ChatGPT stores conversations.
- Netflix stores watch history.
- Amazon stores products.
- Swiggy stores orders.
- Uber stores rides.
- Banking apps store transactions.

Without databases, modern software simply cannot exist.

---

# 📖 What is Data?

Data is a collection of raw facts.

Data has **no meaning** until it is processed.

### Examples

```
John
21
95
Delhi
```

This is just raw data.

---

Another example:

```
101
102
103
104
```

These are just numbers.

No meaning.

---

Another example:

```
98
74
82
65
91
```

Again, just data.

---

# 📖 What is Information?

When data is organized and becomes meaningful,
it becomes **Information**.

Example:

| Name | Marks |
|------|------|
| John | 95 |
| Alice | 90 |
| Bob | 82 |

Now we understand what those numbers mean.

This is **Information**.

---

# 📊 Data vs Information

| Data | Information |
|------|-------------|
| Raw facts | Processed facts |
| No context | Has meaning |
| Hard to understand | Easy to understand |
| Example: 95 | Example: John's marks are 95 |

---

# 🏦 What is a Database?

A Database is an organized collection of related data that can be easily stored, searched, updated, and managed.

Think of it as a **digital cupboard**.

Instead of storing papers physically, everything is stored electronically.

---

### Simple Definition

> A database is a place where information is stored in an organized manner.

---

# Real-Life Example

Imagine your college.

Thousands of students.

Each student has

- Name
- Roll Number
- Address
- Marks
- Attendance
- Fees

Can this be stored in notebooks?

No.

It would become impossible to manage.

Instead, colleges use databases.

---

# Another Example

Think about YouTube.

Every video stores:

- Title
- Description
- Views
- Likes
- Comments
- Channel Name
- Upload Date

All of this is stored in databases.

---

# Another Example

Amazon stores

- Products
- Prices
- Sellers
- Customers
- Orders
- Payments
- Reviews

Without databases, Amazon would stop working.

---

# Why Do We Need Databases?

Imagine storing customer details inside Excel.

```
Customer 1

Customer 2

Customer 3

...

Customer 5,00,000
```

Problems:

❌ Slow

❌ Duplicate data

❌ Difficult searching

❌ Difficult updating

❌ Difficult deleting

Databases solve all these problems.

---

# Advantages of Databases

✅ Fast searching

✅ Secure

✅ Reliable

✅ Easy backup

✅ Easy recovery

✅ Handles millions of records

✅ Supports multiple users

✅ Less duplication

---

# Real-Life Database Examples

## Banking

Stores:

- Customer Accounts
- Transactions
- Balance
- Loans

---

## Hospital

Stores:

- Patients
- Doctors
- Medicines
- Reports

---

## School

Stores:

- Students
- Teachers
- Attendance
- Marks

---

## Netflix

Stores:

- Movies
- Ratings
- Watch History
- Users

---

## Spotify

Stores:

- Songs
- Playlists
- Artists

---

## Google Maps

Stores

- Roads
- Locations
- Traffic
- Reviews

---

# 📚 What is DBMS?

DBMS stands for

**Database Management System**

It is software that helps us create, manage, update, and retrieve data from databases.

Think of DBMS as a **manager**.

Database = Warehouse

DBMS = Warehouse Manager

---

# Real-Life Analogy

Imagine a library.

Books are the data.

The librarian is the DBMS.

Students ask:

"I need Harry Potter."

The librarian searches and gives it.

Similarly,

Application asks:

"Show customer details."

DBMS finds them.

---

# Examples of DBMS

- MySQL
- Oracle
- PostgreSQL
- SQL Server
- SQLite

---

# Responsibilities of DBMS

DBMS performs

- Data Storage
- Data Retrieval
- Data Update
- Data Deletion
- Security
- Backup
- Recovery

---

# Advantages of DBMS

## 1. Security

Only authorized users can access data.

---

## 2. Backup

Data can be restored.

---

## 3. Data Sharing

Many users can use the database simultaneously.

---

## 4. Reduced Redundancy

Duplicate data is minimized.

---

## 5. Better Consistency

Same data everywhere.

---

## 6. Easy Maintenance

Updating records becomes simple.

---

# Problems with Traditional File System

Before databases, people stored information in files.

Example:

```
students.txt
```

```
John

21

95

Delhi
```

Problems:

- Duplicate records
- Difficult searching
- Difficult updating
- Difficult deletion
- No relationships
- No security
- Data corruption

---

# File System vs DBMS

| File System | DBMS |
|-------------|------|
| Slow | Fast |
| Less secure | Highly secure |
| Difficult search | Easy search |
| Duplicate data | Minimal duplication |
| No relationships | Relationships supported |
| Manual backup | Automatic backup |

---

# What is RDBMS?

RDBMS stands for

**Relational Database Management System**

It stores data in the form of tables.

Each table has

Rows

and

Columns

Example

| ID | Name | Age |
|----|------|-----|
|1|John|21|
|2|Alice|22|

This is called a **Table**.

---

# Why "Relational"?

Because tables are related to each other.

Example

Students Table

| StudentID | Name |
|------------|------|
|1|John|

Courses Table

| StudentID | Course |
|------------|--------|
|1|Python|

Both tables are connected.

This relationship makes querying powerful.

---

# Features of RDBMS

✅ Tables

✅ Relationships

✅ Primary Keys

✅ Foreign Keys

✅ Constraints

✅ Transactions

✅ High Security

---

# DBMS vs RDBMS

| DBMS | RDBMS |
|------|--------|
| Stores data | Stores data in tables |
| Relationships not mandatory | Relationships supported |
| Less secure | Highly secure |
| Less efficient | Highly efficient |
| No foreign keys | Supports foreign keys |

---

# Why AI Engineers Must Learn SQL

Many beginners think:

> "I'm learning AI. Why should I learn SQL?"

Because almost every AI project begins with **data**.

Where does data come from?

Databases.

Examples:

- Customer purchase history
- Chat history
- Medical records
- Sales reports
- Employee information
- Sensor data
- Financial transactions

Before training a Machine Learning model, you first **extract data using SQL**.

---

# Real AI Workflow

```text
Database
      │
      ▼
SQL Query
      │
      ▼
Pandas DataFrame
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
```

Without SQL, you cannot efficiently retrieve and prepare the data needed for AI.

---

# SQL vs MySQL vs PostgreSQL

Many beginners confuse these terms.

## SQL

SQL stands for **Structured Query Language**.

It is a language used to communicate with relational databases.

Think of SQL as **English**.

---

## MySQL

MySQL is a **Database Management System** that understands SQL.

Think of it as a person who understands English.

---

## PostgreSQL

PostgreSQL is another Database Management System that also understands SQL.

It offers more advanced features and is widely used for enterprise applications and data-intensive workloads.

---

# Comparison

| Feature | SQL | MySQL | PostgreSQL |
|----------|-----|--------|------------|
| Type | Language | Database Software | Database Software |
| Purpose | Write Queries | Store & Manage Data | Store & Manage Data |
| Uses SQL | — | Yes | Yes |
| Open Source | Standard | Yes | Yes |

---

# Popular Database Systems

| Database | Used For |
|----------|----------|
| MySQL | Web Applications |
| PostgreSQL | Enterprise & Analytics |
| SQLite | Mobile Apps |
| Oracle | Large Enterprises |
| Microsoft SQL Server | Business Applications |
| MariaDB | Open-Source Web Apps |

---

# Important Database Terminologies

| Term | Meaning |
|------|---------|
| Database | Collection of related data |
| Table | Collection of rows and columns |
| Row | One complete record |
| Column | One attribute of data |
| Record | Another name for a row |
| Field | Another name for a column value |

---

# Real-World AI Use Cases

### 🤖 Chatbot

Stores:

- User messages
- Conversation history
- Feedback
- Session IDs

---

### 🛒 E-commerce Recommendation System

Stores:

- Customer orders
- Products
- Categories
- Ratings
- Wishlist

AI uses this data to recommend products.

---

### 🎬 Netflix Recommendation Engine

Stores:

- Watch history
- Ratings
- Genres
- User preferences

Machine Learning models analyze this data to suggest movies.

---

### 🏥 Medical Diagnosis System

Stores:

- Patient records
- Symptoms
- Test reports
- Diagnoses

AI models learn from this structured data to assist doctors.

---

# 📌 Section A Summary

Today you learned:

- What is Data
- What is Information
- Data vs Information
- What is a Database
- Why Databases are important
- DBMS
- RDBMS
- DBMS vs RDBMS
- SQL vs MySQL vs PostgreSQL
- Why SQL is essential for AI Engineers
- Common database terminology
- Real-world AI database use cases

---

## 🚀 Up Next (Section B)

In the next section, you'll learn:

- Installing MySQL
- MySQL Workbench Setup
- SQL Syntax Rules
- SQL Data Types
- CREATE DATABASE
- SHOW DATABASES
- USE DATABASE
- DROP DATABASE
- Hands-on SQL Commands
- Practical Exercises


# ⚙️ Day 32 – Section B
# MySQL Installation, SQL Syntax, Data Types & Database Operations

> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Install MySQL Community Server
- Install MySQL Workbench
- Connect to your database
- Understand SQL syntax
- Learn SQL naming conventions
- Understand SQL data types
- Create databases
- View databases
- Select databases
- Delete databases
- Follow SQL best practices

---

# 💻 Installing MySQL

Before writing SQL queries, you need a database management system.

The most popular options are:

- MySQL
- PostgreSQL
- MariaDB
- SQLite

For this roadmap, we will use **MySQL Community Edition** because it is beginner-friendly and widely used.

---

# Step 1 — Download MySQL Community Server

Visit:

https://dev.mysql.com/downloads/mysql/

Download:

- MySQL Community Server

Choose:

- Windows
- macOS
- Linux

depending on your operating system.

---

# Step 2 — Install MySQL

During installation:

✔ Install Server

✔ Install Workbench

✔ Install Shell

✔ Install Connector

Set a password for the **root** user.

Example:

```
Username:
root

Password:
********
```

Remember this password.

---

# Step 3 — Install MySQL Workbench

Workbench is a GUI (Graphical User Interface).

Instead of typing commands in terminal, Workbench provides:

- SQL Editor
- Database Explorer
- Table Viewer
- Query History
- Data Import
- Data Export

Think of Workbench as VS Code for SQL.

---

# Step 4 — Connect to MySQL

Open MySQL Workbench.

Create a connection.

Example:

```
Connection Name:
Localhost

Hostname:
127.0.0.1

Port:
3306

Username:
root
```

Click

```
Test Connection
```

If successful:

```
Successfully made the MySQL connection
```

---

# Understanding SQL Query Editor

The SQL Editor is where we write SQL commands.

Example:

```sql
SELECT "Hello World";
```

Output

```
Hello World
```

Congratulations!

You have executed your first SQL query.

---

# SQL Syntax

SQL is easy to read because it uses English-like commands.

Example:

```sql
SELECT * FROM students;
```

Breakdown

```
SELECT

means

Fetch data

*

means

Everything

FROM

means

From which table?

students

Table Name
```

---

# SQL Keywords

Keywords are reserved words.

Examples

```sql
SELECT

FROM

WHERE

INSERT

UPDATE

DELETE

CREATE

DROP

ALTER

ORDER BY

GROUP BY
```

Always write keywords in uppercase.

Example

Good

```sql
SELECT * FROM students;
```

Bad

```sql
select * from students;
```

Although SQL ignores case, uppercase improves readability.

---

# SQL Statements End with Semicolon

Every SQL statement ends with

```
;
```

Example

```sql
CREATE DATABASE school;
```

---

# SQL is Case Insensitive

These are identical.

```sql
SELECT * FROM students;
```

```sql
select * from students;
```

```sql
SeLeCt * FrOm students;
```

But use uppercase for keywords.

---

# SQL Comments

Single-line comment

```sql
-- This is a comment
```

Multi-line comment

```sql
/*
This is
multiple line
comment
*/
```

Comments improve code readability.

---

# SQL Naming Conventions

Good

```text
student

student_details

employee_salary
```

Bad

```text
abc

test1

table123

student details
```

Best Practices

✔ lowercase

✔ underscores

✔ meaningful names

---

# SQL Data Types

Every column must have a data type.

Think of data type as the kind of information a column can store.

---

# Numeric Data Types

## INT

Stores whole numbers.

Example

```sql
age INT
```

Values

```
18

25

100
```

---

## BIGINT

Stores very large integers.

Example

```sql
population BIGINT
```

---

## FLOAT

Stores decimal numbers.

Example

```sql
height FLOAT
```

Values

```
5.8

172.5
```

---

## DOUBLE

Higher precision decimal.

Example

```sql
salary DOUBLE
```

---

## DECIMAL

Used for money.

Example

```sql
price DECIMAL(10,2)
```

Output

```
99999.99
```

---

# String Data Types

## CHAR

Fixed length.

```sql
gender CHAR(1)
```

Values

```
M

F
```

---

## VARCHAR

Most commonly used.

Stores variable-length strings.

```sql
name VARCHAR(100)
```

Values

```
Rahul

John

Priya
```

---

## TEXT

Stores large text.

Example

```sql
description TEXT
```

---

# Date Data Types

## DATE

Stores only date.

```sql
dob DATE
```

Output

```
2002-10-15
```

---

## TIME

Stores time.

```sql
login_time TIME
```

Output

```
14:30:20
```

---

## DATETIME

Stores date and time.

```sql
created_at DATETIME
```

Output

```
2026-07-14 19:30:00
```

---

## TIMESTAMP

Automatically stores current timestamp.

Useful for

- Created At
- Updated At

---

# Boolean

Stores

```
TRUE

FALSE
```

Example

```sql
is_active BOOLEAN
```

---

# Choosing the Correct Data Type

| Data | Type |
|-------|------|
| Age | INT |
| Name | VARCHAR |
| Gender | CHAR |
| Salary | DECIMAL |
| Description | TEXT |
| Date of Birth | DATE |
| Login Time | TIME |
| Created At | DATETIME |

---

# CREATE DATABASE

Creates a new database.

Syntax

```sql
CREATE DATABASE database_name;
```

Example

```sql
CREATE DATABASE school;
```

Output

```
Query OK
```

Database created.

---

# SHOW DATABASES

Displays all databases.

```sql
SHOW DATABASES;
```

Output

```
information_schema

mysql

performance_schema

school
```

---

# USE DATABASE

Select a database before creating tables.

Syntax

```sql
USE database_name;
```

Example

```sql
USE school;
```

Output

```
Database Changed
```

Now every table will be created inside

```
school
```

---

# DROP DATABASE

Deletes an entire database permanently.

Syntax

```sql
DROP DATABASE database_name;
```

Example

```sql
DROP DATABASE school;
```

⚠ Warning

Everything inside the database will be deleted permanently.

Use carefully.

---

# IF EXISTS

Avoid errors while deleting.

```sql
DROP DATABASE IF EXISTS school;
```

---

# CREATE DATABASE IF NOT EXISTS

Avoid duplicate database errors.

```sql
CREATE DATABASE IF NOT EXISTS school;
```

---

# Viewing Current Database

```sql
SELECT DATABASE();
```

Output

```
school
```

---

# Best Practices

✅ Use meaningful database names

```
college_db

hospital_db

employee_db
```

Instead of

```
test

abc

new
```

---

✅ Keep names lowercase.

Good

```
student_management
```

Bad

```
StudentManagement
```

---

✅ Use underscores.

```
employee_management
```

---

# Common Beginner Mistakes

❌ Forgetting semicolon

Wrong

```sql
CREATE DATABASE school
```

Correct

```sql
CREATE DATABASE school;
```

---

❌ Forgetting USE command

Wrong

```sql
CREATE TABLE students(...)
```

Correct

```sql
USE school;

CREATE TABLE students(...);
```

---

❌ Using spaces in database names

Wrong

```
Student Database
```

Correct

```
student_database
```

---

# Hands-on Exercise

Create the following databases:

```
college_db

hospital_db

library_db

bank_db

ecommerce_db
```

Then:

1. Show all databases.
2. Select `college_db`.
3. Verify the current database.
4. Delete `library_db`.
5. Show databases again.

---

# Mini Challenge

Design databases for:

- School Management System
- Hospital Management System
- Online Shopping Website
- Banking Application
- Movie Ticket Booking System

Think about what tables each database might need. You'll create those tables in the next section.

---

# What's Next?

In **Day 32 – Section C**, you'll learn:

- `CREATE TABLE`
- Constraints (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `AUTO_INCREMENT`)
- Table Design Best Practices
- 25+ Interview Questions
- Practice Exercises
- Mini Assignment
- Day Summary
- GitHub Commit Message

Happy Learning! 🚀

# 🌍 Real-World SQL Examples

SQL is everywhere! Almost every application you use stores its data in a database and retrieves it using SQL.

---

# 🏦 1. Banking System

Imagine you have a banking application.

Instead of storing customer information in Python variables, banks use databases.

### Customers Table

| Customer ID | Name | Balance |
|-------------|------|----------|
| 101 | Rahul | ₹50,000 |
| 102 | Priya | ₹1,20,000 |
| 103 | Aman | ₹75,000 |

### SQL Query

```sql
SELECT * FROM Customers;
```

### Output

```text
101 Rahul 50000
102 Priya 120000
103 Aman 75000
```

---

# 🛒 2. Amazon

Amazon stores millions of products.

### Products Table

| Product ID | Name | Price |
|------------|------|-------|
| 1 | Laptop | 65000 |
| 2 | Mouse | 700 |
| 3 | Keyboard | 1500 |

To view all products:

```sql
SELECT * FROM Products;
```

To view only laptops:

```sql
SELECT * FROM Products
WHERE Name='Laptop';
```

---

# 🎬 3. Netflix

Netflix stores:

- Movies
- TV Shows
- Users
- Watch History

When you search for a movie:

```text
Search = "Interstellar"
```

SQL behind the scenes:

```sql
SELECT *
FROM Movies
WHERE Movie_Name='Interstellar';
```

---

# 📱 4. Instagram

Instagram stores

- Users
- Followers
- Posts
- Likes
- Comments

When you open your profile:

```sql
SELECT *
FROM Posts
WHERE User_ID = 10;
```

---

# 🎓 5. College Management System

Tables

Students

| ID | Name | Course |
|----|------|---------|
|1|Amit|BCA|
|2|Riya|BBA|

Teachers

Courses

Attendance

Marks

When teacher searches student:

```sql
SELECT *
FROM Students;
```

---

# 🤖 Why AI Engineers Need SQL

Many beginners think SQL is only for Data Analysts.

Wrong!

AI Engineers use SQL every day.

Examples:

- Load training data
- Store predictions
- Store user history
- Save chat history
- Analytics
- Recommendation systems
- Fraud Detection
- Customer Segmentation

Example:

```sql
SELECT *
FROM Customer_Data;
```

Then in Python:

```python
import pandas as pd

data = pd.read_sql(query, connection)
```

Then train ML model.

---

# SQL Workflow

```text
Database
      │
      ▼
SQL Query
      │
      ▼
Python
      │
      ▼
Pandas
      │
      ▼
Machine Learning
      │
      ▼
Prediction
```

---

# Best Practices

## 1. Use Meaningful Names

❌ Bad

```sql
CREATE TABLE t1;
```

✅ Good

```sql
CREATE TABLE Students;
```

---

## 2. Use Uppercase SQL Keywords

Recommended

```sql
SELECT *
FROM Students;
```

Instead of

```sql
select * from students;
```

---

## 3. Use Proper Naming

Good

```text
student_name

course_name

employee_salary
```

Avoid

```text
a

abc

x1
```

---

## 4. Keep Database Organized

Separate tables for

- Students
- Teachers
- Courses
- Fees

Instead of storing everything in one table.

---

## 5. Backup Your Database

Always keep backup before deleting data.

---

## 6. Learn by Practicing

SQL cannot be mastered by reading.

Write queries daily.

---

# Common Beginner Mistakes

## Mistake 1

Forgetting Semicolon

Wrong

```sql
SELECT * FROM Students
```

Correct

```sql
SELECT * FROM Students;
```

---

## Mistake 2

Wrong Database Selected

Always check

```sql
USE CollegeDB;
```

---

## Mistake 3

Typing Errors

Wrong

```sql
CREAT DATABASE
```

Correct

```sql
CREATE DATABASE
```

---

## Mistake 4

Mixing Quotes

Wrong

```sql
WHERE Name = Rahul
```

Correct

```sql
WHERE Name = 'Rahul'
```

---

## Mistake 5

Ignoring Error Messages

Always read MySQL errors carefully.

---

# Practice Questions

## Beginner

### 1

What is a database?

---

### 2

Difference between DBMS and RDBMS.

---

### 3

Write syntax to create a database.

---

### 4

Show all databases.

---

### 5

Delete a database.

---

### 6

Select a database.

---

### 7

What is SQL?

---

### 8

Difference between SQL and MySQL.

---

### 9

Why SQL is important?

---

### 10

Name five real-world applications using SQL.

---

## Intermediate

### 11

Difference between Oracle and MySQL.

---

### 12

What is PostgreSQL?

---

### 13

Can Python work without SQL?

---

### 14

Can AI Engineers avoid SQL?

---

### 15

What is relational data?

---

### 16

What is structured data?

---

### 17

Name three cloud databases.

---

### 18

Difference between Excel and SQL.

---

### 19

Difference between CSV and SQL database.

---

### 20

Why is PostgreSQL popular for AI projects?

---

# Mini Assignment

## Task 1

Install MySQL.

---

## Task 2

Install MySQL Workbench.

---

## Task 3

Create database

```text
StudentDB
```

---

## Task 4

Create another database

```text
CompanyDB
```

---

## Task 5

Show all databases.

---

## Task 6

Use StudentDB.

---

## Task 7

Delete TestDB.

---

## Task 8

Take screenshots of

- MySQL Installation
- Workbench
- Created Databases

Upload to GitHub.

---

# Interview Questions

## Beginner Level

### 1. What is SQL?

SQL (Structured Query Language) is a language used to communicate with relational databases for storing, retrieving, updating, and deleting data.

---

### 2. What is a Database?

A database is an organized collection of data that can be easily accessed, managed, and updated.

---

### 3. What is DBMS?

DBMS (Database Management System) is software used to store and manage data.

Examples:

- MySQL
- Oracle
- SQL Server

---

### 4. What is RDBMS?

RDBMS stores data in tables that are related to each other using keys.

---

### 5. Difference between DBMS and RDBMS?

| DBMS | RDBMS |
|------|--------|
| Stores data | Stores relational data |
| Less secure | More secure |
| No relationships | Supports relationships |

---

### 6. Why SQL is important?

SQL allows us to store, retrieve, filter, and analyze large amounts of data efficiently.

---

### 7. What is MySQL?

MySQL is an open-source relational database management system.

---

### 8. Difference between SQL and MySQL?

SQL is a language.

MySQL is software that uses SQL.

---

### 9. What is PostgreSQL?

PostgreSQL is an advanced open-source relational database with strong support for complex queries and data integrity.

---

### 10. What are databases used for?

- Banking
- Hospitals
- Colleges
- E-commerce
- AI
- Social Media

---

# Intermediate Level

### 11. Why do AI Engineers learn SQL?

To retrieve training data, analyze datasets, store predictions, and build data pipelines.

---

### 12. Which database is best for Machine Learning?

Common choices include PostgreSQL and MySQL, depending on the project and ecosystem.

---

### 13. Can SQL replace Python?

No.

Python and SQL solve different problems and are commonly used together.

---

### 14. Can Python communicate with SQL?

Yes.

Using libraries like

- mysql-connector-python
- SQLAlchemy
- psycopg2

---

### 15. Difference between Excel and SQL?

Excel is ideal for smaller datasets and manual analysis.

SQL databases handle much larger datasets, multiple users, and complex queries efficiently.

---

# Advanced Interview Questions

### 16. Why PostgreSQL is preferred for AI startups?

Because it offers powerful SQL features, good performance, JSON support, and excellent reliability.

---

### 17. Difference between MySQL and PostgreSQL?

MySQL focuses on simplicity and speed for many web applications.

PostgreSQL offers more advanced SQL features, extensibility, and complex query capabilities.

---

### 18. Explain SQL Architecture.

SQL Architecture generally includes:

- Client
- SQL Engine
- Database Server
- Storage Engine
- Data Files

---

### 19. What is ACID?

ACID stands for:

- Atomicity
- Consistency
- Isolation
- Durability

These properties help ensure reliable database transactions.

---

### 20. What is normalization?

Normalization is the process of organizing data into tables to reduce redundancy and improve data integrity.

---

# Quick Revision

✅ Database

✅ DBMS

✅ RDBMS

✅ SQL

✅ MySQL

✅ PostgreSQL

✅ SQL Syntax

✅ CREATE DATABASE

✅ SHOW DATABASES

✅ USE DATABASE

✅ DROP DATABASE

---

# Today's Learning Outcome

Congratulations! 🎉

Today you learned:

- What is SQL
- Database Fundamentals
- DBMS vs RDBMS
- SQL vs MySQL vs PostgreSQL
- Real-world database applications
- SQL workflow in AI projects
- Best practices
- Common mistakes
- Interview questions
- Hands-on assignments

You are now ready to move to **Day 32 – Part 2**, where you'll learn:

- CREATE TABLE
- Data Types
- Constraints
- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE
- DEFAULT
- AUTO_INCREMENT

These are the building blocks of designing real-world databases.

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32 Part 1: Learned SQL Fundamentals and Database Basics"
git push origin main
```

---

# ⭐ Keep Learning

> "A good AI Engineer doesn't just build models—they know how to store, retrieve, and manage data efficiently. SQL is one of the most valuable skills you can invest in early."

# Chapter 1: Creating Tables in SQL

> **Phase 2 – Data & SQL**
>
> **Day 32 – Part 2**
>
> **Topic:** Creating Tables in SQL

---

# 📖 Introduction

A **database** is like a huge cupboard.

Inside that cupboard, we organize information into multiple **tables**.

Think of a school.

The school stores information about:

- Students
- Teachers
- Courses
- Attendance
- Exams

Instead of keeping everything in one large file, each type of information is stored in its own table.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what a table is
- Understand rows and columns
- Create tables in SQL
- Follow table naming conventions
- Design simple database structures
- Understand how tables relate to real-world applications

---

# 🤔 What is a Table?

A **table** is a collection of related data arranged into **rows** and **columns**.

Just like an Excel spreadsheet.

Example:

| Student ID | Name | Age | Course |
|------------|------|-----|---------|
| 101 | Rahul | 20 | BCA |
| 102 | Priya | 21 | BBA |
| 103 | Aman | 19 | B.Tech |

This is a SQL table.

---

# 🏫 Real-Life Example

Imagine a school office.

Instead of remembering every student's information, the school stores it inside a table.

```
Student Table

+-----------+---------+------+---------+
| StudentID | Name    | Age  | Course  |
+-----------+---------+------+---------+
| 101       | Rahul   | 20   | BCA     |
| 102       | Priya   | 21   | BBA     |
| 103       | Aman    | 19   | B.Tech  |
+-----------+---------+------+---------+
```

Each row represents one student.

---

# 📚 Rows

A row is also called a **Record**.

Each row stores information about **one object**.

Example:

```
101 Rahul 20 BCA
```

This complete line is one row.

Another example:

```
102 Priya 21 BBA
```

This is another row.

---

# 📚 Columns

Columns represent the **properties** of an object.

Example:

| Column |
|---------|
| Student ID |
| Name |
| Age |
| Course |

Each column stores one type of information.

---

# 📚 Row vs Column

| Row | Column |
|------|---------|
| Horizontal | Vertical |
| Stores one complete record | Stores one attribute |
| Example: Rahul's data | Example: Name |

---

# 🎯 Example

```
Students Table

+-----------+---------+------+---------+
| StudentID | Name    | Age  | Course  |
+-----------+---------+------+---------+
| 101       | Rahul   | 20   | BCA     |
| 102       | Priya   | 21   | BBA     |
| 103       | Aman    | 19   | B.Tech  |
+-----------+---------+------+---------+
```

Here,

Rows = 3

Columns = 4

---

# 📚 Table Structure

A table has three important parts.

```
Table

│
├── Rows
│
├── Columns
│
└── Data
```

---

# 📌 Why Tables are Important?

Without tables,

Imagine storing every student's information in one paragraph.

```
Rahul 20 BCA
Priya 21 BBA
Aman 19 B.Tech
```

Searching becomes difficult.

Updating becomes difficult.

Deleting becomes difficult.

Tables organize everything neatly.

---

# 🏢 Real-World Examples

## Amazon

Tables:

- Customers
- Products
- Orders
- Payments
- Delivery

---

## Hospital

Tables:

- Patients
- Doctors
- Medicines
- Appointments

---

## Banking

Tables:

- Customers
- Accounts
- Transactions
- Loans

---

## College

Tables:

- Students
- Teachers
- Subjects
- Attendance
- Results

---

# 📌 SQL Naming Conventions

Good table names make databases easy to understand.

### Good Examples

```sql
students
teachers
courses
employees
orders
customers
```

---

### Bad Examples

```sql
abc
table1
xyz
student_data_table_new
```

---

# 📌 Best Practices

✅ Use lowercase names

```sql
students
```

---

✅ Use meaningful names

```sql
employees
```

---

✅ Use plural names

```sql
students
courses
teachers
```

---

✅ Avoid spaces

❌

```sql
Student Data
```

✅

```sql
student_data
```

---

# 📌 Creating Your First Table

General Syntax

```sql
CREATE TABLE table_name (

    column1 datatype,

    column2 datatype,

    column3 datatype

);
```

Example

```sql
CREATE TABLE students (

    student_id INT,

    name VARCHAR(100),

    age INT,

    course VARCHAR(50)

);
```

---

# 🧠 Understanding the Code

```sql
CREATE TABLE
```

Creates a new table.

---

```sql
students
```

Table name.

---

```sql
student_id
```

Column name.

---

```sql
INT
```

Data type.

Stores numbers.

---

```sql
VARCHAR(100)
```

Stores text.

Maximum length = 100 characters.

---

# 📋 Table Created

```
students

+------------+---------------+-------+---------+
| student_id | name          | age   | course  |
+------------+---------------+-------+---------+
```

Notice that the table has **columns only**.

There are **no rows yet** because we haven't inserted any data.

---

# 🔍 View All Tables

```sql
SHOW TABLES;
```

Output

```
+------------------+
| Tables           |
+------------------+
| students         |
+------------------+
```

---

# 🔍 View Table Structure

```sql
DESCRIBE students;
```

Output

```
+------------+-------------+
| Field      | Type        |
+------------+-------------+
| student_id | int         |
| name       | varchar(100)|
| age        | int         |
| course     | varchar(50) |
+------------+-------------+
```

---

# 🚨 Common Mistakes

### Forgetting Semicolon

❌

```sql
CREATE TABLE students (
id INT
)
```

---

✅

```sql
CREATE TABLE students (
id INT
);
```

---

### Missing Data Type

❌

```sql
CREATE TABLE students (

id,

name

);
```

---

✅

```sql
CREATE TABLE students (

id INT,

name VARCHAR(100)

);
```

---

### Using Reserved Keywords

❌

```sql
CREATE TABLE SELECT
```

Use meaningful names instead.

---

# 💡 Practice Questions

### Beginner

1. What is a table?
2. What is a row?
3. What is a column?
4. How many rows can a table contain?
5. Can two tables exist in one database?

---

### Intermediate

6. Create an `employees` table.
7. Create a `books` table.
8. Create a `products` table.
9. Create a `movies` table.
10. Display all tables in the database.

---

# 🎤 Interview Questions

### 1. What is a table in SQL?

A table is a collection of related data organized into rows and columns.

---

### 2. What is the difference between a row and a column?

A row stores one complete record, while a column stores one attribute of every record.

---

### 3. Which command creates a table?

```sql
CREATE TABLE
```

---

### 4. Which command displays all tables?

```sql
SHOW TABLES;
```

---

### 5. Which command shows a table's structure?

```sql
DESCRIBE table_name;
```

---

# 📝 Chapter Summary

In this chapter, you learned:

- ✅ What is a table
- ✅ Rows and columns
- ✅ Table structure
- ✅ Real-world examples
- ✅ SQL naming conventions
- ✅ `CREATE TABLE`
- ✅ `SHOW TABLES`
- ✅ `DESCRIBE`
- ✅ Common mistakes
- ✅ Interview questions
- ✅ Practice exercises

---

# 🚀 Next Chapter

**Chapter 2 – SQL Constraints**

Topics:

- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- DEFAULT
- AUTO_INCREMENT
- Best Practices
- Real-world Examples

# Chapter 2 – SQL Constraints

> **Phase 2: Data & SQL**  
> **Day 32 – Part 2**

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what SQL Constraints are.
- Learn why constraints are important.
- Create tables using different constraints.
- Maintain data accuracy and consistency.
- Understand Primary Key, Foreign Key, NOT NULL, UNIQUE, DEFAULT, CHECK, and AUTO_INCREMENT.
- Answer SQL interview questions confidently.

---

# 📖 What are SQL Constraints?

SQL Constraints are **rules** applied to columns in a table to ensure that the data stored is **accurate, valid, and consistent**.

Think of constraints as **security guards** that prevent invalid or incorrect data from entering your database.

Without constraints, anyone could insert incorrect, duplicate, or incomplete data, making the database unreliable.

---

# 🌍 Real-Life Example

Imagine a college admission system.

Every student must have:

- A unique Roll Number
- A Name
- A Valid Email
- A Date of Admission
- A Course

The database should not allow:

❌ Duplicate Roll Numbers  
❌ Empty Student Names  
❌ Invalid Course IDs

This is exactly what SQL Constraints help us achieve.

---

# 🎯 Why are Constraints Important?

Constraints help maintain:

- Data Accuracy
- Data Integrity
- Data Consistency
- Data Reliability
- Business Rules

Without constraints:

❌ Duplicate records

❌ Missing values

❌ Invalid references

❌ Wrong calculations

---

# Types of SQL Constraints

| Constraint | Purpose |
|------------|---------|
| PRIMARY KEY | Identifies each row uniquely |
| FOREIGN KEY | Connects two tables |
| NOT NULL | Prevents empty values |
| UNIQUE | Prevents duplicate values |
| DEFAULT | Assigns default value |
| CHECK | Validates a condition |
| AUTO_INCREMENT | Automatically increases numeric values |

---

# 1️⃣ PRIMARY KEY

## Definition

A Primary Key uniquely identifies each record in a table.

Every table should ideally have one Primary Key.

---

## Characteristics

- Must be unique
- Cannot contain NULL
- Only one Primary Key per table
- Can consist of multiple columns (Composite Key)

---

## Example

```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

---

### Valid Data

| student_id | name |
|------------|------|
| 1 | Rahul |
| 2 | Priya |
| 3 | Aman |

---

### Invalid Data

```sql
INSERT INTO Students
VALUES (1,'John',20);
```

Again:

```sql
INSERT INTO Students
VALUES (1,'Alex',22);
```

Output

```text
Duplicate entry for PRIMARY KEY
```

---

# Real-Life Example

Think about your:

- Aadhaar Number
- Passport Number
- PAN Number

Each person has only one.

Same concept.

---

# 2️⃣ FOREIGN KEY

## Definition

A Foreign Key creates a relationship between two tables.

It ensures that values exist in another table before they can be inserted.

---

## Example

### Departments Table

```sql
CREATE TABLE Departments(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
```

---

### Students Table

```sql
CREATE TABLE Students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    FOREIGN KEY(department_id)
    REFERENCES Departments(department_id)
);
```

---

## Valid Data

Departments

| ID | Department |
|----|------------|
| 1 | Computer Science |
| 2 | Mechanical |

Students

| Student | Department ID |
|----------|---------------|
| Rahul | 1 |
| Priya | 2 |

---

## Invalid

```sql
INSERT INTO Students
VALUES(1,'John',5);
```

Because Department ID 5 doesn't exist.

---

# Real-Life Example

Think of:

Employee → Department

Order → Customer

Book → Author

The parent record must exist first.

---

# 3️⃣ NOT NULL

## Definition

NOT NULL ensures that a column cannot store NULL values.

---

## Example

```sql
CREATE TABLE Employees(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

### Valid

```sql
INSERT INTO Employees
VALUES(1,'Rahul');
```

---

### Invalid

```sql
INSERT INTO Employees
VALUES(2,NULL);
```

Output

```text
Column 'name' cannot be null
```

---

# Real-Life Example

A student cannot exist without a name.

A customer cannot exist without an email.

---

# 4️⃣ UNIQUE

## Definition

UNIQUE prevents duplicate values.

Unlike Primary Key,

NULL values are generally allowed (database-specific behavior).

---

## Example

```sql
CREATE TABLE Users(
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

---

Valid

```sql
rahul@gmail.com

priya@gmail.com
```

Invalid

```sql
rahul@gmail.com

rahul@gmail.com
```

Duplicate email.

---

# Real-Life Example

Email

Phone Number

Username

Employee ID

---

# Difference Between PRIMARY KEY and UNIQUE

| PRIMARY KEY | UNIQUE |
|--------------|---------|
| Only one | Multiple allowed |
| No NULL | NULL allowed (DB-specific) |
| Uniquely identifies row | Prevents duplicates |

---

# 5️⃣ DEFAULT Constraint

## Definition

DEFAULT automatically inserts a value if none is provided.

---

Example

```sql
CREATE TABLE Employees(

id INT PRIMARY KEY,

city VARCHAR(100) DEFAULT 'Indore'

);
```

---

Insert

```sql
INSERT INTO Employees(id)
VALUES(1);
```

Result

| id | city |
|----|------|
|1|Indore|

---

Another Insert

```sql
INSERT INTO Employees
VALUES(2,'Mumbai');
```

Result

| id | city |
|----|------|
|2|Mumbai|

---

# Real-Life Example

Country → India

Status → Active

Role → Student

---

# 6️⃣ CHECK Constraint

## Definition

CHECK validates data based on a condition.

---

Example

```sql
CREATE TABLE Students(

id INT PRIMARY KEY,

age INT CHECK(age>=18)

);
```

---

Valid

```sql
20
```

Invalid

```sql
16
```

Output

```text
CHECK constraint failed
```

---

# Real-Life Example

Salary > 0

Age >=18

Marks <=100

Quantity >0

---

# 7️⃣ AUTO_INCREMENT

## Definition

Automatically increases numbers.

No need to manually enter IDs.

---

Example

```sql
CREATE TABLE Students(

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100)

);
```

---

Insert

```sql
INSERT INTO Students(name)

VALUES('Rahul');
```

Result

| id | name |
|----|------|
|1|Rahul|

---

Second Insert

```sql
INSERT INTO Students(name)

VALUES('Priya');
```

Result

| id | name |
|----|------|
|2|Priya|

---

Third Insert

```sql
INSERT INTO Students(name)

VALUES('Aman');
```

Result

| id | name |
|----|------|
|3|Aman|

---

# Combining Multiple Constraints

```sql
CREATE TABLE Students(

student_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) NOT NULL,

email VARCHAR(100) UNIQUE,

age INT CHECK(age>=18),

city VARCHAR(50) DEFAULT 'Indore'

);
```

This table uses:

- Primary Key
- Auto Increment
- NOT NULL
- UNIQUE
- CHECK
- DEFAULT

---

# Best Practices

✅ Every table should have a Primary Key.

✅ Use NOT NULL whenever possible.

✅ Use UNIQUE for emails and usernames.

✅ Use Foreign Keys to maintain relationships.

✅ Use CHECK to validate business rules.

✅ Use DEFAULT for common values.

---

# Common Mistakes

❌ Multiple Primary Keys

❌ Duplicate Primary Key values

❌ Missing Foreign Key references

❌ Forgetting NOT NULL

❌ Not using AUTO_INCREMENT

❌ Using UNIQUE where Primary Key is needed

---

# Practice Questions

## Beginner

1. Create a table with PRIMARY KEY.
2. Add NOT NULL to a column.
3. Create UNIQUE email column.
4. Use DEFAULT city.
5. Create AUTO_INCREMENT column.

---

## Intermediate

6. Create Employee table using 4 constraints.
7. Create Student table with CHECK.
8. Create Department table.
9. Link Students and Departments.
10. Insert valid and invalid records.

---

## Advanced

11. Design an E-Commerce Customer table.
12. Create Product table with constraints.
13. Build Banking Account table.
14. Design Hospital Database.
15. Create University Database.

---

# Interview Questions

### Beginner

### 1. What are SQL Constraints?

Constraints are rules that ensure the accuracy and consistency of data stored in a database.

---

### 2. Why do we use Constraints?

To prevent invalid, duplicate, or inconsistent data from being inserted.

---

### 3. What is a Primary Key?

A Primary Key uniquely identifies each record in a table.

---

### 4. Can a Primary Key contain NULL?

No.

---

### 5. Can a table have multiple Primary Keys?

No.

---

### 6. What is a Foreign Key?

A Foreign Key establishes a relationship between two tables.

---

### 7. Difference between Primary Key and Foreign Key?

Primary Key uniquely identifies records in its own table, while Foreign Key references the Primary Key of another table.

---

### 8. What is NOT NULL?

It prevents a column from storing NULL values.

---

### 9. What is UNIQUE?

It ensures that all values in a column are different.

---

### 10. What is DEFAULT?

It automatically assigns a value when none is provided.

---

### 11. What is CHECK?

It validates data against a specified condition.

---

### 12. What is AUTO_INCREMENT?

It automatically generates sequential numeric values for a column.

---

# Summary

Today you learned:

- SQL Constraints
- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE
- DEFAULT
- CHECK
- AUTO_INCREMENT
- Best Practices
- Common Mistakes
- Practice Questions
- Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32 Part 2: Learned SQL Constraints and Table Integrity"
git push origin main
```

---

# 🚀 Next Chapter

**Chapter 3 – CREATE TABLE in Depth**

- CREATE TABLE Syntax
- Naming Conventions
- Data Types in Practice
- Creating Real-World Tables
- Student Management Database Project
- 20+ Practice Problems
- 30+ Interview Questions

# Chapter 3 - CREATE TABLE in SQL

> Phase 2: Data & SQL  
> Day 32 – Part 2

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what a table is
- Create tables in SQL
- Define columns and data types
- Apply constraints while creating tables
- Follow SQL naming conventions
- Design tables for real-world applications

---

# 📖 What is CREATE TABLE?

The `CREATE TABLE` statement is used to create a new table inside a database.

A table stores related data in rows and columns.

Think of it like an Excel spreadsheet.

Example:

| Student ID | Name | Age | Course |
|------------|------|-----|--------|
| 1 | Rahul | 20 | BCA |
| 2 | Priya | 21 | B.Sc |

This is a table.

---

# Syntax

```sql
CREATE TABLE table_name (
    column_name datatype,
    column_name datatype,
    column_name datatype
);
```

---

# Example 1

Create a simple Student table.

```sql
CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50),
    Age INT
);
```

Table Created:

| StudentID | Name | Age |
|------------|------|-----|

Currently it has no data.

---

# Understanding the Syntax

```sql
CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50),
    Age INT
);
```

### CREATE TABLE

Creates a new table.

---

### Students

Table Name

---

### StudentID

Column Name

---

### INT

Stores integer values.

Examples:

```text
1
10
500
9999
```

---

### VARCHAR(50)

Stores text.

Maximum 50 characters.

Example:

```text
Rahul
John
Priya Sharma
```

---

### Age

Stores student's age.

---

# SQL Data Types Used in Tables

| Data Type | Description | Example |
|------------|-------------|----------|
| INT | Integer | 100 |
| BIGINT | Large Integer | 999999999 |
| FLOAT | Decimal Number | 45.78 |
| DECIMAL | Precise Decimal | 999.99 |
| CHAR | Fixed Length Text | A |
| VARCHAR | Variable Length Text | Rahul |
| TEXT | Large Text | Paragraph |
| DATE | Date | 2026-07-15 |
| TIME | Time | 09:30:00 |
| DATETIME | Date & Time | 2026-07-15 09:30:00 |
| BOOLEAN | True/False | TRUE |

---

# Example 2

Employee Table

```sql
CREATE TABLE Employees (

    EmployeeID INT,

    Name VARCHAR(100),

    Department VARCHAR(50),

    Salary DECIMAL(10,2)

);
```

---

# Example 3

Books Table

```sql
CREATE TABLE Books (

    BookID INT,

    Title VARCHAR(200),

    Author VARCHAR(100),

    Price DECIMAL(8,2)

);
```

---

# Example 4

Products Table

```sql
CREATE TABLE Products (

    ProductID INT,

    ProductName VARCHAR(100),

    Price DECIMAL(10,2),

    Quantity INT

);
```

---

# Example 5

Hospital Database

```sql
CREATE TABLE Patients (

    PatientID INT,

    PatientName VARCHAR(100),

    Age INT,

    BloodGroup VARCHAR(5)

);
```

---

# Example 6

College Database

```sql
CREATE TABLE Teachers (

    TeacherID INT,

    TeacherName VARCHAR(100),

    Subject VARCHAR(50)

);
```

---

# Best Practices

✅ Use meaningful table names.

Good

```sql
Students
Employees
Products
```

Bad

```sql
abc
table1
test
```

---

# Use Singular or Plural Consistently

Good

```text
Students
Teachers
Courses
```

OR

```text
Student
Teacher
Course
```

Choose one style and use it consistently.

---

# Use Proper Data Types

Wrong

```sql
Age VARCHAR(100)
```

Correct

```sql
Age INT
```

---

# Give Descriptive Column Names

Bad

```sql
A
B
C
```

Good

```sql
StudentID

StudentName

DateOfBirth
```

---

# Real-Life Example

Imagine you're building a College Management System.

Tables required:

```
Students

Teachers

Courses

Departments

Attendance

Exams

Results
```

Each table stores different types of information.

---

# How SQL Stores Data

```
Database
│
├── Students
│
├── Teachers
│
├── Courses
│
├── Attendance
│
└── Exams
```

Inside Students

| StudentID | Name | Age |
|------------|------|-----|
| 1 | Rahul | 20 |
| 2 | Priya | 21 |

---

# Common Errors

## Missing Comma

Wrong

```sql
CREATE TABLE Students(

StudentID INT

Name VARCHAR(50)

);
```

Correct

```sql
CREATE TABLE Students(

StudentID INT,

Name VARCHAR(50)

);
```

---

## Wrong Data Type

Wrong

```sql
Age VARCHAR(100)
```

Correct

```sql
Age INT
```

---

## Missing Parenthesis

Wrong

```sql
CREATE TABLE Students
StudentID INT;
```

Correct

```sql
CREATE TABLE Students(

StudentID INT

);
```

---

# Viewing Tables

```sql
SHOW TABLES;
```

Output

```
Students

Teachers

Books
```

---

# Viewing Table Structure

```sql
DESCRIBE Students;
```

Output

| Field | Type |
|---------|------|
| StudentID | int |
| Name | varchar(50) |
| Age | int |

---

# Practice Questions

### Beginner

1. Create a Student table.

2. Create an Employee table.

3. Create a Products table.

4. Create a Hospital table.

5. Create a Books table.

---

### Intermediate

6. Create a Movie table.

7. Create a University table.

8. Create a Customer table.

9. Create an Orders table.

10. Create a Library table.

---

### Advanced

11. Design an E-commerce database.

12. Design a Banking database.

13. Design a Hospital Management System.

14. Design an Online Learning Platform.

15. Design an Airline Reservation System.

---

# Interview Questions

## Beginner

### 1. What is a table in SQL?

A table is a collection of related data stored in rows and columns.

---

### 2. What does CREATE TABLE do?

It creates a new table inside a database.

---

### 3. What is a column?

A column represents a single attribute of the data.

Example:

Name

Age

Salary

---

### 4. What is a row?

A row represents one complete record.

---

### 5. Why do we define data types?

Data types tell SQL what kind of values a column can store.

---

## Intermediate

### 6. Difference between CHAR and VARCHAR?

- `CHAR` stores fixed-length text.
- `VARCHAR` stores variable-length text and is more storage-efficient.

---

### 7. Why is INT used for IDs?

Because IDs are numeric and integers are efficient for indexing and searching.

---

### 8. Can a table exist without rows?

Yes. A table can be created without inserting any data.

---

### 9. Can two tables have the same column names?

Yes. Column names only need to be unique within the same table.

---

### 10. Which command shows all tables?

```sql
SHOW TABLES;
```

---

# Assignment

Create the following tables:

- Students
- Teachers
- Courses
- Departments
- Books

Use appropriate data types for each column.

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32: Learned CREATE TABLE statement and designed SQL tables"
git push origin main
```

---

# Chapter Summary

Today you learned:

- What is a table
- CREATE TABLE statement
- SQL syntax
- SQL data types
- Best practices
- Common mistakes
- Viewing table structure
- Practice problems
- Interview questions

🎯 **Next Chapter:** SQL Constraints (PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT, CHECK, FOREIGN KEY, AUTO_INCREMENT)

# 📘 Day 32 – Part 2
# Chapter 4 – ALTER TABLE in SQL

> **Phase 2:** Data & SQL  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what the `ALTER TABLE` statement is.
- Modify the structure of an existing table.
- Add new columns.
- Modify existing columns.
- Rename columns.
- Drop columns.
- Rename tables.
- Understand when to use ALTER TABLE in real-world projects.
- Answer common SQL interview questions related to ALTER TABLE.

---

# 📖 What is ALTER TABLE?

The **ALTER TABLE** statement is used to **change the structure of an existing table** without deleting the data stored inside it.

Think of a table as a classroom.

Initially, the classroom has:

- Roll Number
- Name
- Age

After a few months, the school decides to store students' email addresses.

Instead of creating a brand-new classroom, they simply **add one more column**.

That's exactly what `ALTER TABLE` does.

---

# 📌 Why Do We Need ALTER TABLE?

Imagine you built a Student Management System.

Initially your table looks like:

| Student_ID | Name | Age |
|------------|------|-----|
|101|Rahul|20|
|102|Priya|21|

Later your company wants to store:

- Email
- Phone Number
- Address

Creating the table again would delete all data.

Instead, use:

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

Now your table becomes:

| Student_ID | Name | Age | Email |
|------------|------|-----|--------|

---

# ALTER TABLE Syntax

```sql
ALTER TABLE table_name
action;
```

Example:

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

---

# Operations Supported by ALTER TABLE

ALTER TABLE can:

- Add a Column
- Modify a Column
- Rename a Column
- Drop a Column
- Rename the Table
- Add Constraints
- Remove Constraints

---

# 1️⃣ ADD COLUMN

Adds a new column to an existing table.

### Syntax

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

---

### Example

Current table

|ID|Name|
|--|----|
|1|Rahul|

Now add Age.

```sql
ALTER TABLE students
ADD age INT;
```

Table becomes

|ID|Name|Age|
|--|----|---|
|1|Rahul|NULL|

Notice:

Old records receive NULL unless a default value is specified.

---

### Add Multiple Columns

```sql
ALTER TABLE students
ADD email VARCHAR(100),
ADD phone VARCHAR(15);
```

---

# 2️⃣ MODIFY COLUMN

Used to change:

- Data Type
- Column Size

(MySQL Syntax)

### Syntax

```sql
ALTER TABLE table_name
MODIFY column_name datatype;
```

---

### Example

Current

```sql
Name VARCHAR(20)
```

Need longer names.

```sql
ALTER TABLE students
MODIFY name VARCHAR(100);
```

---

Another Example

```sql
ALTER TABLE students
MODIFY age SMALLINT;
```

---

# Why Modify?

Suppose you stored:

```text
Rahul
```

Later students have full names:

```text
Rahul Kumar Sharma
```

VARCHAR(20) becomes too small.

Increase it.

---

# 3️⃣ CHANGE COLUMN (Rename + Modify)

MySQL provides:

```sql
CHANGE
```

Syntax

```sql
ALTER TABLE students
CHANGE old_name new_name datatype;
```

---

Example

Rename

```text
name
```

to

```text
student_name
```

```sql
ALTER TABLE students
CHANGE name student_name VARCHAR(100);
```

Result

Old

```text
name
```

New

```text
student_name
```

---

# 4️⃣ RENAME COLUMN

Supported in newer MySQL versions.

Syntax

```sql
ALTER TABLE students
RENAME COLUMN age TO student_age;
```

Result

Old

```text
Age
```

New

```text
Student_Age
```

---

# Why Rename?

Bad column names

```text
a
b
c
```

Better

```text
student_name
student_age
student_email
```

Readable code is professional code.

---

# 5️⃣ DROP COLUMN

Removes a column permanently.

### Syntax

```sql
ALTER TABLE students
DROP COLUMN phone;
```

Before

|ID|Name|Phone|

After

|ID|Name|

---

⚠ Warning

Dropped data cannot be recovered unless backed up.

---

# Real Example

Suppose

```text
Whatsapp Number
```

is no longer needed.

Instead of creating a new table

Simply

```sql
ALTER TABLE students
DROP COLUMN whatsapp;
```

---

# 6️⃣ RENAME TABLE

Change table name.

Syntax

```sql
ALTER TABLE students
RENAME TO college_students;
```

Result

Old

```text
students
```

New

```text
college_students
```

---

# Why Rename Tables?

Project grows.

Old

```text
employee
```

New

```text
employees
```

or

```text
company_employees
```

---

# Complete Example

Create Table

```sql
CREATE TABLE students(

student_id INT PRIMARY KEY,
name VARCHAR(50)

);
```

---

Add Column

```sql
ALTER TABLE students
ADD age INT;
```

---

Modify Column

```sql
ALTER TABLE students
MODIFY age SMALLINT;
```

---

Rename Column

```sql
ALTER TABLE students
RENAME COLUMN age TO student_age;
```

---

Drop Column

```sql
ALTER TABLE students
DROP COLUMN student_age;
```

---

Rename Table

```sql
ALTER TABLE students
RENAME TO college_students;
```

---

# Real World Scenario

Version 1

Student Table

```text
ID
Name
Age
```

Version 2

Need Email

```sql
ADD email
```

Version 3

Need Phone

```sql
ADD phone
```

Version 4

Age should become SMALLINT

```sql
MODIFY age
```

Version 5

Phone removed

```sql
DROP phone
```

This is exactly how companies evolve their databases.

---

# Best Practices

✅ Backup database before altering tables.

✅ Use meaningful column names.

✅ Test on a development database first.

✅ Avoid dropping columns without confirmation.

✅ Keep column names consistent.

---

# Common Mistakes

❌ Forgetting data backup.

❌ Using wrong data types.

❌ Renaming columns without updating application code.

❌ Dropping important columns accidentally.

---

# Practice Exercises

## Beginner

1. Create a `students` table.
2. Add an `email` column.
3. Add a `phone` column.
4. Modify the `phone` column length.
5. Rename `phone` to `mobile_number`.

---

## Intermediate

6. Add an `address` column.
7. Drop the `address` column.
8. Rename the table to `college_students`.
9. Increase the size of the `name` column.
10. Add a `date_of_birth` column.

---

## Advanced

11. Design an `employees` table and alter it to include salary and department.
12. Rename multiple columns logically.
13. Build a library table and evolve its schema using ALTER TABLE.
14. Simulate changes in an e-commerce products table.
15. Create a migration plan for a student database.

---

# Interview Questions

## Beginner

### 1. What is ALTER TABLE?

It is used to modify the structure of an existing table.

---

### 2. Can ALTER TABLE change data?

No. It changes the table structure. Existing data remains unless a column is dropped.

---

### 3. Which command adds a new column?

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

---

### 4. Which command removes a column?

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

---

### 5. Difference between MODIFY and CHANGE?

- **MODIFY** changes only the data type or size.
- **CHANGE** can rename the column and modify its definition at the same time.

---

## Intermediate

### 6. Can we rename a table using ALTER TABLE?

Yes.

```sql
ALTER TABLE old_table
RENAME TO new_table;
```

---

### 7. What happens if you drop a column?

All data stored in that column is permanently removed.

---

### 8. Why should ALTER TABLE be used carefully?

Because schema changes can impact applications, queries, and existing data.

---

### 9. Can ALTER TABLE add multiple columns?

Yes.

---

### 10. What precautions should you take before altering production tables?

- Backup the database.
- Test changes in a staging environment.
- Inform the development team.
- Schedule changes during maintenance windows if necessary.

---

# Summary

Today you learned:

- What ALTER TABLE is
- ADD COLUMN
- MODIFY COLUMN
- CHANGE COLUMN
- RENAME COLUMN
- DROP COLUMN
- RENAME TABLE
- Best Practices
- Common Mistakes
- Practice Exercises
- Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32: Learned ALTER TABLE and table modification commands in SQL"
git push origin main
```

---

# 🚀 Next Chapter

**Chapter 5 – DESCRIBE, SHOW TABLES, EXPLAIN, and Understanding Table Metadata**

# Chapter 5 – DESCRIBE Table, SHOW TABLES & EXPLAIN

> **Day 32 – Part 2**
>
> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand how to inspect databases and tables.
- View all tables inside a database.
- View a table's structure.
- Understand column information.
- Use the `EXPLAIN` command.
- Analyze SQL queries.
- Understand query execution.
- Answer SQL interview questions confidently.

---

# Why This Chapter Matters

Imagine joining a company as a Software Engineer.

Your manager says,

> "There's already a database with 500+ tables. Start working."

Would you read every SQL file manually?

No.

Instead, developers use commands like:

- SHOW TABLES
- DESCRIBE
- EXPLAIN

These commands help understand an existing database within minutes.

This is why every SQL developer uses them daily.

---

# What is Metadata?

Metadata means

> "Data about Data"

Example

Suppose we have a table:

| Student_ID | Name | Age |
|------------|------|-----|
|101|Rahul|20|

Actual data is

```
101
Rahul
20
```

Metadata is

```
Column Name
Data Type
Primary Key
Nullable
Default Value
```

Metadata tells us how the data is stored.

---

# SHOW TABLES

## What is SHOW TABLES?

It displays every table inside the currently selected database.

Syntax

```sql
SHOW TABLES;
```

Example

```sql
USE college_db;

SHOW TABLES;
```

Output

```
students

teachers

courses

fees
```

Meaning

The database contains four tables.

---

# Real Life Example

Suppose Netflix has a database.

Instead of opening every file,

they simply run

```sql
SHOW TABLES;
```

Output

```
users

movies

subscriptions

payments

watch_history
```

Within one second,

they know the complete database structure.

---

# SHOW DATABASES

Displays every database.

```sql
SHOW DATABASES;
```

Example

```
mysql

information_schema

college_db

hospital_db

bank_db
```

---

# DESCRIBE TABLE

One of the most important SQL commands.

Also written as

```sql
DESC table_name;
```

Both are same.

---

Syntax

```sql
DESCRIBE students;
```

OR

```sql
DESC students;
```

---

Suppose table

```sql
CREATE TABLE students(

student_id INT PRIMARY KEY,

name VARCHAR(100),

age INT,

email VARCHAR(100)

);
```

Run

```sql
DESC students;
```

Output

| Field | Type | Null | Key | Default | Extra |
|-------|------|------|-----|---------|------|
|student_id|int|NO|PRI|NULL||
|name|varchar(100)|YES||NULL||
|age|int|YES||NULL||
|email|varchar(100)|YES||NULL||

---

# Understanding Every Column

## Field

Column name.

Example

```
student_id

name

age
```

---

## Type

Data type.

Example

```
INT

VARCHAR

DATE

BOOLEAN
```

---

## Null

Can this column store NULL?

YES

Means

Value can be empty.

NO

Means

Value is compulsory.

---

## Key

Shows constraints.

Possible values

```
PRI

MUL

UNI
```

PRI

Primary Key

UNI

Unique

MUL

Indexed column

---

## Default

Default value.

Example

```sql
salary INT DEFAULT 20000
```

DESC output

```
20000
```

---

## Extra

Additional information.

Example

AUTO_INCREMENT

---

# Example

Create table

```sql
CREATE TABLE employees(

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100),

salary INT DEFAULT 30000

);
```

Run

```sql
DESC employees;
```

Output

|Field|Type|Null|Key|Default|Extra|
|------|----|----|----|-------|------|
|id|int|NO|PRI|NULL|auto_increment|
|name|varchar(100)|YES||NULL||
|salary|int|YES||30000||

---

# INFORMATION_SCHEMA

Professional developers rarely use only DESC.

Instead,

they query INFORMATION_SCHEMA.

Example

```sql
SELECT *

FROM INFORMATION_SCHEMA.COLUMNS

WHERE TABLE_NAME='students';
```

This provides

- Column names
- Data types
- Character limits
- Nullable
- Default values

and much more.

---

# SHOW CREATE TABLE

Shows the SQL used to create a table.

Syntax

```sql
SHOW CREATE TABLE students;
```

Output

```sql
CREATE TABLE students(

student_id INT PRIMARY KEY,

name VARCHAR(100),

age INT

);
```

Very useful

when working on old projects.

---

# EXPLAIN Command

One of the most asked interview topics.

---

## What is EXPLAIN?

EXPLAIN shows

how MySQL executes a query.

Think of it as

Google Maps

before starting a journey.

It tells SQL

which route it will take.

---

Syntax

```sql
EXPLAIN

SELECT *

FROM students;
```

---

Example

```sql
EXPLAIN

SELECT *

FROM students

WHERE student_id=10;
```

Output

|id|select_type|table|type|possible_keys|key|
|--|------------|------|------|-------------|----|
|1|SIMPLE|students|const|PRIMARY|PRIMARY|

---

# Why EXPLAIN?

Suppose

Table contains

20 rows.

Query finishes instantly.

Now imagine

50 Million rows.

Wrong query

↓

Slow website

↓

Unhappy users

↓

Company loses money.

EXPLAIN helps optimize queries.

---

# Common EXPLAIN Terms

## table

Which table SQL is reading.

---

## type

How SQL searches.

Best

```
const
```

Good

```
ref
```

Average

```
range
```

Worst

```
ALL
```

ALL means

Full Table Scan.

Avoid whenever possible.

---

## key

Which index SQL used.

If

NULL

No index used.

---

## rows

Estimated number of rows scanned.

Smaller

↓

Better

---

# Example

Query

```sql
SELECT *

FROM students

WHERE age=20;
```

Without index

Rows scanned

```
100000
```

After adding index

```
300
```

Huge performance improvement.

---

# EXPLAIN ANALYZE

(Newer versions)

Runs the query

and

shows actual execution statistics.

Example

```sql
EXPLAIN ANALYZE

SELECT *

FROM students;
```

Used by database engineers.

---

# SHOW INDEX

Shows indexes.

Syntax

```sql
SHOW INDEX

FROM students;
```

Output

```
PRIMARY

student_email_idx
```

---

# Practice

Create database

```sql
CREATE DATABASE college;
```

---

Use database

```sql
USE college;
```

---

Create table

```sql
CREATE TABLE students(

id INT PRIMARY KEY,

name VARCHAR(100),

age INT

);
```

---

Practice

```sql
SHOW TABLES;

DESC students;

SHOW CREATE TABLE students;

EXPLAIN SELECT * FROM students;

SHOW INDEX FROM students;
```

---

# Common Mistakes

❌ Forgetting to select database

```sql
DESC students;
```

Error

No database selected.

---

Correct

```sql
USE college;

DESC students;
```

---

❌ Running EXPLAIN on invalid query.

---

❌ Assuming DESC shows data.

DESC

shows structure,

not records.

---

# Interview Questions

## Beginner

### 1. What does SHOW TABLES do?

Displays all tables inside the selected database.

---

### 2. Difference between SHOW DATABASES and SHOW TABLES?

SHOW DATABASES

lists databases.

SHOW TABLES

lists tables.

---

### 3. What is DESC?

Displays table structure.

---

### 4. What information does DESC provide?

- Column Name
- Data Type
- Null
- Key
- Default
- Extra

---

### 5. What is metadata?

Data describing another piece of data.

---

## Intermediate

### 6. Difference between DESC and SHOW CREATE TABLE?

DESC

shows column information.

SHOW CREATE TABLE

shows complete SQL statement.

---

### 7. What is EXPLAIN?

Shows query execution plan.

---

### 8. Why is EXPLAIN important?

Optimizes SQL performance.

---

### 9. What does "ALL" mean in EXPLAIN?

Full table scan.

Worst performance.

---

### 10. What does PRIMARY in Key column indicate?

Primary Key.

---

## Advanced

### 11. What is INFORMATION_SCHEMA?

System database containing metadata.

---

### 12. What is Full Table Scan?

Reading every row.

Very slow for large tables.

---

### 13. Why do indexes improve EXPLAIN results?

Indexes reduce rows scanned.

---

### 14. Difference between EXPLAIN and EXPLAIN ANALYZE?

EXPLAIN predicts.

EXPLAIN ANALYZE executes and measures.

---

### 15. Which EXPLAIN type is best?

```
const
```

---

# Practice Questions

## Easy

1. Show all databases.
2. Show all tables.
3. Describe a table.
4. Show create table.
5. Show indexes.

---

## Medium

6. Explain a SELECT query.
7. Compare DESC and SHOW CREATE TABLE.
8. Find PRIMARY KEY.
9. Observe AUTO_INCREMENT.
10. Use INFORMATION_SCHEMA.

---

## Advanced

11. Compare execution plans.
12. Analyze indexed vs non-indexed query.
13. Study rows scanned.
14. Explore metadata.
15. Optimize a slow query.

---

# Chapter Summary

Today you learned:

- ✅ SHOW DATABASES
- ✅ SHOW TABLES
- ✅ DESCRIBE
- ✅ DESC
- ✅ SHOW CREATE TABLE
- ✅ INFORMATION_SCHEMA
- ✅ SHOW INDEX
- ✅ EXPLAIN
- ✅ EXPLAIN ANALYZE
- ✅ Query Execution Plan
- ✅ SQL Performance Basics

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32: Learned SHOW TABLES, DESC, EXPLAIN and SQL Metadata"
git push origin main
```

---

# 🚀 Next Chapter

**Chapter 6 – DELETE, TRUNCATE & DROP Commands**

You'll learn:

- DELETE
- TRUNCATE
- DROP
- Differences between them
- Performance comparison
- Recovery possibilities
- Real-world examples
- Interview questions

# Chapter 6: DELETE vs DROP vs TRUNCATE in SQL

> 📚 Day 32 – Part 2 | SQL Fundamentals

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the difference between `DELETE`, `DROP`, and `TRUNCATE`
- Know when to use each command
- Avoid common mistakes that can lead to data loss
- Answer interview questions related to these SQL commands
- Practice using all three commands with real-world examples

---

# 📖 Introduction

When working with databases, there are times when you need to remove data.

SQL provides three different commands for this purpose:

- DELETE
- TRUNCATE
- DROP

Although they all remove data, they work in completely different ways.

Understanding the difference is extremely important because using the wrong command can permanently delete your data or even your entire table.

---

# Imagine This...

Suppose you have a classroom.

The classroom contains:

- Students (Rows)
- Student Information (Data)
- Classroom Structure (Table)

Now imagine three different situations.

### Situation 1

The teacher asks one student to leave.

➡️ This is similar to **DELETE**.

---

### Situation 2

The teacher asks **every student** to leave, but the classroom remains.

➡️ This is similar to **TRUNCATE**.

---

### Situation 3

The principal demolishes the classroom itself.

➡️ This is similar to **DROP**.

---

# Visual Comparison

```text
Table: Students

+-------------------------+
| Roll | Name | Age |
+-------------------------+
| 1    | John | 20  |
| 2    | Alex | 22  |
| 3    | Emma | 19  |
+-------------------------+
```

---

## DELETE

```text
Delete John

+-------------------------+
| Roll | Name | Age |
+-------------------------+
| 2    | Alex | 22  |
| 3    | Emma | 19  |
+-------------------------+
```

Only selected rows disappear.

---

## TRUNCATE

```text
+-------------------------+
| Roll | Name | Age |
+-------------------------+
```

Table exists.

No rows.

---

## DROP

```text
Students Table

❌ Deleted Completely
```

Nothing remains.

---

# 1. DELETE Command

## Definition

The `DELETE` command removes one or more rows from a table.

The table itself still exists.

---

## Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

---

## Example

```sql
DELETE FROM Students
WHERE Roll = 2;
```

---

## Before

| Roll | Name |
|------|------|
|1|John|
|2|Alex|
|3|Emma|

---

## After

| Roll | Name |
|------|------|
|1|John|
|3|Emma|

Only Alex is removed.

---

# Delete All Records

```sql
DELETE FROM Students;
```

---

Result

All rows are deleted.

Table still exists.

---

# Why Use WHERE?

Without WHERE,

```sql
DELETE FROM Students;
```

deletes every row.

This is one of the most common SQL mistakes.

Always double-check your WHERE clause.

---

# Advantages of DELETE

✅ Delete selected rows

✅ Supports WHERE

✅ Can be rolled back (inside transactions)

---

# Disadvantages

❌ Slower for large tables

❌ Deletes rows one by one

---

# Real-World Example

Suppose an employee resigns.

Only that employee's record should be removed.

```sql
DELETE FROM Employees
WHERE EmployeeID = 101;
```

---

# 2. TRUNCATE Command

## Definition

TRUNCATE removes all rows from a table instantly.

The table structure remains.

---

## Syntax

```sql
TRUNCATE TABLE Students;
```

---

## Before

| Roll | Name |
|------|------|
|1|John|
|2|Alex|
|3|Emma|

---

## After

Empty table

```text
Students

(No Records)
```

---

# Important

TRUNCATE

✔ Removes all rows

✔ Keeps table

✔ Keeps columns

✔ Keeps constraints

---

# Why Faster?

DELETE removes rows one by one.

TRUNCATE removes the entire data block at once.

Therefore,

TRUNCATE is much faster.

---

# Advantages

✅ Very Fast

✅ Uses less memory

✅ Resets AUTO_INCREMENT in many databases (e.g., MySQL)

---

# Disadvantages

❌ Cannot delete selected rows

❌ No WHERE clause

---

# Real-World Example

Your application stores temporary login sessions.

Every midnight you want to remove all sessions.

```sql
TRUNCATE TABLE UserSessions;
```

---

# 3. DROP Command

## Definition

DROP permanently removes the table itself.

Everything disappears.

- Table
- Data
- Columns
- Constraints
- Indexes

---

## Syntax

```sql
DROP TABLE Students;
```

---

## Before

```text
Students Table
```

---

## After

```text
ERROR

Table doesn't exist
```

---

# Why Dangerous?

Once dropped,

the table no longer exists.

You cannot insert data because the structure itself is gone.

---

# Advantages

Useful when

- Table no longer needed
- Database cleanup
- Removing old tables

---

# Disadvantages

❌ Complete loss

❌ Cannot recover easily

---

# DROP DATABASE

Deletes entire database.

```sql
DROP DATABASE College;
```

Everything inside disappears.

---

# Comparison Table

| Feature | DELETE | TRUNCATE | DROP |
|----------|----------|-----------|--------|
| Removes Rows | ✅ | ✅ | ❌ |
| Removes Table | ❌ | ❌ | ✅ |
| WHERE Allowed | ✅ | ❌ | ❌ |
| Fast | ❌ | ✅ | ✅ |
| Keeps Structure | ✅ | ✅ | ❌ |
| Deletes Columns | ❌ | ❌ | ✅ |
| Deletes Constraints | ❌ | ❌ | ✅ |
| Deletes Database Object | ❌ | ❌ | ✅ |

---

# Memory Trick

DELETE

> Delete some students.

TRUNCATE

> Empty the classroom.

DROP

> Destroy the classroom.

---

# Example

Create table

```sql
CREATE TABLE Students(
    Roll INT,
    Name VARCHAR(50)
);
```

Insert records

```sql
INSERT INTO Students
VALUES
(1,'John'),
(2,'Alex'),
(3,'Emma');
```

---

Delete one record

```sql
DELETE FROM Students
WHERE Roll = 1;
```

---

Delete all records

```sql
TRUNCATE TABLE Students;
```

---

Delete table

```sql
DROP TABLE Students;
```

---

# Common Mistakes

## Mistake 1

```sql
DELETE FROM Students;
```

Forgot WHERE.

Entire data deleted.

---

## Mistake 2

Using DROP instead of TRUNCATE.

Table permanently removed.

---

## Mistake 3

Trying to use WHERE with TRUNCATE.

```sql
TRUNCATE TABLE Students
WHERE Roll=2;
```

❌ Invalid SQL

---

# Best Practices

✅ Always take backup.

✅ Use DELETE for selective removal.

✅ Use TRUNCATE for clearing all records.

✅ Use DROP only when the table is no longer required.

✅ Always verify before executing.

---

# Practice Questions

## Easy

1. Delete one student.
2. Delete all students.
3. Drop Students table.
4. Create table again.
5. Insert records.

---

## Intermediate

6. Delete students older than 20.
7. Delete duplicate records.
8. Truncate Employee table.
9. Drop Department table.
10. Explain differences.

---

# Interview Questions

### 1. Difference between DELETE and TRUNCATE?

**Answer:**

- DELETE removes selected rows and supports `WHERE`.
- TRUNCATE removes all rows and does not support `WHERE`.
- TRUNCATE is faster than DELETE.

---

### 2. Difference between TRUNCATE and DROP?

**Answer:**

- TRUNCATE removes only data.
- DROP removes the entire table structure and its data.

---

### 3. Which command is fastest?

**Answer:** `TRUNCATE`

---

### 4. Can DELETE use WHERE?

**Answer:** Yes.

---

### 5. Can TRUNCATE use WHERE?

**Answer:** No.

---

### 6. Which command removes the table itself?

**Answer:** `DROP`

---

### 7. Which command keeps the table structure?

**Answer:** `DELETE` and `TRUNCATE`

---

### 8. Which command is safest for deleting one record?

**Answer:** `DELETE`

---

### 9. Can you insert data after TRUNCATE?

**Answer:** Yes, because the table still exists.

---

### 10. Can you insert data after DROP?

**Answer:** No. The table no longer exists.

---

# Chapter Summary

In this chapter, you learned:

- ✅ DELETE Command
- ✅ TRUNCATE Command
- ✅ DROP Command
- ✅ Differences between all three
- ✅ Real-world use cases
- ✅ Common mistakes
- ✅ Best practices
- ✅ Interview questions
- ✅ Hands-on SQL examples

---

# 🚀 Next Chapter

**Chapter 7 – INSERT INTO Statement**

You will learn:

- INSERT INTO
- Multiple Row Insert
- NULL Values
- AUTO_INCREMENT
- Default Values
- Real-world Examples
- Student Database Project
- Interview Questions

---

# 📖 Chapter 7: Hands-on Lab – Student Management Database

> Theory is important, but SQL is learned by **building databases**. In this chapter, you will create a complete Student Management Database from scratch, similar to what is used in schools, colleges, and universities.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Create a real-world database
- Design multiple related tables
- Use Primary Keys
- Use Foreign Keys
- Apply SQL Constraints
- Understand relationships between tables
- Insert sample data
- Query data from multiple tables

---

# 🏫 Project Overview

We will build a **Student Management System Database**.

### Features

- Store student information
- Store teacher information
- Store course information
- Enroll students in courses
- Connect teachers with courses

---

# 🗂 Database Structure

```text
Student_Management_System
│
├── Students
├── Teachers
├── Courses
└── Enrollments
```

---

# 📊 Database Relationship

```text
Students
---------
Student_ID (PK)
Name
Email
Age

        |
        | 1
        |
        | N
Enrollments
-------------
Enrollment_ID (PK)
Student_ID (FK)
Course_ID (FK)
Enrollment_Date

        N
        |
        | 1

Courses
---------
Course_ID (PK)
Course_Name
Teacher_ID (FK)

        N
        |
        | 1

Teachers
---------
Teacher_ID (PK)
Teacher_Name
Department
```

---

# Step 1: Create Database

```sql
CREATE DATABASE Student_Management_System;
```

Use the database.

```sql
USE Student_Management_System;
```

---

# Step 2: Create Students Table

```sql
CREATE TABLE Students (

    Student_ID INT AUTO_INCREMENT PRIMARY KEY,

    Name VARCHAR(100) NOT NULL,

    Email VARCHAR(100) UNIQUE,

    Age INT,

    City VARCHAR(50)

);
```

---

# Explanation

| Column | Purpose |
|----------|----------|
| Student_ID | Unique ID for every student |
| Name | Student Name |
| Email | Unique Email Address |
| Age | Student Age |
| City | Student City |

---

# Step 3: Create Teachers Table

```sql
CREATE TABLE Teachers (

    Teacher_ID INT AUTO_INCREMENT PRIMARY KEY,

    Teacher_Name VARCHAR(100),

    Department VARCHAR(100)

);
```

---

# Step 4: Create Courses Table

```sql
CREATE TABLE Courses (

    Course_ID INT AUTO_INCREMENT PRIMARY KEY,

    Course_Name VARCHAR(100),

    Teacher_ID INT,

    FOREIGN KEY (Teacher_ID)
    REFERENCES Teachers(Teacher_ID)

);
```

---

# Explanation

Each course belongs to one teacher.

Example

```
Python
↓

Mr. Sharma
```

---

# Step 5: Create Enrollments Table

```sql
CREATE TABLE Enrollments (

    Enrollment_ID INT AUTO_INCREMENT PRIMARY KEY,

    Student_ID INT,

    Course_ID INT,

    Enrollment_Date DATE,

    FOREIGN KEY(Student_ID)
    REFERENCES Students(Student_ID),

    FOREIGN KEY(Course_ID)
    REFERENCES Courses(Course_ID)

);
```

---

# Why We Need Enrollments?

One student can join many courses.

One course can have many students.

This is called a **Many-to-Many Relationship**.

Instead of connecting Students directly with Courses, we use a bridge table.

```
Student
↓

Enrollment

↓

Course
```

---

# Step 6: Insert Students

```sql
INSERT INTO Students
(Name, Email, Age, City)

VALUES

('Rahul', 'rahul@gmail.com', 20, 'Delhi'),

('Priya', 'priya@gmail.com', 21, 'Mumbai'),

('Amit', 'amit@gmail.com', 19, 'Indore'),

('Sneha', 'sneha@gmail.com', 22, 'Pune');
```

---

# Step 7: Insert Teachers

```sql
INSERT INTO Teachers

(Teacher_Name, Department)

VALUES

('Ankit Sharma', 'Computer Science'),

('Neha Gupta', 'Artificial Intelligence'),

('Rakesh Verma', 'Data Science');
```

---

# Step 8: Insert Courses

```sql
INSERT INTO Courses

(Course_Name, Teacher_ID)

VALUES

('Python Programming',1),

('Machine Learning',2),

('SQL Fundamentals',3);
```

---

# Step 9: Insert Enrollments

```sql
INSERT INTO Enrollments

(Student_ID, Course_ID, Enrollment_Date)

VALUES

(1,1,'2026-08-01'),

(1,2,'2026-08-03'),

(2,1,'2026-08-02'),

(3,3,'2026-08-04'),

(4,2,'2026-08-05');
```

---

# Verify Tables

Show all tables.

```sql
SHOW TABLES;
```

Output

```
Students

Teachers

Courses

Enrollments
```

---

# View Students

```sql
SELECT * FROM Students;
```

---

# View Teachers

```sql
SELECT * FROM Teachers;
```

---

# View Courses

```sql
SELECT * FROM Courses;
```

---

# View Enrollments

```sql
SELECT * FROM Enrollments;
```

---

# Real World Example

Think about your college.

One student studies many subjects.

One teacher teaches many subjects.

Many students study the same subject.

That is exactly how universities manage their databases.

---

# Mini Challenge 1

Add a new student.

```text
Name : Arjun

Age : 20

City : Jaipur

Email : arjun@gmail.com
```

---

# Mini Challenge 2

Add a teacher.

```
Teacher Name

Rohit Singh

Department

Cyber Security
```

---

# Mini Challenge 3

Create a course.

```
Course Name

Web Development
```

Assign it to Rohit Singh.

---

# Mini Challenge 4

Enroll Arjun into:

- Python Programming
- Web Development

---

# Expected Database

```
Student Management System

Students

Teachers

Courses

Enrollments
```

Everything connected using Foreign Keys.

---

# Practice Questions

## Beginner

1. Create a database called College.

2. Create a Students table.

3. Add Email column.

4. Add Phone Number.

5. Create Teachers table.

---

## Intermediate

6. Create Courses table.

7. Create Enrollments table.

8. Insert five students.

9. Insert five teachers.

10. Insert five courses.

---

## Advanced

11. Design Library Database.

12. Design Hospital Database.

13. Design Banking Database.

14. Design E-Commerce Database.

15. Design Employee Management Database.

---

# Common Mistakes

❌ Forgetting Primary Key

❌ Duplicate Emails

❌ Wrong Foreign Key Reference

❌ Different Data Types in Foreign Keys

❌ Inserting Child Records Before Parent Records

---

# Best Practices

✅ Use meaningful table names

✅ Use singular or plural consistently

✅ Always define Primary Keys

✅ Use Foreign Keys for relationships

✅ Apply NOT NULL where required

✅ Use AUTO_INCREMENT for IDs

✅ Keep database normalized

---

# Interview Questions

### 1. Why do we use a Primary Key?

To uniquely identify every record in a table.

---

### 2. What is a Foreign Key?

A Foreign Key creates a relationship between two tables and ensures referential integrity.

---

### 3. Why is an Enrollment table needed?

Because Students and Courses have a Many-to-Many relationship. The Enrollment table acts as a bridge.

---

### 4. What is AUTO_INCREMENT?

It automatically generates a unique number for each new record.

---

### 5. Can a table have multiple Foreign Keys?

Yes. A table can have multiple Foreign Keys referencing different tables.

---

# Chapter Summary

Today you learned:

- Creating a real-world database
- Designing multiple related tables
- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Many-to-Many Relationships
- Inserting sample data
- Database design best practices

🎉 Congratulations! You have built your first relational database similar to those used in real-world applications.
---

# Chapter 8: Practice Questions

Practice is the key to mastering SQL. The questions below are arranged from **Beginner → Intermediate → Advanced**. Try solving each one on your own before checking the solution.

---

# 🟢 Beginner Level (1–20)

## 1. Create a Database

Create a database named `college_db`.

---

## 2. Show All Databases

Display all databases available on your MySQL server.

---

## 3. Select a Database

Use the `college_db` database.

---

## 4. Create a Students Table

Create a table named `students` with the following columns:

| Column | Data Type |
|----------|----------|
| id | INT |
| name | VARCHAR(100) |
| age | INT |
| city | VARCHAR(50) |

---

## 5. Add a Primary Key

Make the `id` column the Primary Key.

---

## 6. Make Name Mandatory

Ensure the `name` column cannot contain NULL values.

---

## 7. Add Email Column

Add an `email` column to the students table.

---

## 8. Add UNIQUE Constraint

Make the email column unique.

---

## 9. Describe Table

Display the structure of the `students` table.

---

## 10. Show All Tables

Display every table inside the database.

---

## 11. Rename Column

Rename `city` to `address`.

---

## 12. Modify Column Size

Increase the size of the `name` column to 200 characters.

---

## 13. Drop Email Column

Delete the email column.

---

## 14. Rename Table

Rename `students` to `student_info`.

---

## 15. Delete Table

Delete the `student_info` table.

---

## 16. Create Employees Table

Create an employee table with:

- Employee ID
- Name
- Salary

---

## 17. Create Products Table

Columns:

- Product ID
- Product Name
- Price

---

## 18. Create Library Table

Columns:

- Book ID
- Book Name
- Author

---

## 19. Create Customer Table

Columns:

- Customer ID
- Name
- Phone Number

---

## 20. Create Department Table

Columns:

- Department ID
- Department Name

---

# 🟡 Intermediate Level (21–40)

## 21.

Create a table with:

- Primary Key
- NOT NULL
- UNIQUE

---

## 22.

Create a table where salary defaults to 25000.

---

## 23.

Create a table with AUTO_INCREMENT.

---

## 24.

Create a table having two UNIQUE columns.

---

## 25.

Create a table with CHECK constraint.

Example:

Age must be greater than 18.

---

## 26.

Create a Course table.

Columns:

- Course ID
- Course Name
- Fees

---

## 27.

Create Teacher table.

Columns:

- Teacher ID
- Teacher Name
- Subject

---

## 28.

Create Department table using DEFAULT values.

---

## 29.

Create Student table using AUTO_INCREMENT.

---

## 30.

Create Employee table with Salary > 10000.

---

## 31.

Modify Salary column datatype.

---

## 32.

Rename Employee table.

---

## 33.

Delete one column.

---

## 34.

Add three new columns.

---

## 35.

Change datatype from INT to BIGINT.

---

## 36.

Create a Bank table.

---

## 37.

Create Hospital table.

---

## 38.

Create School table.

---

## 39.

Create Inventory table.

---

## 40.

Create Hotel table.

---

# 🔴 Advanced Level (41–60)

## 41.

Design a College Database.

Tables:

- Students
- Teachers
- Courses

---

## 42.

Design an E-commerce Database.

Tables:

- Customers
- Products
- Orders

---

## 43.

Design a Hospital Database.

Tables:

- Doctors
- Patients
- Medicines

---

## 44.

Design a Banking Database.

Tables:

- Customers
- Accounts
- Transactions

---

## 45.

Design a Library Database.

Tables:

- Books
- Members
- Borrow Records

---

## 46.

Design a Food Delivery Database.

---

## 47.

Design a Railway Reservation Database.

---

## 48.

Design a School Management Database.

---

## 49.

Design an Online Shopping Database.

---

## 50.

Design an HR Management Database.

---

## 51.

Create every table with proper constraints.

---

## 52.

Identify Primary Keys.

---

## 53.

Identify Candidate Keys.

---

## 54.

Identify Foreign Keys.

---

## 55.

Apply UNIQUE constraints wherever necessary.

---

## 56.

Use DEFAULT values.

---

## 57.

Use AUTO_INCREMENT.

---

## 58.

Use CHECK constraints.

---

## 59.

Normalize your database to 3NF.

---

## 60.

Explain why your database design is efficient.

---

# 🚀 Challenge Questions

Try these without looking at any notes.

### Challenge 1

Design a Student Management System Database.

Include:

- Students
- Teachers
- Courses
- Attendance
- Exams

---

### Challenge 2

Design an Amazon-like Database.

Include:

- Users
- Products
- Categories
- Orders
- Payments

---

### Challenge 3

Design a Netflix Database.

Include:

- Users
- Movies
- Actors
- Ratings

---

### Challenge 4

Design a Hospital Management System.

---

### Challenge 5

Design a Social Media Database.

Include:

- Users
- Posts
- Comments
- Likes
- Followers

---

# 🎯 Interview Coding Challenge

Create the following table in a single SQL statement.

```text
Employee
---------
EmployeeID
FirstName
LastName
Email
Phone
Salary
Department
JoiningDate
```

Constraints:

- EmployeeID → Primary Key
- Email → UNIQUE
- Salary → DEFAULT 30000
- FirstName → NOT NULL
- AUTO_INCREMENT

---

# 📝 Self-Evaluation Checklist

Can you confidently:

- [ ] Create a Database
- [ ] Create Tables
- [ ] Choose correct Data Types
- [ ] Add Constraints
- [ ] Create Primary Keys
- [ ] Create Foreign Keys
- [ ] Use AUTO_INCREMENT
- [ ] Use DEFAULT
- [ ] Modify Tables
- [ ] Delete Tables
- [ ] Rename Tables
- [ ] Explain why Constraints are important

If you answered **Yes** to all the above, you're ready to move to **Day 33 – SQL Data Manipulation (INSERT, UPDATE, DELETE, SELECT, WHERE)**.

---
# Chapter 9: SQL Interview Questions

> 🎯 **Objective:** Prepare for SQL interview questions commonly asked in internships, placements, and AI/ML Engineer interviews.

---

# 📌 Beginner Level Interview Questions

## 1. What is SQL?

**Answer:**

SQL (Structured Query Language) is a standard language used to communicate with relational databases. It is used to create, read, update, and delete data.

---

## 2. What is a Database?

**Answer:**

A database is an organized collection of related data that can be stored, managed, and retrieved efficiently.

### Example

A college database may contain:

- Students
- Teachers
- Courses
- Marks

---

## 3. What is DBMS?

**Answer:**

DBMS (Database Management System) is software used to store and manage data.

### Examples

- MySQL
- PostgreSQL
- SQLite
- Oracle
- SQL Server

---

## 4. What is RDBMS?

**Answer:**

RDBMS (Relational Database Management System) stores data in tables and maintains relationships between them.

Examples:

- MySQL
- PostgreSQL
- Oracle

---

## 5. Difference between DBMS and RDBMS?

| DBMS | RDBMS |
|------|--------|
| Stores data | Stores data in tables |
| No relationships | Supports relationships |
| Less secure | More secure |
| Small applications | Enterprise applications |

---

## 6. What is a Table?

A table is a collection of rows and columns.

Example:

| Roll No | Name | Age |
|----------|------|-----|
| 101 | Rahul | 20 |

---

## 7. What is a Row?

A row represents one complete record.

Example:

```
101 Rahul 20
```

---

## 8. What is a Column?

A column represents one attribute.

Example:

```
Name
Age
Email
```

---

## 9. What is a Record?

A record is another name for a row.

---

## 10. What is a Field?

A field is a single value inside a row.

Example:

```
Rahul
```

is a field inside the Name column.

---

# 📌 Intermediate Interview Questions

## 11. What is a Primary Key?

A Primary Key uniquely identifies every row.

Properties:

- Unique
- Cannot be NULL
- One Primary Key per table

Example:

```sql
StudentID INT PRIMARY KEY
```

---

## 12. Can Primary Key contain NULL?

No.

Primary Key never contains NULL values.

---

## 13. What is UNIQUE Constraint?

It prevents duplicate values.

Unlike Primary Key, UNIQUE allows NULL (implementation may vary by database).

Example:

```sql
Email VARCHAR(100) UNIQUE
```

---

## 14. Difference between PRIMARY KEY and UNIQUE

| PRIMARY KEY | UNIQUE |
|--------------|---------|
| Only one | Multiple allowed |
| Cannot be NULL | NULL allowed (DB dependent) |
| Uniquely identifies row | Prevents duplicates |

---

## 15. What is NOT NULL?

It ensures a column always has a value.

Example:

```sql
Name VARCHAR(50) NOT NULL
```

---

## 16. What is DEFAULT Constraint?

Provides a default value.

Example:

```sql
Country VARCHAR(30) DEFAULT 'India'
```

---

## 17. What is AUTO_INCREMENT?

Automatically generates sequential numbers.

Example:

```sql
StudentID INT AUTO_INCREMENT PRIMARY KEY
```

---

## 18. What is FOREIGN KEY?

A Foreign Key connects two tables.

Example:

Students

| ID | Name |
|----|------|
|1|Rahul|

Courses

| StudentID | Course |
|-----------|---------|
|1|Python|

StudentID references Students(ID).

---

## 19. Why use Foreign Keys?

- Maintain relationships
- Prevent invalid data
- Improve integrity

---

## 20. What is Referential Integrity?

It ensures that relationships between tables remain valid.

---

# 📌 Advanced Interview Questions

## 21. Difference between DELETE, DROP and TRUNCATE

| DELETE | DROP | TRUNCATE |
|---------|------|-----------|
| Removes rows | Deletes table | Removes all rows |
| Can rollback | Cannot rollback (DB dependent) | Faster than DELETE |
| Table remains | Table removed | Table remains |

---

## 22. What is Composite Primary Key?

A Primary Key made using two or more columns.

Example:

```sql
PRIMARY KEY(StudentID, CourseID)
```

---

## 23. Why do we normalize databases?

To:

- Remove redundancy
- Improve consistency
- Reduce duplicate data

---

## 24. What is Data Redundancy?

Duplicate storage of the same information.

Example:

Saving the student's address in every table.

---

## 25. What is SQL Constraint?

Rules applied to columns to maintain data accuracy.

Examples:

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- CHECK
- DEFAULT
- NOT NULL

---

## 26. What happens if Primary Key is duplicated?

Database throws an error.

Example:

```text
Duplicate entry for PRIMARY KEY
```

---

## 27. Can a table have multiple Foreign Keys?

Yes.

Example:

Orders table

```
CustomerID
ProductID
EmployeeID
```

All three can be Foreign Keys.

---

## 28. What is CHECK Constraint?

Restricts values.

Example:

```sql
Age INT CHECK (Age >= 18)
```

---

## 29. What is the purpose of ALTER TABLE?

Used to modify an existing table.

Example:

```sql
ALTER TABLE Students
ADD Email VARCHAR(100);
```

---

## 30. What is DESCRIBE command?

Displays table structure.

Example:

```sql
DESC Students;
```

---

# 📌 Scenario-Based Interview Questions

## 31. Why shouldn't Email be a Primary Key?

Because:

- Emails can change.
- Primary Keys should remain stable.

---

## 32. Why is StudentID better than Name as Primary Key?

Names can repeat.

Student IDs are unique.

---

## 33. Why use AUTO_INCREMENT?

It automatically generates unique IDs.

No manual effort is needed.

---

## 34. When should FOREIGN KEY be used?

Whenever two tables are related.

Examples:

- Students → Courses
- Customers → Orders
- Doctors → Patients

---

## 35. Can PRIMARY KEY be updated?

Technically yes, but it is not recommended because it may break relationships.

---

## 36. Why is NULL different from 0?

NULL means:

"No value."

0 is an actual numeric value.

---

## 37. Can UNIQUE contain duplicate NULL values?

It depends on the database.

MySQL generally allows multiple NULL values in a UNIQUE column.

---

## 38. What happens when FOREIGN KEY references a non-existing record?

Database throws an integrity error.

---

## 39. Why do companies use PostgreSQL instead of Excel?

Because PostgreSQL:

- Handles millions of records
- Supports multiple users
- Provides security
- Maintains data integrity
- Supports transactions

---

## 40. What are Constraints?

Constraints enforce rules on data.

They improve:

- Accuracy
- Consistency
- Reliability

---

# 📌 Frequently Asked Placement Questions

- Difference between CHAR and VARCHAR?
- Difference between DELETE and TRUNCATE?
- What is a Candidate Key?
- What is a Super Key?
- What is Referential Integrity?
- What is Normalization?
- What is Denormalization?
- Why do databases need indexes?
- What is ACID?
- What is a Transaction?

---

# 💼 AI/ML Interview Tip

Even if you're applying for an **AI/ML Engineer** or **Generative AI Engineer** role, SQL is almost always part of the interview because real-world AI systems rely on structured data stored in databases.

Interviewers often expect you to:

- Design simple database schemas
- Write SQL queries
- Explain relationships between tables
- Understand constraints and data integrity
- Retrieve data efficiently for machine learning pipelines

A strong SQL foundation will make it much easier to work with datasets, build data pipelines, and integrate AI applications with production databases.

---

# 🎯 Quick Revision

✅ SQL manages relational databases.

✅ Tables store data in rows and columns.

✅ Primary Key uniquely identifies a record.

✅ Foreign Key creates relationships.

✅ Constraints improve data integrity.

✅ AUTO_INCREMENT automatically generates IDs.

✅ ALTER TABLE modifies existing tables.

✅ DESC displays table structure.

---

# 🚀 What's Next?

In **Chapter 10**, you'll complete a **real-world Student Management Database Assignment**, combining everything you've learned about creating tables, constraints, and database design.

# 📚 Chapter 10: Assignment

> **Goal:** Apply everything you've learned about SQL tables, constraints, and database design by building a real-world database from scratch.

---

# 🎯 Assignment Objectives

By completing this assignment, you should be able to:

- Create a database
- Create multiple tables
- Use appropriate SQL data types
- Apply constraints correctly
- Design relationships between tables
- Insert sample data
- Verify table structures
- Think like a Database Designer

---

# 🏫 Assignment 1: Student Management System Database

Create a database named:

```sql
StudentManagementSystem
```

---

## Step 1: Create Database

```sql
CREATE DATABASE StudentManagementSystem;
```

Use the database.

```sql
USE StudentManagementSystem;
```

---

## Step 2: Create Students Table

Requirements:

- Student ID should auto increment.
- Student name is mandatory.
- Email must be unique.
- Phone number is unique.
- Age should have a default value of 18.
- Admission date should automatically store today's date.

Expected Columns

| Column | Data Type |
|---------|-----------|
| student_id | INT |
| first_name | VARCHAR(50) |
| last_name | VARCHAR(50) |
| email | VARCHAR(100) |
| phone | VARCHAR(15) |
| age | INT |
| city | VARCHAR(50) |
| admission_date | DATE |

---

## Step 3: Create Courses Table

Requirements

- Course ID should auto increment.
- Course Name cannot be NULL.
- Duration should be stored in months.
- Fees must be positive.

Expected Columns

| Column | Data Type |
|---------|-----------|
| course_id | INT |
| course_name | VARCHAR(100) |
| duration | INT |
| fees | DECIMAL(10,2) |

---

## Step 4: Create Teachers Table

Requirements

- Teacher ID
- Teacher Name
- Email
- Subject
- Experience

---

## Step 5: Create Enrollments Table

Requirements

Relationship:

Student → Course

Columns

| Column | Description |
|---------|-------------|
| enrollment_id | Primary Key |
| student_id | Foreign Key |
| course_id | Foreign Key |
| enrollment_date | Current Date |

---

# 📝 Assignment 2: Library Database

Create a database called

```text
LibraryDB
```

Create these tables:

- Books
- Authors
- Members
- BookIssue

Each table should have proper primary keys and foreign keys.

---

# 🛒 Assignment 3: Online Shopping Database

Create database:

```text
ShoppingDB
```

Tables

- Customers
- Products
- Orders
- Payments

Think carefully about relationships between tables.

---

# 🏥 Assignment 4: Hospital Management Database

Database Name

```text
HospitalDB
```

Tables

- Doctors
- Patients
- Appointments
- Medicines

Use:

- Primary Keys
- Foreign Keys
- NOT NULL
- UNIQUE

---

# 🏦 Assignment 5: Banking Database

Database Name

```text
BankDB
```

Tables

- Customers
- Accounts
- Transactions
- Branches

Design a relational database with appropriate constraints.

---

# ⭐ Bonus Challenge

Design your own database for one of the following:

- Movie Booking System
- Hotel Management System
- Food Delivery App
- School Management System
- Cricket Tournament
- College ERP
- Inventory Management
- Employee Management
- Flight Booking System
- E-Commerce Website

Rules

- Minimum 5 tables
- Use Primary Keys
- Use Foreign Keys
- Use UNIQUE constraints
- Use NOT NULL where required
- Use AUTO_INCREMENT
- Add DEFAULT values where applicable

---

# 🧠 Thinking Challenge

Before writing SQL, answer these questions:

### 1. What is the main entity?

Example:

```
Student
```

---

### 2. What information belongs to that entity?

Example

```
Name
Email
Phone
Age
```

---

### 3. Which column should uniquely identify each record?

Example

```
Student ID
```

---

### 4. Which columns should never contain duplicate values?

Example

```
Email
Phone
```

---

### 5. Which columns should never be NULL?

Example

```
Student Name
Email
```

---

### 6. Which tables should be connected?

Example

```
Students
↓

Enrollments

↓

Courses
```

---

# 💻 Practical Task

Create all databases using SQL only.

Do **not** use any GUI tools to generate tables automatically.

Practice writing every SQL statement manually.

---

# 📂 Submission Checklist

Complete all of the following:

- [ ] Created StudentManagementSystem database
- [ ] Created LibraryDB
- [ ] Created ShoppingDB
- [ ] Created HospitalDB
- [ ] Created BankDB
- [ ] Added all required tables
- [ ] Applied Primary Keys
- [ ] Applied Foreign Keys
- [ ] Used UNIQUE constraints
- [ ] Used NOT NULL constraints
- [ ] Used AUTO_INCREMENT
- [ ] Added DEFAULT values
- [ ] Verified table structures

---

# 🚀 GitHub Challenge

Create a repository named:

```text
SQL-Day32-Assignments
```

Repository Structure

```text
SQL-Day32-Assignments/
│
├── StudentManagementSystem.sql
├── LibraryDB.sql
├── ShoppingDB.sql
├── HospitalDB.sql
├── BankDB.sql
└── README.md
```

Push all SQL files to GitHub.

---

# 🎯 Expected Learning Outcomes

After completing these assignments, you will be able to:

- Design relational databases
- Choose appropriate data types
- Apply SQL constraints effectively
- Create production-ready table structures
- Understand relationships between tables
- Build the foundation required for Data Analysis, Machine Learning, and Backend Development

---

# 🏁 Next Chapter

➡️ **Chapter 11: GitHub Commit Message & Day Summary**

# 📅 Day 32 – Part 3A
# SQL Data Manipulation Language (DML) – INSERT INTO, SELECT, DISTINCT & Aliases

> **Phase 2 – Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📖 Table of Contents

- Introduction
- What is DML?
- INSERT INTO Statement
- Single Row Insertion
- Multiple Row Insertion
- INSERT Best Practices
- Common INSERT Mistakes
- SELECT Statement
- SELECT *
- Selecting Specific Columns
- DISTINCT Keyword
- Column Aliases (AS)
- Real-Life Examples
- Summary

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand Data Manipulation Language (DML)
- Insert records into database tables
- Retrieve data using SELECT
- Display only required columns
- Remove duplicate values using DISTINCT
- Rename columns using AS
- Understand common interview questions
- Perform basic SQL operations confidently

---

# 🌍 Why is SQL Important for AI Engineers?

Every AI application stores data somewhere.

Examples:

- User Accounts
- Chat History
- Customer Information
- Model Predictions
- Logs
- Product Catalog
- Employee Data

Before building ML models, you must know how to retrieve data from databases.

Example:

Imagine Netflix wants to recommend movies.

Where does the data come from?

A SQL Database.

SQL helps us retrieve:

- User Watch History
- Ratings
- Genres
- Search History

Without SQL, AI cannot access data efficiently.

---

# 📚 What is DML?

DML stands for **Data Manipulation Language**.

It is used to work with the data inside tables.

Common DML Commands:

| Command | Purpose |
|----------|----------|
| INSERT | Add data |
| SELECT | Retrieve data |
| UPDATE | Modify data |
| DELETE | Remove data |

Today's focus:

- INSERT
- SELECT

---

# 🏫 Example Database

We will use the following table throughout this lesson.

**students**

| student_id | name | age | course | marks |
|------------|------|-----|---------|-------|
| 1 | Rahul | 20 | Python | 85 |

---

# 📥 INSERT INTO Statement

The INSERT statement is used to add new records into a table.

### Syntax

```sql
INSERT INTO table_name
VALUES(value1, value2, value3);
```

---

# Example 1

```sql
INSERT INTO students
VALUES
(1,'Rahul',20,'Python',85);
```

Data becomes:

| student_id | name | age | course | marks |
|------------|------|-----|---------|-------|
|1|Rahul|20|Python|85|

---

# Example 2

```sql
INSERT INTO students
VALUES
(2,'Amit',21,'Java',91);
```

Table

| ID | Name | Age | Course | Marks |
|----|------|------|----------|--------|
|1|Rahul|20|Python|85|
|2|Amit|21|Java|91|

---

# Inserting Using Column Names

Instead of writing every column, we can specify them.

Syntax

```sql
INSERT INTO students
(name,course)
VALUES
('Priya','AI');
```

Remaining columns become NULL or default values.

---

# Why Use Column Names?

Suppose your table has

20 columns

but you only know

- name
- email

You don't need to insert all 20 columns.

Example

```sql
INSERT INTO users
(name,email)
VALUES
('John','john@gmail.com');
```

Cleaner and safer.

---

# Multiple Row Insert

Instead of writing INSERT many times,

we can insert multiple records together.

Example

```sql
INSERT INTO students
VALUES
(3,'Neha',22,'SQL',89),
(4,'Rohan',19,'Python',76),
(5,'Karan',23,'Java',92);
```

Now database stores

5 students at once.

---

# Real Life Example

Imagine a school admits 500 students.

Bad way

```sql
INSERT INTO students ...
```

500 times ❌

Good way

```sql
INSERT INTO students
VALUES
(...),
(...),
(...),
(...);
```

One query.

Faster.

---

# INSERT Best Practices

✅ Always specify column names.

Good

```sql
INSERT INTO students
(name,age)
VALUES
('Rahul',20);
```

Bad

```sql
INSERT INTO students
VALUES
('Rahul',20);
```

If the table structure changes,

your query may fail.

---

# Common INSERT Errors

## 1. Duplicate Primary Key

```sql
INSERT INTO students
VALUES
(1,'Amit',22,'SQL',90);
```

Error

```text
Duplicate entry
```

Because ID = 1 already exists.

---

## 2. Wrong Data Type

```sql
INSERT INTO students
VALUES
('ABC','Rahul',20,'Python',80);
```

If student_id is INT,

error occurs.

---

## 3. Missing Values

```sql
INSERT INTO students
VALUES
(2,'Rahul');
```

Error

Number of values does not match.

---

# 📖 SELECT Statement

SELECT is one of the most important SQL commands.

It retrieves data from tables.

Syntax

```sql
SELECT column_name
FROM table_name;
```

---

# Select Everything

```sql
SELECT *
FROM students;
```

Output

| student_id | name | age | course | marks |
|------------|------|------|----------|--------|
|1|Rahul|20|Python|85|
|2|Amit|21|Java|91|
|3|Neha|22|SQL|89|

---

# What does * mean?

The asterisk means

**All Columns**

Equivalent to

```sql
SELECT
student_id,
name,
age,
course,
marks
FROM students;
```

---

# Selecting Specific Columns

Suppose HR only wants

- Name
- Course

Query

```sql
SELECT
name,
course
FROM students;
```

Output

| Name | Course |
|------|----------|
|Rahul|Python|
|Amit|Java|
|Neha|SQL|

---

# Selecting Three Columns

```sql
SELECT
name,
age,
marks
FROM students;
```

Output

| Name | Age | Marks |
|------|------|--------|
|Rahul|20|85|
|Amit|21|91|
|Neha|22|89|

---

# Why Avoid SELECT *

Imagine

Employee table

contains

- Salary
- Password
- Aadhaar
- Phone

Using

```sql
SELECT *
```

returns everything.

Instead

retrieve only required columns.

Benefits

- Faster
- Secure
- Less memory
- Better performance

---

# DISTINCT Keyword

Sometimes tables contain duplicate values.

Example

| Course |
|----------|
|Python|
|Java|
|Python|
|SQL|
|Java|

Query

```sql
SELECT DISTINCT course
FROM students;
```

Output

| Course |
|----------|
|Python|
|Java|
|SQL|

Duplicates removed.

---

# Why DISTINCT?

Suppose you want

all available courses.

Without DISTINCT

Python appears many times.

With DISTINCT

Only unique values.

---

# Another Example

Table

| City |
|------|
|Delhi|
|Delhi|
|Mumbai|
|Indore|
|Mumbai|

Query

```sql
SELECT DISTINCT city
FROM customers;
```

Output

| City |
|------|
|Delhi|
|Mumbai|
|Indore|

---

# Column Aliases (AS)

Aliases change the display name of a column.

Syntax

```sql
SELECT column_name AS alias_name
FROM table_name;
```

---

# Example

```sql
SELECT
name AS Student_Name
FROM students;
```

Output

| Student_Name |
|---------------|
|Rahul|
|Amit|
|Neha|

---

# Multiple Aliases

```sql
SELECT

student_id AS ID,

name AS Student,

course AS Subject,

marks AS Score

FROM students;
```

Output

| ID | Student | Subject | Score |
|----|----------|-----------|--------|
|1|Rahul|Python|85|
|2|Amit|Java|91|

---

# Why Use Aliases?

Suppose database column is

```text
customer_first_name
```

Display

```sql
SELECT
customer_first_name AS First_Name
FROM customers;
```

Reports become much easier to read.

---

# Combining Everything

```sql
SELECT DISTINCT

course AS Available_Courses

FROM students;
```

Output

| Available_Courses |
|-------------------|
|Python|
|Java|
|SQL|

This combines:

- SELECT
- DISTINCT
- AS

in one query.

---

# Real-World Scenario

Imagine you're working for an online learning platform.

The management asks:

> "Show all unique courses offered on our platform."

SQL Query:

```sql
SELECT DISTINCT course AS Available_Courses
FROM students;
```

Simple, readable, and efficient.

---

# ✅ Day 32 – Part 3A Summary

Today you learned:

- What is DML
- INSERT INTO
- Single Row Insert
- Multiple Row Insert
- INSERT Best Practices
- Common INSERT Errors
- SELECT Statement
- SELECT *
- Selecting Specific Columns
- DISTINCT
- Column Aliases (AS)

---

# ⏭️ Next: Day 32 – Part 3B

In the next part, you'll learn:

- WHERE Clause
- Comparison Operators
- Logical Operators (AND, OR, NOT)
- LIKE
- IN
- BETWEEN
- IS NULL
- ORDER BY
- LIMIT
- Mini Project: Student Database
- Practice Questions
- Interview Questions
- GitHub Commit Message

---

# 🌍 Real-World Example

Imagine you're working as a Data Analyst in a school.

The school database contains thousands of student records.

Instead of displaying every column every time, you may only need specific information.

### Student Table

| student_id | name | age | course | city | marks |
|------------|------|-----|--------|------|-------|
| 1 | Rahul | 20 | BCA | Indore | 89 |
| 2 | Priya | 21 | BCA | Delhi | 91 |
| 3 | Aman | 20 | B.Tech | Mumbai | 76 |
| 4 | Neha | 22 | BCA | Indore | 95 |
| 5 | Rahul | 20 | BCA | Indore | 89 |

---

## Example 1

Display every student.

```sql
SELECT * FROM students;
```

---

## Example 2

Display only names.

```sql
SELECT name FROM students;
```

---

## Example 3

Display name and marks.

```sql
SELECT name, marks
FROM students;
```

---

## Example 4

Display unique cities.

```sql
SELECT DISTINCT city
FROM students;
```

Output

| city |
|------|
| Indore |
| Delhi |
| Mumbai |

---

## Example 5

Rename column.

```sql
SELECT name AS Student_Name,
marks AS Score
FROM students;
```

Output

| Student_Name | Score |
|--------------|------|
| Rahul | 89 |
| Priya | 91 |

---

# 🚀 Best Practices

✅ Always write SQL keywords in uppercase.

Good

```sql
SELECT name
FROM students;
```

Bad

```sql
select name from students;
```

---

✅ Use meaningful aliases.

Good

```sql
SELECT marks AS Total_Marks
FROM students;
```

Bad

```sql
SELECT marks AS m
FROM students;
```

---

✅ Avoid unnecessary `SELECT *`

Instead,

```sql
SELECT name, course
FROM students;
```

This improves:

- Performance
- Readability
- Security

---

# ⚠ Common Mistakes

## 1 Missing Semicolon

Wrong

```sql
SELECT * FROM students
```

Correct

```sql
SELECT * FROM students;
```

---

## 2 Wrong Table Name

Wrong

```sql
SELECT *
FROM student;
```

Correct

```sql
SELECT *
FROM students;
```

---

## 3 Wrong Column Name

Wrong

```sql
SELECT fullname
FROM students;
```

Correct

```sql
SELECT name
FROM students;
```

---

## 4 Duplicate Records

Wrong

```sql
SELECT city
FROM students;
```

Correct

```sql
SELECT DISTINCT city
FROM students;
```

---

# 🧠 Practice Questions

## Beginner

1. Display all students.
2. Display only names.
3. Display only course.
4. Display age.
5. Display city.
6. Display marks.
7. Display names and marks.
8. Display names and courses.
9. Display unique cities.
10. Display unique courses.

---

## Intermediate

11. Rename name as Student_Name.

12. Rename marks as Total_Marks.

13. Display age and rename it Student_Age.

14. Display city as Student_City.

15. Display all columns.

16. Display three columns together.

17. Display two renamed columns.

18. Find unique marks.

19. Find unique ages.

20. Find unique names.

---

# 💼 Mini Assignment

Create a database called

```text
college_db
```

Create a table

```text
students
```

Insert at least **10 records**.

Practice

- SELECT *
- SELECT column
- DISTINCT
- AS

Take screenshots and upload them to GitHub.

---

# 🎯 Interview Questions

## Beginner

### 1. What is SQL?

SQL stands for Structured Query Language.

Used to communicate with relational databases.

---

### 2. What is SELECT?

Used to retrieve data from a table.

---

### 3. What does SELECT * mean?

It retrieves every column.

---

### 4. Can we retrieve only specific columns?

Yes.

```sql
SELECT name, age
FROM students;
```

---

### 5. What is DISTINCT?

Removes duplicate values.

---

### 6. What is an Alias?

Temporary name for a column.

---

### 7. Does Alias change the database?

No.

Only the output.

---

### 8. Why use Alias?

Improves readability.

---

### 9. Difference between

```sql
SELECT *
```

and

```sql
SELECT name
```

First returns all columns.

Second returns only one column.

---

### 10. Can Alias be used without AS?

Yes.

Example

```sql
SELECT name Student_Name
FROM students;
```

---

## Intermediate

### 11. Difference between DISTINCT and GROUP BY?

DISTINCT removes duplicate rows.

GROUP BY groups records for aggregation.

---

### 12. Does SELECT modify data?

No.

It only reads data.

---

### 13. Which command retrieves data?

SELECT

---

### 14. Which SQL category does SELECT belong to?

DQL (Data Query Language)

---

### 15. Which category does INSERT belong to?

DML (Data Manipulation Language)

---

### 16. Can SELECT be used without FROM?

Yes.

Example

```sql
SELECT 100;
```

Output

```text
100
```

---

### 17. Is SQL case-sensitive?

Keywords are generally not case-sensitive.

Best practice is uppercase.

---

### 18. Why avoid SELECT *?

Because

- Slower
- Uses more memory
- Returns unnecessary data

---

### 19. What happens if DISTINCT is omitted?

Duplicate values appear.

---

### 20. Which is faster?

```sql
SELECT name
```

is faster than

```sql
SELECT *
```

because fewer columns are retrieved.

---

# 🧪 Coding Challenge

Create this table.

| Roll | Name | Course | City | Marks |
|------|------|--------|------|------|

Insert **10 students**.

Now perform

- Display all students.
- Display only names.
- Display marks.
- Display names and cities.
- Display unique cities.
- Rename marks as Score.
- Rename name as Student_Name.
- Display unique courses.
- Display unique marks.
- Display all columns.

---

# 📚 Revision Notes

Remember

```text
SELECT → Retrieve data

SELECT * → All columns

SELECT column → Specific column

DISTINCT → Remove duplicates

AS → Rename columns

INSERT INTO → Add records
```

---

# 📝 GitHub Repository Structure

```text
Day-32-SQL-DML/
│
├── README.md
├── queries.sql
├── screenshots/
│   ├── insert.png
│   ├── select.png
│   ├── distinct.png
│   └── alias.png
└── notes.pdf
```

---

# 💻 GitHub Commit Message

```bash
git add .
git commit -m "Day 32 Part 3A: Learned INSERT, SELECT, DISTINCT and Aliases in SQL"
git push origin main
```

---

# 🎯 Day Summary

Today you learned:

- ✅ Data Manipulation Language (DML)
- ✅ INSERT INTO
- ✅ INSERT Multiple Records
- ✅ SELECT Statement
- ✅ SELECT Specific Columns
- ✅ SELECT *
- ✅ DISTINCT Keyword
- ✅ Column Aliases (AS)
- ✅ SQL Best Practices
- ✅ Common Mistakes
- ✅ Real-World Examples
- ✅ 20 Practice Questions
- ✅ 20 Interview Questions
- ✅ Mini Assignment

---

# 🚀 Next Topic

## **Day 32 – Part 3B**

Topics:

- WHERE Clause
- Comparison Operators
- Logical Operators (`AND`, `OR`, `NOT`)
- LIKE
- IN
- BETWEEN
- IS NULL
- ORDER BY
- LIMIT
- Mini Project: Student Database Query System

By the end of Part 3B, you'll be able to filter, sort, and search data like a real SQL developer.
# 📘 Day 32 – Part 3B.1: SQL Filtering Data with WHERE, Comparison Operators, AND, OR, NOT & LIKE

> **Phase 2 – Data & SQL**
>
> **Roadmap:** AI/ML Engineer → ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand why filtering data is important.
- Use the `WHERE` clause to retrieve specific records.
- Use comparison operators (`=`, `!=`, `>`, `<`, `>=`, `<=`).
- Combine conditions using `AND`, `OR`, and `NOT`.
- Search for patterns using the `LIKE` operator.
- Use SQL wildcards `%` and `_`.
- Write real-world SQL queries.
- Solve beginner SQL interview questions.

---

# 📖 Introduction

Imagine Instagram has **5 billion posts**.

Can you display all of them every time a user searches?

❌ No.

Instead, you search for exactly what you need.

For example:

- Posts by "Virat Kohli"
- Posts uploaded today
- Posts with more than 1M likes

This is exactly what SQL's **WHERE** clause does.

It filters data.

---

# What is WHERE?

The `WHERE` clause filters rows based on a condition.

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

---

# Example Table

## Students

| ID | Name | Age | City | Marks |
|----|------|-----|------|------|
|1|Rahul|20|Delhi|88|
|2|Amit|22|Mumbai|91|
|3|Priya|21|Delhi|75|
|4|Sneha|23|Pune|95|
|5|Rohan|20|Mumbai|82|

---

# Example 1

Display every student.

```sql
SELECT * FROM Students;
```

Output

| ID | Name | Age | City | Marks |
|----|------|-----|------|------|
|1|Rahul|20|Delhi|88|
|2|Amit|22|Mumbai|91|
|3|Priya|21|Delhi|75|
|4|Sneha|23|Pune|95|
|5|Rohan|20|Mumbai|82|

---

# Example 2

Display only students from Delhi.

```sql
SELECT *
FROM Students
WHERE City='Delhi';
```

Output

| ID | Name | City |
|----|------|------|
|1|Rahul|Delhi|
|3|Priya|Delhi|

---

# Comparison Operators

These compare values.

| Operator | Meaning |
|----------|---------|
| = | Equal |
| != | Not Equal |
| <> | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

# Equal (=)

Find student with ID = 2.

```sql
SELECT *
FROM Students
WHERE ID=2;
```

Output

|ID|Name|
|--|----|
|2|Amit|

---

# Greater Than (>)

Students with marks greater than 90.

```sql
SELECT *
FROM Students
WHERE Marks>90;
```

Output

|Name|Marks|
|----|-----|
|Amit|91|
|Sneha|95|

---

# Less Than (<)

Students scoring below 80.

```sql
SELECT *
FROM Students
WHERE Marks<80;
```

Output

|Name|Marks|
|----|-----|
|Priya|75|

---

# Greater Than or Equal (>=)

```sql
SELECT *
FROM Students
WHERE Marks>=88;
```

---

# Less Than or Equal (<=)

```sql
SELECT *
FROM Students
WHERE Age<=20;
```

---

# Not Equal (!=)

Display students except Delhi.

```sql
SELECT *
FROM Students
WHERE City!='Delhi';
```

Output

|Name|City|
|----|----|
|Amit|Mumbai|
|Sneha|Pune|
|Rohan|Mumbai|

---

# Multiple Conditions

Real applications rarely search using only one condition.

Example

Find students

- From Delhi
- Marks above 80

---

# AND Operator

Both conditions must be TRUE.

Syntax

```sql
SELECT *
FROM table
WHERE condition1
AND condition2;
```

Example

```sql
SELECT *
FROM Students
WHERE City='Delhi'
AND Marks>80;
```

Output

|Name|City|Marks|
|----|----|-----|
|Rahul|Delhi|88|

---

# Real-Life Example

E-commerce

Find

- Electronics
- Price below ₹50,000

```sql
SELECT *
FROM Products
WHERE Category='Electronics'
AND Price<50000;
```

---

# OR Operator

At least one condition should be TRUE.

Syntax

```sql
SELECT *
FROM table
WHERE condition1
OR condition2;
```

Example

```sql
SELECT *
FROM Students
WHERE City='Delhi'
OR City='Mumbai';
```

Output

Rahul

Amit

Priya

Rohan

---

# Real-Life Example

Find employees

Working in

- HR
- Finance

```sql
SELECT *
FROM Employees
WHERE Department='HR'
OR Department='Finance';
```

---

# NOT Operator

Reverses condition.

Example

```sql
SELECT *
FROM Students
WHERE NOT City='Delhi';
```

Output

Mumbai

Mumbai

Pune

---

# Combining AND + OR

Example

Students

- Delhi
OR
- Mumbai
AND
- Marks above 85

```sql
SELECT *
FROM Students
WHERE (City='Delhi' OR City='Mumbai')
AND Marks>85;
```

Output

Rahul

Amit

---

# LIKE Operator

Used to search patterns inside text.

Example

Search names beginning with "R".

```sql
SELECT *
FROM Students
WHERE Name LIKE 'R%';
```

Output

Rahul

Rohan

---

# Wildcards

SQL uses two wildcards.

| Wildcard | Meaning |
|----------|----------|
| % | Any number of characters |
| _ | Exactly one character |

---

# %

Matches zero or more characters.

Example

Starts with R.

```sql
SELECT *
FROM Students
WHERE Name LIKE 'R%';
```

Matches

Rahul

Rohan

Rakesh

R

---

Contains "it"

```sql
SELECT *
FROM Students
WHERE Name LIKE '%it%';
```

Matches

Amit

---

Ends with "a"

```sql
SELECT *
FROM Students
WHERE Name LIKE '%a';
```

Matches

Priya

Sneha

---

# _

Represents exactly one character.

Example

Four-letter names.

```sql
SELECT *
FROM Students
WHERE Name LIKE '____';
```

Matches

Amit

Only names having exactly four letters.

---

# Multiple Wildcards

Example

Starts with P

Ends with a

```sql
SELECT *
FROM Students
WHERE Name LIKE 'P%a';
```

Matches

Priya

---

# Real-World Examples

## Gmail

Search emails

Containing "OpenAI"

```sql
SELECT *
FROM Emails
WHERE Subject LIKE '%OpenAI%';
```

---

## Amazon

Products

Starting with iPhone

```sql
SELECT *
FROM Products
WHERE ProductName LIKE 'iPhone%';
```

---

## YouTube

Search channels

Containing "Code"

```sql
SELECT *
FROM Channels
WHERE Name LIKE '%Code%';
```

---

# Common Mistakes

❌

```sql
WHERE Name=Rohan
```

✅

```sql
WHERE Name='Rohan'
```

---

❌

```sql
WHERE Marks=>"90"
```

✅

```sql
WHERE Marks>=90
```

---

❌

```sql
LIKE %Rahul%
```

✅

```sql
LIKE '%Rahul%'
```

---

# Practice Questions

## Easy

1. Display students from Mumbai.
2. Display students older than 21.
3. Display students scoring below 80.
4. Display students except Pune.
5. Display students with marks above 90.

---

## Medium

6. Students from Delhi having marks above 85.
7. Students from Mumbai OR Pune.
8. Students NOT from Delhi.
9. Students whose names start with S.
10. Students whose names end with a.

---

## Challenge

11. Students from Delhi OR Mumbai with marks above 80.
12. Students whose names contain "it".
13. Students older than 20 but below 23.
14. Students whose names have exactly five letters.
15. Students not from Mumbai and marks above 85.

---

# Interview Questions

## Beginner

### 1. What is the WHERE clause?

The `WHERE` clause filters records based on a specified condition.

---

### 2. Can WHERE be used with SELECT?

✅ Yes.

---

### 3. Difference between WHERE and HAVING?

| WHERE | HAVING |
|--------|---------|
| Filters rows before grouping | Filters groups after aggregation |

---

### 4. Which operator checks equality?

`=`

---

### 5. Which operator checks inequality?

`!=` or `<>`

---

### 6. What does AND do?

Returns rows only if **all** conditions are true.

---

### 7. What does OR do?

Returns rows if **at least one** condition is true.

---

### 8. What does NOT do?

Reverses a condition.

---

### 9. What is LIKE used for?

Pattern matching in text values.

---

### 10. Difference between `%` and `_`?

- `%` → Zero or more characters
- `_` → Exactly one character

---

# Assignment

Create a table named **Employees** with the following columns:

- EmployeeID
- Name
- Department
- Salary
- City

Insert at least **10 records**, then write SQL queries to:

- Find employees with salary greater than ₹50,000.
- Find employees working in Delhi.
- Find employees from Delhi **and** salary above ₹70,000.
- Find employees from Mumbai **or** Pune.
- Find employees whose names start with **A**.
- Find employees whose names contain **"an"**.
- Find employees not working in HR.

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32 Part 3B.1: Learned WHERE clause, comparison operators, logical operators, and LIKE in SQL"
git push origin main
```

---

# 🎉 Day Summary

Today you learned:

- ✅ WHERE Clause
- ✅ Comparison Operators
- ✅ AND
- ✅ OR
- ✅ NOT
- ✅ LIKE Operator
- ✅ SQL Wildcards (`%` and `_`)
- ✅ Pattern Matching
- ✅ Filtering Data
- ✅ Real-world SQL Queries
- ✅ Practice Problems
- ✅ Interview Questions

---

# 🚀 Next Lesson

**Day 32 – Part 3B.2**

Topics:

- `IN`
- `BETWEEN`
- `IS NULL`
- `ORDER BY`
- `LIMIT`
- Mini Project: Student Database
- 30+ Interview Questions
- Advanced SQL Practice
# 📅 Day 32 – SQL Fundamentals (Part 3B)

> **Phase 2: Data & SQL**
>
> **Topics Covered Today**
>
> - IN Operator
> - BETWEEN Operator
> - IS NULL & IS NOT NULL
> - ORDER BY
> - LIMIT
> - Mini Project
> - Practice Questions
> - Interview Questions

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Filter data using multiple values
- Filter data within a range
- Handle NULL values
- Sort records
- Limit output
- Build simple SQL queries used in real-world applications

---

# 📚 Sample Database

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    marks INT,
    course VARCHAR(30),
    email VARCHAR(100)
);
```

---

# Sample Data

```sql
INSERT INTO students VALUES
(1,'Rahul',20,'Indore',90,'BCA','rahul@gmail.com'),
(2,'Priya',21,'Delhi',82,'BTech',NULL),
(3,'Aman',22,'Mumbai',75,'BCA','aman@gmail.com'),
(4,'Sneha',20,'Delhi',95,'BSc','sneha@gmail.com'),
(5,'Riya',23,'Indore',68,'BCA',NULL),
(6,'Arjun',21,'Pune',88,'BTech','arjun@gmail.com');
```

---

# IN Operator

## What is IN?

The **IN** operator checks whether a value exists in a list.

Instead of writing multiple OR conditions, we use IN.

---

## Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name IN(value1,value2,...);
```

---

## Example 1

Students from Delhi or Indore

```sql
SELECT *
FROM students
WHERE city IN ('Delhi','Indore');
```

Output

```
Rahul
Priya
Sneha
Riya
```

---

## Example 2

Students studying BCA or BTech

```sql
SELECT *
FROM students
WHERE course IN ('BCA','BTech');
```

---

# NOT IN

Returns rows that are NOT in the list.

```sql
SELECT *
FROM students
WHERE city NOT IN ('Delhi','Indore');
```

---

# BETWEEN Operator

## What is BETWEEN?

Used to find values within a range.

---

## Syntax

```sql
SELECT *
FROM table_name
WHERE column BETWEEN value1 AND value2;
```

---

## Example 1

Students scoring between 80 and 95.

```sql
SELECT *
FROM students
WHERE marks BETWEEN 80 AND 95;
```

Output

```
Rahul
Priya
Sneha
Arjun
```

---

## Example 2

Students aged between 20 and 22.

```sql
SELECT *
FROM students
WHERE age BETWEEN 20 AND 22;
```

---

# NOT BETWEEN

```sql
SELECT *
FROM students
WHERE marks NOT BETWEEN 80 AND 95;
```

---

# IS NULL

## What is NULL?

NULL means **no value**.

It is NOT:

- Zero
- Empty string
- False

It simply means data is missing.

---

## Syntax

```sql
SELECT *
FROM table_name
WHERE column IS NULL;
```

---

## Example

Find students whose email is missing.

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

Output

```
Priya
Riya
```

---

# IS NOT NULL

```sql
SELECT *
FROM students
WHERE email IS NOT NULL;
```

---

# ORDER BY

## What is ORDER BY?

Sorts records.

Ascending

Descending

---

## Syntax

```sql
SELECT *
FROM table_name
ORDER BY column;
```

---

# Ascending Order

```sql
SELECT *
FROM students
ORDER BY marks;
```

Lowest marks first.

---

# Descending Order

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

Highest marks first.

---

# Multiple Columns

```sql
SELECT *
FROM students
ORDER BY city,marks DESC;
```

Sort by city first.

Then marks.

---

# LIMIT

## What is LIMIT?

Returns only a fixed number of rows.

Useful for:

- Top 10 students
- Latest 5 records
- Pagination

---

## Syntax

```sql
SELECT *
FROM table_name
LIMIT number;
```

---

## Example

First three students

```sql
SELECT *
FROM students
LIMIT 3;
```

---

## Example

Top two highest scorers

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 2;
```

Output

```
Sneha
Rahul
```

---

# Real World Examples

## Highest Paid Employees

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

---

## Recent Orders

```sql
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 10;
```

---

## Products in Stock

```sql
SELECT *
FROM products
WHERE stock > 0;
```

---

# Mini Project

## Student Database

### Task 1

Find students from Delhi.

```sql
SELECT *
FROM students
WHERE city='Delhi';
```

---

### Task 2

Students scoring above 85.

```sql
SELECT *
FROM students
WHERE marks>85;
```

---

### Task 3

Students between age 20–22.

```sql
SELECT *
FROM students
WHERE age BETWEEN 20 AND 22;
```

---

### Task 4

Students whose email is missing.

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

---

### Task 5

Top three scorers.

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3;
```

---

# Practice Questions

## Easy

1. Display students from Mumbai.
2. Display students from Delhi or Pune.
3. Find students older than 21.
4. Display students with marks above 80.
5. Display students whose email is NULL.

---

## Medium

6. Find students with marks between 70 and 90.
7. Find students not from Delhi.
8. Display top 5 scorers.
9. Sort students alphabetically.
10. Display students ordered by city.

---

## Advanced

11. Find BCA students from Indore.
12. Find students with marks above 80 and city Delhi.
13. Find students whose email exists.
14. Find lowest three scorers.
15. Sort by course and marks.

---

# Interview Questions

## Beginner

### 1. What is IN?

Checks multiple values.

---

### 2. Difference between IN and OR?

IN is shorter and easier to read.

---

### 3. What does BETWEEN do?

Returns values inside a range.

---

### 4. Is BETWEEN inclusive?

Yes.

---

### 5. What is NULL?

Represents missing data.

---

### 6. Can NULL equal zero?

No.

---

### 7. Difference between NULL and Empty String?

NULL means no value.

Empty string is a value.

---

### 8. What is ORDER BY?

Sorts records.

---

### 9. Default ORDER BY?

Ascending.

---

### 10. DESC keyword?

Sorts descending.

---

## Intermediate

### 11. Can ORDER BY use multiple columns?

Yes.

---

### 12. Why use LIMIT?

To reduce returned records.

---

### 13. Which clause executes first?

WHERE executes before ORDER BY.

---

### 14. Difference between LIMIT and TOP?

LIMIT → MySQL

TOP → SQL Server

---

### 15. Can LIMIT work without ORDER BY?

Yes.

But results may not be deterministic.

---

## Advanced

### 16. Why avoid SELECT *?

Because it:

- Reads unnecessary columns
- Slows queries
- Increases network traffic

---

### 17. Can NULL be compared using = ?

No.

Use

```sql
IS NULL
```

---

### 18. Which is faster?

```sql
WHERE city='Delhi'
```

than

```sql
WHERE city LIKE 'Delhi'
```

because LIKE performs pattern matching.

---

### 19. Difference between WHERE and HAVING?

WHERE filters rows.

HAVING filters grouped data.

---

### 20. Best Practices

- Avoid SELECT *
- Use LIMIT when testing
- Always use WHERE carefully
- Use indexes on frequently searched columns
- Write readable SQL

---

# Assignment

Create a database named

```
CollegeDB
```

Create table

```
Students
```

Insert

10 student records.

Perform

- WHERE
- BETWEEN
- IN
- ORDER BY
- LIMIT

Take screenshots of your queries and results.

---

# GitHub Folder Structure

```text
Day-32-SQL-Part-3B/
│
├── README.md
├── queries.sql
├── database.sql
└── screenshots/
```

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 32: Mastered SQL Filtering, Sorting and Limiting Results"
git push origin main
```

---

# 📌 Day 32 Summary

Today you learned:

- ✅ IN
- ✅ NOT IN
- ✅ BETWEEN
- ✅ NOT BETWEEN
- ✅ IS NULL
- ✅ IS NOT NULL
- ✅ ORDER BY
- ✅ LIMIT
- ✅ SQL Filtering Techniques
- ✅ SQL Sorting
- ✅ Student Database Mini Project

---

# 🚀 What's Next?

**Day 33 – SQL Aggregate Functions & Grouping**

Topics:
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING
- Real-world Business Queries