# Day 21 - Mini Project: Expense Tracker (Python CLI)

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📌 Project Overview

The **Expense Tracker** is a Command Line Interface (CLI) application built using Python. It helps users manage their daily expenses by allowing them to add, view, delete, search, and summarize expenses.

This project reinforces Python fundamentals such as:

- Variables
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- Modular Programming

This is one of the first real-world projects that demonstrates problem-solving and clean code practices.

---

# 🎯 Learning Objectives

By completing this project, you will be able to:

- Build a complete Python CLI application
- Organize code using functions
- Store and manipulate data
- Read from and write to files
- Handle invalid user input gracefully
- Generate useful reports
- Improve logical thinking and debugging skills

---

# 🛠️ Technologies Used

- Python 3.x
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.txt
├── README.md
└── screenshots/
```

---

# 📋 Features

✅ Add Expense

✅ View All Expenses

✅ Delete Expense

✅ Search Expense

✅ Monthly Expense Summary

✅ Category-wise Expense Report

✅ Save Data in File

✅ Load Data Automatically

✅ Error Handling

---

# 📌 How It Works

The application displays a menu.

```text
===== Expense Tracker =====

1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expense
5. Monthly Summary
6. Exit
```

The user chooses an option, performs the task, and returns to the main menu.

---

# 📌 Expense Format

Each expense contains:

| Field | Description |
|---------|------------|
| Date | Expense Date |
| Category | Food, Travel, Shopping etc. |
| Amount | Expense Amount |
| Description | Optional Note |

Example

```text
01-07-2026
Food
250
Lunch
```

---

# 📌 Functions Used

```python
add_expense()

view_expenses()

delete_expense()

search_expense()

monthly_summary()

save_expenses()

load_expenses()
```

---

# 📌 Data Structure

Expenses can be stored as dictionaries.

Example

```python
expense = {
    "date": "01-07-2026",
    "category": "Food",
    "amount": 250,
    "description": "Lunch"
}
```

Multiple expenses are stored in a list.

```python
expenses = []
```

---

# 📌 Sample Workflow

### Add Expense

```text
Enter Date:
01-07-2026

Category:
Food

Amount:
250

Description:
Lunch
```

Output

```text
Expense Added Successfully
```

---

### View Expenses

```text
Date          Category      Amount      Description

01-07-2026    Food          250         Lunch

02-07-2026    Travel        120         Bus Ticket
```

---

### Search Expense

Input

```text
Food
```

Output

```text
Food

250

Lunch
```

---

### Monthly Summary

```text
Total Expenses

₹5230

Food

₹1500

Travel

₹800

Shopping

₹1200
```

---

# 📌 Algorithm

```
Start

↓

Display Menu

↓

Take User Choice

↓

If Add Expense

↓

Store Expense

↓

Save File

↓

Return Menu

↓

If Exit

↓

End
```

---

# 📌 File Handling

Expenses should be stored inside

```
expenses.txt
```

or

```
expenses.csv
```

This allows data to remain available even after closing the application.

---

# 📌 Error Handling

Handle

- Invalid Amount
- Empty Input
- File Not Found
- Invalid Menu Choice

Example

```python
try:
    amount = float(input("Enter Amount: "))
except ValueError:
    print("Please enter a valid number.")
```

---

# 📌 Skills Practiced

- Variables
- Loops
- Lists
- Dictionaries
- Functions
- Exception Handling
- File Handling
- User Input
- Modular Programming

---

# 🚀 Future Improvements

- SQLite Database Integration
- GUI using Tkinter
- Web Version using Flask
- FastAPI Backend
- React Frontend
- User Authentication
- Expense Charts
- CSV Export
- PDF Reports
- AI-powered Expense Analysis

---

# 💡 Real-World Applications

Expense tracking systems are commonly used in:

- Personal Finance Apps
- Banking Applications
- Accounting Software
- Budget Management Systems
- Business Expense Management

---

# 🧠 Interview Questions

## Beginner

### 1. Why did you build this project?

To practice Python fundamentals by developing a real-world application involving CRUD operations, file handling, and exception handling.

---

### 2. Why did you choose Python?

Python is simple, readable, and widely used in automation, web development, data science, and AI.

---

### 3. Which data structure is used?

A list stores multiple expense records, while each expense is represented as a dictionary.

---

### 4. Why use functions?

Functions improve code readability, modularity, and reusability.

---

### 5. Why use file handling?

To persist expense data so that it remains available after the program closes.

---

## Intermediate

### 6. Why choose dictionaries for storing expenses?

Dictionaries allow storing related information using meaningful keys such as `date`, `category`, and `amount`.

---

### 7. What exception handling is used?

The project uses `try-except` blocks to prevent crashes caused by invalid user input.

---

### 8. How would you improve the project?

- Add a database
- Build a GUI
- Add authentication
- Generate charts
- Deploy as a web application

---

### 9. What is CRUD?

CRUD stands for:

- Create
- Read
- Update
- Delete

The Expense Tracker mainly implements Create, Read, and Delete operations.

---

### 10. How would you store millions of expenses?

Instead of using text files, use relational databases such as MySQL or PostgreSQL for better performance and scalability.

---

## Advanced

### 11. How would you optimize search?

Use indexing or hash-based lookups instead of iterating through every expense.

---

### 12. How would you make the project production-ready?

- Use a relational database
- Implement authentication
- Build REST APIs
- Add frontend
- Deploy on cloud
- Write unit tests
- Use Docker
- Implement logging

---

### 13. How would this project fit into an AI application?

Expense data can be analyzed using machine learning models to predict spending patterns, detect anomalies, and provide personalized financial recommendations.

---

# 📝 Assignment

Extend the project by adding:

- Edit Expense
- Filter by Date
- Filter by Category
- Highest Expense
- Lowest Expense
- Monthly Statistics
- Export to CSV
- Import from CSV

---

# 🎯 Expected Outcome

After completing this project, you should be able to:

- Build Python CLI applications confidently
- Organize code into reusable functions
- Work with files effectively
- Handle user input and exceptions
- Understand CRUD operations
- Push projects to GitHub with proper documentation

---

# 📸 Suggested Screenshots

Add screenshots of:

- Main Menu
- Add Expense
- View Expenses
- Search Expense
- Monthly Summary

Store them in the `screenshots/` folder and embed them here once available.

---

# 📚 Resources

## Official Documentation

- Python Documentation: https://docs.python.org/3/

## Practice Platforms

- HackerRank
- LeetCode
- Codewars

---

# 🏁 Conclusion

This Expense Tracker project is an excellent milestone in your Python journey. It combines core programming concepts into a practical application and lays the foundation for future projects involving databases, web development, APIs, and AI-powered financial tools.

⭐ If you found this project helpful, consider giving the repository a **star** and continue building more real-world Python projects!