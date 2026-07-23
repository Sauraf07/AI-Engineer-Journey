# 📘 Day 40 – SQL Common Table Expressions (CTEs) (Part 1A.1)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what Common Table Expressions (CTEs) are
- Learn why CTEs are used in SQL
- Write your first CTE
- Understand the syntax of CTEs
- Use CTEs to simplify complex SQL queries
- Read and write professional SQL code
- Prepare for SQL interview questions on CTEs

---

# 📚 What is a Common Table Expression (CTE)?

A **Common Table Expression (CTE)** is a **temporary named result set** that exists only for the duration of a single SQL query.

Think of it as creating a temporary table that can be used immediately in the next SQL statement.

Unlike permanent tables, CTEs:

- Are not stored in the database
- Exist only during query execution
- Improve readability
- Help break complex queries into smaller parts

---

# 🧠 Real-Life Analogy

Imagine you are solving a difficult math problem.

Instead of solving everything in one step, you first calculate some intermediate values on rough paper and then use those values to get the final answer.

A CTE works exactly like that rough paper.

Instead of writing one huge SQL query, you divide it into smaller, understandable steps.

---

# ❓ Why Do We Need CTEs?

Suppose you want to find employees whose salary is higher than the company average.

Without CTE:

```sql
SELECT *
FROM Employees
WHERE Salary >
(
SELECT AVG(Salary)
FROM Employees
);
```

This works.

But imagine the query contains:

- Multiple joins
- Multiple subqueries
- Aggregate functions
- Window functions

The query quickly becomes difficult to understand.

Using CTE:

```sql
WITH AverageSalary AS
(
SELECT AVG(Salary) AS AvgSalary
FROM Employees
)

SELECT *

FROM Employees, AverageSalary

WHERE Salary > AvgSalary;
```

Much cleaner.

Much easier to read.

---

# 🚀 Advantages of CTEs

✅ Improves readability

✅ Makes debugging easier

✅ Reduces repeated code

✅ Easier maintenance

✅ Better organization

✅ Works well with Window Functions

✅ Supports Recursive Queries

---

# ❌ Limitations

- Exists only during query execution
- Cannot create indexes
- Cannot be reused in another query
- Large recursive CTEs may affect performance

---

# 📌 Basic Syntax

```sql
WITH CTE_Name AS
(
    SELECT ...
)

SELECT *
FROM CTE_Name;
```

---

# Syntax Breakdown

```sql
WITH
```

Starts a Common Table Expression.

---

```sql
CTE_Name
```

Temporary name.

---

```sql
AS
```

Defines the CTE.

---

```sql
(
SELECT ...
)
```

Contains the query.

---

```sql
SELECT *
FROM CTE_Name;
```

Uses the temporary result.

---

# Sample Database

## Employees Table

| EmployeeID | Name | Department | Salary |
|------------|------|------------|---------|
|1|John|IT|60000|
|2|Alice|HR|45000|
|3|Bob|IT|70000|
|4|Emma|Finance|80000|
|5|David|HR|50000|
|6|Sophia|Finance|90000|
|7|Chris|IT|75000|
|8|Olivia|Marketing|65000|

---

# Example 1

## Basic CTE

```sql
WITH EmployeeList AS
(
SELECT *

FROM Employees
)

SELECT *

FROM EmployeeList;
```

Output

Same as Employees table.

---

# Example 2

## Selecting Specific Columns

```sql
WITH EmployeeInfo AS
(
SELECT

Name,
Salary

FROM Employees
)

SELECT *

FROM EmployeeInfo;
```

Output

| Name | Salary |
|------|---------|
|John|60000|
|Alice|45000|
|Bob|70000|

...

---

# Example 3

## Filtering Records

```sql
WITH HighSalary AS
(
SELECT *

FROM Employees

WHERE Salary > 60000
)

SELECT *

FROM HighSalary;
```

Output

Only employees earning more than ₹60,000.

---

# Example 4

## Using Calculated Columns

```sql
WITH BonusCalculation AS
(
SELECT

Name,

Salary,

Salary * 0.10 AS Bonus

FROM Employees
)

SELECT *

FROM BonusCalculation;
```

Output

| Name | Salary | Bonus |
|------|---------|--------|
|John|60000|6000|

---

# Example 5

## Average Salary

```sql
WITH AverageSalary AS
(
SELECT

AVG(Salary)

AS AvgSalary

FROM Employees
)

SELECT *

FROM AverageSalary;
```

Output

| AvgSalary |
|-----------|
|66875|

---

# Example 6

## Employees Above Average Salary

