# 📊 Day 39 - SQL Window Functions (Part 1A)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what SQL Window Functions are.
- Learn why Window Functions are important.
- Understand the `OVER()` clause.
- Learn how `PARTITION BY` works.
- Learn how `ORDER BY` works inside Window Functions.
- Understand the difference between Aggregate Functions and Window Functions.
- Write analytical SQL queries.
- Solve real-world business problems using Window Functions.

---

# 📌 What are SQL Window Functions?

A **Window Function** performs a calculation across a set of rows that are related to the current row **without reducing the number of rows returned**.

Unlike `GROUP BY`, Window Functions allow you to:

- Keep every row in the result.
- Perform calculations across groups of rows.
- Rank records.
- Calculate running totals.
- Compare rows.

---

# 🤔 Why Do We Need Window Functions?

Imagine a company wants to know:

- Which employee has the highest salary in each department?
- What is each employee's salary compared to the department average?
- What is the running total of monthly sales?

Using only `GROUP BY` is difficult because it combines rows into one.

Window Functions solve this problem while keeping every record visible.

---

# 📈 GROUP BY vs Window Functions

| GROUP BY | Window Function |
|----------|-----------------|
| Combines rows | Keeps all rows |
| Returns one row per group | Returns every row |
| Cannot compare with original rows easily | Perfect for comparisons |
| Used for summaries | Used for analytics |

Example using `GROUP BY`:

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department;
```

Output:

| Department | Average Salary |
|------------|---------------:|
| IT | 78000 |
| HR | 52000 |

Notice that employee-level information is lost.

---

Window Function example:

```sql
SELECT
employee_name,
department,
salary,
AVG(salary) OVER(PARTITION BY department) AS department_average
FROM employees;
```

Output:

| Employee | Department | Salary | Department Average |
|----------|------------|-------:|-------------------:|
| Alice | IT | 90000 | 78000 |
| Bob | IT | 70000 | 78000 |
| Charlie | IT | 74000 | 78000 |

Every employee remains visible.

---

# 🏢 Sample Database

```sql
CREATE TABLE employees (

employee_id INT PRIMARY KEY,

employee_name VARCHAR(50),

department VARCHAR(30),

salary INT,

joining_date DATE

);
```

---

## Insert Sample Data

```sql
INSERT INTO employees VALUES
(1,'Alice','IT',90000,'2023-01-10'),
(2,'Bob','IT',70000,'2022-06-18'),
(3,'Charlie','IT',74000,'2021-09-25'),
(4,'David','HR',50000,'2022-01-15'),
(5,'Eva','HR',54000,'2021-11-05'),
(6,'Frank','Finance',85000,'2023-03-12'),
(7,'Grace','Finance',79000,'2022-08-21');
```

---

# 🪟 Window Function Syntax

```sql
FUNCTION_NAME(column_name)
OVER(

PARTITION BY column_name

ORDER BY column_name

)
```

General Syntax:

```sql
SELECT
column1,
FUNCTION(column2)
OVER(
PARTITION BY column3
ORDER BY column4
)
FROM table_name;
```

---

# 🔍 Understanding OVER()

The `OVER()` clause tells SQL:

> "Apply this calculation over a specific set of rows."

Example:

```sql
SELECT

employee_name,

salary,

AVG(salary) OVER()

FROM employees;
```

Output:

| Employee | Salary | Company Average |
|----------|-------:|----------------:|
| Alice | 90000 | 71714 |
| Bob | 70000 | 71714 |
| Charlie | 74000 | 71714 |
| David | 50000 | 71714 |

Every row displays the company average.

---

# 🧩 Understanding PARTITION BY

Think of `PARTITION BY` as dividing your data into separate groups before performing calculations.

Example:

```sql
SELECT

employee_name,

department,

salary,

AVG(salary)
OVER(PARTITION BY department)

AS department_average

FROM employees;
```

Output:

| Employee | Department | Salary | Department Avg |
|----------|------------|-------:|---------------:|
| Alice | IT | 90000 | 78000 |
| Bob | IT | 70000 | 78000 |
| Charlie | IT | 74000 | 78000 |
| David | HR | 50000 | 52000 |
| Eva | HR | 54000 | 52000 |

Each department has its own average.

---

# 🔄 PARTITION BY vs GROUP BY

### GROUP BY

```sql
SELECT

department,

AVG(salary)

FROM employees

GROUP BY department;
```

Returns:

```
IT
HR
Finance
```

Only one row per department.

---

### PARTITION BY

```sql
AVG(salary)

OVER(PARTITION BY department)
```

Returns every employee with the department average.

---

# 📊 Understanding ORDER BY in Window Functions

Inside `OVER()`, `ORDER BY` determines the sequence used by the Window Function.

Example:

```sql
SELECT

employee_name,

salary,

SUM(salary)

OVER(ORDER BY salary)

AS running_total

