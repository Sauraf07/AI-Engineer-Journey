# 🚀 Day 35 – SQL Aggregate Functions (Part 1)

> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📖 Table of Contents

- Introduction
- What are Aggregate Functions?
- Why Aggregate Functions Matter
- Sample Database
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- Real-World Examples
- Practice Questions
- Mini Project
- Summary
- Resources

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand Aggregate Functions
- Count rows using COUNT()
- Calculate totals using SUM()
- Find averages using AVG()
- Find minimum values using MIN()
- Find maximum values using MAX()
- Apply Aggregate Functions in real-world scenarios
- Solve beginner SQL interview questions

---

# 🤔 What are Aggregate Functions?

Aggregate Functions perform calculations on **multiple rows** and return **a single value**.

Instead of looking at one row at a time, they summarize the data.

Think of them as **data summarizers**.

---

# 🎯 Real-Life Example

Imagine you own a supermarket.

Instead of checking every customer's bill individually, you want to know:

- Total Sales
- Average Bill Amount
- Highest Sale
- Lowest Sale
- Number of Customers

Aggregate Functions help answer these questions instantly.

---

# 📌 Why Aggregate Functions Matter

Almost every company uses Aggregate Functions.

Examples:

- Amazon → Total Orders
- Flipkart → Average Product Rating
- Swiggy → Total Daily Revenue
- Zomato → Highest Order Value
- Netflix → Total Active Users

As an AI/ML Engineer, you'll often summarize datasets before training models.

---

# 🗂 Sample Database

We'll use the following **Employees** table throughout this chapter.

| Emp_ID | Name | Department | Salary | Age |
|---------|------|------------|--------|-----|
|101|Rahul|IT|50000|24|
|102|Priya|HR|40000|28|
|103|Aman|IT|60000|30|
|104|Sneha|Sales|45000|27|
|105|John|IT|70000|35|
|106|Sara|HR|38000|26|

---

# SQL Script

```sql
CREATE TABLE Employees (
    Emp_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(30),
    Salary INT,
    Age INT
);

INSERT INTO Employees VALUES
(101,'Rahul','IT',50000,24),
(102,'Priya','HR',40000,28),
(103,'Aman','IT',60000,30),
(104,'Sneha','Sales',45000,27),
(105,'John','IT',70000,35),
(106,'Sara','HR',38000,26);
```

---

# 1️⃣ COUNT()

## What is COUNT()?

COUNT() counts rows.

Think of it as counting students inside a classroom.

---

## Syntax

```sql
SELECT COUNT(*) FROM Employees;
```

---

## Output

| COUNT |
|--------|
|6|

---

There are 6 employees.

---

## Count Only IT Employees

```sql
SELECT COUNT(*)
FROM Employees
WHERE Department='IT';
```

Output

| COUNT |
|--------|
|3|

---

## Count Non-NULL Values

```sql
SELECT COUNT(Salary)
FROM Employees;
```

Counts only rows where Salary is NOT NULL.

---

## Real World Example

Amazon

```text
How many orders were placed today?
```

SQL

```sql
SELECT COUNT(*)
FROM Orders
WHERE Order_Date='2026-07-17';
```

---

# 2️⃣ SUM()

## What is SUM()?

SUM() adds values together.

Think of calculating total money inside your wallet.

---

## Syntax

```sql
SELECT SUM(Salary)
FROM Employees;
```

---

Output

| SUM |
|------|
|303000|

---

Total salary of all employees = ₹303000

---

## Total Salary of IT Department

```sql
SELECT SUM(Salary)
FROM Employees
WHERE Department='IT';
```

Output

| SUM |
|------|
|180000|

---

## Real World Example

E-commerce

```text
Total Revenue Today
```

```sql
SELECT SUM(Amount)
FROM Orders
WHERE Order_Date='2026-07-17';
```

---

# 3️⃣ AVG()

## What is AVG()?

AVG() calculates the average.

Formula

```text
Average = Sum ÷ Count
```

---

## Syntax

```sql
SELECT AVG(Salary)
FROM Employees;
```

---

Output

| AVG |
|------|
|50500|

---

Average salary = ₹50,500

---

## Average IT Salary

```sql
SELECT AVG(Salary)
FROM Employees
WHERE Department='IT';
```

---

Output

| AVG |
|------|
|60000|

---

## Real World Example

Netflix

```text
Average Watch Time
```