```sql
WITH AverageSalary AS
(
SELECT

AVG(Salary)

AS AvgSalary

FROM Employees
)

SELECT

Name,
Salary

FROM Employees,
AverageSalary

WHERE Salary > AvgSalary;
```

Output

Employees whose salary is above company average.

---

# CTE Execution Flow

```text
Step 1

WITH EmployeeCTE

↓

Step 2

Execute Query Inside CTE

↓

Step 3

Store Result Temporarily

↓

Step 4

Main Query Uses CTE

↓

Step 5

CTE Deleted Automatically
```

---

# Real-World Use Cases

## Banking

Calculate customers whose balance is above average.

---

## E-Commerce

Find products whose sales exceed average sales.

---

## HR

Employees earning above department average.

---

## Healthcare

Patients with more visits than average.

---

## Education

Students scoring above class average.

---

## Finance

Highest monthly revenue.

---

## Social Media

Most active users.

---

# Best Practices

✅ Give meaningful CTE names

Good

```sql
WITH HighSalaryEmployees AS
```

Bad

```sql
WITH Temp1 AS
```

---

Keep each CTE focused on one task.

---

Write readable SQL.

---

Avoid unnecessary nesting.

---

Comment complex CTEs.

---

# Common Mistakes

❌ Forgetting `WITH`

Wrong

```sql
EmployeeCTE AS
(
SELECT *
FROM Employees
)
```

Correct

```sql
WITH EmployeeCTE AS
(
SELECT *
FROM Employees
)
```

---

❌ Missing parentheses

Wrong

```sql
WITH EmployeeCTE AS

SELECT *
FROM Employees;
```

Correct

```sql
WITH EmployeeCTE AS
(
SELECT *
FROM Employees
)
```

---

❌ Using CTE outside its query

Wrong

```sql
SELECT *

FROM EmployeeCTE;
```

A CTE only exists for the query in which it is defined.

---

# Practice Exercises

## Easy

1. Create a CTE containing all employees.

2. Display only employee names.

3. Show employees earning above ₹50,000.

4. Find average salary.

5. Find maximum salary.

---

## Medium

6. Employees below average salary.

7. Employees in IT department.

8. Employees in Finance department.

9. Employees with salary between ₹60,000–₹80,000.

10. Create a CTE with calculated bonus.

---

# Interview Questions

## Beginner

### 1. What is a CTE?

A temporary named result set that exists only during query execution.

---

### 2. Why are CTEs used?

To simplify complex SQL queries and improve readability.

---

### 3. Is a CTE a permanent table?

No.

---

### 4. Which keyword starts a CTE?

```sql
WITH
```

---

### 5. Can a CTE be reused in another query?

No.

---

### 6. Does a CTE improve readability?

Yes.

---

### 7. Can CTEs contain joins?

Yes.

---

### 8. Can aggregate functions be used inside a CTE?

Yes.

---

### 9. Can a CTE be nested?

Yes, but keep it readable.

---

### 10. What is the biggest advantage of CTEs?

Breaking large queries into smaller, understandable parts.

---

# Mini Assignment

Using the Employees table:

- Create a CTE for IT employees.
- Find employees earning above average salary.
- Calculate a 15% bonus using a CTE.
- Display employees in Finance.
- Find the employee with the highest salary.

---

# Day 40 Progress

✅ What is a CTE

✅ Why CTEs Matter

✅ CTE Syntax

✅ Basic Examples

✅ Sample Database

✅ Best Practices

✅ Common Mistakes

✅ Practice Questions

✅ Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 40: Learned SQL Common Table Expressions (CTEs) fundamentals"
git push origin main
```

---

# 🚀 Next Part

**📙 Day 40 – Part 1A.2**

Topics:

- Multiple CTEs
- CTE vs Subqueries
- CTE with Joins
- Advanced Practice Queries
- Intermediate Interview Questions
- Hands-on Assignments
- Real-World Business Scenarios

# 📘 Day 40 – SQL Common Table Expressions (CTEs) – Part 1A.2

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer  
> **Topic:** Multiple CTEs, CTE vs Subqueries, Practice Queries & Interview Questions

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Write multiple CTEs in a single query
- Chain CTEs together
- Understand the difference between CTEs and Subqueries
- Write cleaner and more readable SQL
- Solve interview-level SQL problems
- Apply CTEs to real-world business scenarios

---

# 🔄 Multiple CTEs

SQL allows multiple CTEs separated by commas.

## Syntax

```sql
WITH
CTE1 AS
(
    SELECT ...
),

CTE2 AS
(
    SELECT ...
)