FROM employees;
```

Conceptual Output:

| Employee | Salary | Running Total |
|----------|-------:|--------------:|
| David | 50000 | 50000 |
| Eva | 54000 | 104000 |
| Bob | 70000 | 174000 |
| Charlie | 74000 | 248000 |
| Grace | 79000 | 327000 |
| Frank | 85000 | 412000 |
| Alice | 90000 | 502000 |

This is called a **Running Total**.

---

# 🎯 Real-World Use Cases

Window Functions are heavily used in:

- Banking
- E-commerce
- HR Analytics
- Finance
- Healthcare
- Data Warehousing
- Business Intelligence Dashboards

Examples:

- Rank top-selling products
- Compare employee salaries
- Running account balance
- Monthly sales analysis
- Customer purchase history

---

# 💡 Why AI Engineers Should Learn Window Functions

As an AI/ML Engineer, you'll often work with data before training models.

Window Functions help you:

- Engineer features
- Analyze trends
- Detect anomalies
- Create rolling statistics
- Prepare datasets efficiently

Many ML pipelines use SQL Window Functions before data reaches Python.

---

# 📝 Practice Queries

### 1. Display all employees with company average salary.

```sql
SELECT

employee_name,

salary,

AVG(salary) OVER()

FROM employees;
```

---

### 2. Show department average salary.

```sql
SELECT

employee_name,

department,

salary,

AVG(salary)
OVER(PARTITION BY department)

FROM employees;
```

---

### 3. Display running salary total.

```sql
SELECT

employee_name,

salary,

SUM(salary)

OVER(ORDER BY salary)

FROM employees;
```

---

### 4. Show maximum salary in each department.

```sql
SELECT

employee_name,

department,

salary,

MAX(salary)

OVER(PARTITION BY department)

AS highest_salary

FROM employees;
```

---

### 5. Show minimum salary in each department.

```sql
SELECT

employee_name,

department,

salary,

MIN(salary)

OVER(PARTITION BY department)

AS minimum_salary

FROM employees;
```

---

# 🧪 Hands-on Exercise

Using the sample database, write queries to:

- Display company average salary.
- Display department average salary.
- Display department maximum salary.
- Display department minimum salary.
- Display running salary total.
- Compare employee salary with department average.

---

# 💼 Mini Assignment

Create a new table called `sales`.

Columns:

- sale_id
- employee_name
- month
- sales_amount

Then write SQL queries to:

1. Calculate total company sales.
2. Calculate department-wise sales.
3. Show running sales total.
4. Compare employee sales with department average.

---

# 🎤 Interview Questions

### Beginner

1. What is a Window Function?
2. Why do we use Window Functions?
3. What is the purpose of `OVER()`?
4. What does `PARTITION BY` do?
5. How is `GROUP BY` different from `PARTITION BY`?

### Intermediate

6. Can Window Functions reduce the number of rows?
7. Can Window Functions use Aggregate Functions?
8. What is the role of `ORDER BY` inside `OVER()`?
9. When should you use a Window Function instead of `GROUP BY`?
10. Name some commonly used Window Functions.

---

# 📚 Key Takeaways

- Window Functions perform calculations without collapsing rows.
- `OVER()` defines the window.
- `PARTITION BY` creates logical groups.
- `ORDER BY` controls calculation order.
- Window Functions are essential for analytics and reporting.
- They are widely used in data engineering, BI, and AI pipelines.

---

# 🚀 GitHub Commit Message

```bash
git add .
git commit -m "Day 39 Part 1A: Learned SQL Window Functions Fundamentals"
git push origin main
```

---

# ⏭️ Next Lesson

## **Day 39 – Part 1B**

Topics:

- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- Differences between Ranking Functions
- Real-world Ranking Examples
- 20+ Practice Queries
- Interview Questions

# Day 39 -- SQL Window Functions (Part 1B)

> **Phase 2: Data & SQL**\
> **Topic:** `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`

------------------------------------------------------------------------

# 🎯 Learning Objectives

By the end of this lesson you will be able to:

-   Understand ranking window functions
-   Use `ROW_NUMBER()`
-   Use `RANK()`
-   Use `DENSE_RANK()`
-   Know the difference between all three
-   Solve common interview questions

------------------------------------------------------------------------

# Sample Table

``` sql
CREATE TABLE employees (
    emp_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT
);

INSERT INTO employees VALUES
(1,'Alice','IT',70000),
(2,'Bob','IT',90000),
(3,'Charlie','IT',90000),
(4,'David','HR',50000),
(5,'Eva','HR',60000),
(6,'Frank','Sales',75000),
(7,'Grace','Sales',75000);
```

------------------------------------------------------------------------

# 1. ROW_NUMBER()

Assigns a unique sequential number to each row.

``` sql
SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER(
        PARTITION BY department
        ORDER BY salary DESC
    ) AS row_num
FROM employees;
```

Example output:

  Name      Department     Salary   Row Number
  --------- ------------ -------- ------------
  Bob       IT              90000            1
  Charlie   IT              90000            2
  Alice     IT              70000            3

**Use Cases** - Pagination - Removing duplicates - Top-N records

------------------------------------------------------------------------

# 2. RANK()

Rows with the same value receive the same rank. Gaps appear after ties.

``` sql
SELECT
    name,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS rank_no
