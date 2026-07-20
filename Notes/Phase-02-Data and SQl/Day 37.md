# 🔗 Day 37 – SQL Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN & SELF JOIN

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer
> **Day:** 37
> **Topic:** SQL Joins

---

# 📌 Table of Contents

1. [Learning Objectives](#-learning-objectives)
2. [What is a SQL JOIN?](#-what-is-a-sql-join)
3. [Why SQL Joins Matter](#-why-sql-joins-matter)
4. [Prerequisites](#-prerequisites)
5. [Sample Database](#-sample-database)
6. [INNER JOIN](#1️⃣-inner-join)
7. [LEFT JOIN](#2️⃣-left-join)
8. [RIGHT JOIN](#3️⃣-right-join)
9. [CROSS JOIN](#4️⃣-cross-join)
10. [SELF JOIN](#5️⃣-self-join)
11. [Joining Multiple Tables](#-joining-multiple-tables)
12. [JOIN with WHERE](#-join-with-where)
13. [JOIN with GROUP BY](#-join-with-group-by)
14. [JOIN with Aggregate Functions](#-join-with-aggregate-functions)
15. [Common Mistakes](#-common-mistakes)
16. [Real-World Use Cases](#-real-world-use-cases)
17. [Hands-On Exercises](#-hands-on-exercises)
18. [Mini Project](#-mini-project--e-commerce-sales-analysis)
19. [Interview Questions](#-sql-joins-interview-questions)
20. [Quick Revision Cheat Sheet](#-quick-revision-cheat-sheet)
21. [Day 37 Summary](#-day-37-summary)

---

# 🎯 Learning Objectives

By the end of Day 37, you will be able to:

* Understand relationships between database tables
* Understand Primary Keys and Foreign Keys
* Understand why joins are required
* Combine data from multiple tables
* Use `INNER JOIN`
* Use `LEFT JOIN`
* Use `RIGHT JOIN`
* Understand `FULL OUTER JOIN`
* Use `CROSS JOIN`
* Perform `SELF JOIN`
* Join three or more tables
* Use joins with `WHERE`
* Use joins with `GROUP BY`
* Use joins with aggregate functions
* Solve real-world SQL problems
* Answer common SQL JOIN interview questions
* Build an E-Commerce Sales Analysis mini project

---

# 🤔 What is a SQL JOIN?

In a relational database, data is usually stored across multiple tables.

For example, an e-commerce application might have separate tables for:

```text
Customers
Products
Orders
Payments
Employees
```

Instead of storing everything inside one huge table, databases separate related information into different tables.

A `JOIN` allows us to combine related data from these tables.

---

# 🌍 Real-Life Example

Imagine we have two tables.

## Customers Table

| customer_id | customer_name | city   |
| ----------- | ------------- | ------ |
| 1           | Rahul         | Indore |
| 2           | Priya         | Bhopal |
| 3           | Amit          | Delhi  |
| 4           | Neha          | Mumbai |

## Orders Table

| order_id | customer_id | amount |
| -------- | ----------- | ------ |
| 101      | 1           | 5000   |
| 102      | 2           | 3000   |
| 103      | 1           | 2000   |
| 104      | 3           | 7000   |

Suppose we want to answer:

> Which customer placed which order?

The `Customers` table contains the customer's name.

The `Orders` table contains the order information.

The common column is:

```text
customer_id
```

We can combine the tables using a JOIN.

```sql
SELECT
    customers.customer_name,
    orders.order_id,
    orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

Result:

| customer_name | order_id | amount |
| ------------- | -------- | ------ |
| Rahul         | 101      | 5000   |
| Rahul         | 103      | 2000   |
| Priya         | 102      | 3000   |
| Amit          | 104      | 7000   |

This is the basic idea behind SQL Joins.

---

# 🚀 Why SQL Joins Matter

In real-world applications, data is rarely stored in one table.

For example:

## E-Commerce

```text
Customers
    ↓
Orders
    ↓
Order_Items
    ↓
Products
```

## Social Media

```text
Users
    ↓
Posts
    ↓
Comments
    ↓
Likes
```

## AI Application

```text
Users
    ↓
Conversations
    ↓
Messages
    ↓
Feedback
```

## Machine Learning Platform

```text
Users
    ↓
Datasets
    ↓
Experiments
    ↓
Models
    ↓
Predictions
```

To analyze data across these tables, we use SQL joins.

---

# 📚 Prerequisites

Before learning joins, you should understand:

* Tables
* Rows
* Columns
* `SELECT`
* `WHERE`
* Primary Keys
* Foreign Keys
* Aggregate Functions
* `GROUP BY`
* `HAVING`

---

# 🔑 Primary Key

A Primary Key uniquely identifies every row in a table.

Example:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100)
);
```

Here:

```text
customer_id
```

is the Primary Key.

Each customer must have a unique `customer_id`.

---

# 🔗 Foreign Key

A Foreign Key creates a relationship between two tables.

Example:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
```

Here:

```text
customer_id
```

connects the `orders` table with the `customers` table.

Relationship:

```text
Customers
customer_id
     │
     │
     ▼
Orders
customer_id
```

---

# 🗄️ Sample Database

We will use the following database throughout this lesson.

---

## Create Database

```sql
CREATE DATABASE ecommerce_db;
```

Use the database:

```sql
USE ecommerce_db;
```

---

# Create Customers Table

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100)
);
```

Insert data:

```sql
INSERT INTO customers
VALUES
(1, 'Rahul', 'Indore'),
(2, 'Priya', 'Bhopal'),
(3, 'Amit', 'Delhi'),
(4, 'Neha', 'Mumbai'),
(5, 'Rohan', 'Pune');
```

---

# Create Orders Table

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2),
    order_date DATE
);
```

Insert data:

```sql
INSERT INTO orders
VALUES
(101, 1, 5000, '2026-01-10'),
(102, 2, 3000, '2026-01-15'),
(103, 1, 2000, '2026-02-01'),
(104, 3, 7000, '2026-02-10'),
(105, 2, 1500, '2026-03-05');
```

---

# 🔥 Types of SQL Joins

The major types of joins are:

```text
1. INNER JOIN
2. LEFT JOIN
3. RIGHT JOIN
4. FULL OUTER JOIN
5. CROSS JOIN
6. SELF JOIN
```

Let's understand each one.

---

# 1️⃣ INNER JOIN

`INNER JOIN` returns only the rows that have matching values in both tables.

Think of it as:

```text
Customers ∩ Orders
```

Only matching records are returned.

---

## Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

---

## Example

```sql
SELECT
    customers.customer_name,
    orders.order_id,
    orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

Result:

| customer_name | order_id | amount |
| ------------- | -------- | ------ |
| Rahul         | 101      | 5000   |
| Rahul         | 103      | 2000   |
| Priya         | 102      | 3000   |
| Priya         | 105      | 1500   |
| Amit          | 104      | 7000   |

Rohan and Neha are not shown because they don't have matching orders.

---

# Using Table Aliases

Instead of writing:

```sql
customers.customer_name
```

We can use aliases.

```sql
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;
```

Shorter version:

```sql
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

`JOIN` normally means `INNER JOIN`.

---

# 2️⃣ LEFT JOIN

`LEFT JOIN` returns:

```text
All rows from LEFT table
+
Matching rows from RIGHT table
```

If there is no matching record, SQL returns `NULL`.

---

## Syntax

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

---

## Example

```sql
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
```

Possible result:

| customer_name | order_id | amount |
| ------------- | -------- | ------ |
| Rahul         | 101      | 5000   |
| Rahul         | 103      | 2000   |
| Priya         | 102      | 3000   |
| Priya         | 105      | 1500   |
| Amit          | 104      | 7000   |
| Neha          | NULL     | NULL   |
| Rohan         | NULL     | NULL   |

Even customers without orders appear.

---

# 🎯 Find Customers Who Never Ordered

This is a very common SQL interview question.

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

Result:

```text
Neha
Rohan
```

This pattern is extremely useful.

```text
LEFT JOIN
+
WHERE right_table.id IS NULL
```

It finds records with no matching relationship.

---

# 3️⃣ RIGHT JOIN

`RIGHT JOIN` returns:

```text
All rows from RIGHT table
+
Matching rows from LEFT table
```

---

## Syntax

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

---

## Example

```sql
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;
```

All orders will appear.

If an order has no matching customer, customer information may appear as `NULL`.

---

# 💡 LEFT JOIN vs RIGHT JOIN

| LEFT JOIN                          | RIGHT JOIN                        |
| ---------------------------------- | --------------------------------- |
| Keeps all left-table rows          | Keeps all right-table rows        |
| More commonly used                 | Less commonly used                |
| Unmatched right values become NULL | Unmatched left values become NULL |

In many cases, a `RIGHT JOIN` can be rewritten as a `LEFT JOIN` by reversing the table order.

---

# FULL OUTER JOIN

A `FULL OUTER JOIN` returns:

```text
All matching rows
+
Unmatched rows from left table
+
Unmatched rows from right table
```

Conceptually:

```text
LEFT TABLE ∪ RIGHT TABLE
```

General syntax:

```sql
SELECT *
FROM table1
FULL OUTER JOIN table2
ON table1.id = table2.id;
```

> Note: `FULL OUTER JOIN` support varies by database system. If your database does not support it directly, you may need an alternative approach such as combining results with `UNION`.

---

# 4️⃣ CROSS JOIN

`CROSS JOIN` creates every possible combination of rows from two tables.

This is called a:

```text
Cartesian Product
```

---

## Example

Table A has:

```text
3 rows
```

Table B has:

```text
4 rows
```

CROSS JOIN produces:

```text
3 × 4 = 12 rows
```

---

## Syntax

```sql
SELECT *
FROM customers
CROSS JOIN products;
```

---

# Real-World CROSS JOIN Example

Imagine:

```text
Sizes:
Small
Medium
Large
```

And:

```text
Colors:
Black
White
Blue
```

A CROSS JOIN generates:

```text
Small - Black
Small - White
Small - Blue

Medium - Black
Medium - White
Medium - Blue

Large - Black
Large - White
Large - Blue
```

Useful for generating all possible combinations.

---

# 5️⃣ SELF JOIN

A SELF JOIN joins a table with itself.

Imagine an employee table:

| employee_id | employee_name | manager_id |
| ----------- | ------------- | ---------- |
| 1           | Amit          | NULL       |
| 2           | Rahul         | 1          |
| 3           | Priya         | 1          |
| 4           | Neha          | 2          |

The `manager_id` refers to another employee.

We can find each employee's manager using a SELF JOIN.

---

## Query

```sql
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id;
```

Result:

| employee | manager |
| -------- | ------- |
| Amit     | NULL    |
| Rahul    | Amit    |
| Priya    | Amit    |
| Neha     | Rahul   |

---

# 🔗 Joining Multiple Tables

Real applications often require joining more than two tables.

Suppose we have:

```text
Customers
Orders
Products
```

We can join multiple tables.

Example:

```sql
SELECT
    c.customer_name,
    o.order_id,
    p.product_name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN products p
ON o.product_id = p.product_id;
```

Conceptually:

```text
Customers
    │
    ▼
Orders
    │
    ▼
Products
```

---

# 🔍 JOIN with WHERE

We can filter joined data using `WHERE`.

Example:

Find orders greater than ₹3000.

```sql
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.amount > 3000;
```

---

# 📊 JOIN with GROUP BY

Suppose we want to calculate the number of orders placed by each customer.

```sql
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;
```

---

# 💰 JOIN with Aggregate Functions

Calculate total spending by each customer.

```sql
SELECT
    c.customer_name,
    SUM(o.amount) AS total_spending
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;
```

Possible result:

| customer_name | total_spending |
| ------------- | -------------: |
| Rahul         |           7000 |
| Priya         |           4500 |
| Amit          |           7000 |

---

# JOIN with GROUP BY and HAVING

Find customers who spent more than ₹5000.

```sql
SELECT
    c.customer_name,
    SUM(o.amount) AS total_spending
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
HAVING SUM(o.amount) > 5000;
```

This combines concepts from:

```text
Day 35 → Aggregate Functions
Day 36 → GROUP BY & HAVING
Day 37 → JOINs
```

This is how SQL concepts start working together.

---

# 🧠 Understanding ON vs WHERE

Consider:

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.amount > 3000;
```

`ON` defines:

```text
How tables are connected
```

`WHERE` defines:

```text
Which resulting rows should remain
```

Remember:

```text
ON → Relationship
WHERE → Filtering
```

---

# ⚠️ Common Mistake 1: Missing JOIN Condition

Wrong:

```sql
SELECT *
FROM customers
JOIN orders;
```

This may create unwanted combinations.

Correct:

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

---

# ⚠️ Common Mistake 2: Joining Wrong Columns

Wrong:

```sql
ON c.customer_id = o.order_id
```

Correct:

```sql
ON c.customer_id = o.customer_id
```

Always understand table relationships before joining.

---

# ⚠️ Common Mistake 3: Ambiguous Column Names

Wrong:

```sql
SELECT customer_id
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

Both tables contain `customer_id`.

Better:

```sql
SELECT c.customer_id
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

---

# ⚠️ Common Mistake 4: Turning LEFT JOIN into INNER JOIN

Consider:

```sql
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.amount > 1000;
```

Customers without orders have:

```text
o.amount = NULL
```

The `WHERE` condition removes those rows.

Therefore, you may accidentally lose the unmatched rows you wanted from the `LEFT JOIN`.

Always think carefully about filters after an outer join.

---

# 🌍 Real-World Use Cases

## E-Commerce

Join:

```text
Customers + Orders
```

To find:

* Customer purchase history
* Customer lifetime value
* Top customers

---

## Banking

Join:

```text
Customers + Accounts + Transactions
```

To analyze:

* Account transactions
* Customer balances
* Spending behavior

---

## AI Applications

Join:

```text
Users + Conversations + Messages
```

To analyze:

* Number of conversations
* User activity
* LLM usage
* Message history

---

## Machine Learning

Join:

```text
Customer Data
+
Transaction Data
+
Behavior Data
```

To create:

```text
Training Dataset
```

This process is commonly known as feature preparation or feature engineering.

---

# 📝 Hands-On Exercises

## Beginner

### Question 1

Display all customers with their orders.

```sql
-- Write your query
```

---

### Question 2

Display customer names and order amounts.

```sql
-- Write your query
```

---

### Question 3

Find customers who placed at least one order.

```sql
-- Write your query
```

---

### Question 4

Display all customers, including those without orders.

```sql
-- Write your query
```

---

### Question 5

Find customers who never placed an order.

```sql
-- Write your query
```

---

# Intermediate Exercises

### Question 6

Find the total number of orders placed by each customer.

---

### Question 7

Calculate total spending for every customer.

---

### Question 8

Find customers whose total spending exceeds ₹5000.

---

### Question 9

Find the customer who spent the most money.

---

### Question 10

Display customers who placed more than one order.

---

# Advanced Exercises

### Question 11

Find the top 3 highest-spending customers.

---

### Question 12

Find customers who haven't placed any orders.

---

### Question 13

Calculate average order value for each customer.

---

### Question 14

Find the number of orders placed each month.

---

### Question 15

Find customers whose average order amount is greater than ₹3000.

---

# 🚀 Mini Project – E-Commerce Sales Analysis

Your task is to build a small SQL analytics project.

Create the following tables:

```text
Customers
Products
Orders
Order_Items
```

Relationship:

```text
Customers
    │
    │ customer_id
    ▼
Orders
    │
    │ order_id
    ▼
Order_Items
    │
    │ product_id
    ▼
Products
```

---

# Business Questions

Write SQL queries to answer:

1. Which customers placed orders?
2. Which customers never placed an order?
3. How many orders did each customer place?
4. What is the total spending of each customer?
5. Who are the top 5 customers?
6. Which products were never ordered?
7. Which product generated the most revenue?
8. What is the average order value?
9. Which city generated the highest revenue?
10. Which customer purchased the most products?

---

# 💼 SQL Joins Interview Questions

## Beginner Level

### 1. What is a JOIN in SQL?

A JOIN combines related data from multiple tables based on a relationship between columns.

---

### 2. Why do we use JOINs?

Because relational databases usually store related information across multiple tables.

---

### 3. What are the main types of JOINs?

Common types include:

```text
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL OUTER JOIN
CROSS JOIN
SELF JOIN
```

---

### 4. What does INNER JOIN return?

Only rows that have matching values in both tables.

---

### 5. What does LEFT JOIN return?

All rows from the left table and matching rows from the right table.

Unmatched values from the right table become `NULL`.

---

### 6. What does RIGHT JOIN return?

All rows from the right table and matching rows from the left table.

---

### 7. What is CROSS JOIN?

It returns every possible combination of rows from both tables.

---

### 8. What is SELF JOIN?

A table joined with itself.

---

### 9. What is the difference between INNER JOIN and LEFT JOIN?

`INNER JOIN` returns only matching records.

`LEFT JOIN` returns all records from the left table plus matching records from the right table.

---

### 10. Can we join more than two tables?

Yes.

Example:

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id;
```

---

# Intermediate Interview Questions

### 11. How do you find records that don't have a match?

Use `LEFT JOIN` with `IS NULL`.

```sql
SELECT c.*
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

---

### 12. What is the difference between ON and WHERE?

`ON` defines the join relationship.

`WHERE` filters the resulting rows.

---

### 13. What happens if you forget the JOIN condition?

You may create a Cartesian product where many combinations of rows are returned.

---

### 14. What is a Cartesian Product?

Every row from one table is combined with every row from another table.

If:

```text
Table A = 10 rows
Table B = 20 rows
```

Then:

```text
10 × 20 = 200 rows
```

---

### 15. Can a table be joined with itself?

Yes.

This is called a SELF JOIN.

---

### 16. When would you use a SELF JOIN?

Common examples:

* Employee-manager relationships
* Hierarchical data
* Comparing rows within the same table

---

### 17. Can JOINs use multiple conditions?

Yes.

```sql
SELECT *
FROM table1 t1
JOIN table2 t2
ON t1.id = t2.id
AND t1.category = t2.category;
```

---

### 18. Can we use JOIN with GROUP BY?

Yes.

Example:

```sql
SELECT
    c.customer_name,
    COUNT(o.order_id)
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
```

---

### 19. Can we use aggregate functions with JOINs?

Yes.

Common functions include:

```text
COUNT()
SUM()
AVG()
MIN()
MAX()
```

---

### 20. Which JOIN is most commonly used?

`INNER JOIN` and `LEFT JOIN` are among the most commonly used joins in application development and data analysis.

---

# 🔥 Advanced Interview Questions

### 21. How do you find duplicate records using SELF JOIN?

One approach is to join a table with itself using matching columns while ensuring the row identifiers are different.

---

### 22. What is the difference between JOIN and UNION?

`JOIN` combines columns from related tables.

`UNION` combines rows from compatible query results.

---

### 23. What is the difference between LEFT JOIN and FULL OUTER JOIN?

`LEFT JOIN` keeps every row from the left table.

`FULL OUTER JOIN` keeps rows from both tables, whether matched or unmatched.

---

### 24. How can JOIN performance be improved?

Common approaches include:

* Indexing join columns
* Using appropriate keys
* Avoiding unnecessary columns
* Filtering data when appropriate
* Examining query execution plans
* Avoiding accidental Cartesian products

---

### 25. Should foreign keys be indexed?

It depends on the database and workload, but indexes on frequently joined and filtered columns can significantly improve query performance.

---

### 26. Can you JOIN tables without foreign keys?

Yes.

SQL can join columns even without a formal foreign-key constraint, as long as the join condition is valid.

However, foreign keys help maintain referential integrity.

---

### 27. What happens when duplicate matching values exist?

A row can match multiple rows from the other table, producing multiple result rows.

Understanding table cardinality is therefore important.

---

### 28. What is table cardinality in JOINs?

Relationships can be:

```text
One-to-One
One-to-Many
Many-to-One
Many-to-Many
```

Understanding these relationships helps predict JOIN results.

---

### 29. How would you find the highest-spending customer?

```sql
SELECT
    c.customer_name,
    SUM(o.amount) AS total_spending
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_spending DESC
LIMIT 1;
```

---

### 30. How would you find customers with no orders?

```sql
SELECT
    c.customer_name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

This is one of the most important JOIN patterns to remember for interviews.

---

# 🧪 Interview Challenge

You have:

```text
Customers
Orders
Products
Order_Items
```

Write SQL queries to find:

1. Top 5 customers by revenue
2. Top 5 products by sales
3. Customers with zero orders
4. Products with zero sales
5. Average order value per customer
6. Total revenue by city
7. Monthly sales
8. Customer with maximum orders
9. Most frequently purchased product
10. Customers who purchased more than 3 different products

Try solving these without looking at the solutions first.

---

# 📌 Quick Revision Cheat Sheet

## INNER JOIN

```sql
SELECT *
FROM A
INNER JOIN B
ON A.id = B.id;
```

Returns:

```text
Matching rows only
```

---

## LEFT JOIN

```sql
SELECT *
FROM A
LEFT JOIN B
ON A.id = B.id;
```

Returns:

```text
All A
+
Matching B
```

---

## RIGHT JOIN

```sql
SELECT *
FROM A
RIGHT JOIN B
ON A.id = B.id;
```

Returns:

```text
All B
+
Matching A
```

---

## CROSS JOIN

```sql
SELECT *
FROM A
CROSS JOIN B;
```

Returns:

```text
Every possible combination
```

---

## SELF JOIN

```sql
SELECT *
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

Used for:

```text
Employee → Manager
```

---

# 🧠 Remember This

```text
INNER JOIN
→ Give me matching data.

LEFT JOIN
→ Give me everything from the left.

RIGHT JOIN
→ Give me everything from the right.

FULL OUTER JOIN
→ Give me everything from both.

CROSS JOIN
→ Give me every possible combination.

SELF JOIN
→ Join the table with itself.
```

---

# 📊 Day 37 Practice Target

| Activity              |     Target |
| --------------------- | ---------: |
| Learn JOIN concepts   |    2 Hours |
| Practice basic JOINs  |     1 Hour |
| Solve SQL problems    |     1 Hour |
| Build Mini Project    |  1–2 Hours |
| Interview Preparation | 30 Minutes |
| GitHub Documentation  | 30 Minutes |

---

# 🎯 Day 37 Assignment

Before completing Day 37:

* [ ] Understand Primary and Foreign Keys
* [ ] Practice INNER JOIN
* [ ] Practice LEFT JOIN
* [ ] Practice RIGHT JOIN
* [ ] Understand FULL OUTER JOIN
* [ ] Practice CROSS JOIN
* [ ] Practice SELF JOIN
* [ ] Join three tables
* [ ] Combine JOIN with WHERE
* [ ] Combine JOIN with GROUP BY
* [ ] Combine JOIN with HAVING
* [ ] Solve at least 15 JOIN problems
* [ ] Complete E-Commerce Sales Analysis
* [ ] Push your work to GitHub

---

# 🏆 Day 37 Milestone

After completing Day 37, you should be able to answer questions like:

> Which customers haven't purchased anything?

> Who are our highest-spending customers?

> Which products generate the most revenue?

> How many orders has each customer placed?

> How can I combine customer, order, and product information?

These are real analytical problems that appear frequently when working with relational databases.

---

# 🚀 GitHub Commit Message

```bash
git add .

git commit -m "Day 37: Learned SQL Joins - INNER, LEFT, RIGHT, CROSS and SELF JOIN"

git push origin main
```

---

# 📚 Recommended Resources

## Official Documentation

* MySQL Documentation
* PostgreSQL Documentation

## Practice Platforms

* HackerRank SQL
* LeetCode SQL 50
* SQLBolt
* DataLemur
* StrataScratch

## Recommended Learning

Focus especially on:

```text
INNER JOIN
LEFT JOIN
Multi-Table JOINs
JOIN + GROUP BY
JOIN + Aggregate Functions
Finding Missing Records
```

These patterns are highly valuable for Data, Backend, Machine Learning, and AI Engineering roles.

---

# 📅 What's Next?

## Day 38 – SQL Subqueries

Next, learn how to write queries inside other SQL queries.

Topics:

* What is a Subquery?
* Single-Row Subqueries
* Multi-Row Subqueries
* Subqueries with WHERE
* Subqueries with FROM
* Subqueries with SELECT
* Correlated Subqueries
* `IN`
* `EXISTS`
* `NOT EXISTS`
* Subquery vs JOIN
* Real-world SQL problems
* Interview Questions

---

# 🎉 Day 37 Complete!

You have now learned one of the most important concepts in SQL:

# 🔗 SQL JOINS

Your SQL journey is progressing from:

```text
SELECT
   ↓
WHERE
   ↓
ORDER BY
   ↓
Aggregate Functions
   ↓
GROUP BY
   ↓
HAVING
   ↓
JOINS
   ↓
SUBQUERIES
   ↓
WINDOW FUNCTIONS
```

The goal is not just to memorize SQL syntax.

The real goal is to look at multiple related tables, understand their relationships, and confidently write queries that answer real business questions.

Keep Learning.
Keep Practicing.
Keep Building. 🚀

---

**Day 37 of My AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer Journey**

⭐ If this repository helps you learn, consider giving it a star!