Swiggy

```text
Average Delivery Time
```

Hospital

```text
Average Patient Age
```

---

# 4️⃣ MIN()

## What is MIN()?

Returns the smallest value.

---

Example

```sql
SELECT MIN(Salary)
FROM Employees;
```

---

Output

| MIN |
|------|
|38000|

---

Employee Sara earns the lowest salary.

---

Find Youngest Employee

```sql
SELECT MIN(Age)
FROM Employees;
```

Output

24

---

Real World Example

Amazon

```text
Cheapest Product
```

Hospital

```text
Youngest Patient
```

School

```text
Lowest Marks
```

---

# 5️⃣ MAX()

Returns the largest value.

---

Syntax

```sql
SELECT MAX(Salary)
FROM Employees;
```

---

Output

| MAX |
|------|
|70000|

---

Highest salary = ₹70,000

---

Find Oldest Employee

```sql
SELECT MAX(Age)
FROM Employees;
```

Output

35

---

Real World Example

Amazon

```text
Most Expensive Product
```

Bank

```text
Highest Transaction
```

Hospital

```text
Oldest Patient
```

---

# Multiple Aggregate Functions Together

Instead of writing multiple queries, SQL allows us to use all Aggregate Functions in a single query.

```sql
SELECT
COUNT(*) AS TotalEmployees,
SUM(Salary) AS TotalSalary,
AVG(Salary) AS AverageSalary,
MIN(Salary) AS LowestSalary,
MAX(Salary) AS HighestSalary
FROM Employees;
```

---

Output

| TotalEmployees | TotalSalary | AverageSalary | LowestSalary | HighestSalary |
|---------------|------------|--------------|-------------|--------------|
|6|303000|50500|38000|70000|

---

# Real-World Business Dashboard

Imagine you are working for Amazon.

The dashboard might display:

```text
Today's Orders : 1,245

Today's Revenue : ₹9,45,000

Average Order : ₹760

Lowest Order : ₹120

Highest Order : ₹18,500
```

All of these numbers are calculated using Aggregate Functions.

---

# Mini Project

## Employee Salary Report

Write SQL queries to find:

- Total Employees
- Total Salary
- Average Salary
- Highest Salary
- Lowest Salary

---

Expected Queries

```sql
SELECT COUNT(*) FROM Employees;

SELECT SUM(Salary) FROM Employees;

SELECT AVG(Salary) FROM Employees;

SELECT MIN(Salary) FROM Employees;

SELECT MAX(Salary) FROM Employees;
```

---

# Practice Questions

## Easy

1. Count all employees.

2. Find total salary.

3. Find average salary.

4. Find highest salary.

5. Find lowest salary.

6. Find youngest employee.

7. Find oldest employee.

8. Count HR employees.

9. Find total salary of HR.

10. Find average age.

---

## Medium

11. Find total salary of employees older than 25.

12. Count employees earning more than ₹50,000.

13. Find highest salary in IT department.

14. Find average salary of HR department.

15. Find minimum age in Sales department.

---

# Interview Questions

## Beginner

### 1. What are Aggregate Functions?

Aggregate Functions perform calculations on multiple rows and return a single summarized value.

---

### 2. Name five Aggregate Functions.

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

---

### 3. Difference between COUNT(*) and COUNT(column)?

| COUNT(*) | COUNT(column) |
|-----------|---------------|
|Counts all rows|Counts only non-NULL values|

---

### 4. Which Aggregate Function calculates average?

AVG()

---

### 5. Which Aggregate Function returns highest value?

MAX()

---

### 6. Which Aggregate Function returns lowest value?

MIN()

---

### 7. Which Aggregate Function calculates total?

SUM()

---

### 8. Can Aggregate Functions work with WHERE?

Yes.

Example

```sql
SELECT SUM(Salary)
FROM Employees
WHERE Department='IT';
```

---

### 9. Can Aggregate Functions return multiple rows?

No.

They return a summarized result unless combined with `GROUP BY`.

---

### 10. Where are Aggregate Functions commonly used?

- Dashboards
- Reports
- Analytics
- AI datasets
- Business Intelligence
- Data Analysis

---

# Common Mistakes

❌ Using SUM() on text columns

❌ Forgetting WHERE conditions

❌ Confusing COUNT(*) with COUNT(column)

❌ Expecting Aggregate Functions to return individual rows

