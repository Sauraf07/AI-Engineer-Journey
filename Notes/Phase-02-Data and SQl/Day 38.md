# 📊 Day 38 – SQL Subqueries & Nested Queries

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer
> **Day:** 38
> **Topic:** SQL Subqueries & Nested Queries

---

# 🎯 Learning Objectives

By the end of Day 38, you will be able to:

* Understand what a **Subquery** is
* Understand **Outer Query vs Inner Query**
* Write simple SQL subqueries
* Use subqueries with `WHERE`
* Use subqueries with `SELECT`
* Use subqueries with `FROM`
* Understand **Single-Row Subqueries**
* Understand **Multiple-Row Subqueries**
* Use `IN` and `NOT IN`
* Use `EXISTS` and `NOT EXISTS`
* Understand **Correlated Subqueries**
* Combine Subqueries with Aggregate Functions
* Understand **Subquery vs JOIN**
* Solve common SQL interview problems
* Write real-world analytical SQL queries

---

# 🧠 What is a Subquery?

A **Subquery** is a SQL query written inside another SQL query.

In simple words:

> A query inside another query is called a Subquery.

A subquery is also commonly called:

* Inner Query
* Nested Query
* Inner SELECT

---

# 📌 Basic Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name = (
    SELECT column_name
    FROM another_table
    WHERE condition
);
```

Here:

```sql
SELECT column_name
FROM another_table
WHERE condition
```

is the **Subquery**.

The query outside it is called the **Outer Query**.

---

# 🌍 Real-Life Example

Imagine we have an employee database.

We want to answer:

> Which employees earn more than the average salary?

First, we need to calculate the average salary.

```sql
SELECT AVG(salary)
FROM employees;
```

Suppose the result is:

```text
50000
```

Now we could write:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

But instead of manually inserting `50000`, we can put the first query inside the second query.

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

This is a **Subquery**.

---

# 🔄 How Does a Subquery Work?

Consider:

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

Conceptually:

### Step 1

The database calculates:

```sql
SELECT AVG(salary)
FROM employees;
```

Example result:

```text
50000
```

### Step 2

The outer query effectively becomes:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

### Step 3

Employees earning more than the average salary are returned.

---

# 📊 Sample Database

Throughout today's examples, we will use the following tables.

---

# Employees Table

```sql
CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(100),

    department_id INT,

    salary DECIMAL(10,2),

    city VARCHAR(50)
);
```

Insert data:

```sql
INSERT INTO employees
(employee_id, employee_name, department_id, salary, city)

VALUES

(1, 'Aman', 101, 45000, 'Indore'),

(2, 'Rahul', 102, 60000, 'Delhi'),

(3, 'Priya', 101, 75000, 'Mumbai'),

(4, 'Neha', 103, 50000, 'Indore'),

(5, 'Arjun', 102, 80000, 'Bangalore'),

(6, 'Simran', 103, 40000, 'Delhi'),

(7, 'Rohit', 101, 90000, 'Pune');
```

---

# Departments Table

```sql
CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(100),

    location VARCHAR(100)
);
```

Insert data:

```sql
INSERT INTO departments
(department_id, department_name, location)

VALUES

(101, 'Engineering', 'Indore'),

(102, 'Data Science', 'Bangalore'),

(103, 'HR', 'Delhi'),

(104, 'Marketing', 'Mumbai');
```

---

# 📋 Employees Data

| employee_id | employee_name | department_id | salary | city      |
| ----------: | ------------- | ------------: | -----: | --------- |
|           1 | Aman          |           101 |  45000 | Indore    |
|           2 | Rahul         |           102 |  60000 | Delhi     |
|           3 | Priya         |           101 |  75000 | Mumbai    |
|           4 | Neha          |           103 |  50000 | Indore    |
|           5 | Arjun         |           102 |  80000 | Bangalore |
|           6 | Simran        |           103 |  40000 | Delhi     |
|           7 | Rohit         |           101 |  90000 | Pune      |

---

# 📋 Departments Data

| department_id | department_name | location  |
| ------------: | --------------- | --------- |
|           101 | Engineering     | Indore    |
|           102 | Data Science    | Bangalore |
|           103 | HR              | Delhi     |
|           104 | Marketing       | Mumbai    |

---

# 1️⃣ Simple Subquery

Let's find employees earning more than the average salary.

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

# Inner Query

```sql
SELECT AVG(salary)
FROM employees;
```

---

# Outer Query

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary > average_salary;
```

