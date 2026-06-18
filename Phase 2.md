# 🚀 Phase 2: Data & SQL Roadmap (30 Days)
## AI/ML Engineer Roadmap - Phase 2

> Goal: Master SQL, Databases, Data Analysis, NumPy, Pandas, and Data Visualization.
>
> By the end of this phase, you should be able to:
>
> ✅ Write complex SQL queries  
> ✅ Design databases  
> ✅ Clean and analyze datasets  
> ✅ Perform Exploratory Data Analysis (EDA)  
> ✅ Use NumPy and Pandas professionally  
> ✅ Create insightful visualizations  
> ✅ Build data-driven projects  
> ✅ Become ready for Machine Learning Phase

---

# 📅 Phase Duration

- Duration: 30 Days
- Study Time: 4-6 Hours Daily
- Projects: 6
- SQL Problems: 150+
- Data Analysis Exercises: 50+

---

# 🗓️ Week 1: SQL Foundations

## Day 1 - Introduction to Databases

### Topics

- What is a Database?
- DBMS vs RDBMS
- SQL Introduction
- MySQL Installation
- MySQL Workbench Setup

### Learning Objectives

- Understand database fundamentals
- Install and configure MySQL

### Practice

Create Database:

```sql
CREATE DATABASE company;
```

Create Table:

```sql
CREATE TABLE employees(
id INT PRIMARY KEY,
name VARCHAR(100),
salary DECIMAL(10,2)
);
```

### Assignment

Create:

- School Database
- Employee Database

---

# Day 2 - SQL Basics

## Topics

- SELECT
- WHERE
- ORDER BY
- LIMIT

### Practice

```sql
SELECT * FROM employees;

SELECT * FROM employees
WHERE salary > 50000;

SELECT * FROM employees
ORDER BY salary DESC;
```

### Assignment

Solve 20 SQL Queries

---

# Day 3 - Filtering Data

## Topics

- AND
- OR
- NOT
- BETWEEN
- IN
- LIKE

### Practice

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 30000 AND 70000;
```

### Assignment

15 Query Challenges

---

# Day 4 - Aggregate Functions

## Topics

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

### Practice

```sql
SELECT AVG(salary)
FROM employees;
```

### Assignment

Analyze employee salary data

---

# Day 5 - GROUP BY

## Topics

- GROUP BY
- HAVING

### Practice

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department;
```

### Assignment

Department Salary Report

---

# Day 6 - Joins Part 1

## Topics

- INNER JOIN
- LEFT JOIN

### Practice

```sql
SELECT *
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.id;
```

### Assignment

20 Join Problems

---

# Day 7 - Weekly Revision

### Revise

- SQL Basics
- Aggregations
- Joins

### Weekly Project

Employee Management Database

Features:

- Employee Table
- Department Table
- Salary Reports

---

# 🗓️ Week 2: Advanced SQL

## Day 8 - Joins Part 2

### Topics

- RIGHT JOIN
- FULL JOIN
- SELF JOIN

### Assignment

15 Join Challenges

---

# Day 9 - Subqueries

### Topics

- Nested Queries
- Correlated Queries

### Practice

```sql
SELECT name
FROM employees
WHERE salary >
(
SELECT AVG(salary)
FROM employees
);
```

---

# Day 10 - Window Functions

### Topics

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

### Practice

```sql
SELECT name,
salary,
RANK() OVER(
ORDER BY salary DESC
)
FROM employees;
```

---

# Day 11 - CTEs

### Topics

- Common Table Expressions

### Practice

```sql
WITH high_salary AS
(
SELECT *
FROM employees
WHERE salary > 60000
)
SELECT *
FROM high_salary;
```

---

# Day 12 - Views

### Topics

- CREATE VIEW
- Benefits of Views

### Assignment

Create Reporting Views

---

# Day 13 - Indexes

### Topics

- Indexes
- Query Optimization

### Practice

```sql
CREATE INDEX idx_name
ON employees(name);
```

---

# Day 14 - Weekly Revision

### Project

Company Analytics Dashboard Database

---

# 🗓️ Week 3: NumPy Fundamentals

## Day 15 - NumPy Introduction

### Topics

- Arrays
- Array Creation

### Practice

```python
import numpy as np

arr = np.array([1,2,3,4])
print(arr)
```

### Assignment

20 NumPy Exercises

---

# Day 16 - Array Operations

### Topics

- Indexing
- Slicing
- Reshaping

### Practice

```python
arr.reshape(2,2)
```

---

# Day 17 - Mathematical Operations

### Topics

- Mean
- Median
- Std
- Variance

### Practice

