# 📘 Day 45 – SQL Database Design & Normalization

> **Phase 2: Data & SQL**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of today, you will be able to:

- Understand Database Design
- Learn Normalization
- Understand 1NF, 2NF, 3NF
- Learn Denormalization
- Design efficient databases
- Reduce data redundancy
- Improve database performance

---

# 📌 What is Database Design?

Database Design is the process of organizing data into tables, relationships, and constraints to ensure:

- Data consistency
- Easy maintenance
- Fast querying
- Reduced redundancy

---

# 📌 What is Normalization?

Normalization is the process of organizing data to eliminate duplicate data and improve data integrity.

### Benefits

- Reduces redundancy
- Prevents update anomalies
- Saves storage
- Improves consistency

---

# 🔹 First Normal Form (1NF)

### Rules

- Each column contains atomic values.
- No repeating groups.
- Every row is unique.

### Example

❌ Before

| Student | Subjects |
|----------|----------|
| Rahul | Math, Science |

✅ After

| Student | Subject |
|----------|----------|
| Rahul | Math |
| Rahul | Science |

---

# 🔹 Second Normal Form (2NF)

### Rules

- Must satisfy 1NF.
- Remove partial dependency.

### Example

Separate student information from course information.

---

# 🔹 Third Normal Form (3NF)

### Rules

- Must satisfy 2NF.
- Remove transitive dependency.

Example:

Instead of storing Department Name repeatedly in Employee table, create a Department table.

---

# 🔹 Denormalization

Sometimes duplicate data is intentionally added to improve query performance.

Used in:

- Reporting
- Data Warehouses
- Analytics Dashboards

---

# 📊 Real-World Example

## E-Commerce Database

Tables:

- Customers
- Orders
- Products
- Categories
- Payments

Each table stores only related information.

---

# 💻 Mini Project

## Library Management Database

Create tables for:

- Books
- Authors
- Members
- Borrow Records
- Categories

Relationships:

- One Author → Many Books
- One Member → Many Borrow Records

---

# 🎤 Interview Questions

### Beginner

**1. What is Normalization?**

Normalization is the process of organizing data to reduce redundancy and improve consistency.

---

**2. Why is Normalization important?**

To eliminate duplicate data and maintain data integrity.

---

**3. What is 1NF?**

Every column should contain a single (atomic) value.

---

**4. What is 2NF?**

Removes partial dependency.

---

**5. What is 3NF?**

Removes transitive dependency.

---

### Intermediate

**6. What is Denormalization?**

Adding redundancy intentionally to improve performance.

---

**7. When should Denormalization be used?**

In reporting systems and data warehouses.

---

**8. Difference between Normalization and Denormalization?**

| Normalization | Denormalization |
|---------------|-----------------|
| Less redundancy | More redundancy |
| Better consistency | Faster reads |
| More joins | Fewer joins |

---

**9. What are anomalies?**

- Insert Anomaly
- Update Anomaly
- Delete Anomaly

---

**10. Is 3NF always required?**

No. Some systems intentionally use denormalization for better performance.

---

# 📝 Practice Questions

1. Convert an unnormalized table into 1NF.
2. Convert a table from 1NF to 2NF.
3. Convert a table from 2NF to 3NF.
4. Design a Student Management Database.
5. Design an E-Commerce Database.
6. Identify partial dependencies.
7. Identify transitive dependencies.
8. Design relationships between tables.
9. Compare normalized and denormalized schemas.
10. Explain normalization using a real-world example.

---

# 💡 Best Practices

- Keep tables focused on one entity.
- Use Primary Keys.
- Use Foreign Keys.
- Avoid duplicate data.
- Normalize first, optimize later.
- Denormalize only when necessary.

---

# 🏆 Skills Gained

- Database Design
- Entity Relationships
- Normalization
- Denormalization
- Data Integrity
- SQL Best Practices

---

# 📚 Cheat Sheet

| Normal Form | Purpose |
|--------------|---------|
| 1NF | Atomic values |
| 2NF | Remove partial dependency |
| 3NF | Remove transitive dependency |

---

# 💻 GitHub Assignment

Create a repository:

```text
SQL-Database-Design/
│
├── README.md
├── ecommerce_schema.sql
├── library_schema.sql
├── student_schema.sql
├── normalization_examples.sql
└── interview_questions.md
```

---

# 🚀 GitHub Commit

```bash
git add .
git commit -m "Day 45: Learned SQL Database Design and Normalization"
git push origin main
```

---

# 📅 Next Day

## Day 46 – SQL Performance Optimization

### Topics

- Indexes
- Query Optimization
- EXPLAIN
- Execution Plans
- Best Practices
- Performance Tuning
- Real-World Examples

---

## 🎉 Congratulations!

You now understand how professional databases are designed for scalability, consistency, and performance. This knowledge is essential for backend development, data engineering, and AI applications where well-structured data is the foundation for reliable models.