FROM employees;
```

Example:

    Salary   Rank
  -------- ------
     90000      1
     90000      1
     75000      3

------------------------------------------------------------------------

# 3. DENSE_RANK()

Same rank for ties, but **no gaps**.

``` sql
SELECT
    name,
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS dense_rank
FROM employees;
```

Example:

    Salary   Dense Rank
  -------- ------------
     90000            1
     90000            1
     75000            2

------------------------------------------------------------------------

# Comparison

  Function     Duplicate Values   Gaps   Best Use
  ------------ ------------------ ------ ---------------------
  ROW_NUMBER   No                 No     Unique numbering
  RANK         Yes                Yes    Competition ranking
  DENSE_RANK   Yes                No     Business reports

------------------------------------------------------------------------

# Top 2 Employees Per Department

``` sql
SELECT *
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER(
            PARTITION BY department
            ORDER BY salary DESC
        ) rn
    FROM employees
) t
WHERE rn <= 2;
```

------------------------------------------------------------------------

# Practice Questions

1.  Find the highest-paid employee in each department.
2.  Find the top 3 salaries.
3.  Rank employees by salary.
4.  Show dense rank for every department.
5.  Remove duplicate rows using `ROW_NUMBER()`.

------------------------------------------------------------------------

# Interview Questions

### 1. What is a window function?

A function that performs calculations across related rows without
collapsing them.

### 2. Difference between `RANK()` and `DENSE_RANK()`?

`RANK()` leaves gaps after ties, `DENSE_RANK()` does not.

### 3. When should `ROW_NUMBER()` be used?

When every row needs a unique sequence.

### 4. Can window functions be used with `GROUP BY`?

Yes, but they are evaluated after grouping in the logical query order.

### 5. Why are window functions popular?

They simplify analytical SQL such as leaderboards, running totals, and
rankings.

------------------------------------------------------------------------

# Assignment

-   Create a `students` table.
-   Insert at least 15 records.
-   Rank students by marks.
-   Show top 3 students in each class.
-   Compare results using all three ranking functions.

------------------------------------------------------------------------

# Git Commit

``` bash
git add .
git commit -m "Day 39 Part 1B: ROW_NUMBER, RANK and DENSE_RANK"
git push origin main
```

------------------------------------------------------------------------

# Next Lesson

**Day 39 -- Part 2**

-   LAG()
-   LEAD()
-   FIRST_VALUE()
-   LAST_VALUE()
-   Running Totals
-   Moving Average

# 📊 Day 39 – SQL Window Functions (Part 2)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Understand advanced SQL Window Functions
- Compare current and previous rows
- Compare current and next rows
- Calculate cumulative sums
- Calculate running averages
- Divide data into buckets
- Rank data using percentages
- Solve real-world analytics problems
- Answer SQL interview questions confidently

---

# 📖 Recap

In Part 1 you learned:

- OVER()
- PARTITION BY
- ORDER BY
- ROW_NUMBER()
- RANK()
- DENSE_RANK()

Now we'll learn the most powerful window functions used by Data Analysts, Data Engineers and AI Engineers.

---

# Sample Dataset

## Employee Table

| Emp_ID | Name | Department | Salary |
|---------|------|------------|--------|
|101|Alice|HR|50000|
|102|Bob|HR|65000|
|103|Charlie|HR|75000|
|104|David|IT|80000|
|105|Eva|IT|85000|
|106|Frank|IT|90000|
|107|Grace|Sales|60000|
|108|Henry|Sales|65000|
|109|Ivy|Sales|70000|

---

# 1️⃣ LAG()

## What is LAG()?

Returns the value from the previous row.

Think of it as looking behind.

---

## Syntax

```sql
LAG(column, offset, default)
OVER(
PARTITION BY column
ORDER BY column
)
```

---

## Example

```sql
SELECT
Name,
Salary,

LAG(Salary)
OVER(
ORDER BY Salary
)

AS PreviousSalary

FROM Employee;
```

### Output

| Name | Salary | Previous Salary |
|------|---------|----------------|
Alice|50000|NULL|
Grace|60000|50000|
Bob|65000|60000|
Henry|65000|65000|
Ivy|70000|65000|
Charlie|75000|70000|

---

# Real World Example

Monthly Sales

| Month | Sales |
|--------|-------|
January|10000|
February|15000|
March|12000|

Using LAG()

| Month | Sales | Previous Month |
|--------|-------|----------------|
Jan|10000|NULL|
Feb|15000|10000|
Mar|12000|15000|

---

# Sales Growth

```sql
SELECT

Month,

Sales,

LAG(Sales)
OVER(
ORDER BY Month
)

AS PreviousMonth,

Sales -

LAG(Sales)
OVER(
ORDER BY Month)

AS Growth

FROM Sales;
```

---

# 2️⃣ LEAD()

Returns next row value.

Think of it as looking ahead.

---

## Syntax

```sql
LEAD(column)
OVER(
ORDER BY column
)
```

---

## Example

```sql
SELECT

Name,

Salary,

LEAD(Salary)
OVER(
ORDER BY Salary
)

AS NextSalary

FROM Employee;
```

---

Output

| Salary | Next Salary |
|----------|--------------|
50000|60000|
60000|65000|
65000|65000|
65000|70000|

---

# Use Cases

Predict:

- Next Month Sales
- Next Employee Salary
- Upcoming Stock Price

---

# Difference

| LAG | LEAD |
|------|------|
Looks Previous|Looks Next|

---

# 3️⃣ FIRST_VALUE()

Returns first value inside window.

---

Example

```sql
SELECT