---

# 2️⃣ Subquery with WHERE

The most common place to use a subquery is inside `WHERE`.

Example:

Find employees whose salary is greater than the minimum salary.

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary > (
    SELECT MIN(salary)
    FROM employees
);
```

---

# 3️⃣ Subquery with MAX()

Find the employee receiving the highest salary.

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

This is a very common SQL interview question.

---

# 4️⃣ Subquery with MIN()

Find the employee receiving the lowest salary.

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
);
```

---

# 5️⃣ Subquery with AVG()

Find employees earning below the average salary.

```sql
SELECT employee_name,
       salary
FROM employees
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
);
```

---

# 📌 Types of Subqueries

Subqueries can be classified into several categories.

The major ones are:

```text
Subqueries
│
├── Single-Row Subquery
│
├── Multiple-Row Subquery
│
├── Scalar Subquery
│
├── Correlated Subquery
│
└── Nested Subquery
```

---

# 6️⃣ Single-Row Subquery

A **Single-Row Subquery** returns only one row.

Example:

```sql
SELECT AVG(salary)
FROM employees;
```

It returns one value.

Therefore:

```sql
SELECT employee_name
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

uses a single-row subquery.

---

# Operators Used with Single-Row Subqueries

Common operators include:

```text
=
>
<
>=
<=
<>
```

---

# Example

```sql
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

---

# 7️⃣ Multiple-Row Subquery

A Multiple-Row Subquery returns multiple rows.

For example:

```sql
SELECT department_id
FROM departments
WHERE location IN ('Indore', 'Bangalore');
```

It could return:

```text
101
102
```

Because multiple values are returned, using `=` would not be appropriate.

Instead, we commonly use:

```text
IN
NOT IN
ANY
ALL
```

---

# 8️⃣ Subquery with IN

Suppose we want employees working in departments located in Indore or Bangalore.

```sql
SELECT employee_name,
       department_id
FROM employees
WHERE department_id IN (

    SELECT department_id
    FROM departments
    WHERE location IN ('Indore', 'Bangalore')

);
```

---

# How It Works

Inner query:

```sql
SELECT department_id
FROM departments
WHERE location IN ('Indore', 'Bangalore');
```

Returns:

```text
101
102
```

Outer query becomes conceptually:

```sql
SELECT employee_name,
       department_id
FROM employees
WHERE department_id IN (101, 102);
```

---

# 9️⃣ Subquery with NOT IN

Find employees who are NOT working in departments located in Indore.

```sql
SELECT employee_name
FROM employees
WHERE department_id NOT IN (

    SELECT department_id
    FROM departments
    WHERE location = 'Indore'

);
```

---

# ⚠️ Important: NOT IN and NULL

Be careful when using:

```sql
NOT IN
```

If the subquery contains `NULL`, the result may behave differently than expected because SQL uses three-valued logic.

In many existence-check scenarios, `NOT EXISTS` can be safer and clearer.

---

# 🔟 EXISTS Operator

`EXISTS` checks whether a subquery returns at least one row.

Syntax:

```sql
SELECT columns
FROM table1
WHERE EXISTS (
    SELECT 1
    FROM table2
    WHERE condition
);
```

---

# Example

Find employees whose department exists in the departments table.

```sql
SELECT employee_name
FROM employees e
WHERE EXISTS (

    SELECT 1
    FROM departments d

    WHERE d.department_id = e.department_id

);
```

---

# 🤔 Why SELECT 1?

You will often see:

```sql
SELECT 1
```

inside `EXISTS`.

The actual selected value is not important.

