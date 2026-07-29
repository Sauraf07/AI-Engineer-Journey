# 📘 Day 43 – SQL Triggers

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand SQL Triggers
- Create Triggers
- Use BEFORE and AFTER Triggers
- Handle INSERT, UPDATE and DELETE events
- Build audit logs using Triggers
- Solve SQL Trigger interview questions

---

# 📌 What is a Trigger?

A **Trigger** is a special SQL object that automatically executes when a specific event occurs on a table.

Events include:

- INSERT
- UPDATE
- DELETE

Triggers help automate repetitive database tasks.

---

# 🏢 Real-World Use Cases

- Audit Logs
- Employee Salary History
- Banking Transactions
- Inventory Updates
- Security Monitoring
- Activity Logging

---

# Trigger Syntax

```sql
CREATE TRIGGER trigger_name

BEFORE | AFTER

INSERT | UPDATE | DELETE

ON table_name

FOR EACH ROW

BEGIN

-- SQL Statements

END;
```

---

# BEFORE INSERT Trigger

```sql
CREATE TRIGGER check_salary

BEFORE INSERT

ON Employees

FOR EACH ROW

BEGIN

IF NEW.salary < 10000 THEN

SET NEW.salary = 10000;

END IF;

END;
```

---

# AFTER INSERT Trigger

```sql
CREATE TRIGGER employee_log

AFTER INSERT

ON Employees

FOR EACH ROW

BEGIN

INSERT INTO Employee_Log(EmployeeID, Action)

VALUES(NEW.id, 'Inserted');

END;
```

---

# AFTER UPDATE Trigger

```sql
CREATE TRIGGER update_log

AFTER UPDATE

ON Employees

FOR EACH ROW

BEGIN

INSERT INTO Employee_Log(EmployeeID, Action)

VALUES(NEW.id, 'Updated');

END;
```

---

# AFTER DELETE Trigger

```sql
CREATE TRIGGER delete_log

AFTER DELETE

ON Employees

FOR EACH ROW

BEGIN

INSERT INTO Employee_Log(EmployeeID, Action)

VALUES(OLD.id, 'Deleted');

END;
```

---

# OLD vs NEW

| Keyword | Description |
|----------|-------------|
| NEW | New row values |
| OLD | Previous row values |

---

# Mini Project

## Employee Audit System

### Tables

- Employees
- Employee_Log

Whenever an employee is:

- Added
- Updated
- Deleted

Automatically insert a record into **Employee_Log**.

---

# Practice Questions

1. Create an INSERT Trigger.
2. Create an UPDATE Trigger.
3. Create a DELETE Trigger.
4. Log employee salary changes.
5. Track deleted records.

---

# Interview Questions

### 1. What is a Trigger?

A Trigger is a database object that automatically executes when an event occurs.

---

### 2. Types of Triggers?

- BEFORE
- AFTER

---

### 3. Which events activate Triggers?

- INSERT
- UPDATE
- DELETE

---

### 4. Difference between Trigger and Stored Procedure?

| Trigger | Stored Procedure |
|----------|------------------|
| Automatic | Manual execution |
| Event Driven | Called explicitly |

---

### 5. What are OLD and NEW?

OLD contains previous values.

NEW contains updated values.

---

# Advantages

- Automation
- Data Integrity
- Auditing
- Security
- Consistency

---

# Disadvantages

- Hard to Debug
- Can Reduce Performance
- Hidden Business Logic

---

# Best Practices

- Keep Triggers small.
- Avoid nested Triggers.
- Don't perform heavy calculations.
- Document every Trigger.

---

# Assignment

Build an **Employee Audit System** that automatically stores:

- Employee ID
- Operation Type
- Timestamp

whenever data changes.

---

# Skills Gained

- SQL Triggers
- Database Automation
- Audit Logging
- Data Integrity
- Event-Based Programming

---

# GitHub Commit

```bash
git add .
git commit -m "Day 43: Learned SQL Triggers and Built Employee Audit System"
git push origin main
```

---

# 🚀 Next Day

## 📘 Day 44 – SQL Transactions

### Topics

- COMMIT
- ROLLBACK
- SAVEPOINT
- ACID Properties
- Transaction Control Language (TCL)
- Banking System Project