Name,

Salary,

FIRST_VALUE(Salary)

OVER(
PARTITION BY Department
ORDER BY Salary
)

AS LowestSalary

FROM Employee;
```

---

Output

HR

| Name | Salary | Lowest Salary |
|------|---------|--------------|
Alice|50000|50000|
Bob|65000|50000|
Charlie|75000|50000|

---

# 4️⃣ LAST_VALUE()

Returns last value.

Example

```sql
SELECT

Name,

Salary,

LAST_VALUE(Salary)

OVER(

PARTITION BY Department

ORDER BY Salary

ROWS BETWEEN UNBOUNDED PRECEDING

AND UNBOUNDED FOLLOWING

)

AS HighestSalary

FROM Employee;
```

---

Output

| Name | Highest Salary |
|------|----------------|
Alice|75000|
Bob|75000|
Charlie|75000|

---

# Why ROWS Clause?

Without it,

LAST_VALUE()

returns current row instead of last row.

Always use

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
```

---

# 5️⃣ NTILE()

Divides rows into equal groups.

Example

```sql
SELECT

Name,

Salary,

NTILE(4)

OVER(

ORDER BY Salary

)

AS Quartile

FROM Employee;
```

---

Output

| Name | Quartile |
|------|-----------|
Alice|1|
Grace|1|
Bob|2|
Henry|2|
Ivy|3|
Charlie|3|
David|4|
Eva|4|

---

Use Cases

- Customer Segmentation
- Salary Bands
- Student Ranking
- Sales Analysis

---

# 6️⃣ CUME_DIST()

Returns cumulative distribution.

Formula

```
Rows less than current
------------------------
Total Rows
```

---

Example

```sql
SELECT

Name,

Salary,

CUME_DIST()

OVER(
ORDER BY Salary
)

FROM Employee;
```

---

Output

| Salary | Distribution |
|----------|--------------|
50000|0.11|
60000|0.22|
65000|0.44|

---

Use Cases

Top

- 10%
- 20%
- 30%

Employees

---

# 7️⃣ PERCENT_RANK()

Ranks rows between

0 and 1

Formula

```
Rank-1
------------
Rows-1
```

---

Example

```sql
SELECT

Name,

Salary,

PERCENT_RANK()

OVER(

ORDER BY Salary

)

FROM Employee;
```

---

Output

| Salary | Rank |
|----------|-------|
50000|0|
60000|0.12|
65000|0.25|

---

Difference

| CUME_DIST | PERCENT_RANK |
|------------|--------------|
Uses cumulative rows|Uses ranking|

---

# Running Total

One of the most common interview questions.

---

Example

```sql
SELECT

Month,

Sales,

SUM(Sales)

OVER(

ORDER BY Month

)

AS RunningTotal

FROM Sales;
```

---

Output

| Month | Sales | Total |
|--------|-------|--------|
Jan|10000|10000|
Feb|12000|22000|
Mar|8000|30000|
Apr|15000|45000|

---

# Running Average

```sql
SELECT

Month,

AVG(Sales)

OVER(

ORDER BY Month

)

AS RunningAverage

FROM Sales;
```

---

Output

| Month | Average |
|--------|----------|
Jan|10000|
Feb|11000|
Mar|10000|
Apr|11250|

---

# Moving Average

Last 3 Months

```sql
SELECT

Month,

AVG(Sales)

OVER(

ORDER BY Month

ROWS BETWEEN

2 PRECEDING

AND CURRENT ROW

)

FROM Sales;
```

---

Use Cases

- Stock Market
- AI Forecasting
- Time Series
- Business Analytics

---

# Real World Business Examples

## Banking

Running Balance

## Amazon

Top Selling Products

## Netflix

Most Watched Shows

## Uber

Trips Per Driver

## Swiggy

Daily Orders

## LinkedIn

Top Recruiters

## Flipkart

Highest Revenue Category

---

# Common Mistakes

❌ Forgetting ORDER BY

❌ Using LAST_VALUE without ROWS clause

❌ Mixing GROUP BY and Window Functions incorrectly

❌ Wrong PARTITION BY column

❌ Confusing RANK() with ROW_NUMBER()

---

# Performance Tips

✅ Index ORDER BY columns

✅ Partition wisely

✅ Avoid unnecessary sorting

✅ Filter data before applying window functions

✅ Use EXPLAIN to analyze execution plans

---

# Practice Questions

## Easy

1. Find previous salary.
2. Find next salary.
3. Find first salary in department.
4. Find last salary.
5. Divide employees into 4 groups.

---

## Medium

6. Running total of sales.
7. Running average.
8. Moving average.
9. Rank customers.
10. Sales growth month over month.

---

## Advanced

11. Find top 10% employees.
12. Revenue percentile.
13. Salary comparison with previous employee.
14. Compare current month with previous.
15. Detect salary jumps greater than ₹10,000.

---

# Interview Questions

## Beginner

1. What is LAG()?
2. What is LEAD()?
3. Difference between LAG and LEAD?
4. What is FIRST_VALUE()?
5. What is LAST_VALUE()?

---

## Intermediate