SELECT *
FROM CTE1
JOIN CTE2
ON ...
```

---

# Example Database

## Employees

| EmployeeID | Name | Department | Salary |
|------------|------|------------|--------|
|101|John|IT|75000|
|102|Alice|HR|55000|
|103|Bob|IT|90000|
|104|Emma|Finance|70000|
|105|David|IT|80000|

---

## Departments

| Department | Manager |
|------------|---------|
|IT|Michael|
|HR|Sophia|
|Finance|James|

---

# Example 1

Find employees along with department managers.

```sql
WITH EmployeeData AS
(
    SELECT *
    FROM Employees
),

DepartmentData AS
(
    SELECT *
    FROM Departments
)

SELECT
e.Name,
e.Department,
d.Manager

FROM EmployeeData e
JOIN DepartmentData d

ON e.Department = d.Department;
```

---

# Example 2

Average Salary of Every Department

```sql
WITH AvgSalary AS
(
SELECT

Department,

AVG(Salary) AS AverageSalary

FROM Employees

GROUP BY Department
)

SELECT *

FROM AvgSalary;
```

---

# Example 3

Employees Above Department Average

```sql
WITH AvgSalary AS
(
SELECT

Department,

AVG(Salary) AvgSalary

FROM Employees

GROUP BY Department
)

SELECT

e.Name,
e.Department,
e.Salary

FROM Employees e

JOIN AvgSalary a

ON e.Department = a.Department

WHERE e.Salary > a.AvgSalary;
```

---

# Example 4

Highest Salary Employee

```sql
WITH HighestSalary AS
(
SELECT

MAX(Salary) AS Highest

FROM Employees
)

SELECT *

FROM Employees

WHERE Salary =

(
SELECT Highest

FROM HighestSalary
);
```

---

# Example 5

Lowest Salary Employee

```sql
WITH LowestSalary AS
(
SELECT

MIN(Salary) Lowest

FROM Employees
)

SELECT *

FROM Employees

WHERE Salary =

(
SELECT Lowest

FROM LowestSalary
);
```

---

# Chaining Multiple CTEs

CTEs can reference previous CTEs.

```sql
WITH

EmployeeSalary AS
(
SELECT *

FROM Employees
),

HighSalary AS
(
SELECT *

FROM EmployeeSalary

WHERE Salary > 70000
)

SELECT *

FROM HighSalary;
```

---

# Real World Example

Suppose Amazon wants:

Step 1

Find department average salary.

Step 2

Compare every employee.

Step 3

Generate report.

Instead of writing nested queries, CTEs make it simple.

---

# CTE vs Subquery

## Subquery

```sql
SELECT *

FROM Employees

WHERE Salary >

(

SELECT AVG(Salary)

FROM Employees

);
```

---

## Same using CTE

```sql
WITH AverageSalary AS
(
SELECT

AVG(Salary)

AS AvgSalary

FROM Employees
)

SELECT *

FROM Employees

WHERE Salary >

(
SELECT AvgSalary

FROM AverageSalary
);
```

---

# Difference

| CTE | Subquery |
|------|----------|
| Easier to read | Harder to read |
| Reusable | Repeated logic |
| Better for complex queries | Better for small queries |
| Supports recursion | No recursion |
| Improves maintainability | Difficult to maintain |

---

# When Should You Use CTE?

✅ Complex SQL

✅ Recursive queries

✅ Multiple calculations

✅ Reporting

✅ Analytics

✅ Data cleaning

---

# When Should You Use Subqueries?

✅ Small queries

✅ Simple filtering

✅ Single calculations

---

# Business Use Cases

## Amazon

Generate sales reports.

---

## Netflix

Top watched shows.

---

## Swiggy

Restaurant ranking.

---

## Uber

Driver performance.

---

## Google

Search analytics.

---

## Spotify

Trending songs.

---

## LinkedIn

Employee analytics.

---

## Microsoft

Department reports.

---

# Practice Queries

## Easy

### 1

Find average salary.

```sql
WITH AvgSalary AS
(
SELECT AVG(Salary) AS AvgSalary

FROM Employees
)

SELECT *

FROM AvgSalary;
```

---

### 2

Find highest salary.

```sql
WITH HighestSalary AS
(
SELECT

MAX(Salary)

Highest

FROM Employees
)

SELECT *