---

# Day 35 Summary

Today you learned:

- What Aggregate Functions are
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- Using multiple Aggregate Functions together
- Real-world applications
- Practice problems
- Beginner interview questions

---

# 📚 Resources

## Official Documentation

- https://dev.mysql.com/doc/
- https://www.postgresql.org/docs/
- https://www.sqlite.org/docs.html

## Practice Platforms

- HackerRank SQL
- LeetCode SQL
- StrataScratch
- SQLBolt

---

# 💻 GitHub Commit Message

```bash
git add .
git commit -m "Day 35: Learned SQL Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)"
git push origin main
```

---

# 🚀 Next Chapter

## Day 35 – Part 2

You'll learn:

- GROUP BY
- HAVING
- WHERE vs HAVING
- Aggregate Functions with GROUP BY
- Department-wise Reports
- Real Business Reports
- Advanced SQL Queries
- Intermediate Interview Questions

Happy Learning! 🚀


# Day 35 – SQL Aggregate Functions (Part 2)

> **Phase 2 – Data & SQL**
>
> **Topic:** GROUP BY, HAVING, Aggregate Functions with WHERE, Multiple Aggregates, Optimization & Interview Preparation

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Use `GROUP BY` effectively
- Filter grouped data using `HAVING`
- Understand the difference between `WHERE` and `HAVING`
- Use multiple aggregate functions together
- Write optimized SQL queries
- Avoid common mistakes
- Solve interview-style SQL questions

---

# 📌 Recap from Part 1

Previously, you learned:

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

These functions calculate values from multiple rows.

Now you'll learn **how to group data** before applying these functions.

---

# Sample Database

## Employees Table

| EmpID | Name | Department | Salary | City |
|-------|------|------------|--------|------|
| 101 | Rahul | IT | 60000 | Delhi |
| 102 | Priya | HR | 45000 | Mumbai |
| 103 | Aman | IT | 70000 | Delhi |
| 104 | Neha | Sales | 50000 | Pune |
| 105 | Vikas | HR | 55000 | Mumbai |
| 106 | Riya | IT | 80000 | Bangalore |
| 107 | Karan | Sales | 65000 | Pune |
| 108 | Anjali | IT | 75000 | Bangalore |

---

# GROUP BY

## What is GROUP BY?

GROUP BY groups rows having the same values.

Instead of calculating on the entire table,

it calculates separately for each group.

---

Imagine this table:

```
IT
IT
IT

HR
HR

Sales
Sales
```

GROUP BY creates three groups.

```
IT
↓

60000
70000
80000
75000

HR
↓

45000
55000

Sales
↓

50000
65000
```

Now SQL can calculate

- Total Salary
- Average Salary
- Maximum Salary

for each department separately.

---

## Syntax

```sql
SELECT column_name,
       AGGREGATE_FUNCTION(column)
FROM table_name
GROUP BY column_name;
```

---

# Example 1

Count employees in each department.

```sql
SELECT Department,
COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department;
```

Output

| Department | TotalEmployees |
|------------|---------------|
| IT | 4 |
| HR | 2 |
| Sales | 2 |

---

# Example 2

Average salary of each department.

```sql
SELECT Department,
AVG(Salary)
FROM Employees
GROUP BY Department;
```

Output

| Department | Average Salary |
|------------|---------------|
| IT | 71250 |
| HR | 50000 |
| Sales | 57500 |

---

# Example 3

Maximum salary in each department.

```sql
SELECT Department,
MAX(Salary)
FROM Employees
GROUP BY Department;
```

---

# Example 4

Minimum salary by city.

```sql
SELECT City,
MIN(Salary)
FROM Employees
GROUP BY City;
```

---

# Multiple Columns in GROUP BY

You can group using multiple columns.

```sql
SELECT
Department,
City,
COUNT(*)
FROM Employees
GROUP BY Department, City;
```

Output

| Department | City | Count |
|------------|------|-------|
| IT | Delhi | 2 |
| IT | Bangalore | 2 |
| HR | Mumbai | 2 |
| Sales | Pune | 2 |

---

# GROUP BY with SUM()

```sql
SELECT
Department,
SUM(Salary)
FROM Employees
GROUP BY Department;
```

---

# GROUP BY with AVG()

```sql
SELECT
Department,
AVG(Salary)
FROM Employees
GROUP BY Department;
```

---