6. Why use ROWS clause?
7. What is NTILE()?
8. Difference between CUME_DIST() and PERCENT_RANK()?
9. How is Running Total calculated?
10. What is Moving Average?

---

## Advanced

11. How do Window Functions improve analytics?
12. Can Window Functions replace GROUP BY?
13. Explain execution order of Window Functions.
14. How do Window Functions affect performance?
15. When should you avoid using Window Functions?

---

# Mini Project

## Sales Analytics Dashboard (SQL)

Create queries to:

- Rank salespeople
- Calculate monthly revenue
- Running total
- Running average
- Sales growth
- Highest selling month
- Lowest selling month
- Top 10% customers
- Customer segmentation using NTILE()
- Monthly performance report

---

# Day 39 Summary

Today you learned:

- ✅ LAG()
- ✅ LEAD()
- ✅ FIRST_VALUE()
- ✅ LAST_VALUE()
- ✅ NTILE()
- ✅ CUME_DIST()
- ✅ PERCENT_RANK()
- ✅ Running Total
- ✅ Running Average
- ✅ Moving Average
- ✅ Business Use Cases
- ✅ Performance Tips
- ✅ Interview Questions
- ✅ SQL Analytics Dashboard

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 39: Mastered Advanced SQL Window Functions and Analytics"
git push origin main
```

---

# 🚀 Next Day

**Day 40 – SQL Common Table Expressions (CTEs) & Recursive Queries**

Topics:

- What are CTEs?
- WITH Clause
- Recursive CTEs
- Hierarchical Queries
- Recursive Tree Traversal
- Employee-Manager Relationships
- SQL Interview Questions
- Hands-on Project

# 📊 Day 39 – SQL Window Functions (Part 3A)

> **Phase 2: Data & SQL**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer
>
> **Part 3A:** Interview Questions, Common Mistakes, Optimization & Best Practices

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Answer SQL Window Function interview questions confidently.
- Understand the differences between ranking functions.
- Avoid common mistakes.
- Write optimized SQL queries.
- Apply best practices used in production databases.

---

# 💼 Why Interviewers Love Window Functions

Window Functions test whether you can:

- Analyze data efficiently.
- Write optimized SQL.
- Solve business problems.
- Avoid unnecessary subqueries.
- Think like a Data Analyst or Data Engineer.

They are commonly asked in interviews at:

- Google
- Microsoft
- Amazon
- Meta
- Uber
- Airbnb
- Netflix
- JPMorgan
- Walmart Global Tech
- Product-based startups

---

# 🟢 Beginner Interview Questions

---

## 1. What are SQL Window Functions?

A Window Function performs calculations across a set of rows related to the current row without collapsing the result into a single row.

Unlike `GROUP BY`, every row remains visible.

---

## 2. What is the syntax of a Window Function?

```sql
FUNCTION_NAME() OVER (
    PARTITION BY column
    ORDER BY column
)
```

---

## 3. What is the purpose of OVER()?

`OVER()` defines the window over which the function operates.

Example:

```sql
ROW_NUMBER() OVER(ORDER BY salary DESC)
```

---

## 4. Can Window Functions reduce rows?

No.

Unlike GROUP BY, Window Functions preserve every row.

---

## 5. What is PARTITION BY?

It divides data into groups before applying the Window Function.

Example:

```sql
PARTITION BY department
```

Each department becomes its own window.

---

## 6. What happens if PARTITION BY is omitted?

The entire table becomes one window.

---

## 7. Is ORDER BY mandatory?

Not always.

Ranking functions require it.

Aggregate window functions may not.

---

## 8. Difference between GROUP BY and Window Functions?

| GROUP BY | Window Function |
|-----------|-----------------|
| Combines rows | Keeps rows |
| Returns one row per group | Returns every row |
| Aggregate only | Aggregate + Ranking + Analytics |

---

## 9. Which SQL functions can be Window Functions?

Examples:

- SUM()
- AVG()
- COUNT()
- MIN()
- MAX()
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LAG()
- LEAD()

---

## 10. Why are Window Functions useful?

They simplify analytics queries that otherwise require complex joins or subqueries.

---

# 🟡 Intermediate Interview Questions

---

## 11. Difference between ROW_NUMBER() and RANK()?

### ROW_NUMBER()

Always unique.

```
100
90
90
80
```

Produces:

```
1
2
3
4
```

---

### RANK()

Produces gaps.

```
1
2
2
4
```

---

## 12. Difference between RANK() and DENSE_RANK()

RANK()

```
1
2
2
4
```

DENSE_RANK()

```
1
2
2
3
```

---

## 13. When should ROW_NUMBER() be used?

When every row needs a unique sequence.

Example:

- Invoice numbers
- Employee IDs
- Pagination

---

## 14. When should RANK() be used?

Leaderboard.

Competition ranking.

---

## 15. When should DENSE_RANK() be used?

Ranking products without gaps.

---

## 16. What is LAG()?

Returns the previous row.

Example:

```sql
LAG(salary)
OVER(ORDER BY salary)
```

---

## 17. What is LEAD()?

Returns the next row.

---

## 18. Difference between LAG() and LEAD()

| LAG | LEAD |
|------|------|
| Previous row | Next row |

---

## 19. What is FIRST_VALUE()?

Returns the first value in the partition.

---

## 20. What is LAST_VALUE()?

Returns the last value inside the window.

---

## 21. What is NTILE()?

Splits data into equal buckets.

Example:

```sql
NTILE(4)
```

Creates Quartiles.

---

## 22. What is CUME_DIST()?

Calculates cumulative distribution.

---

## 23. What is PERCENT_RANK()?

Calculates percentage ranking.

---

## 24. Can Window Functions be nested?

Generally no.

Instead use CTEs or Subqueries.

---

## 25. Can Window Functions be used inside WHERE?

No.

SQL execution order prevents this.

Use:

- CTE
- Subquery

---

# 🔴 Advanced Interview Questions

---

## 26. SQL Execution Order

```
FROM