FROM HighestSalary;
```

---

### 3

Find lowest salary.

---

### 4

Find employee count.

---

### 5

Find department count.

---

# Intermediate Queries

6. Employees above average salary.

7. Employees below average salary.

8. Highest salary department.

9. Lowest salary department.

10. Department wise salary.

11. Employees earning more than manager average.

12. Department report.

13. Monthly report.

14. Salary statistics.

15. Company report.

---

# Assignment

Using Employees table:

Write queries for:

- Average salary
- Highest salary
- Lowest salary
- Department average
- Employees above department average
- Employee ranking
- Salary report
- Employee summary

---

# Mini Challenge

Create one SQL report showing:

- Employee Name
- Department
- Salary
- Department Average
- Difference from Average

---

# Interview Questions

## Beginner

### 1. What is a CTE?

A Common Table Expression (CTE) is a temporary named result set that can be referenced within a SQL query.

---

### 2. Why use a CTE?

To improve readability, maintainability, and simplify complex SQL queries.

---

### 3. What keyword starts a CTE?

```sql
WITH
```

---

### 4. Can multiple CTEs exist?

Yes.

---

### 5. Can one CTE use another?

Yes.

---

### 6. Is a CTE stored permanently?

No.

---

### 7. Difference between CTE and View?

A CTE exists only during query execution, while a View is stored in the database.

---

### 8. Difference between CTE and Temporary Table?

CTEs are temporary within a query, whereas temporary tables exist until the session ends or they are dropped.

---

### 9. Can CTE improve readability?

Yes.

---

### 10. Can CTE replace subqueries?

In many cases, yes.

---

# Intermediate Interview Questions

### 11. CTE vs Subquery?

CTEs are more readable and reusable.

---

### 12. Why do companies prefer CTEs?

They simplify large analytical queries and improve maintainability.

---

### 13. Can CTE contain JOIN?

Yes.

---

### 14. Can CTE contain GROUP BY?

Yes.

---

### 15. Can CTE contain Window Functions?

Yes.

---

# Best Practices

✅ Give meaningful CTE names.

✅ Keep each CTE focused on one task.

✅ Avoid unnecessary nested CTEs.

✅ Use comments in large queries.

✅ Prefer CTEs over deeply nested subqueries for readability.

---

# Common Mistakes

❌ Forgetting the `WITH` keyword.

❌ Missing commas between multiple CTEs.

❌ Using duplicate CTE names.

❌ Referencing a CTE before it is defined.

❌ Writing extremely long CTE chains when a simpler query would suffice.

---

# Day Summary

Today you learned:

- Multiple CTEs
- Chaining CTEs
- CTE vs Subqueries
- Business Applications
- Practice Queries
- Interview Questions
- Best Practices
- Common Mistakes

---

# 📝 GitHub Commit Message

```bash
git add .
git commit -m "Day 40: Learned Multiple CTEs, CTE vs Subqueries, and SQL reporting queries"
git push origin main
```

---

# 🚀 Next Lesson

## 📘 Day 40 – Part 1B

Topics:

- CTE with JOIN
- CTE with Aggregate Functions
- CTE with Window Functions
- Nested CTEs
- Performance Considerations
- Real-World Business Scenarios
- Mini Project
- Advanced Practice Queries

# 📘 Day 40 – SQL Common Table Expressions (CTEs) – Part 1B

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Use CTEs with JOIN operations
* Use CTEs with Aggregate Functions
* Combine CTEs with Window Functions
* Write Multiple CTEs in a single query
* Understand Nested CTE concepts
* Improve query readability
* Apply CTEs to real-world business scenarios

---

# 📖 What You Learned in Part 1A

* What is a CTE?
* CTE Syntax
* Basic CTE Examples
* CTE vs Subquery
* Multiple Basic Queries

Now we'll move to advanced usage.

---

# 🔗 CTE with JOIN

CTEs can simplify complex JOIN queries.

## Employees Table

| EmployeeID | Name  | DepartmentID | Salary |
| ---------- | ----- | ------------ | ------ |
| 1          | John  | 1            | 50000  |
| 2          | Alice | 2            | 70000  |
| 3          | Bob   | 1            | 65000  |

---

## Departments Table

| DepartmentID | Department |
| ------------ | ---------- |
| 1            | IT         |
| 2            | HR         |

---

### Query

```sql
WITH EmployeeData AS
(
    SELECT
        EmployeeID,
        Name,
        DepartmentID,
        Salary
    FROM Employees
)

SELECT
    e.Name,
    d.Department,
    e.Salary

FROM EmployeeData e

