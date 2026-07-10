# Day 28 - Python Virtual Environments, pip & Requirements.txt

> Phase 1: Programming Foundation  
> Roadmap: AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📚 Table of Contents

- Introduction
- Learning Objectives
- What is a Virtual Environment?
- Why Do We Need Virtual Environments?
- Real-World Example
- Creating a Virtual Environment
- Activating a Virtual Environment
- Deactivating a Virtual Environment
- Installing Packages with pip
- Upgrading Packages
- Uninstalling Packages
- Understanding requirements.txt
- Installing Dependencies
- Best Practices
- Common Errors
- Mini Project
- Hands-on Exercises
- Interview Questions
- Resources
- GitHub Commit
- What's Next?

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand what a virtual environment is
- Create isolated Python environments
- Install and manage packages using pip
- Create and use a requirements.txt file
- Reproduce projects on another machine
- Follow industry-standard Python project structure
- Prepare projects for deployment

---

# 📌 What is a Virtual Environment?

A **Virtual Environment (venv)** is an isolated Python environment where a project has its own dependencies, independent of other Python projects on your computer.

Instead of installing libraries globally, each project gets its own separate environment.

---

# 🤔 Why Do We Need Virtual Environments?

Imagine you have two projects:

### Project A

Uses:

- Django 4.2

### Project B

Uses:

- Django 5.2

If both are installed globally, version conflicts can occur.

Using a virtual environment keeps each project's dependencies separate.

---

# 🏢 Real-World Example

Think of a virtual environment like a separate room for each project.

Without Virtual Environment:

```
Computer
│
├── Project A
├── Project B
└── Same installed libraries
```

Version conflicts happen.

---

With Virtual Environment:

```
Computer
│
├── Project A
│   └── Own Libraries
│
├── Project B
│   └── Own Libraries
│
└── No conflicts
```

---

# 📂 Creating a Virtual Environment

Open your terminal inside the project folder.

```bash
python -m venv venv
```

Here:

- python → Python interpreter
- -m → Run module
- venv → Virtual environment module
- venv → Folder name

---

Example:

```
MyProject/
│
├── venv/
├── app.py
```

---

# ▶ Activating the Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

---

## macOS / Linux

```bash
source venv/bin/activate
```

---

If activated successfully, you'll see something like:

```text
(venv) C:\Users\YourName\Project>
```

The `(venv)` prefix indicates the environment is active.

---

# ⏹ Deactivating the Virtual Environment

To exit the environment:

```bash
deactivate
```

The `(venv)` prefix disappears.

---

# 📦 What is pip?

`pip` is Python's package manager.

It is used to install, update, and remove Python libraries.

---

# Check pip Version

```bash
pip --version
```

---

# Install a Package

Example:

```bash
pip install requests
```

---

Install Multiple Packages

```bash
pip install numpy pandas matplotlib
```

---

# Upgrade a Package

```bash
pip install --upgrade requests
```

---

# Uninstall a Package

```bash
pip uninstall requests
```

---

# View Installed Packages

```bash
pip list
```

---

# Show Package Information

```bash
pip show requests
```

Example Output:

```
Name: requests
Version: 2.32.0
Summary: HTTP library
```

---

# Freeze Installed Packages

```bash
pip freeze
```

Example:

```
numpy==2.0.1
pandas==2.3.0
requests==2.32.0
```

---

# What is requirements.txt?

`requirements.txt` stores all project dependencies.

It allows anyone to install the exact same package versions.

---

# Create requirements.txt

```bash
pip freeze > requirements.txt
```

Example:

```
numpy==2.0.1
pandas==2.3.0
requests==2.32.0
```

---

# Install Dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

This installs every package listed in the file.

---

# Why is requirements.txt Important?

Imagine sharing your project on GitHub.

Another developer only needs:

```bash
git clone repository
cd project

python -m venv venv

pip install -r requirements.txt
```

Everything works exactly as expected.

---

# Recommended Project Structure

```
MyProject/
│
├── venv/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
```

