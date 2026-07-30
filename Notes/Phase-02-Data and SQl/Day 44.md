# 📘 Day 44 – SQL Transactions & ACID Properties

> **Phase 2: Data & SQL**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand SQL Transactions
- Learn ACID Properties
- Use COMMIT and ROLLBACK
- Use SAVEPOINT
- Handle transaction failures
- Build reliable database applications

---

# 📌 What is a Transaction?

A **Transaction** is a group of SQL statements executed as a single unit of work.

Either:

- ✅ All operations succeed
- ❌ Or none of them are applied

This prevents inconsistent data.

---

# 💡 Real-Life Example

Imagine transferring ₹1000 from Account A to Account B.

Steps:

1. Deduct ₹1000 from Account A
2. Add ₹1000 to Account B

If step 2 fails, step 1 should also be cancelled.

This is why transactions are important.

---

# Transaction Syntax

```sql
START TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 1000
WHERE AccountID = 1;

UPDATE Accounts
SET Balance = Balance + 1000
WHERE AccountID = 2;

COMMIT;
```

---

# COMMIT

Saves all changes permanently.

```sql
COMMIT;
```

---

# ROLLBACK

Undo all changes if an error occurs.

```sql
ROLLBACK;
```

---

# SAVEPOINT

Create a checkpoint inside a transaction.

```sql
SAVEPOINT payment_done;
```

Rollback to savepoint:

```sql
ROLLBACK TO payment_done;
```

---

# ACID Properties

## A — Atomicity

All operations happen or none happen.

Example:

Bank Transfer

---

## C — Consistency

Database remains valid before and after transaction.

Example:

Balance cannot become negative.

---

## I — Isolation

Multiple users can execute transactions safely without interfering.

Example:

Two users booking the same seat simultaneously.

---

## D — Durability

Once committed, data remains saved even after a crash.

---

# Practical Example

```sql
START TRANSACTION;

UPDATE Products
SET Stock = Stock - 1
WHERE ProductID = 101;

UPDATE Orders
SET Status = 'Confirmed'
WHERE OrderID = 10;

COMMIT;
```

---

# Interview Questions

### 1. What is a transaction?

A transaction is a sequence of SQL statements executed as one logical unit.

---

### 2. What is COMMIT?

Permanently saves changes.

---

### 3. What is ROLLBACK?

Reverts changes made during a transaction.

---

### 4. What is SAVEPOINT?

Creates a point to roll back to without undoing the entire transaction.

---

### 5. What are ACID properties?

- Atomicity
- Consistency
- Isolation
- Durability

---

### 6. Why are transactions important?

They ensure data integrity and prevent partial updates.

---

# Practice Questions

1. Create a bank transfer transaction.
2. Use COMMIT.
3. Use ROLLBACK.
4. Create a SAVEPOINT.
5. Roll back to a SAVEPOINT.

---

# Mini Project

## Banking System

Features:

- Deposit Money
- Withdraw Money
- Transfer Money
- Rollback on Failure

---

# Best Practices

- Keep transactions short.
- Commit only after validation.
- Rollback on errors.
- Avoid unnecessary locks.
- Use SAVEPOINT for complex operations.

---

# Key Takeaways

✅ Transactions ensure reliable database operations.

✅ COMMIT saves changes permanently.

✅ ROLLBACK restores the previous state.

✅ SAVEPOINT allows partial rollback.

✅ ACID properties guarantee data reliability.

---

# GitHub Commit

```bash
git add .
git commit -m "Day 44: Learned SQL Transactions and ACID Properties"
git push origin main
```

---

# 🚀 Next Day

## Day 45 – SQL Indexes

Topics:

- What are Indexes?
- Clustered Index
- Non-Clustered Index
- Composite Index
- Query Optimization
- Performance Tuning
- EXPLAIN Statement
- Interview Questions