JOIN Departments d
ON e.DepartmentID = d.DepartmentID;
```

### Output

| Name  | Department | Salary |
| ----- | ---------- | ------ |
| John  | IT         | 50000  |
| Alice | HR         | 70000  |
| Bob   | IT         | 65000  |

---

# 📊 CTE with Aggregate Functions

Aggregate calculations become easier to read.

```sql
WITH DepartmentSalary AS
(
    SELECT
        DepartmentID,
        AVG(Salary) AS AverageSalary
    FROM Employees
    GROUP BY DepartmentID
)

SELECT *
FROM DepartmentSalary;
```

Output

| DepartmentID | AverageSalary |
| ------------ | ------------- |
| 1            | 57500         |
| 2            | 70000         |

---

# 📈 CTE with Multiple Aggregates

```sql
WITH DepartmentStats AS
(
SELECT

DepartmentID,

COUNT(*) AS TotalEmployees,

SUM(Salary) AS TotalSalary,

AVG(Salary) AS AverageSalary,

MIN(Salary) AS LowestSalary,

MAX(Salary) AS HighestSalary

FROM Employees

GROUP BY DepartmentID
)

SELECT *

FROM DepartmentStats;
```

---

# 🚀 CTE with Window Functions

Window Functions work beautifully inside CTEs.

```sql
WITH EmployeeRank AS
(
SELECT

Name,

DepartmentID,

Salary,

ROW_NUMBER()

OVER(

PARTITION BY DepartmentID
ORDER BY Salary DESC

)

AS Rank

FROM Employees
)

SELECT *

FROM EmployeeRank;
```

Output

| Name  | DepartmentID | Salary | Rank |
| ----- | ------------ | ------ | ---- |
| Bob   | 1            | 65000  | 1    |
| John  | 1            | 50000  | 2    |
| Alice | 2            | 70000  | 1    |

---

# 📌 Why Combine CTEs with Window Functions?

Benefits:

* Better readability
* Easier debugging
* Reusable logic
* Cleaner reports

---

# 🧩 Multiple CTEs

You can define multiple CTEs separated by commas.

```sql
WITH

DepartmentSalary AS
(
SELECT

DepartmentID,

AVG(Salary) AverageSalary

FROM Employees

GROUP BY DepartmentID
),

HighSalary AS
(
SELECT *

FROM Employees

WHERE Salary > 60000
)

SELECT

h.Name,

d.AverageSalary

FROM HighSalary h

JOIN DepartmentSalary d

ON h.DepartmentID=d.DepartmentID;
```

---

# 🪆 Nested CTE Concept

A CTE can reference another CTE defined before it.

```sql
WITH

SalaryData AS
(
SELECT *

FROM Employees
),

HighSalary AS
(
SELECT *

FROM SalaryData

WHERE Salary>60000
)

SELECT *

