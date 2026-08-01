# 📘 Day 46 – SQL Transactions & ACID Properties (Part 1)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand SQL Transactions
- Learn why Transactions are important
- Understand ACID Properties
- Use BEGIN TRANSACTION
- Use COMMIT
- Use ROLLBACK
- Use SAVEPOINT
- Handle transaction failures
- Build a Banking Transaction System

---

# 📌 What is a Transaction?

A **Transaction** is a sequence of one or more SQL operations that are executed as a **single unit of work**.

A transaction ensures that **either all operations are completed successfully or none of them are applied**.

---

# 🏦 Real-Life Example

Imagine transferring **₹5,000** from your account to your friend's account.

Steps:

1. Deduct ₹5,000 from your account.
2. Add ₹5,000 to your friend's account.

If the first step succeeds but the second fails, money is lost.

Transactions prevent this problem.

---

# Why Transactions Matter

Without Transactions:

❌ Data inconsistency

❌ Partial updates

❌ Lost money

With Transactions:

✅ Reliable database

✅ Consistent data

✅ Safe operations

---

# Transaction Flow

```text
Start Transaction
        │
        ▼
 Execute SQL Statements
        │
        ▼
   Success?
   /      \
 Yes       No
 │          │
 ▼          ▼
COMMIT   ROLLBACK
```

---

# ACID Properties

ACID is the foundation of reliable database systems.

| Property | Meaning |
|----------|---------|
| Atomicity | All or Nothing |
| Consistency | Database remains valid |
| Isolation | Transactions don't interfere |
| Durability | Data stays saved permanently |

---

# 1️⃣ Atomicity

Either every statement executes successfully or none of them do.

Example:

```sql
BEGIN;

UPDATE Accounts
SET Balance = Balance - 5000
WHERE AccountID = 1;

UPDATE Accounts
SET Balance = Balance + 5000
WHERE AccountID = 2;

COMMIT;
```

If any statement fails:

```sql
ROLLBACK;
```

---

# 2️⃣ Consistency

The database must always remain valid.

Example:

Before Transfer

```text
Account A = ₹20,000
Account B = ₹10,000

Total = ₹30,000
```

After Transfer

```text
Account A = ₹15,000
Account B = ₹15,000

Total = ₹30,000
```

Consistency is maintained.

---

# 3️⃣ Isolation

Multiple users can work simultaneously without affecting each other.

Example

Customer A transfers money.

Customer B checks balance.

Customer B should not see incomplete updates.

---

# 4️⃣ Durability

Once committed, data remains safe even if power fails.

Example

```sql
COMMIT;
```

Even after system restart:

Data remains saved.

---

# SQL Transaction Syntax

```sql
BEGIN TRANSACTION;

-- SQL Statements

COMMIT;
```

---

# BEGIN TRANSACTION

Starts a transaction.

```sql
BEGIN TRANSACTION;
```

No changes become permanent until COMMIT.

---

# COMMIT

Permanently saves changes.

```sql
BEGIN TRANSACTION;

UPDATE Employees
SET Salary = Salary + 5000
WHERE EmployeeID = 101;

COMMIT;
```

---

# ROLLBACK

Undo all changes.

```sql
BEGIN TRANSACTION;

UPDATE Employees
SET Salary = Salary + 5000
WHERE EmployeeID = 101;

ROLLBACK;
```

Nothing changes.

---

# SAVEPOINT

Creates a checkpoint inside a transaction.

```sql
BEGIN TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 1000
WHERE AccountID = 1;

SAVEPOINT Step1;

UPDATE Accounts
SET Balance = Balance + 1000
WHERE AccountID = 2;
```

Rollback to savepoint:

```sql
ROLLBACK TO Step1;
```

---

# Banking Example

Initial Data

| Account | Balance |
|----------|---------|
| A | ₹50,000 |
| B | ₹20,000 |

Transfer ₹10,000

```sql
BEGIN TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 10000
WHERE AccountID = 1;

UPDATE Accounts
SET Balance = Balance + 10000
WHERE AccountID = 2;

COMMIT;
```

Result

| Account | Balance |
|----------|---------|
| A | ₹40,000 |
| B | ₹30,000 |

---

# Employee Salary Example

Increase salary.

```sql
BEGIN TRANSACTION;

UPDATE Employees
SET Salary = Salary + 3000
WHERE Department = 'IT';

COMMIT;
```

---

# Order Management Example