WHERE

GROUP BY

HAVING

WINDOW FUNCTIONS

SELECT

ORDER BY
```

Notice:

Window Functions execute **after HAVING**.

---

## 27. Why can't Window Functions be used inside WHERE?

Because WHERE executes before Window Functions.

---

## 28. How do you filter Window Function results?

Use CTE.

Example:

```sql
WITH ranked AS
(
SELECT *,
ROW_NUMBER() OVER(
ORDER BY salary DESC
) AS rn
FROM employees
)

SELECT *
FROM ranked
WHERE rn <= 5;
```

---

## 29. Explain Running Total.

```sql
SUM(sales)
OVER(
ORDER BY order_date
)
```

---

## 30. Explain Moving Average.

Average over previous rows.

Example:

```sql
AVG(sales)
OVER(
ORDER BY order_date
ROWS BETWEEN 2 PRECEDING
AND CURRENT ROW
)
```

---

## 31. Explain ROWS BETWEEN.

Defines frame boundaries.

Example:

```sql
ROWS BETWEEN
UNBOUNDED PRECEDING
AND CURRENT ROW
```

---

## 32. Difference between ROWS and RANGE?

ROWS

Physical rows.

RANGE

Logical values.

---

## 33. Can Window Functions improve readability?

Yes.

Often replace:

- Nested queries
- Self joins
- Correlated subqueries

---

## 34. Why are Window Functions faster?

They reduce:

- Multiple scans
- Complex joins
- Duplicate calculations

---

## 35. Can aggregate functions become Window Functions?

Yes.

Example:

```sql
SUM(salary)
OVER()
```

---

# ⭐ Scenario-Based Interview Questions

---

## 36.

Find top 3 highest-paid employees from each department.

Expected:

```
ROW_NUMBER()

PARTITION BY department
```

---

## 37.

Calculate running sales.

Expected:

```
SUM()

OVER()
```

---

## 38.

Find previous month's revenue.

Expected:

```
LAG()
```

---

## 39.

Compare current salary with previous salary.

Expected:

```
LAG(salary)
```

---

## 40.

Assign quartiles to customers.

Expected:

```
NTILE(4)
```

---

## 41.

Find first employee hired in each department.

Expected:

```
FIRST_VALUE()
```

---

## 42.

Find last sale of every region.

Expected:

```
LAST_VALUE()
```

---

## 43.

Find sales difference between two consecutive months.

Expected:

```
LAG()
```

---

## 44.

Rank products within categories.

Expected:

```
RANK()

PARTITION BY category
```

---

## 45.

Assign serial numbers to invoices.

Expected:

```
ROW_NUMBER()
```

---

# 🔥 Common Mistakes

## Mistake 1

Using Window Functions in WHERE.

❌ Wrong

```sql
WHERE
ROW_NUMBER() OVER(...)
```

✅ Correct

Use CTE.

---

## Mistake 2

Forgetting ORDER BY.

Ranking becomes meaningless.

---

## Mistake 3

Using RANK() instead of ROW_NUMBER().

Duplicates produce unexpected gaps.

---

## Mistake 4

Ignoring PARTITION BY.

Entire dataset becomes one window.

---

## Mistake 5

Using LAST_VALUE() incorrectly.

Specify frame.

Correct:

```sql
LAST_VALUE(salary)
OVER(
ORDER BY salary
ROWS BETWEEN
UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
)
```

---

# 🚀 SQL Optimization Tips

### ✅ Index columns used in

- ORDER BY
- PARTITION BY

---

### ✅ Filter data before applying Window Functions

Good:

```sql
WHERE year = 2026
```

before ranking.

---

### ✅ Avoid unnecessary nested subqueries.

Use CTEs.

---

### ✅ Avoid SELECT *

Fetch only needed columns.

---

### ✅ Use Window Functions instead of self joins whenever possible.

---

### ✅ Analyze query plan.

Use:

```sql
EXPLAIN
```

---

### ✅ Partition wisely.

Too many partitions reduce efficiency.

---

# 💡 Best Practices

✔ Use meaningful aliases.

```sql
salary_rank
```

instead of

```sql
r1
```

---

✔ Write readable SQL.

---

✔ Prefer CTEs over deeply nested queries.

---

✔ Comment complex analytics.

---

✔ Always test ranking with duplicate values.

---

✔ Understand execution order.

---

✔ Choose the correct ranking function.

| Situation | Function |
|------------|----------|
| Unique IDs | ROW_NUMBER() |
| Competition Ranking | RANK() |
| Dense Ranking | DENSE_RANK() |
| Previous Row | LAG() |
| Next Row | LEAD() |
| Running Total | SUM() OVER() |
| Moving Average | AVG() OVER() |
| Quartiles | NTILE() |

---

# 📚 Quick Revision

- Window Functions keep all rows.
- OVER() defines the window.
- PARTITION BY creates groups.
- ORDER BY sorts within the window.
- ROW_NUMBER() gives unique numbers.
- RANK() leaves gaps.
- DENSE_RANK() removes gaps.
- LAG() returns the previous row.
- LEAD() returns the next row.
- FIRST_VALUE() returns the first value.
- LAST_VALUE() returns the last value.
- Window Functions cannot be used directly in WHERE.
- Use CTEs for filtering ranked data.

---

# 🎯 Self-Assessment Checklist

Mark yourself after completing Day 39:

- [ ] I can explain Window Functions.
- [ ] I know the purpose of OVER().
- [ ] I understand PARTITION BY.
- [ ] I can use ROW_NUMBER().
- [ ] I can differentiate RANK() and DENSE_RANK().
- [ ] I can use LAG() and LEAD().
- [ ] I know when to use FIRST_VALUE() and LAST_VALUE().
- [ ] I can optimize Window Function queries.
- [ ] I can answer SQL Window Function interview questions confidently.
- [ ] I am ready to solve real-world analytics problems.

---

# 🚀 Next Part

**Day 39 – Part 3B**

- Production-Grade Sales Analytics Project
- 30+ Practice Problems
- Assignments
- SQL Window Functions Cheat Sheet
- GitHub Commit Message
- Day Summary
- Next Day Roadmap
```