FROM HighSalary;
```

---

# 💼 Real-World Business Example

## HR Dashboard

Goal:

Generate a report showing:

* Department Name
* Average Salary
* Highest Salary
* Employee Ranking

Solution:

Use

* CTE
* Aggregate Functions
* Window Functions
* JOIN

This produces one clean and maintainable query.

---

# 🏢 Business Use Cases

## Amazon

Average salary by department.

---

## Netflix

Rank movies by rating.

---

## Google

Top searched keywords.

---

## Swiggy

Top restaurants by monthly revenue.

---

## Uber

Driver earnings leaderboard.

---

## Spotify

Top songs by monthly plays.

---

## LinkedIn

Most active creators.

---

# ⚠️ Common Mistakes

### 1. Forgetting WITH

❌

```sql
EmployeeData AS (...)
```

✅

```sql
WITH EmployeeData AS (...)
```

---

### 2. Forgetting Parentheses

Wrong

```sql
WITH EmployeeData AS
SELECT *
FROM Employees;
```

Correct

```sql
WITH EmployeeData AS
(
SELECT *
FROM Employees
)
```

---

### 3. Referencing Undefined CTE

Always define CTEs before using them.

---

### 4. Infinite Recursive Logic

Recursive CTEs must have a stopping condition.

---

# ⚡ Performance Tips

✅ Select only required columns.

✅ Filter rows as early as possible.

✅ Avoid unnecessary nested CTEs.

✅ Index JOIN columns.

✅ Use CTEs for readability—not as a replacement for every subquery.

---

# 🛠️ Mini Project

## Employee Analytics Report

Create a report containing:

* Employee Name
* Department
* Salary
* Department Average Salary
* Department Rank
* Highest Salary
* Lowest Salary

Use:

* CTE
* JOIN
* Aggregate Functions
* ROW_NUMBER()

---

# 📝 Hands-on Assignment

Using the Employees table, write SQL queries to:

1. Display average salary by department.
2. Display total employees in each department.
3. Rank employees by salary.
4. Show employees earning above department average.
5. Display highest-paid employee in each department.
6. Display lowest-paid employee in each department.
7. Show department salary statistics.
8. Combine two CTEs in one query.
9. Join a CTE with another table.
10. Create an employee analytics report.

---

# 🎤 Interview Questions

## Beginner

### 1. Can a CTE contain JOIN?

Yes.

---

### 2. Can a CTE use Aggregate Functions?

Yes.

---

### 3. Can multiple CTEs exist in one query?

Yes.

---

### 4. Can a CTE contain Window Functions?

Yes.

---

### 5. Is a CTE stored permanently?

No.

---

## Intermediate

### 6. Why are CTEs preferred over deeply nested subqueries?

Because they improve readability and maintainability.

---

### 7. Can one CTE reference another?

Yes, if it is defined earlier.

---

### 8. Are CTEs faster than subqueries?

Not always. Performance depends on the database optimizer and query design.

---

### 9. What is the biggest advantage of CTEs?

Cleaner and more modular SQL queries.

---

### 10. Where are CTEs commonly used?

Reporting systems, dashboards, analytics, ETL pipelines, and business intelligence.

---

# 📚 Best Practices

* Give meaningful CTE names.
* Keep each CTE focused on one task.
* Avoid unnecessary nesting.
* Add comments for complex logic.
* Test each CTE individually before combining them.

---

# 📖 Day 40 Part 1B Summary

Today you learned:

* ✅ CTE with JOIN
* ✅ CTE with Aggregate Functions
* ✅ CTE with Window Functions
* ✅ Multiple CTEs
* ✅ Nested CTE Concept
* ✅ Performance Tips
* ✅ Real-world Business Examples
* ✅ Interview Questions
* ✅ Mini Project

---

# 💻 GitHub Commit Message

```bash
git add .
git commit -m "Day 40 Part 1B: Advanced SQL CTEs with JOIN, Aggregates, Window Functions, and Business Use Cases"
git push origin main
```

---

# 🚀 Next Part

**Day 40 – Part 2**

Topics:

* Recursive CTEs
* Hierarchical Data
* Organizational Charts
* Tree Structures
* Recursive Query Examples
* Performance Optimization
* Advanced Business Scenarios

# 📗 Day 40 – SQL Common Table Expressions (CTEs) | Part 2A

> **Phase 2: Data & SQL**  
> **Topic:** Advanced CTEs (Recursive CTEs)

---

# 🎯 Learning Objectives

After completing this lesson, you will be able to:

- Understand Recursive CTEs
- Work with hierarchical data
- Generate sequences using SQL
- Solve interview questions on Recursive CTEs

---

# 📌 What is a Recursive CTE?

A **Recursive CTE** is a CTE that refers to itself.

It is mainly used for:

- Organizational hierarchy
- Category hierarchy
- Folder structure
- Family tree
- Bill of Materials (BOM)
- Generating numbers or dates

---

# 📖 Syntax

```sql
WITH RECURSIVE cte_name AS (

    -- Anchor Query
    SELECT ...

    UNION ALL

    -- Recursive Query
    SELECT ...
    FROM cte_name
)

SELECT * FROM cte_name;
```

---

# 🔹 Anchor Query

The starting point of recursion.

```sql
SELECT 1 AS Number
```

---

# 🔹 Recursive Query

Keeps generating rows until the condition becomes false.

```sql
SELECT Number + 1
FROM Numbers
WHERE Number < 10;
```

---

# Example 1 – Generate Numbers 1 to 10

```sql
WITH RECURSIVE Numbers AS (

SELECT 1 AS Number

UNION ALL

SELECT Number + 1

FROM Numbers

WHERE Number < 10

)

SELECT * FROM Numbers;
```

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

---

# Example 2 – Employee Hierarchy

Employee Table

| EmployeeID | Name | ManagerID |
|------------|------|-----------|
|1|CEO|NULL|
|2|Alice|1|
|3|Bob|1|
|4|David|2|
|5|Emma|2|

Query

```sql
WITH RECURSIVE EmployeeHierarchy AS (

SELECT
EmployeeID,
Name,
ManagerID

FROM Employees

WHERE ManagerID IS NULL

UNION ALL

SELECT
e.EmployeeID,
e.Name,
e.ManagerID

FROM Employees e

JOIN EmployeeHierarchy h

ON e.ManagerID = h.EmployeeID

)