---

# .gitignore

Never upload your virtual environment to GitHub.

Example:

```
venv/
__pycache__/
*.pyc
.env
```

---

# Complete Workflow

## Step 1

Create Project

```bash
mkdir WeatherApp
```

---

## Step 2

Move into Project

```bash
cd WeatherApp
```

---

## Step 3

Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4

Activate Environment

```bash
venv\Scripts\activate
```

---

## Step 5

Install Packages

```bash
pip install requests
```

---

## Step 6

Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Step 7

Run Program

```bash
python app.py
```

---

# Best Practices

✅ Create a virtual environment for every project

✅ Never upload `venv/` to GitHub

✅ Always include `requirements.txt`

✅ Keep packages updated

✅ Remove unused libraries

✅ Use meaningful project names

---

# Common Errors

## Error 1

```
pip not recognized
```

Solution:

Check Python installation and PATH configuration.

---

## Error 2

```
ModuleNotFoundError
```

Solution:

Install the missing package.

```bash
pip install package_name
```

---

## Error 3

```
No module named requests
```

Solution:

Activate the virtual environment first.

---

# Mini Project

## Weather App Setup

### Create Virtual Environment

```bash
python -m venv venv
```

---

Activate

```bash
venv\Scripts\activate
```

---

Install Requests

```bash
pip install requests
```

---

Generate requirements.txt

```bash
pip freeze > requirements.txt
```

---

Run App

```bash
python weather.py
```

---

# Hands-on Exercises

## Beginner

- Create a virtual environment
- Activate it
- Install requests
- Install numpy
- Create requirements.txt

---

## Intermediate

- Install pandas
- Install matplotlib
- Remove a package
- Reinstall using requirements.txt

---

## Advanced

Create two different projects with separate virtual environments and verify that installing a package in one does not affect the other.

---

# Interview Questions

## Beginner

### 1. What is a virtual environment?

A virtual environment is an isolated Python environment for a specific project.

---

### 2. Why do we use virtual environments?

To avoid dependency conflicts between projects.

---

### 3. Which module creates a virtual environment?

`venv`

---

### 4. Command to create a virtual environment?

```bash
python -m venv venv
```

---

### 5. How do you activate a virtual environment?

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

### 6. How do you deactivate it?

```bash
deactivate
```

---

### 7. What is pip?

Python's package manager.

---

### 8. Command to install requests?

```bash
pip install requests
```

---

### 9. What does pip freeze do?

Lists installed packages with their versions.

---

### 10. Why use requirements.txt?

To recreate the same environment on another machine.

---

# Intermediate Questions

11. Difference between global and virtual environments?

12. What is dependency management?

13. Why should venv not be committed to GitHub?

14. Difference between pip install and pip install -r requirements.txt?

15. How do you update an existing package?

---

# Advanced Questions

16. What is semantic versioning?

17. What happens if two packages require different versions of the same dependency?

18. How does pip resolve dependencies?

19. What are lock files?

20. What tools besides venv can manage Python environments? (e.g., Conda, Poetry, Pipenv)

---

# Resources

## Official Documentation

- https://docs.python.org/3/library/venv.html
- https://pip.pypa.io/

## Free Courses

- Python Official Tutorial
- freeCodeCamp Python Course

## Books

- Python Crash Course
- Automate the Boring Stuff with Python

---

# Day 28 Summary

Today you learned:

- Virtual Environments
- pip
- Installing Packages
- Updating Packages
- Removing Packages
- requirements.txt
- Dependency Management
- Best Practices
- Project Structure
- Industry Workflow

---

# GitHub Commit

```bash
git add .
git commit -m "Day 28: Learned Python Virtual Environments, pip and requirements.txt"
git push origin main
```

---

# 🚀 Next Day

**Day 29 – Final Python Project: Personal Assistant CLI**

Topics:

- Project Planning
- Modular Python Code
- API Integration
- File Handling
- Exception Handling
- Virtual Environment
- Packaging
- GitHub Deployment