```python
np.mean(arr)
```

---

# Day 18 - Broadcasting

### Topics

- Broadcasting Rules

### Assignment

Matrix Operations

---

# Day 19 - Linear Algebra

### Topics

- Matrix Multiplication
- Dot Product

### Practice

```python
np.dot(a,b)
```

---

# Day 20 - Random Module

### Topics

- Random Numbers
- Sampling

### Practice

```python
np.random.rand(5)
```

---

# Day 21 - NumPy Revision

### Project

Student Marks Analyzer

---

# 🗓️ Week 4: Pandas + Data Analysis

## Day 22 - Pandas Basics

### Topics

- Series
- DataFrame

### Practice

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

---

# Day 23 - Data Cleaning

### Topics

- Missing Values
- Duplicates

### Practice

```python
df.isnull().sum()
```

---

# Day 24 - Data Manipulation

### Topics

- Filtering
- Sorting
- Grouping

### Practice

```python
df.groupby("department")
```

---

# Day 25 - Data Visualization

### Topics

- Matplotlib
- Seaborn

### Charts

- Line Chart
- Bar Chart
- Histogram

---

# Day 26 - Exploratory Data Analysis

### Topics

- Correlation
- Outliers
- Distribution

### Assignment

Perform EDA on Dataset

---

# Day 27 - Real Dataset Analysis

### Dataset

Titanic Dataset

### Tasks

- Cleaning
- Analysis
- Visualization

---

# Day 28 - Project 1

## Sales Analytics Dashboard

### Features

- Revenue Analysis
- Product Analysis
- Customer Analysis

---

# Day 29 - Project 2

## Netflix Data Analysis

### Features

- Genre Analysis
- Ratings Analysis
- Country Analysis

---

# Day 30 - Final Capstone Project

# Data Analytics Platform

### Features

- Import CSV
- Clean Data
- Perform Analysis
- Generate Visualizations
- Export Reports

### Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- MySQL

---

# 📚 Resources

## SQL

### Free

- SQLBolt
- W3Schools SQL
- Mode SQL Tutorial
- PostgreSQL Tutorial

### YouTube

- FreeCodeCamp SQL Course
- CodeWithHarry SQL Playlist
- Programming with Mosh SQL

### Books

- SQL for Data Analytics
- Learning SQL

---

# NumPy

### Official Docs

https://numpy.org/doc

### YouTube

- Keith Galli NumPy
- FreeCodeCamp NumPy

### Book

Python for Data Analysis

---

# Pandas

### Official Docs

https://pandas.pydata.org/docs

### YouTube

- Data School Pandas Playlist

### Book

Python for Data Analysis

---

# 🎯 Interview Questions

## SQL

1. Difference between WHERE and HAVING?
2. INNER JOIN vs LEFT JOIN?
3. What are indexes?
4. What is normalization?
5. What are window functions?
6. What are CTEs?

## NumPy

1. Why NumPy is faster than lists?
2. What is broadcasting?
3. Difference between reshape and resize?

## Pandas

1. Difference between loc and iloc?
2. How do you handle missing values?
3. What is groupby?
4. Difference between merge and join?

---

# 🚀 GitHub Repository Structure

```text
Phase-2-Data-SQL/
│
├── SQL/
│   ├── Day01_Database_Basics
│   ├── Day02_SQL_Basics
│   ├── Day03_Filtering
│   ├── Day04_Aggregations
│   ├── Day05_GroupBy
│   ├── Day06_Joins
│   ├── Day07_Project
│
├── Advanced_SQL/
│   ├── Subqueries
│   ├── WindowFunctions
│   ├── CTEs
│   ├── Views
│   ├── Indexes
│
├── NumPy/
│
├── Pandas/
│
├── EDA/
│
├── Projects/
│   ├── EmployeeManagementDB
│   ├── StudentMarksAnalyzer
│   ├── SalesAnalyticsDashboard
│   ├── NetflixAnalysis
│   └── DataAnalyticsPlatform
│
└── README.md
```

---

# 🏆 End of Phase 2 Milestone

You should be able to:

✅ Write complex SQL queries

✅ Use joins confidently

✅ Perform EDA independently

✅ Analyze real-world datasets

✅ Create dashboards

✅ Clean messy data

✅ Build portfolio-worthy data projects

✅ Be fully prepared for Phase 3 (Machine Learning)

---

# Next Phase

➡️ Phase 3: Machine Learning Engineering

Topics:


- Statistics
- Probability
- Machine Learning Algorithms
- Scikit-Learn
- Model Evaluation
- Feature Engineering
- Real ML Projects
- End-to-End ML Pipeline