SELECT * FROM EmployeeHierarchy;
```

---

# Example 3 – Category Hierarchy

```sql
WITH RECURSIVE Categories AS (

SELECT *

FROM Category

WHERE ParentID IS NULL

UNION ALL

SELECT c.*

FROM Category c

JOIN Categories p

ON c.ParentID = p.CategoryID

)

SELECT * FROM Categories;
```

---

# Real-World Uses

- Company organization chart
- Product categories
- Folder navigation
- Family tree
- Reporting hierarchy

---

# Performance Tips

- Always use a stopping condition.
- Avoid infinite recursion.
- Keep recursion depth small.
- Index ParentID columns.

---

# Common Mistakes

❌ Missing `UNION ALL`

❌ No stopping condition

❌ Wrong JOIN condition

❌ Recursive query returns duplicate rows

---

# Interview Questions

### 1. What is a Recursive CTE?

A CTE that references itself until a stopping condition is met.

---

### 2. Difference between CTE and Recursive CTE?

| CTE | Recursive CTE |
|------|---------------|
| Runs once | Runs repeatedly |
| Simple query | Hierarchical query |

---

### 3. When do we use Recursive CTE?

- Hierarchical data
- Tree structures
- Number generation

---

### 4. What are the two parts of a Recursive CTE?

- Anchor Query
- Recursive Query

---

### 5. Why is a stopping condition important?

To prevent infinite recursion.

---

# Practice Questions

1. Generate numbers from 1 to 20.
2. Generate dates for one month.
3. Display employee hierarchy.
4. Display product category tree.
5. Create folder hierarchy.

---

# 📝 Summary

✅ Recursive CTE references itself.

✅ It contains:
- Anchor Query
- Recursive Query

✅ Best used for:
- Hierarchies
- Trees
- Recursive data
- Sequence generation

---

# 🚀 Next

**Part 2B**

- Multiple CTEs
- CTE + JOIN
- CTE + Window Functions
- Business Case Studies
- Performance Optimization

# 📘 Day 40 - SQL Common Table Expressions (CTEs) - Part 2B

> **Phase 2: Data & SQL**  
> **Topic:** Advanced CTE Applications

---

# 🎯 Learning Objectives

- Use Multiple CTEs
- Combine CTEs with JOIN
- Use CTEs with Window Functions
- Generate Reports using CTEs
- Solve Interview-Level SQL Problems

---

# 📌 Multiple CTEs

You can define multiple CTEs in a single query.

```sql
WITH EmployeeCount AS (
    SELECT Department,
           COUNT(*) AS TotalEmployees
    FROM Employees
    GROUP BY Department
),
DepartmentSalary AS (
    SELECT Department,
           AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY Department
)

SELECT
e.Department,
e.TotalEmployees,
d.AvgSalary

FROM EmployeeCount e
JOIN DepartmentSalary d
ON e.Department = d.Department;
```

---

# 📌 CTE with JOIN

```sql
WITH HighSalary AS (

SELECT *
FROM Employees
WHERE Salary > 60000

)

SELECT

e.Name,
d.DepartmentName

FROM HighSalary e
JOIN Departments d

ON e.DepartmentID = d.DepartmentID;
```

---

# 📌 CTE with Window Functions

```sql
WITH RankedEmployee AS (

SELECT

Name,
Department,
Salary,

RANK() OVER(
PARTITION BY Department
ORDER BY Salary DESC
) AS Rank

FROM Employees

)

SELECT *

FROM RankedEmployee

WHERE Rank <=3;
```

---

# 📌 Sales Report Example

```sql
WITH MonthlySales AS (

SELECT

Month,
SUM(Amount) AS Revenue

FROM Sales

GROUP BY Month

)

SELECT *