# GROUP BY with MAX()

```sql
SELECT
Department,
MAX(Salary)
FROM Employees
GROUP BY Department;
```

---

# GROUP BY with MIN()

```sql
SELECT
Department,
MIN(Salary)
FROM Employees
GROUP BY Department;
```

---

# HAVING Clause

## What is HAVING?

HAVING filters groups.

WHERE filters rows.

---

Imagine:

Employees

↓

GROUP BY Department

↓

IT

HR

Sales

↓

HAVING Average Salary > 60000

↓

Only IT remains.

---

## Syntax

```sql
SELECT column,
COUNT(*)
FROM table
GROUP BY column
HAVING condition;
```

---

# Example

Departments having more than 2 employees.

```sql
SELECT Department,
COUNT(*)
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 2;
```

Output

| Department | Count |
|------------|------|
| IT | 4 |

---

# Example

Departments whose average salary exceeds 60,000.

```sql
SELECT Department,
AVG(Salary)
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 60000;
```

---

# Example

Cities having salary greater than 100000 total.

```sql
SELECT City,
SUM(Salary)
FROM Employees
GROUP BY City
HAVING SUM(Salary) > 100000;
```

---

# WHERE vs HAVING

| WHERE | HAVING |
|--------|---------|
| Filters rows | Filters groups |
| Executes before GROUP BY | Executes after GROUP BY |
| Cannot use aggregate functions | Can use aggregate functions |

---

Example

WHERE

```sql
SELECT *
FROM Employees
WHERE Salary > 50000;
```

HAVING

```sql
SELECT Department,
AVG(Salary)
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 60000;
```

---

# WHERE + GROUP BY

```sql
SELECT
Department,
COUNT(*)
FROM Employees
WHERE Salary > 50000
GROUP BY Department;
```

---

# WHERE + GROUP BY + HAVING

```sql
SELECT
Department,
AVG(Salary)
FROM Employees
WHERE Salary > 45000
GROUP BY Department
HAVING AVG(Salary) > 60000;
```

Execution Order

```
FROM

↓

WHERE

↓

GROUP BY

↓

HAVING

↓

SELECT

↓

ORDER BY
```

---

# Multiple Aggregate Functions Together

```sql
SELECT

Department,

COUNT(*) AS Employees,

SUM(Salary) AS Total,

AVG(Salary) AS Average,

MIN(Salary) AS Minimum,

MAX(Salary) AS Maximum

FROM Employees

GROUP BY Department;
```

Output

| Department | Count | Sum | Avg | Min | Max |
|------------|------|------|------|------|------|

---

# ORDER BY with GROUP BY

```sql
SELECT

Department,

AVG(Salary)

FROM Employees

GROUP BY Department

ORDER BY AVG(Salary) DESC;
```

---

# Common Mistakes

## Mistake 1

Missing GROUP BY

Wrong

```sql
SELECT Department,
AVG(Salary)
FROM Employees;
```

Correct

```sql
SELECT Department,
AVG(Salary)
FROM Employees
GROUP BY Department;
```

---

## Mistake 2

Using WHERE with Aggregate

Wrong

```sql
WHERE AVG(Salary)>50000
```

Correct

```sql
HAVING AVG(Salary)>50000
```

---

## Mistake 3

Selecting columns not in GROUP BY

Wrong

```sql
SELECT Name,
Department,
AVG(Salary)
FROM Employees
GROUP BY Department;
```

---

# Performance Tips

✅ Filter early using WHERE.

Bad

```sql
SELECT *

FROM Employees

GROUP BY Department;
```

Better

```sql
SELECT *

FROM Employees

WHERE Salary > 50000

GROUP BY Department;
```

---

Use indexes on grouped columns.

Example

```
Department

City

CustomerID

Category
```

---

Avoid unnecessary GROUP BY.

---

Only select required columns.

---

Use aliases.

Example

```sql
AVG(Salary) AS AverageSalary
```

instead of

```
AVG(Salary)
```

---

# Real World Examples

## Amazon

Average order value per customer.

---

## Netflix

Movies released each year.

---

## Flipkart

Sales by category.

---

## Uber

Trips per city.

---

## Swiggy

Orders per restaurant.

---

## Hospital

Patients per doctor.

---

## School

Average marks per class.

---

# Practice Questions

## Easy

1. Count employees in each department.

2. Average salary by city.

3. Maximum salary by department.