```sql
BEGIN TRANSACTION;

INSERT INTO Orders
VALUES (101,'Laptop',2);

UPDATE Products
SET Stock = Stock - 2
WHERE ProductID = 10;

COMMIT;
```

---

# When to Use Transactions

Use transactions whenever multiple related operations must succeed together.

Examples:

- Bank transfers
- Online payments
- Flight booking
- Hotel reservation
- Inventory updates
- Payroll systems
- E-commerce orders

---

# Mini Project

## Banking System

### Create Table

```sql
CREATE TABLE Accounts(
    AccountID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    Balance DECIMAL(10,2)
);
```

---

### Insert Data

```sql
INSERT INTO Accounts
VALUES
(1,'John',50000),
(2,'Alice',20000);
```

---

### Transfer Money

```sql
BEGIN TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 5000
WHERE AccountID = 1;

UPDATE Accounts
SET Balance = Balance + 5000
WHERE AccountID = 2;

COMMIT;
```

---

# Practice Questions

## Easy

1. Create a transaction.
2. Update employee salary.
3. Use COMMIT.
4. Use ROLLBACK.
5. Create SAVEPOINT.

---

## Medium

6. Bank transfer system.
7. Online order system.
8. Hotel booking.
9. Inventory update.
10. Student fee payment.

---

# Best Practices

- Always use transactions for critical operations.
- Commit only after successful execution.
- Rollback if any error occurs.
- Keep transactions short.
- Avoid unnecessary locks.

---

# Key Takeaways

✅ Transaction = Group of SQL statements executed as one unit.

✅ ACID ensures reliable databases.

✅ COMMIT saves changes permanently.

✅ ROLLBACK cancels changes.

✅ SAVEPOINT allows partial rollback.

---

# GitHub Assignment

Create a repository:

```text
SQL-Transactions/
│
├── README.md
├── banking_system.sql
├── employee_salary.sql
├── order_management.sql
├── savepoint_examples.sql
└── transaction_practice.sql
```

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 46: Learned SQL Transactions and ACID Properties"
git push origin main
```

---

# 🚀 Next Part

**Part 2: Isolation Levels, Concurrency Control, Deadlocks, and Transaction Interview Questions**
# 📘 Day 46 – SQL Transactions & ACID Properties (Part 2)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand transaction isolation levels
- Learn concurrency problems
- Prevent data inconsistencies
- Understand database locking
- Solve interview questions on transactions

---

# 📌 What is Concurrency?

Concurrency means **multiple users accessing or modifying the database at the same time**.

### Example

Imagine two customers trying to book the **last movie ticket** simultaneously.

Without proper transaction management, both users may book the same seat.

---

# Why Isolation Levels Matter

Isolation levels control **how transactions interact with each other**.

They help prevent data corruption and inconsistent results.

---

# SQL Isolation Levels

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|-----------------|------------|---------------------|--------------|
| Read Uncommitted | ✅ Yes | ✅ Yes | ✅ Yes |
| Read Committed | ❌ No | ✅ Yes | ✅ Yes |
| Repeatable Read | ❌ No | ❌ No | ✅ Yes |
| Serializable | ❌ No | ❌ No | ❌ No |

---

# 1. Read Uncommitted

- Lowest isolation level
- Fastest
- Allows reading uncommitted data

### Problem

May return incorrect or temporary data.

---

# 2. Read Committed

- Reads only committed data
- Most commonly used isolation level

### Benefits

- Prevents dirty reads
- Better balance between speed and consistency

---

# 3. Repeatable Read

- Ensures data remains the same during a transaction
- Prevents non-repeatable reads

---

# 4. Serializable

- Highest isolation level
- Safest but slowest
- Executes transactions one by one

---

# Concurrency Problems

---

## 1. Dirty Read

Occurs when one transaction reads data that has **not yet been committed**.

### Example

Transaction A updates salary to ₹70,000.

Transaction B reads ₹70,000.

Transaction A rolls back.

Transaction B has read incorrect data.

---

## 2. Non-Repeatable Read

Occurs when the same row is read twice and returns different values.

### Example

First Read:

```text
Salary = ₹50,000
```

Another transaction updates salary.

Second Read:

```text
Salary = ₹60,000
```

---

## 3. Phantom Read

Occurs when new rows appear between two identical queries.

### Example

Query 1

```sql
SELECT * FROM Employees;
```

Returns:

10 rows

Another transaction inserts a new employee.

Query 2

Returns:

11 rows

---

# Setting Isolation Level

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

Other options:

```sql
READ UNCOMMITTED
REPEATABLE READ
SERIALIZABLE
```

---

# Locking

Databases use locks to avoid conflicts.

### Types of Locks

- Shared Lock (Read)
- Exclusive Lock (Write)

---

# Deadlock

A deadlock occurs when two transactions wait for each other forever.

### Example

Transaction A locks Table A.

Transaction B locks Table B.

A waits for B.

B waits for A.

Neither can continue.

---

# Preventing Deadlocks

- Keep transactions short
- Access tables in the same order
- Commit quickly
- Avoid unnecessary locks

---

# Banking Example

### Transaction A

Withdraw ₹500

### Transaction B

Deposit ₹1000

Without isolation:

Balance may become incorrect.

With transactions:

Database always remains consistent.

---

# Real-World Use Cases

## Banking

- Money Transfer
- ATM Withdrawal
- Online Payments

---

## E-Commerce

- Order Placement
- Inventory Management
- Payment Confirmation

---

## Hospital

- Patient Records
- Appointment Booking

---

## Airline Booking

- Seat Reservation
- Ticket Cancellation

---

## Stock Trading

- Buy/Sell Orders
- Portfolio Updates

---

# Performance Tips

✅ Keep transactions short.

✅ Commit as soon as possible.

✅ Avoid long-running transactions.

✅ Choose the appropriate isolation level.

✅ Index frequently used columns.

---

# Best Practices

- Always use transactions for critical operations.
- Use `COMMIT` only after successful execution.
- Use `ROLLBACK` when an error occurs.
- Avoid nested transactions unless necessary.
- Keep business logic outside long transactions.

---

# Interview Questions

## Beginner

### 1. What is transaction isolation?

Isolation controls how multiple transactions interact with each other.

---

### 2. Why do we need isolation levels?

To prevent inconsistent data caused by concurrent transactions.

---

### 3. Which isolation level is the safest?

**Serializable**.

---

### 4. Which isolation level is fastest?

**Read Uncommitted**.

---

### 5. Which isolation level is most commonly used?

**Read Committed**.

---

## Intermediate

### 6. What is Dirty Read?

Reading uncommitted data.

---

### 7. What is Non-Repeatable Read?

Reading the same row twice and getting different values.

---

### 8. What is Phantom Read?

Getting additional rows when executing the same query again.

---

### 9. What is a Deadlock?

Two transactions waiting indefinitely for each other to release locks.

---

### 10. How can deadlocks be prevented?

- Keep transactions short.
- Lock resources in a consistent order.
- Commit quickly.
- Avoid unnecessary locking.

---

# Practice Questions

1. Explain all four isolation levels.
2. Differentiate Dirty Read and Phantom Read.
3. What causes deadlocks?
4. Write SQL to set the isolation level.
5. Explain shared and exclusive locks.
6. Compare Read Committed vs Serializable.
7. Why are transactions important in banking?
8. What happens if a transaction is not committed?
9. How do transactions improve data integrity?
10. When would you use Repeatable Read?

---

# Day 46 Summary

Today you learned:

- Concurrency
- Isolation Levels
- Dirty Read
- Non-Repeatable Read
- Phantom Read
- Locking
- Deadlocks
- Performance Tips
- Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 46: Learned SQL Isolation Levels, Concurrency and Deadlock Handling"
git push origin main
```

---

# 🚀 Next Day

## Day 47 – SQL Stored Procedures & Functions

### Topics

- Stored Procedures
- User Defined Functions (UDF)
- Parameters
- Output Parameters
- Benefits
- Real-world Examples
- Interview Questions
- Hands-on Project

# 📘 Day 46 – SQL Transactions & ACID Properties (Part 3)

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Build a transaction-based banking system
- Apply COMMIT, ROLLBACK, and SAVEPOINT
- Solve interview-level SQL transaction questions
- Understand real-world database consistency

---

# 🚀 Mini Project

# Banking Management System

Imagine you're developing a banking application.

## Requirements

- Deposit Money
- Withdraw Money
- Transfer Money
- Rollback failed transactions
- Commit successful transactions

---

# Database

## Accounts

| Account_ID | Name | Balance |
|------------|------|---------|
|101|John|50000|
|102|Alice|30000|
|103|Bob|45000|

---

# Transaction Example

## Money Transfer