FROM MonthlySales;
```

---

# 📌 Business Use Cases

- Sales Dashboard
- Employee Ranking
- Revenue Reports
- Financial Reports
- HR Analytics
- Inventory Reports
- Customer Analytics
- KPI Dashboards

---

# 📌 Best Practices

✅ Keep CTE names meaningful

✅ Use CTEs to improve readability

✅ Avoid deeply nested CTEs

✅ Use indexes on joined columns

✅ Filter data as early as possible

---

# ⚠️ Common Mistakes

❌ Forgetting `WITH`

❌ Missing commas between CTEs

❌ Infinite recursion

❌ Using CTE when a simple query is enough

---

# 💼 Interview Questions

### Beginner

1. What is a CTE?
2. Why use CTE instead of subqueries?
3. Can multiple CTEs be used?
4. Can CTE be joined?
5. Difference between CTE and View?

### Intermediate

6. What is a Recursive CTE?
7. Can Window Functions be used inside a CTE?
8. Is a CTE stored permanently?
9. Can CTE improve readability?
10. When should you avoid using a CTE?

---

# 📝 Practice Questions

1. Find Top 3 employees using CTE.
2. Find department-wise average salary.
3. Generate monthly sales report.
4. Combine two CTEs.
5. Use CTE with JOIN.

---

# 🚀 Mini Assignment

Create queries for:

- Employee Ranking
- Sales Dashboard
- Department Salary Report
- Customer Revenue Report
- Top Selling Products

---

# 🎯 Summary

Today you learned:

- Multiple CTEs
- CTE with JOIN
- CTE with Window Functions
- Reporting using CTEs
- Business Applications
- Best Practices
- Interview Questions

---

# 💻 Git Commit

```bash
git add .
git commit -m "Day 40: Advanced SQL CTE Applications"
git push origin main
```

---

# 📅 Next Day

**Day 41 – SQL Views & Materialized Views**

# 📘 Day 40 – SQL Common Table Expressions (CTEs) | Part 3

> **Phase 2: Data & SQL**  
> **Topic:** Interview Questions, Project & Cheat Sheet

---

# 🎯 Mini Project

## Employee Management System

Create reports for:

- Highest Paid Employee
- Department-wise Salary
- Top 3 Employees
- Salary Ranking
- Employee Hierarchy

### Sample Query

```sql
WITH DepartmentSalary AS (
    SELECT Department,
           AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY Department
)
SELECT *
FROM DepartmentSalary
WHERE AvgSalary > 50000;
```

---

# 💼 Practice Questions

1. Find employees earning above department average.
2. Find top 3 salaries.
3. Calculate average salary by department.
4. Find duplicate records using CTE.
5. Use recursive CTE to display employee hierarchy.
6. Compare CTE and Subquery.
7. Find highest salary in each department.
8. Calculate running total using CTE.
9. Display monthly sales report.
10. Rank employees using CTE + Window Function.

---

# 🎤 Interview Questions

### Beginner

**1. What is a CTE?**

A temporary named result set used within a SQL query.

---

**2. Why use a CTE?**

To improve query readability and simplify complex SQL.

---

**3. What does WITH keyword do?**

It creates a Common Table Expression.

---

**4. Can multiple CTEs be used?**

Yes.

---

**5. Does a CTE store data permanently?**

No.

---

### Intermediate

**6. Difference between CTE and Subquery?**

| CTE | Subquery |
|------|----------|
| More readable | Harder to read |
| Can be reused | Cannot be reused |
| Supports recursion | Usually doesn't |

---

**7. What is Recursive CTE?**

A CTE that references itself to process hierarchical or recursive data.

---

**8. Where are Recursive CTEs used?**

- Organization hierarchy
- Folder structures
- Category trees
- Family trees

---

**9. Can Window Functions be used with CTEs?**

Yes.

---

**10. Is CTE faster than Subquery?**

Not always. Performance depends on the query and database optimizer.

---

# 📌 Best Practices

- Use meaningful CTE names.
- Avoid unnecessary nested CTEs.
- Use recursive CTEs only when required.
- Combine CTEs with Window Functions for analytics.
- Keep queries simple and readable.

---

# 📝 Cheat Sheet

## Basic CTE

```sql
WITH EmployeeData AS (
    SELECT *
    FROM Employees
)
SELECT *
FROM EmployeeData;
```

---

## Multiple CTEs

```sql
WITH CTE1 AS (...),
CTE2 AS (...)
SELECT *
FROM CTE2;
```

---

## Recursive CTE

```sql
WITH RECURSIVE EmployeeTree AS (
    SELECT EmployeeID, ManagerID
    FROM Employees
)
SELECT *
FROM EmployeeTree;
```

---

# 🎯 Assignment

Build SQL queries for:

- Employee Hierarchy
- Department Salary Report
- Sales Summary
- Top Customers
- Monthly Revenue Report

---

# 🏆 Skills Gained

- Common Table Expressions (CTEs)
- Recursive CTEs
- SQL Optimization
- Business Reporting
- Advanced Query Writing

---

# 💡 GitHub Commit

```bash
git add .
git commit -m "Day 40: Learned SQL Common Table Expressions (CTEs)"
git push origin main
```

---

# 📅 Next Day

## Day 41 – SQL Views

### Topics

- CREATE VIEW
- ALTER VIEW
- DROP VIEW
- Updatable Views
- Materialized Views
- Security Benefits
- Real-world Use Cases

---

⭐ **Milestone:** You can now write cleaner, reusable, and interview-ready SQL queries using CTEs.