4. Minimum salary by city.

5. Total salary by department.

---

## Medium

6. Departments having more than 5 employees.

7. Cities where average salary exceeds 70000.

8. Total salary by city.

9. Count employees by department and city.

10. Highest salary by city.

---

## Hard

11. Department with highest average salary.

12. Top 3 departments by salary.

13. Count employees earning above average salary.

14. Department with minimum total salary.

15. Average salary excluding HR.

---

# Interview Questions

## Beginner

### 1. What is GROUP BY?

Groups rows having the same values.

---

### 2. Why use GROUP BY?

To perform aggregate calculations on groups instead of the whole table.

---

### 3. Can GROUP BY have multiple columns?

Yes.

---

### 4. Can COUNT work with GROUP BY?

Yes.

---

### 5. Can SUM work with GROUP BY?

Yes.

---

### 6. Difference between WHERE and HAVING?

WHERE filters rows.

HAVING filters groups.

---

### 7. Which executes first?

WHERE executes before GROUP BY.

---

### 8. Can HAVING exist without GROUP BY?

Yes, but it is uncommon because it treats the whole result as one group.

---

### 9. Which clause is faster?

WHERE is generally faster because it filters data before grouping.

---

### 10. Can ORDER BY be used with GROUP BY?

Yes.

---

# Intermediate Interview Questions

11. Explain SQL execution order.

12. Why can't aggregate functions be used in WHERE?

13. What happens if GROUP BY is omitted?

14. Can GROUP BY use aliases?

15. How do indexes improve GROUP BY performance?

16. Difference between COUNT(*) and COUNT(column)?

17. Can NULL values affect aggregates?

18. Explain HAVING with an example.

19. When should GROUP BY be avoided?

20. How do you optimize aggregate queries?

---

# Assignment

Using an **Employees** table, write SQL queries to:

- Count employees in each department.
- Find the highest salary in every department.
- Find the lowest salary in every city.
- Calculate total salary department-wise.
- Show departments having more than two employees.
- Display departments with an average salary greater than 60,000.
- Sort departments by average salary in descending order.
- Count employees by department and city.
- Show cities where total salary exceeds 100,000.
- Display department, employee count, total salary, average salary, minimum salary, and maximum salary in a single query.

---

# Day 35 Summary

Today you learned:

- ✅ GROUP BY
- ✅ HAVING
- ✅ WHERE vs HAVING
- ✅ Multiple Aggregate Functions
- ✅ GROUP BY with ORDER BY
- ✅ SQL Execution Order
- ✅ Common Mistakes
- ✅ Query Optimization
- ✅ Real-world Use Cases
- ✅ Interview Questions
- ✅ Practice Problems

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 35 Part 2: Mastered GROUP BY, HAVING, and SQL Aggregate Queries"
git push origin main
```

---

# 🚀 Next Chapter

**Day 35 – Part 3**

Topics:

- Aggregate Functions with JOIN
- Nested Aggregate Queries
- Business Case Studies
- 40+ Advanced Interview Questions
- SQL Cheat Sheet
- Mini Project
- Advanced Practice Problems
```

# Day 35 – SQL Aggregate Functions (Part 3)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this part, you will:

- Solve real-world SQL business problems
- Answer SQL interview questions confidently
- Optimize aggregate queries
- Practice advanced SQL questions
- Complete a mini case study
- Build confidence for AI/ML interviews

---

# 🏢 Real-World Case Study 1: E-Commerce Store

## Table: Orders

| Order_ID | Customer | Product | Category | Price | Quantity |
|----------|----------|----------|----------|-------:|---------:|
| 1 | Rahul | Laptop | Electronics | 50000 | 1 |
| 2 | Priya | Mouse | Electronics | 700 | 2 |
| 3 | Aman | Shoes | Fashion | 2500 | 1 |
| 4 | Rahul | Keyboard | Electronics | 1500 | 1 |
| 5 | Priya | T-Shirt | Fashion | 800 | 3 |

---

## Q1. Total Revenue

```sql
SELECT SUM(price * quantity) AS total_revenue
FROM orders;
```

---

## Q2. Highest Selling Category

```sql
SELECT
category,
SUM(quantity) AS total_quantity
FROM orders
GROUP BY category
ORDER BY total_quantity DESC;
```

---

## Q3. Average Order Value

```sql
SELECT
AVG(price * quantity) AS average_order
FROM orders;
```

