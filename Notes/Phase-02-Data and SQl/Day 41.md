# 📘 Day 41 – SQL Views

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand SQL Views
- Create and use Views
- Update Views
- Delete Views
- Learn Materialized Views
- Use Views for security and reporting

---

# 📌 What is a View?

A **View** is a **virtual table** created from one or more SQL queries.

It does **not store data** itself (except Materialized Views).

Think of a View as a **saved SQL query**.

---

# Why Use Views?

- Simplify complex queries
- Improve security
- Reuse SQL code
- Hide sensitive columns
- Create reporting dashboards

---

# Syntax

```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name;
```

---

# Example

```sql
CREATE VIEW EmployeeView AS
SELECT EmployeeID, Name, Salary
FROM Employees;
```

Retrieve data:

```sql
SELECT * FROM EmployeeView;
```

---

# Update a View

```sql
CREATE VIEW ITEmployees AS
SELECT *
FROM Employees
WHERE Department = 'IT';
```

```sql
UPDATE ITEmployees
SET Salary = 70000
WHERE EmployeeID = 1;
```

> Note: Updatable Views depend on your database and the complexity of the View.

---

# Replace a View

```sql
CREATE OR REPLACE VIEW EmployeeView AS
SELECT Name, Department
FROM Employees;
```

---

# Delete a View

```sql
DROP VIEW EmployeeView;
```

---

# Materialized View

Unlike a normal View, a **Materialized View stores data physically**.

### Advantages

- Faster queries
- Better for reporting
- Suitable for large datasets

---

# Real-World Use Cases

### Banking

Customer account summaries

---

### E-commerce

Top-selling products dashboard

---

### Hospital

Doctor schedule reports

---

### HR

Employee performance reports

---

### AI Projects

Create reusable datasets for Machine Learning pipelines.

---

# Interview Questions

### Beginner

**1. What is a View?**

A virtual table created from a SQL query.

---

**2. Does a View store data?**

No, except Materialized Views.

---

**3. Why use Views?**

To simplify queries, improve security, and reuse SQL.

---

**4. Can Views be updated?**

Some simple Views can be updated.

---

**5. Difference between Table and View?**

| Table | View |
|--------|------|
| Stores data | Virtual table |
| Occupies storage | Usually no storage |
| Faster writes | Faster for reusable queries |

---

### Intermediate

**6. What is a Materialized View?**

A View that stores query results physically.

---

**7. Difference between View and Materialized View?**

| View | Materialized View |
|------|-------------------|
| Virtual | Physical |
| Always current | Needs refresh |
| Less storage | Uses storage |

---

**8. Can a View join multiple tables?**

Yes.

---

**9. Why are Views used in dashboards?**

Because they simplify complex reporting queries.

---

**10. Can Views improve security?**

Yes, by exposing only required columns or rows.

---

# Practice Questions

1. Create a View for IT employees.
2. Create a View showing high salaries.
3. Display only employee names using a View.
4. Drop an existing View.
5. Create a View using two joined tables.
6. Create a sales report View.
7. Compare View vs Table.
8. Compare View vs CTE.
9. Create a department summary View.
10. Explain Materialized Views.

---

# Mini Project

## Employee Dashboard

Create Views for:

- IT Employees
- HR Employees
- High Salary Employees
- Department Summary
- Monthly Sales Report

---

# Best Practices

- Use meaningful View names.
- Avoid unnecessary nested Views.
- Use Views for reporting.
- Restrict sensitive data through Views.
- Refresh Materialized Views when needed.

---

# Cheat Sheet

## Create View

```sql
CREATE VIEW EmployeeView AS
SELECT *
FROM Employees;
```

---

## View Data

```sql
SELECT *
FROM EmployeeView;
```

---

## Replace View

```sql
CREATE OR REPLACE VIEW EmployeeView AS
SELECT Name, Salary
FROM Employees;
```

---

## Delete View

```sql
DROP VIEW EmployeeView;
```

---

# Skills Gained

- SQL Views
- Virtual Tables
- Materialized Views
- SQL Reporting
- Security using Views
- Reusable SQL Queries

---

# GitHub Assignment

Create a repository:

```text
SQL-Views/
│
├── README.md
├── create_views.sql
├── reporting_views.sql
├── materialized_views.sql
├── practice_queries.sql
└── interview_questions.md
```

---

# GitHub Commit

```bash
git add .
git commit -m "Day 41: Learned SQL Views and Materialized Views"
git push origin main
```

---

# 🚀 Next Day

## 📅 Day 42 – SQL Stored Procedures & Functions

### Topics

- Stored Procedures
- User Defined Functions (UDF)
- Parameters
- IN / OUT Parameters
- Advantages
- Real-world Use Cases
- Interview Questions

---

⭐ **Milestone:** You can now build reusable SQL reports and secure data access using Views, a common requirement in enterprise applications and analytics dashboards.