```sql
START TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 10000
WHERE Account_ID = 101;

UPDATE Accounts
SET Balance = Balance + 10000
WHERE Account_ID = 102;

COMMIT;
```

---

## Rollback Example

```sql
START TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 5000
WHERE Account_ID = 101;

ROLLBACK;
```

---

## Savepoint Example

```sql
START TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 1000
WHERE Account_ID = 101;

SAVEPOINT after_withdraw;

UPDATE Accounts
SET Balance = Balance + 1000
WHERE Account_ID = 102;

ROLLBACK TO after_withdraw;

COMMIT;
```

---

# 💼 Practice Questions

1. Create a bank transfer transaction.
2. Rollback a failed transaction.
3. Use SAVEPOINT.
4. Commit successful updates.
5. Simulate salary payment.
6. Undo accidental updates.
7. Update multiple tables in one transaction.
8. Create order and payment transaction.
9. Restore transaction using SAVEPOINT.
10. Create student fee payment transaction.

---

# 🎤 Interview Questions

## Beginner

### 1. What is a Transaction?

A transaction is a group of SQL operations executed as a single unit of work.

---

### 2. Why are transactions important?

They ensure data consistency and reliability.

---

### 3. What is COMMIT?

Permanently saves all changes made during a transaction.

---

### 4. What is ROLLBACK?

Undoes all changes made since the transaction started.

---

### 5. What is SAVEPOINT?

A checkpoint inside a transaction that allows partial rollback.

---

## Intermediate

### 6. Explain ACID Properties.

- **Atomicity** – All operations succeed or none.
- **Consistency** – Database remains valid.
- **Isolation** – Transactions don't interfere.
- **Durability** – Committed data is permanently stored.

---

### 7. Difference between COMMIT and ROLLBACK?

| COMMIT | ROLLBACK |
|---------|----------|
| Saves changes | Undoes changes |

---

### 8. Can a transaction contain multiple SQL statements?

Yes.

---

### 9. Can ROLLBACK happen after COMMIT?

No. Once committed, changes cannot be rolled back.

---

### 10. Where are transactions used?

- Banking
- E-commerce
- Payroll
- Booking Systems
- Payment Gateways

---

# 📌 Best Practices

- Always use transactions for critical operations.
- Commit only after successful execution.
- Rollback on errors.
- Keep transactions short.
- Avoid long-running transactions.

---

# 📝 SQL Cheat Sheet

## Start Transaction

```sql
START TRANSACTION;
```

---

## Commit

```sql
COMMIT;
```

---

## Rollback

```sql
ROLLBACK;
```

---

## Savepoint

```sql
SAVEPOINT save_name;
```

---

## Rollback to Savepoint

```sql
ROLLBACK TO save_name;
```

---

# 🎯 Assignment

Build SQL queries for:

- Bank Transfer
- Salary Payment
- Online Shopping Checkout
- Student Fee Payment
- Ticket Booking System

Use:

- START TRANSACTION
- COMMIT
- ROLLBACK
- SAVEPOINT

---

# 🏆 Skills Gained

- SQL Transactions
- ACID Properties
- COMMIT
- ROLLBACK
- SAVEPOINT
- Database Consistency
- Real-World Transaction Handling

---

# 💡 GitHub Assignment

Create the following repository structure:

```text
SQL-Transactions/
│
├── README.md
├── banking_system.sql
├── transaction_examples.sql
├── savepoint_examples.sql
├── practice_queries.sql
├── interview_questions.md
└── assignments.sql
```

---

# 📖 Key Takeaways

✅ Transactions ensure reliable database operations.

✅ ACID properties maintain data integrity.

✅ COMMIT permanently saves changes.

✅ ROLLBACK cancels unwanted changes.

✅ SAVEPOINT enables partial rollback.

✅ Transactions are essential for banking, e-commerce, and financial systems.

---

# 💻 GitHub Commit

```bash
git add .
git commit -m "Day 46: Learned SQL Transactions and ACID Properties"
git push origin main
```

---

# 🚀 Next Day

## 📅 Day 47 – SQL Stored Procedures

### Topics

- What are Stored Procedures?
- CREATE PROCEDURE
- Parameters (IN, OUT, INOUT)
- Calling Procedures
- Advantages & Limitations
- Real-world Use Cases
- Interview Questions
- Hands-on Project

---

🎉 **Congratulations!** You have now completed **Day 46 – SQL Transactions & ACID Properties** and are ready to learn how to automate SQL logic using **Stored Procedures**.