`EXISTS` only checks:

> Does at least one matching row exist?

---

# 1️⃣1️⃣ NOT EXISTS

`NOT EXISTS` checks whether no matching row exists.

Example:

Find departments that have no employees.

```sql
SELECT department_name
FROM departments d

WHERE NOT EXISTS (

    SELECT 1
    FROM employees e

    WHERE e.department_id = d.department_id

);
```

This can return:

```text
Marketing
```

because department `104` does not have an employee in our sample data.

---

# 🔥 EXISTS vs IN

Both can sometimes solve similar problems.

### Using IN

```sql
SELECT employee_name
FROM employees

WHERE department_id IN (

    SELECT department_id
    FROM departments

);
```

### Using EXISTS

```sql
SELECT employee_name
FROM employees e

WHERE EXISTS (

    SELECT 1
    FROM departments d

    WHERE d.department_id = e.department_id

);
```

---

# 📊 IN vs EXISTS

| IN                            | EXISTS                               |
| ----------------------------- | ------------------------------------ |
| Compares values               | Checks existence                     |
| Useful for sets of values     | Useful for existence checks          |
| Common with simple subqueries | Common with correlated queries       |
| Can require care with NULLs   | Often convenient for existence logic |

Performance depends on:

* Database engine
* Query optimizer
* Indexes
* Dataset
* Query structure

Therefore, don't blindly assume that one is always faster.

---

# 1️⃣2️⃣ Subquery in SELECT

Subqueries can also appear inside the `SELECT` list.

Example:

```sql
SELECT employee_name,
       salary,

       (
           SELECT AVG(salary)
           FROM employees
       ) AS company_average_salary

FROM employees;
```

Example result:

| employee_name | salary | company_average_salary |
| ------------- | -----: | ---------------------: |
| Aman          |  45000 |               62857.14 |
| Rahul         |  60000 |               62857.14 |
| Priya         |  75000 |               62857.14 |

---

# Real-World Use

This is useful when you want to compare each row against a calculated metric.

For example:

```sql
SELECT employee_name,

       salary,

       (
           SELECT AVG(salary)
           FROM employees
       ) AS average_salary,

       salary - (
           SELECT AVG(salary)
           FROM employees
       ) AS salary_difference

FROM employees;
```

---

# 1️⃣3️⃣ Subquery in FROM

A subquery can also appear inside the `FROM` clause.

Example:

```sql
SELECT department_id,
       average_salary

FROM (

    SELECT department_id,
           AVG(salary) AS average_salary

    FROM employees

    GROUP BY department_id

) AS department_salary;
```

The result of the inner query behaves like a temporary result set for the outer query.

This is often called a:

> Derived Table

---

# ⚠️ Important

A subquery used inside `FROM` should normally have an alias.

Example:

```sql
AS department_salary
```

---

# 1️⃣4️⃣ Correlated Subquery

This is one of the most important SQL interview concepts.

A **Correlated Subquery** depends on the current row of the outer query.

Example:

Find employees earning more than the average salary of their own department.

```sql
SELECT e.employee_name,
       e.department_id,
       e.salary

FROM employees e

WHERE e.salary > (

    SELECT AVG(e2.salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

---

# 🧠 Understanding the Correlation

Notice:

```sql
e2.department_id = e.department_id
```

The inner query references:

```text
e.department_id
```

from the outer query.

Therefore, the subquery is **correlated** with the outer query.

---

# Normal vs Correlated Subquery

## Normal Subquery

```sql
SELECT *
FROM employees

WHERE salary > (

    SELECT AVG(salary)
    FROM employees

);
```

The subquery does not depend on the current outer row.

---

## Correlated Subquery

```sql
SELECT *
FROM employees e

