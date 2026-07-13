# 🚀 Day 31 - Introduction to Databases & SQL

> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Goal of Day 31

Welcome to **Phase 2** of the roadmap!

Today marks the beginning of your journey into databases and SQL, one of the most important skills for AI Engineers, Machine Learning Engineers, Data Scientists, and Backend Developers.

By the end of today, you will:

* Understand what a database is
* Learn why SQL is important
* Understand different database types
* Learn relational databases
* Install MySQL
* Connect to MySQL Workbench
* Write your first SQL query
* Understand basic SQL terminology

---

# 📚 Why Learn SQL?

Almost every AI or ML project stores data in a database.

Examples include:

* Customer information
* Sales records
* Chat history
* User profiles
* Training datasets
* Model predictions
* Analytics dashboards

Before building AI systems, you must know how to retrieve and manage data efficiently.

---

# 🌍 Real-World Example

Imagine you're building an AI-powered e-commerce recommendation system.

Instead of storing products in Python variables like this:

```python
products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]
```

Real companies store millions of products inside databases.

Your AI model retrieves only the required data using SQL.

---

# 🗄️ What is a Database?

A **database** is an organized collection of data that allows you to store, manage, retrieve, and update information efficiently.

Think of a database as a **digital library** where information is stored in a structured manner.

---

# 💡 Why Do We Need Databases?

Without databases:

* Data is difficult to manage
* Searching is slow
* Data gets duplicated
* Security becomes difficult

With databases:

* Fast searching
* Easy updates
* Better security
* Handles millions of records
* Multiple users can access data simultaneously

---

# 📊 Types of Databases

## 1. Relational Database (SQL)

Stores data in tables.

Examples:

* MySQL
* PostgreSQL
* SQLite
* Microsoft SQL Server
* Oracle Database

Example:

| Student ID | Name  | Marks |
| ---------- | ----- | ----- |
| 1          | Rahul | 92    |
| 2          | Priya | 88    |
| 3          | Aman  | 95    |

---

## 2. NoSQL Database

Stores unstructured or semi-structured data.

Examples:

* MongoDB
* Firebase Firestore
* Cassandra
* Redis

Example:

```json
{
  "name": "Rahul",
  "age": 21,
  "skills": ["Python", "SQL", "Machine Learning"]
}
```

---

# 🤔 SQL vs NoSQL

| SQL                    | NoSQL                             |
| ---------------------- | --------------------------------- |
| Tables                 | Documents/Key-Value/Graph         |
| Structured Data        | Flexible Data                     |
| Fixed Schema           | Dynamic Schema                    |
| ACID Transactions      | High Scalability                  |
| Best for Banking & ERP | Best for Chat Apps & Social Media |

---

# 🧠 What is SQL?

**SQL (Structured Query Language)** is the language used to communicate with relational databases.

SQL allows you to:

* Create databases
* Create tables
* Insert data
* Update data
* Delete data
* Retrieve data
* Analyze data

---

# 📌 Where is SQL Used?

* Banking Systems
* Amazon
* Netflix
* Google
* Uber
* Swiggy
* Flipkart
* Hospital Management Systems
* Student Portals
* AI Applications

---

# 🛠️ Popular SQL Databases

| Database   | Best For                |
| ---------- | ----------------------- |
| MySQL      | Web Applications        |
| PostgreSQL | AI & Analytics          |
| SQLite     | Small Projects          |
| SQL Server | Enterprise Applications |
| Oracle     | Large Organizations     |

---

# 🧩 Basic Database Terminology

## Database

A collection of related tables.

---

## Table

A collection of rows and columns.

Example:

| ID | Name  | City   |
| -- | ----- | ------ |
| 1  | Rahul | Indore |
| 2  | Priya | Bhopal |

---

## Row (Record)

A single entry in a table.

Example:

| ID | Name  | City   |
| -- | ----- | ------ |
| 1  | Rahul | Indore |

---

## Column (Field)

A specific attribute of the data.

Example:

* ID
* Name
* City

---

## Primary Key

A unique identifier for every row.