---

## Q4. Customer Who Spent the Most

```sql
SELECT
customer,
SUM(price * quantity) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC;
```

---

# 🏦 Real-World Case Study 2: Banking System

## Table: Transactions

| ID | Customer | Type | Amount |
|----|----------|------|-------:|
|1|Aman|Deposit|5000|
|2|Rahul|Withdraw|1000|
|3|Aman|Deposit|2000|
|4|Priya|Deposit|3000|
|5|Rahul|Deposit|4000|

---

## Total Deposits

```sql
SELECT
SUM(amount)
FROM transactions
WHERE type='Deposit';
```

---

## Total Withdrawal

```sql
SELECT
SUM(amount)
FROM transactions
WHERE type='Withdraw';
```

---

## Customer Balance

```sql
SELECT
customer,
SUM(
CASE
WHEN type='Deposit'
THEN amount
ELSE -amount
END
) AS balance
FROM transactions
GROUP BY customer;
```

---

# 🏥 Real-World Case Study 3: Hospital

## Table: Patients

| ID | Department | Bill |
|----|------------|------:|
|1|Cardiology|25000|
|2|Neurology|35000|
|3|Cardiology|20000|
|4|Orthopedic|18000|
|5|Neurology|42000|

---

## Revenue Per Department

```sql
SELECT
department,
SUM(bill)
FROM patients
GROUP BY department;
```

---

## Average Bill

```sql
SELECT
AVG(bill)
FROM patients;
```

---

## Highest Bill

```sql
SELECT
MAX(bill)
FROM patients;
```

---

# 🏢 Real-World Case Study 4: Employee Database

## Table

| Employee | Department | Salary |
|-----------|------------|-------:|
|John|IT|65000|
|Alice|HR|45000|
|David|IT|75000|
|Emma|Sales|55000|
|Sophia|HR|48000|

---

## Average Salary

```sql
SELECT
AVG(salary)
FROM employees;
```

---

## Department Wise Salary

```sql
SELECT
department,
AVG(salary)
FROM employees
GROUP BY department;
```

---

## Highest Paid Employee

```sql
SELECT
MAX(salary)
FROM employees;
```

---

# 🔥 SQL Interview Questions

## Beginner

### 1. What are Aggregate Functions?

Functions that perform calculations on multiple rows and return a single value.

Examples:

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

---

### 2. Difference between COUNT(*) and COUNT(column)?

COUNT(*)

Counts all rows.

COUNT(column)

Counts only non-null values.

---

### 3. Difference between WHERE and HAVING?

| WHERE | HAVING |
|--------|---------|
| Filters rows | Filters groups |
| Before GROUP BY | After GROUP BY |

---

### 4. Can Aggregate Functions Ignore NULL?

Yes.

Example

```sql
AVG(salary)
```

NULL values are ignored.

---

### 5. Which Aggregate Function Returns Highest Value?

```sql
MAX()
```

---

### 6. Which Aggregate Function Returns Lowest Value?

```sql
MIN()
```

---

### 7. Difference between SUM() and COUNT()?

SUM

Adds values.

COUNT

Counts rows.

---

### 8. Which Clause is Mandatory with HAVING?

```sql
GROUP BY
```

---

### 9. Can HAVING be used without GROUP BY?

Yes, in some SQL databases, but it is uncommon.

---

### 10. Which Aggregate Function is Used Most?

Usually

```sql
COUNT()
```

---

# Intermediate Interview Questions

---

### 11. Explain SQL Execution Order.

1. FROM

2. WHERE

3. GROUP BY

4. HAVING

5. SELECT

6. ORDER BY

---

### 12. Why can't Aggregate Functions be used in WHERE?

Because WHERE executes before aggregation.

---

### 13. Difference between DISTINCT and GROUP BY?

DISTINCT removes duplicates.

GROUP BY creates groups.

---

### 14. What happens if GROUP BY is missing?

SQL throws an error if non-aggregated columns are selected with aggregate functions.

---

### 15. Can Aggregate Functions be Nested?

Yes.

Example

```sql
SELECT MAX(avg_salary)

FROM

(
SELECT AVG(salary) avg_salary
FROM employees
GROUP BY department
) t;
```

---

### 16. Why is GROUP BY expensive?

Because it scans and groups rows.

---

### 17. Which Index helps Aggregate Queries?