WHERE salary > (

    SELECT AVG(salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

The inner query depends on the outer row.

---

# 📊 Normal vs Correlated Subquery

| Normal Subquery                   | Correlated Subquery                     |
| --------------------------------- | --------------------------------------- |
| Independent of outer query row    | Depends on outer query row              |
| Often conceptually evaluated once | Conceptually evaluated for outer rows   |
| Usually simpler                   | Usually more complex                    |
| Good for global comparisons       | Good for row/group-specific comparisons |

---

# 1️⃣5️⃣ Find Second Highest Salary

🔥 Extremely common SQL interview problem.

One solution:

```sql
SELECT MAX(salary) AS second_highest_salary

FROM employees

WHERE salary < (

    SELECT MAX(salary)
    FROM employees

);
```

---

# How It Works

First:

```sql
SELECT MAX(salary)
FROM employees;
```

Returns:

```text
90000
```

Then:

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < 90000;
```

returns the next lower distinct salary.

---

# 1️⃣6️⃣ Find Employee with Second Highest Salary

```sql
SELECT employee_name,
       salary

FROM employees

WHERE salary = (

    SELECT MAX(salary)

    FROM employees

    WHERE salary < (

        SELECT MAX(salary)
        FROM employees

    )

);
```

This contains a nested subquery.

---

# 1️⃣7️⃣ Nested Subquery

A subquery can contain another subquery.

Example structure:

```sql
SELECT *
FROM table1

WHERE column1 = (

    SELECT column2
    FROM table2

    WHERE column3 = (

        SELECT column4
        FROM table3

    )

);
```

This is called a:

> Nested Subquery

---

# 1️⃣8️⃣ Employees in Highest-Paid Department

First calculate department averages.

```sql
SELECT department_id,
       AVG(salary)

FROM employees

GROUP BY department_id;
```

Then we can build more advanced queries from these results.

Example:

```sql
SELECT *
FROM employees

WHERE department_id = (

    SELECT department_id

    FROM employees

    GROUP BY department_id

    ORDER BY AVG(salary) DESC

    LIMIT 1

);
```

---

# 1️⃣9️⃣ Subquery with COUNT()

Find departments having more than two employees.

```sql
SELECT department_name

FROM departments d

WHERE (

    SELECT COUNT(*)

    FROM employees e

    WHERE e.department_id = d.department_id

) > 2;
```

---

# 2️⃣0️⃣ Subquery with UPDATE

Subqueries aren't limited to `SELECT`.

Example:

```sql
UPDATE employees

SET salary = salary * 1.10

WHERE department_id IN (

    SELECT department_id

    FROM departments

    WHERE location = 'Indore'

);
```

This gives a 10% salary increase to employees belonging to departments located in Indore.

> Always verify your `WHERE` condition with a `SELECT` before running important `UPDATE` statements.

---

# 2️⃣1️⃣ Subquery with DELETE

Example:

```sql
DELETE FROM employees

WHERE department_id IN (

    SELECT department_id

    FROM departments

    WHERE location = 'Mumbai'

);
```

⚠️ Be extremely careful when using `DELETE`.

Before running it, first test:

```sql
SELECT *
FROM employees

WHERE department_id IN (

    SELECT department_id

    FROM departments

    WHERE location = 'Mumbai'

);
```

---

# 🔄 Subquery vs JOIN

Many problems can be solved using either a Subquery or JOIN.

---

# Using Subquery

```sql
SELECT employee_name

FROM employees

WHERE department_id IN (

    SELECT department_id

    FROM departments

    WHERE location = 'Indore'

);
```

---

# Using JOIN

```sql
SELECT e.employee_name

FROM employees e

JOIN departments d

ON e.department_id = d.department_id

WHERE d.location = 'Indore';
```

---

# 📊 Subquery vs JOIN

| Subquery                                    | JOIN                                                     |
| ------------------------------------------- | -------------------------------------------------------- |
| Query inside another query                  | Combines tables                                          |
| Can be very readable for derived conditions | Often natural for retrieving columns from related tables |
| Useful for aggregate comparisons            | Excellent for relational combinations                    |
| Supports correlated logic                   | Often preferred for direct table relationships           |
| Can simplify certain problems               | Can simplify multi-table retrieval                       |

Neither is automatically better in every situation.

Choose based on:

* Readability
* Query plan
* Data size
* Indexes
* Database optimizer
* Problem requirements

---

# 💼 Real-World Applications of Subqueries

Subqueries are commonly useful in:

### 💰 Finance

Find transactions above average transaction value.

```sql
SELECT *
FROM transactions

WHERE amount > (

    SELECT AVG(amount)
    FROM transactions

);
```

---

### 🛒 E-Commerce

Find products more expensive than average.

```sql
SELECT product_name,
       price

FROM products

WHERE price > (

    SELECT AVG(price)
    FROM products

);
```

---

### 👨‍💼 HR

Find employees earning above department average.

```sql
SELECT *
FROM employees e

WHERE salary > (

    SELECT AVG(salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

---

### 🤖 AI/ML Applications

SQL subqueries can help prepare datasets before model training.

Examples:

* Find users with above-average activity
* Find high-value customers
* Select unusual transactions
* Filter data based on aggregate statistics
* Build analytical features
* Prepare training datasets
* Perform cohort-based filtering

---

# 🧪 Hands-On Exercises

## 🟢 Beginner

### Exercise 1

Find employees earning more than the average salary.

---

### Exercise 2

Find the employee with the highest salary.

---

### Exercise 3

Find the employee with the lowest salary.

---

### Exercise 4

Find employees earning below average salary.

---

### Exercise 5

Find employees belonging to Engineering.

Use a subquery.

---

# 🟡 Intermediate

### Exercise 6

Find the second-highest salary.

---

### Exercise 7

Find the employee receiving the second-highest salary.

---

### Exercise 8

Find employees earning more than their department average.

---

### Exercise 9

Find departments that currently have employees.

Use:

```sql
EXISTS
```

---

### Exercise 10

Find departments with no employees.

Use:

```sql
NOT EXISTS
```

---

# 🔴 Advanced

### Exercise 11

Find the third-highest distinct salary using subqueries.

---

### Exercise 12

Find employees earning more than the average salary of employees in their city.

---

### Exercise 13

Find the highest-paid employee from each department.

---

### Exercise 14

Find departments whose average salary is greater than the company's average salary.

---

### Exercise 15

Find employees whose salaries are greater than every employee in department 103.

Research and try:

```sql
ALL
```

---

# 🚀 Mini Project – Employee Salary Analytics System

## Project Objective

Build an SQL-based Employee Salary Analytics system using subqueries.

---

# Database

Create:

```text
EmployeeAnalytics
```

---

# Tables

## employees

```text
employee_id
employee_name
department_id
salary
city
joining_date
```

## departments

```text
department_id
department_name
location
```

---

# Required Queries

Write queries to:

1. Find average company salary.

2. Find employees earning above company average.

3. Find employees earning below company average.

4. Find highest-paid employee.

5. Find lowest-paid employee.

6. Find second-highest salary.

7. Find employee with second-highest salary.

8. Find employees earning above their department average.

9. Find departments without employees.

10. Find departments having employees.

11. Find department with highest average salary.

12. Find employees working in departments located in Indore.

13. Find employees whose salary is above their city's average salary.

14. Find department-wise employee counts using correlated queries.

15. Find employees earning more than employees in a selected department.

---

# 🎯 Expected Project Skills

After completing the project, you should understand:

```text
Subqueries
    ↓
Aggregate Functions
    ↓
IN / NOT IN
    ↓
EXISTS / NOT EXISTS
    ↓
Correlated Subqueries
    ↓
Nested Queries
    ↓
Business Analytics
```

---

# 🎤 SQL Interview Questions

# 🟢 Beginner Interview Questions

## 1. What is a Subquery?

A subquery is a SQL query written inside another SQL statement.

---

## 2. What is another name for a Subquery?

A subquery is also commonly called:

* Inner Query
* Nested Query

---

## 3. What is an Outer Query?

The query containing the subquery is called the Outer Query.

---

## 4. Where can subqueries be used?

Common locations include:

```text
SELECT
FROM
WHERE
HAVING
```

They can also be used in appropriate `UPDATE`, `DELETE`, and other SQL operations.

---

## 5. Can a subquery return multiple rows?

Yes.

A subquery may return:

* One value
* One row
* Multiple rows
* Multiple columns, depending on context

---

## 6. What is a Single-Row Subquery?

A subquery that returns a single row.

---

## 7. What is a Multiple-Row Subquery?

A subquery that returns multiple rows.

---

## 8. Which operators can be used with multiple-row subqueries?

Common operators include:

```text
IN
NOT IN
ANY
ALL
EXISTS
```

---

## 9. What does EXISTS do?

`EXISTS` checks whether the subquery returns at least one matching row.

---

## 10. What does NOT EXISTS do?

It checks whether the subquery returns no matching rows.

---

# 🟡 Intermediate Interview Questions

## 11. What is a Correlated Subquery?

A correlated subquery references values from the outer query.

Example:

```sql
SELECT *

FROM employees e

WHERE salary > (

    SELECT AVG(salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

---

## 12. Difference between Normal and Correlated Subquery?

### Normal Subquery

Does not depend on the current outer-query row.

### Correlated Subquery

References columns from the outer query.

---

## 13. What is a Scalar Subquery?

A scalar subquery returns exactly one value.

Example:

```sql
SELECT (
    SELECT MAX(salary)
    FROM employees
);
```

---

## 14. What happens if a scalar subquery returns multiple rows?

The database generally produces an error because a scalar context expects one value.

---

## 15. Difference between IN and EXISTS?

`IN` compares a value against a result set.

`EXISTS` checks whether matching rows exist.

---

## 16. What is a Derived Table?

A subquery used inside the `FROM` clause is commonly called a derived table.

Example:

```sql
SELECT *

FROM (

    SELECT department_id,
           AVG(salary) AS avg_salary

    FROM employees

    GROUP BY department_id

) AS department_stats;
```

---

## 17. Can we use aggregate functions inside subqueries?

Yes.

Examples:

```sql
AVG()
MAX()
MIN()
COUNT()
SUM()
```

---

## 18. Can a Subquery contain another Subquery?

Yes.

This creates nested queries.

---

## 19. Can Subqueries be used with UPDATE?

Yes.

Example:

```sql
UPDATE employees

SET salary = salary * 1.10

WHERE department_id IN (

    SELECT department_id
    FROM departments
    WHERE location = 'Indore'

);
```

---

## 20. Can Subqueries be used with DELETE?

Yes, depending on the database and query structure.

---

# 🔴 Advanced Interview Questions

## 21. How would you find employees earning above their department average?

```sql
SELECT employee_name,
       salary,
       department_id

FROM employees e

WHERE salary > (

    SELECT AVG(salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

---

## 22. How would you find the second-highest salary?

```sql
SELECT MAX(salary)

FROM employees

WHERE salary < (

    SELECT MAX(salary)
    FROM employees

);
```

---

## 23. How would you find departments without employees?

```sql
SELECT department_name

FROM departments d

WHERE NOT EXISTS (

    SELECT 1

    FROM employees e

    WHERE e.department_id = d.department_id

);
```

---

## 24. Which is faster: JOIN or Subquery?

There is no universal answer.

Performance depends on:

* Database optimizer
* Indexes
* Data distribution
* Dataset size
* Query structure
* Execution plan

Always inspect the query plan for performance-sensitive queries.

---

## 25. What is the problem with NOT IN and NULL?

If the subquery returns `NULL`, SQL's three-valued logic can make `NOT IN` return unexpected results.

`NOT EXISTS` is often preferable for anti-join/existence logic.

---

## 26. Can a subquery return multiple columns?

Yes, depending on where and how it is used.

For example, a derived table can return multiple columns.

---

## 27. What is ANY in SQL?

`ANY` compares a value against one or more values returned by a subquery.

Example:

```sql
SELECT *

FROM employees

WHERE salary > ANY (

    SELECT salary

    FROM employees

    WHERE department_id = 103

);
```

---

## 28. What is ALL in SQL?

`ALL` requires the comparison to be true for every value returned by the subquery.

Example:

```sql
SELECT *

FROM employees

WHERE salary > ALL (

    SELECT salary

    FROM employees

    WHERE department_id = 103

);
```

---

## 29. Why can correlated subqueries become expensive?

Conceptually, they may require work related to many outer-query rows.

However, modern database optimizers may rewrite or optimize them.

Therefore, always examine the actual execution plan instead of assuming poor performance.

---

## 30. When should you use Subqueries?

Subqueries are useful when:

* Comparing against aggregate values
* Filtering using another query's results
* Checking existence
* Creating derived result sets
* Writing row-dependent calculations
* Breaking complex analytical problems into logical steps

---

# 🔥 Important Interview Queries to Practice

Make sure you can write these without looking at notes:

```text
1. Highest salary

2. Second-highest salary

3. Third-highest salary

4. Employees above average salary

5. Employees below average salary

6. Employees above department average

7. Highest-paid employee in each department

8. Departments without employees

9. Departments with employees

10. Employees belonging to specific department locations

11. Products above average price

12. Customers with above-average spending

13. Students scoring above class average

14. Employees above city average salary

15. Department with highest average salary
```

---

# 🧠 Quick Revision Cheat Sheet

```sql
-- Above Average

SELECT *
FROM employees

WHERE salary > (

    SELECT AVG(salary)
    FROM employees

);
```

---

```sql
-- Highest Salary

SELECT *

FROM employees

WHERE salary = (

    SELECT MAX(salary)
    FROM employees

);
```

---

```sql
-- Second Highest Salary

SELECT MAX(salary)

FROM employees

WHERE salary < (

    SELECT MAX(salary)
    FROM employees

);
```

---

```sql
-- IN Subquery

SELECT *

FROM employees

WHERE department_id IN (

    SELECT department_id
    FROM departments

);
```

---

```sql
-- EXISTS

SELECT *

FROM employees e

WHERE EXISTS (

    SELECT 1

    FROM departments d

    WHERE d.department_id = e.department_id

);
```

---

```sql
-- NOT EXISTS

SELECT *

FROM departments d

WHERE NOT EXISTS (

    SELECT 1

    FROM employees e

    WHERE e.department_id = d.department_id

);
```

---

```sql
-- Correlated Subquery

SELECT *

FROM employees e

WHERE salary > (

    SELECT AVG(salary)

    FROM employees e2

    WHERE e2.department_id = e.department_id

);
```

---

# 📋 Day 38 Practice Checklist

Before completing Day 38, make sure you can:

* [ ] Explain Subqueries
* [ ] Explain Inner Query
* [ ] Explain Outer Query
* [ ] Write Single-Row Subqueries
* [ ] Write Multiple-Row Subqueries
* [ ] Use `IN`
* [ ] Use `NOT IN`
* [ ] Use `EXISTS`
* [ ] Use `NOT EXISTS`
* [ ] Write Subqueries in `WHERE`
* [ ] Write Subqueries in `SELECT`
* [ ] Write Subqueries in `FROM`
* [ ] Understand Scalar Subqueries
* [ ] Understand Correlated Subqueries
* [ ] Explain Subquery vs JOIN
* [ ] Find Highest Salary
* [ ] Find Second Highest Salary
* [ ] Find Employees Above Average
* [ ] Find Employees Above Department Average
* [ ] Solve at least 15 Subquery problems

---

# 🏆 Today's Assignment

Create a file:

```text
day38_subqueries.sql
```

Write at least:

```text
5 Basic Subqueries

5 Aggregate Subqueries

5 IN / NOT IN Queries

5 EXISTS / NOT EXISTS Queries

5 Correlated Subqueries

5 Interview Queries
```

### 🎯 Target

```text
30 SQL Queries
```

---

# 📁 Recommended GitHub Structure

```text
Day-38-SQL-Subqueries/
│
├── README.md
│
├── database/
│   └── employee_database.sql
│
├── examples/
│   ├── basic_subqueries.sql
│   ├── multiple_row_subqueries.sql
│   ├── exists_queries.sql
│   └── correlated_subqueries.sql
│
├── practice/
│   └── day38_practice.sql
│
├── interview/
│   └── interview_queries.sql
│
└── project/
    └── employee_salary_analytics.sql
```

---

# 📚 Recommended Resources

## Official Documentation

Study SQL subqueries using the official documentation of the database you're using.

Recommended:

* MySQL Documentation – Subqueries
* PostgreSQL Documentation
* SQL database documentation for `EXISTS`, `IN`, `ANY`, and `ALL`

---

# 🎥 YouTube Topics to Search

Search for:

```text
SQL Subqueries for Beginners

SQL Correlated Subqueries

SQL EXISTS vs IN

SQL Subquery Interview Questions

SQL Second Highest Salary

SQL Subquery vs JOIN
```

Focus more on writing queries yourself than watching multiple tutorials.

---

# 💡 Pro Tip

Don't memorize Subqueries like this:

```text
Syntax → Syntax → Syntax
```

Instead, think:

```text
What information do I need?

        ↓

Can I get that information using another query?

        ↓

Write the inner query.

        ↓

Test the inner query.

        ↓

Use its result in the outer query.
```

Example:

```text
Question:

Employees earning above average salary

        ↓

Need average salary

        ↓

SELECT AVG(salary)
FROM employees

        ↓

Use result to filter employees

        ↓

SELECT *
FROM employees
WHERE salary > (...)
```

This thinking pattern will make complex SQL much easier.

---

# 📝 Day 38 Summary

Today you learned:

```text
SQL Subqueries
      │
      ├── Inner Query
      ├── Outer Query
      │
      ├── Single-Row Subquery
      ├── Multiple-Row Subquery
      ├── Scalar Subquery
      │
      ├── IN
      ├── NOT IN
      ├── EXISTS
      ├── NOT EXISTS
      │
      ├── SELECT Subquery
      ├── FROM Subquery
      ├── WHERE Subquery
      │
      ├── Correlated Subquery
      ├── Nested Subquery
      │
      ├── Aggregate Subqueries
      │
      └── Subquery vs JOIN
```

---

# 🎯 Day 38 Completion Target

By the end of today:

```text
Theory                 ✅

SQL Examples           ✅

30 Practice Queries    ✅

Interview Questions    ✅

Mini Project           ✅

GitHub Update          ✅
```

---

# 💻 Git Commands

After completing your work:

```bash
git add .

git commit -m "Day 38: Learned SQL Subqueries and Correlated Subqueries"

git push origin main
```

---

# 🚀 Phase 2 Progress

```text
Phase 1 – Programming Foundation        ✅ COMPLETE

Phase 2 – Data & SQL                    🔄 IN PROGRESS

Day 31                                 ✅

Day 32                                 ✅

Day 33                                 ✅

Day 34                                 ✅

Day 35                                 ✅

Day 36 – GROUP BY & HAVING             ✅

Day 37                                 ✅

Day 38 – SQL Subqueries                ✅
```

---

# 🔜 What's Next?

## 📊 Day 39 – SQL Window Functions

Next, we will learn one of the **most important SQL topics for Data, AI/ML, and technical interviews**:

```text
Window Functions

ROW_NUMBER()

RANK()

DENSE_RANK()

PARTITION BY

OVER()

Running Totals

Top-N per Group

Ranking Employees

Nth Highest Salary
```

This will take your SQL skills from **basic/intermediate SQL toward analytical SQL**.

---

# 🌟 Final Thought

> **Don't just learn SQL syntax — learn how to think in data.**

Every SQL problem should start with:

```text
What data do I have?

        ↓

What result do I need?

        ↓

What intermediate result is required?

        ↓

Which SQL technique solves it?

        ↓

Write → Test → Improve
```

Keep learning. Keep querying. Keep building. 🚀

**Day 38 Complete! 🎉**