# 📊 Day 39 – SQL Window Functions (Part 3B)

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer
> **Topic:** SQL Window Functions – Capstone Project, Practice Questions & Cheat Sheet

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Build a real-world analytics project using Window Functions
- Solve interview-level SQL problems
- Apply ranking and analytical functions
- Understand business reporting scenarios
- Prepare for SQL coding interviews

---

# 🚀 Production Grade Project

# Sales Analytics Dashboard Database

Imagine you are working as a Data Analyst at an E-commerce company.

Management wants reports like:

- Top selling employees
- Monthly sales trend
- Best performing products
- Running revenue
- Previous month comparison
- Customer ranking
- Department ranking

---

# Database Schema

## Sales Table

| Sale_ID | Employee | Department | Product | Month | Amount |
|----------|----------|------------|---------|-------|--------|
|1|John|Electronics|Laptop|Jan|50000|
|2|John|Electronics|Mouse|Jan|3000|
|3|Alice|Electronics|Laptop|Feb|55000|
|4|Bob|Furniture|Chair|Jan|12000|
|5|Bob|Furniture|Table|Feb|25000|
|6|David|Furniture|Chair|Mar|15000|
|7|Emma|Fashion|Shoes|Jan|8000|
|8|Emma|Fashion|Bag|Feb|10000|

---

# Step 1

## Employee Ranking

```sql
SELECT
Employee,
Amount,
ROW_NUMBER() OVER(
ORDER BY Amount DESC
) AS Rank
FROM Sales;
```

---

# Step 2

## Department Ranking

```sql
SELECT
Department,
Employee,
Amount,

RANK() OVER(
PARTITION BY Department
ORDER BY Amount DESC
) AS Department_Rank

FROM Sales;
```

---

# Step 3

## Running Revenue

```sql
SELECT
Month,
Amount,

SUM(Amount)
OVER(
ORDER BY Month
) AS Running_Revenue

FROM Sales;
```

---

# Step 4

## Previous Sale Comparison

```sql
SELECT

Employee,

Amount,

LAG(Amount)
OVER(
PARTITION BY Employee
ORDER BY Month
)

AS Previous_Sale

FROM Sales;
```

---

# Step 5

## Next Sale Prediction

```sql
SELECT

Employee,

Amount,

LEAD(Amount)
OVER(
PARTITION BY Employee
ORDER BY Month
)

AS Next_Sale

FROM Sales;
```

---

# Step 6

## Top Performer in Every Department

```sql
SELECT *

FROM(

SELECT

Employee,

Department,

Amount,

ROW_NUMBER()
OVER(

PARTITION BY Department
ORDER BY Amount DESC

)

AS Rank

FROM Sales

)t

WHERE Rank=1;
```

---

# Step 7

## Monthly Sales Difference

```sql
SELECT

Month,

Amount,

Amount -

LAG(Amount)

OVER(

ORDER BY Month

)

AS Difference

FROM Sales;
```

---

# Step 8

## Running Average

```sql
SELECT

Month,

Amount,

AVG(Amount)

OVER(

ORDER BY Month

)

AS Running_Average

FROM Sales;
```

---

# Step 9

## Highest Product Sale

```sql
SELECT

Product,

MAX(Amount)

OVER()

AS HighestSale

FROM Sales;
```

---

# Step 10

## Cumulative Sales

```sql
SELECT

Employee,

SUM(Amount)

OVER(

PARTITION BY Employee
ORDER BY Month

)

AS TotalSales

FROM Sales;
```

---

# 🏆 Mini Dashboard Reports

Create SQL queries for:

- Employee Ranking
- Product Ranking
- Monthly Growth
- Running Revenue
- Quarterly Revenue
- Best Product
- Worst Product
- Top 5 Customers
- Top Department
- Highest Monthly Sale

---

# 🎯 Hands-on Assignment

Using the Sales table, write SQL queries for:

### Easy

1. Rank employees by sales.
2. Find highest sale.
3. Find lowest sale.
4. Running total.
5. Running average.

---

### Medium

6. Compare current sale with previous.
7. Find next month's sale.
8. Department ranking.
9. Top employee in each department.
10. Bottom employee.

---

### Advanced

11. Monthly revenue growth.
12. Sales trend.
13. Top 3 products.
14. Customer segmentation.
15. Revenue leaderboard.

---

# 💼 Business Case Studies

## Case Study 1

### Amazon

Rank sellers by monthly revenue.

---

## Case Study 2

### Flipkart

Running sales report.

---

## Case Study 3

### Netflix

Rank movies by views.

---

## Case Study 4

### Uber

Top drivers by earnings.

---

## Case Study 5

### Swiggy

Restaurant ranking.

---

## Case Study 6

### Zomato

Monthly order growth.

---

## Case Study 7

### LinkedIn

Most active users.

---

## Case Study 8

### Google

Top searched keywords.

---

## Case Study 9

### Spotify

Top songs every month.

---

## Case Study 10

### Microsoft

Employee performance ranking.

---

# 💻 SQL Practice Questions

Solve these without looking at notes.

### Easy

- Find highest salary.
- Find second highest salary.
- Running total.
- Running average.
- Rank students.
- Rank employees.
- Department ranking.
- Product ranking.
- Count employees.
- Monthly revenue.

---

### Medium

- Previous order.
- Next order.
- Running balance.
- Highest product.
- Top customer.
- Revenue difference.
- Customer ranking.
- Dense ranking.
- Monthly growth.
- Sales comparison.

---

### Advanced

- Top 5 products.
- Revenue leaderboard.
- Department leaderboard.
- Product trend.
- Employee trend.
- Customer lifetime ranking.
- Quarterly comparison.
- Running profit.
- Inventory ranking.
- Business KPI dashboard.

---

# 📌 SQL Window Functions Cheat Sheet

## Ranking

```sql
ROW_NUMBER()
```

Unique ranking

---

```sql
RANK()
```

Ranking with gaps

---

```sql
DENSE_RANK()
```

Ranking without gaps

---

## Previous Value

```sql
LAG()
```

---

## Next Value

```sql
LEAD()
```

---

## First Value

```sql
FIRST_VALUE()
```

---

## Last Value

```sql
LAST_VALUE()
```

---

## Running Total

```sql
SUM()

OVER(
ORDER BY
)
```

---

## Running Average

```sql
AVG()

OVER(
ORDER BY
)
```

---

## Running Count

```sql
COUNT()

OVER(
ORDER BY
)
```

---

## Window Clause

```sql
OVER()
```

---

## Partition

```sql
PARTITION BY
```

Creates separate windows.

---

## Order

```sql
ORDER BY
```

Defines calculation order.

---

# 📚 Interview Tips

Always explain:

- Why Window Functions are better than GROUP BY.
- Difference between ROW_NUMBER(), RANK(), and DENSE_RANK().
- Real-world applications.
- Performance considerations.
- When to use PARTITION BY.
- Running total use cases.

---

# 📝 GitHub Assignment

Create a repository:

```text
SQL-Window-Functions/
│
├── README.md
├── sales_database.sql
├── employee_queries.sql
├── ranking_queries.sql
├── lag_lead_queries.sql
├── running_total.sql
├── dashboard_queries.sql
└── interview_questions.md
```

---

# 🏆 End of Day Challenge

Build a **Sales Analytics SQL Report** that includes:

- Employee Ranking
- Product Ranking
- Monthly Sales
- Running Revenue
- Previous Month Comparison
- Department Leaderboard
- Top Products
- Bottom Products
- Running Average
- Top 3 Customers

---

# 📖 Key Takeaways

✅ Window Functions analyze rows without collapsing data.

✅ `OVER()` defines the window.

✅ `PARTITION BY` creates groups.

✅ `ORDER BY` controls the sequence.

✅ Ranking functions help identify top performers.

✅ `LAG()` and `LEAD()` compare rows across time.

✅ Running totals and averages are essential for analytics dashboards.

---

# 🎯 Skills Gained

- SQL Analytics
- Business Reporting
- Ranking Techniques
- Running Totals
- Time-Series Analysis
- Dashboard Query Writing
- Interview-Level SQL
- Real-World Data Analysis

---

# 💡 GitHub Commit Message

```bash
git add .
git commit -m "Day 39: Mastered SQL Window Functions with analytics project, practice queries, and cheat sheet"
git push origin main
```

---

# 🚀 Next Day

## 📅 Day 40 – SQL Common Table Expressions (CTEs)

### Topics

- Introduction to CTEs
- Syntax
- Recursive CTEs
- Multiple CTEs
- CTE vs Subqueries
- Recursive Hierarchies
- Interview Questions
- Real-World Use Cases
- Hands-on Project

Happy Learning! 🚀