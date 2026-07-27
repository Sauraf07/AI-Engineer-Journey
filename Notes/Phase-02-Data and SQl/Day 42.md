# 📘 Day 42 – SQL Stored Procedures

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand Stored Procedures
- Create Stored Procedures
- Execute Stored Procedures
- Pass Parameters
- Modify Stored Procedures
- Delete Stored Procedures
- Learn Advantages of Stored Procedures
- Solve Interview Questions

---

# 📌 What is a Stored Procedure?

A **Stored Procedure** is a precompiled collection of SQL statements stored inside the database.

It can be executed whenever required without rewriting the SQL query.

---

# 💡 Why Stored Procedures?

Instead of writing the same SQL query multiple times:

```sql
SELECT *
FROM Employees
WHERE Department = 'IT';
```

You can save it as a Stored Procedure and call it whenever needed.

Benefits:

- Reusable
- Faster execution
- Better security
- Less network traffic
- Easier maintenance

---

# 🏗 Syntax

```sql
CREATE PROCEDURE procedure_name()
BEGIN

SQL Statements;

END;
```

---

# 📝 Example

```sql
CREATE PROCEDURE GetEmployees()

BEGIN

SELECT *
FROM Employees;

END;
```

Execute:

```sql
CALL GetEmployees();
```

---

# 📌 Procedure with Parameters

```sql
CREATE PROCEDURE GetEmployeeByDept(

IN dept_name VARCHAR(50)

)

BEGIN

SELECT *
FROM Employees
WHERE Department = dept_name;

END;
```

Execute:

```sql
CALL GetEmployeeByDept('IT');
```

---

# 📌 Multiple Parameters

```sql
CREATE PROCEDURE EmployeeSalary(

IN dept VARCHAR(50),
IN salary DECIMAL(10,2)

)

BEGIN

SELECT *

FROM Employees

WHERE Department = dept
AND Salary > salary;

END;
```

---

# 📌 Update Data

```sql
CREATE PROCEDURE IncreaseSalary(

IN emp_id INT,
IN increment DECIMAL(10,2)

)

BEGIN

UPDATE Employees

SET Salary = Salary + increment

WHERE EmployeeID = emp_id;

END;
```

---

# 📌 Delete Procedure

```sql
DROP PROCEDURE GetEmployees;
```

---

# 🚀 Advantages

- Faster than repeated SQL
- Reusable code
- Better security
- Easier debugging
- Reduces duplication

---

# ❌ Disadvantages

- Harder to maintain if very large
- Database-specific syntax
- Debugging can become difficult

---

# 🌍 Real-World Use Cases

### Banking

Transfer Money

---

### E-Commerce

Place Order

---

### Hospital

Patient Records

---

### School

Student Result Generation

---

### HRMS

Employee Salary Processing

---

# 💼 Mini Project

## Employee Management System

Create Stored Procedures for:

- Add Employee
- Update Employee
- Delete Employee
- Search Employee
- Department Report

---

# 📝 Practice Questions

1. Create a Stored Procedure to display all employees.
2. Create a procedure using parameters.
3. Update salary using a procedure.
4. Delete a procedure.
5. Execute a procedure.

---

# 🎤 Interview Questions

### Beginner

### 1. What is a Stored Procedure?

A precompiled SQL program stored inside the database.

---

### 2. Why use Stored Procedures?

For performance, security, and code reusability.

---

### 3. How do you execute a Stored Procedure?

```sql
CALL procedure_name();
```

---

### 4. Can Stored Procedures accept parameters?

Yes.

---

### 5. Difference between Procedure and Function?

| Procedure | Function |
|------------|----------|
| Can return multiple values | Returns one value |
| Can modify data | Usually returns computed value |
| Called using CALL | Used inside SQL expressions |

---

### Intermediate

6. What are IN, OUT, and INOUT parameters?

7. Can Stored Procedures call other Stored Procedures?

8. Are Stored Procedures precompiled?

9. How do Stored Procedures improve security?

10. When should Stored Procedures be avoided?

---

# 📚 Cheat Sheet

## Create

```sql
CREATE PROCEDURE procedure_name()
BEGIN
END;
```

---

## Execute

```sql
CALL procedure_name();
```

---

## Drop

```sql
DROP PROCEDURE procedure_name;
```

---

## Parameter

```sql
IN parameter datatype
```

---

# 🎯 Assignment

Build procedures for:

- Student Management System
- Employee Database
- Banking System
- Inventory Management
- Library Management

---

# 🏆 Skills Gained

- Stored Procedures
- SQL Automation
- Parameter Passing
- Database Programming
- Performance Optimization

---

# 💡 GitHub Commit

```bash
git add .
git commit -m "Day 42: Learned SQL Stored Procedures"
git push origin main
```

---

# 🚀 Next Day

## 📅 Day 43 – SQL Triggers

### Topics

- What are Triggers?
- BEFORE Trigger
- AFTER Trigger
- INSERT Trigger
- UPDATE Trigger
- DELETE Trigger
- Real-world Examples
- Interview Questions

---

⭐ **Milestone:** You can now automate database operations using SQL Stored Procedures.