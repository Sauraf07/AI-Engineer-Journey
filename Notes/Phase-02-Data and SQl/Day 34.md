# 🚀 Day 34 - SQL JOINS (Complete Guide)

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Understand why SQL JOINs are used
* Learn different types of JOINs
* Retrieve data from multiple tables
* Write efficient JOIN queries
* Solve real-world SQL problems
* Answer SQL JOIN interview questions confidently

---

# 📖 What is a JOIN?

A **JOIN** is used to combine data from two or more tables based on a related column.

Instead of storing duplicate data, relational databases connect tables using keys.

### Real-Life Example

Imagine two tables:

### Students

| Student_ID | Name    |
| ---------- | ------- |
| 101        | Alice   |
| 102        | Bob     |
| 103        | Charlie |

### Courses

| Student_ID | Course |
| ---------- | ------ |
| 101        | Python |
| 102        | SQL    |
| 104        | Java   |

Using a JOIN, we can combine these tables based on `Student_ID`.

---

# Why JOINs Matter

JOINs are used in almost every real-world application.

Examples:

* Banking Systems
* E-commerce Websites
* Hospital Management
* School Management
* AI Data Pipelines
* Analytics Dashboards

---

# Types of SQL JOINs

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL OUTER JOIN
* CROSS JOIN
* SELF JOIN

---

# Sample Database

## Students

| Student_ID | Name    | City   |
| ---------- | ------- | ------ |
| 101        | Alice   | Delhi  |
| 102        | Bob     | Mumbai |
| 103        | Charlie | Pune   |

---

## Courses

| Student_ID | Course |
| ---------- | ------ |
| 101        | Python |
| 102        | SQL    |
| 104        | Java   |

---

# 1. INNER JOIN

Returns only matching rows.

```sql
SELECT
    Students.Name,
    Courses.Course
FROM Students
INNER JOIN Courses
ON Students.Student_ID = Courses.Student_ID;
```

### Output

| Name  | Course |
| ----- | ------ |
| Alice | Python |
| Bob   | SQL    |

---

# 2. LEFT JOIN

Returns all records from the left table and matching records from the right table.

```sql
SELECT
    Students.Name,
    Courses.Course
FROM Students
LEFT JOIN Courses
ON Students.Student_ID = Courses.Student_ID;
```

### Output

| Name    | Course |
| ------- | ------ |
| Alice   | Python |
| Bob     | SQL    |
| Charlie | NULL   |

---

# 3. RIGHT JOIN

Returns all rows from the right table.

```sql
SELECT
    Students.Name,
    Courses.Course
FROM Students
RIGHT JOIN Courses
ON Students.Student_ID = Courses.Student_ID;
```

### Output

| Name  | Course |
| ----- | ------ |
| Alice | Python |
| Bob   | SQL    |
| NULL  | Java   |

---

# 4. FULL OUTER JOIN

Returns all rows from both tables.

```sql
SELECT
    Students.Name,
    Courses.Course
FROM Students
FULL OUTER JOIN Courses
ON Students.Student_ID = Courses.Student_ID;
```

### Output

| Name    | Course |
| ------- | ------ |
| Alice   | Python |
| Bob     | SQL    |
| Charlie | NULL   |
| NULL    | Java   |

> **Note:** MySQL does not directly support `FULL OUTER JOIN`. It can be simulated using `UNION` of `LEFT JOIN` and `RIGHT JOIN`.

---

# 5. CROSS JOIN

Returns every possible combination.

```sql
SELECT
    Students.Name,
    Courses.Course
FROM Students
CROSS JOIN Courses;
```

If there are 3 students and 3 courses:

**Total Rows = 3 × 3 = 9**

---

# 6. SELF JOIN

A table joins with itself.

Example:

```sql
SELECT
    A.Name AS Employee,
    B.Name AS Manager
FROM Employees A
JOIN Employees B
ON A.Manager_ID = B.Employee_ID;
```

---

# Primary Key vs Foreign Key

## Primary Key

* Unique
* Cannot be NULL
* Identifies each row

Example:

```text
Student_ID
```

---

## Foreign Key

References the primary key of another table.

Example:

```text
Student_ID
```

in the `Courses` table.

---

# Real-World Examples

## E-Commerce

Tables:

* Customers
* Orders

```sql
SELECT Customers.Name,
       Orders.Order_ID
FROM Customers
JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;
```

---

## Banking

Tables:

* Customers
* Accounts

JOIN them to display account details.

---

## Hospital

Tables:

* Patients
* Doctors
* Appointments

JOIN them to display appointment history.

---

# Mini Project

## Student Course Management System

### Tables

Students

```text
Student_ID
Name
Email
```

Courses

```text
Course_ID
Student_ID
Course_Name
```

### Tasks

* Display student names with courses
* Find students without courses
* Count students in each course
* List all students and their enrolled courses

---

# Practice Questions

## Beginner

1. Display student names with courses.
2. Find students who are enrolled.
3. Display all students using LEFT JOIN.
4. Display all courses using RIGHT JOIN.
5. Count total matching records.

---

## Intermediate

6. Join three tables.
7. Find students without courses.
8. Find courses without students.
9. Display student-city with course.
10. Group results using JOIN.

---

## Advanced

11. Employee-Manager hierarchy.
12. Customer Orders Report.
13. Product Sales Dashboard.
14. Banking Transaction Report.
15. Multi-table JOIN challenge.

---

# Common Mistakes

❌ Forgetting the `ON` condition

```sql
SELECT *
FROM Students
JOIN Courses;
```

This creates a Cartesian product.

---

❌ Using the wrong key

Always join using related columns.

```sql
Students.Student_ID = Courses.Student_ID
```

---

# Interview Questions

## Beginner

### 1. What is a JOIN?

A JOIN combines data from multiple tables using a related column.

---

### 2. Why do we use JOINs?

To retrieve related data stored in different tables.

---

### 3. What is INNER JOIN?

Returns only matching rows from both tables.

---

### 4. What is LEFT JOIN?

Returns all rows from the left table and matching rows from the right table.

---

### 5. What is RIGHT JOIN?

Returns all rows from the right table and matching rows from the left table.

---

### 6. What is FULL OUTER JOIN?

Returns all rows from both tables, whether matched or not.

---

### 7. What is CROSS JOIN?

Returns every possible combination of rows.

---

### 8. What is SELF JOIN?

A table joined with itself.

---

### 9. What is the difference between Primary Key and Foreign Key?

| Primary Key       | Foreign Key                            |
| ----------------- | -------------------------------------- |
| Unique identifier | References another table's primary key |

---

### 10. Which JOIN is most commonly used?

`INNER JOIN` and `LEFT JOIN`.

---

# Best Practices

* Always use meaningful aliases.
* Join using indexed columns when possible.
* Select only required columns instead of `SELECT *`.
* Understand table relationships before writing queries.
* Test queries with sample data before using them in production.

---

# Summary

Today you learned:

* SQL JOINs
* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL OUTER JOIN
* CROSS JOIN
* SELF JOIN
* Primary & Foreign Keys
* Real-world use cases
* Interview questions
* Hands-on mini project

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 34: Learned SQL JOINs with practical examples and interview questions"
git push origin main
```

---

# 🚀 Next Day

**Day 35 – SQL Aggregate Functions & GROUP BY**

Topics:

* COUNT()
* SUM()
* AVG()
* MIN()
* MAX()
* GROUP BY
* HAVING
* Real-world analytics queries
* Interview questions