Example:

```
Student ID
```

Every student has a different ID.

---

# 🔧 Installing MySQL

Download and install:

* MySQL Community Server
* MySQL Workbench

During installation:

* Create a root password
* Remember the password
* Keep default settings unless required otherwise

---

# 🖥️ Connecting to MySQL

Open MySQL Workbench.

Create a new connection.

Fill in:

* Host: `localhost`
* Port: `3306`
* Username: `root`
* Password: Your password

Click **Test Connection**.

If successful, connect to the server.

---

# ✨ Your First SQL Query

```sql
SELECT 'Hello, SQL!';
```

Output:

```
Hello, SQL!
```

Congratulations! 🎉 You just executed your first SQL query.

---

# 📝 SQL Comments

Single-line comment:

```sql
-- This is a comment
```

Multi-line comment:

```sql
/*
This is
a multi-line comment
*/
```

---

# 💻 Practice Exercises

1. Install MySQL.
2. Install MySQL Workbench.
3. Connect to the database.
4. Execute `SELECT 'Hello, SQL!';`
5. Explore the Workbench interface.
6. Learn keyboard shortcuts.
7. Read about SQL syntax.

---

# 🎯 Mini Assignment

Complete the following tasks:

* Install MySQL Server
* Install MySQL Workbench
* Connect successfully
* Execute your first SQL query
* Take a screenshot of the successful connection
* Upload your notes to GitHub

---

# 💼 Industry Use Cases

AI Engineers use SQL to:

* Load training datasets
* Analyze customer behavior
* Build recommendation systems
* Generate reports
* Store chatbot conversations
* Retrieve user information
* Build analytics dashboards

---

# 🎤 Interview Questions

## Beginner

### 1. What is a database?

A database is an organized collection of data that allows efficient storage, retrieval, and management.

---

### 2. What is SQL?

SQL (Structured Query Language) is used to communicate with relational databases.

---

### 3. What is a relational database?

A database that stores data in tables with relationships between them.

---

### 4. Name five popular SQL databases.

* MySQL
* PostgreSQL
* SQLite
* SQL Server
* Oracle Database

---

### 5. What is the difference between SQL and NoSQL?

SQL databases use structured tables and fixed schemas, while NoSQL databases support flexible data models like documents and key-value pairs.

---

### 6. What is a table?

A table is a collection of rows and columns used to store related data.

---

### 7. What is a row?

A row represents a single record in a table.

---

### 8. What is a column?

A column stores a specific type of information for every record.

---

### 9. What is a primary key?

A column that uniquely identifies every row in a table.

---

### 10. Why is SQL important for AI Engineers?

Because AI applications rely on data stored in databases, and SQL is used to retrieve, clean, filter, and analyze that data efficiently.

---

# 📖 Resources

## Official Documentation

* https://dev.mysql.com/doc/
* https://www.mysql.com/

## Free Learning

* SQLBolt
* W3Schools SQL Tutorial
* MySQL Tutorial by GeeksforGeeks

## Practice Platforms

* HackerRank SQL
* LeetCode Database
* StrataScratch

---

# 📅 Today's Checklist

* [ ] Learn what a database is
* [ ] Understand SQL basics
* [ ] Learn SQL vs NoSQL
* [ ] Install MySQL
* [ ] Install MySQL Workbench
* [ ] Connect to the database
* [ ] Execute your first SQL query
* [ ] Push today's notes to GitHub

---

# 🎉 Day 31 Summary

Today you learned:

* What is a Database
* Why Databases are Important
* SQL vs NoSQL
* Relational Databases
* Database Terminology
* MySQL Installation
* MySQL Workbench
* First SQL Query
* Real-World Use Cases
* Interview Questions

---

# 🚀 What's Next?

**Day 32 – Creating Databases and Tables**

Topics:

* CREATE DATABASE
* CREATE TABLE
* Data Types
* Constraints
* Primary Key
* Auto Increment
* NOT NULL
* DEFAULT
* Hands-on Practice
* Mini Project

Happy Learning! 🎯