Indexes on grouping columns.

---

### 18. Difference between Aggregate Function and Window Function?

Aggregate

Returns one row per group.

Window

Returns value for every row.

---

### 19. Can COUNT return NULL?

No.

It returns 0 if no rows match.

---

### 20. How to optimize Aggregate Queries?

- Index columns

- Filter before GROUP BY

- Avoid unnecessary columns

- Use WHERE instead of HAVING whenever possible

---

# Advanced Interview Questions

---

### 21. Explain Hash Aggregation.

Hash tables are used to group data efficiently.

---

### 22. Explain Stream Aggregation.

Works on sorted data.

---

### 23. Which is faster?

Hash Aggregation

or

Sort Aggregation?

Depends on data size and indexes.

---

### 24. What is Cardinality?

Number of unique values.

---

### 25. How does GROUP BY work internally?

Database

- Reads rows
- Groups rows
- Performs aggregate
- Returns result

---

### 26. Why are indexes important?

Reduce scanning time.

---

### 27. What is Query Optimization?

Making SQL queries execute faster.

---

### 28. Difference between HAVING COUNT(*)>5 and WHERE?

HAVING filters groups.

WHERE filters rows.

---

### 29. Can Aggregate Functions use CASE?

Yes.

Example

```sql
SELECT
SUM(
CASE
WHEN salary>50000
THEN salary
ELSE 0
END)
FROM employees;
```

---

### 30. Most Asked SQL Interview Topics

- COUNT()
- SUM()
- AVG()
- GROUP BY
- HAVING
- Joins
- Subqueries
- Window Functions

---

# 🧠 Practice Questions

## Easy

1. Count students.
2. Find total salary.
3. Find highest salary.
4. Find lowest salary.
5. Find average marks.

---

## Medium

6. Revenue per category.

7. Customer order count.

8. Average salary per department.

9. Find departments having more than 5 employees.

10. Find highest-selling product.

---

## Advanced

11. Top customer by revenue.

12. Monthly revenue report.

13. Daily sales summary.

14. Department-wise average salary.

15. Product performance dashboard.

16. Branch-wise profit.

17. Employee bonus report.

18. Sales leaderboard.

19. Revenue by city.

20. Customer lifetime value.

---

# 💻 Mini Project

## Sales Dashboard

### Database Tables

- Customers
- Products
- Orders
- Categories

---

### Features

✔ Total Revenue

✔ Total Customers

✔ Best Selling Product

✔ Average Order Value

✔ Highest Paying Customer

✔ Category Revenue

---

### Queries to Build

- Revenue Report

- Product Report

- Customer Report

- Category Report

- Daily Sales Report

---

# 📋 SQL Cheat Sheet

```sql
COUNT(*)

COUNT(column)

SUM(column)

AVG(column)

MIN(column)

MAX(column)

GROUP BY

HAVING

ORDER BY

DISTINCT
```

---

# 📝 Assignment

Create a database called

```text
CompanyDB
```

Tables

- Employees

- Departments

- Projects

Write SQL queries for:

1. Total employees

2. Average salary

3. Highest salary

4. Lowest salary

5. Department-wise salary

6. Departments with more than 3 employees

7. Average salary above 50000

8. Total projects

9. Employees per department

10. Salary report

---

# 🎯 Learning Checklist

- [ ] Understand Aggregate Functions
- [ ] Know COUNT()
- [ ] Know SUM()
- [ ] Know AVG()
- [ ] Know MIN()
- [ ] Know MAX()
- [ ] Master GROUP BY
- [ ] Master HAVING
- [ ] Solve 20 Practice Problems
- [ ] Complete Mini Project

---

# 🏆 Day 35 Summary

Today you mastered:

- Aggregate Functions
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING
- Real-world SQL reports
- Business case studies
- Query optimization basics
- Interview questions
- Practice problems
- Mini project

You are now ready to move on to more advanced SQL concepts like **Joins**, which are one of the most frequently tested topics in technical interviews.

---

# 💬 Git Commit Message

```bash
git add .
git commit -m "Day 35: Mastered SQL Aggregate Functions with real-world case studies and interview questions"
git push origin main
```

---

# 🚀 Next Day

**Day 36 – SQL Joins**

Topics:
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- SELF JOIN
- CROSS JOIN
- Real-world database relationships
- 50+ Interview Questions
- Company-level SQL Join problems