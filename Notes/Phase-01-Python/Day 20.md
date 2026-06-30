# Day 20 - GitHub Fundamentals & Remote Repositories

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📖 Overview

Welcome to **Day 20** of the roadmap!

Yesterday, you learned the basics of Git and how to track changes locally. Today, you'll learn how to use **GitHub**, the world's largest platform for hosting Git repositories, collaborating with developers, and showcasing your projects.

By the end of today, you'll be able to:

- Understand GitHub
- Create repositories
- Clone repositories
- Connect local Git with GitHub
- Push and pull code
- Work with branches
- Create Pull Requests
- Understand GitHub workflow
- Build your professional GitHub profile

---

# 🎯 Learning Objectives

After completing today's lesson, you will be able to:

- Explain what GitHub is
- Create repositories
- Clone repositories
- Connect local repository to GitHub
- Push local code to GitHub
- Pull latest changes
- Understand GitHub workflow
- Create branches
- Open Pull Requests
- Resolve simple merge conflicts
- Use `.gitignore`
- Write professional README files

---

# What is GitHub?

GitHub is a cloud platform that hosts Git repositories.

Think of it as:

- Cloud storage for code
- Portfolio for developers
- Collaboration platform
- Version control hosting
- Open-source community

Git stores your code locally.

GitHub stores your code online.

---

# Git vs GitHub

| Git | GitHub |
|------|---------|
| Version Control System | Cloud Hosting Platform |
| Works Offline | Requires Internet |
| Installed on Computer | Web Platform |
| Tracks Changes | Hosts Repositories |
| Local Repository | Remote Repository |

---

# Why GitHub Matters?

Companies check your GitHub before interviews.

A strong GitHub profile shows:

- Coding skills
- Project quality
- Consistency
- Documentation skills
- Collaboration experience

For AI Engineers, GitHub is almost as important as your resume.

---

# Create a GitHub Account

Visit:

https://github.com

Create an account and verify your email.

---

# Create a New Repository

Click:

```
New Repository
```

Example:

```
Python-Projects
```

Repository Settings

```
Repository Name

Python-Projects

Visibility

Public

Initialize README

Yes
```

Click

```
Create Repository
```

---

# Clone Repository

Clone downloads a repository from GitHub to your computer.

Command

```bash
git clone https://github.com/username/Python-Projects.git
```

Example

```bash
git clone https://github.com/john/Python-Projects.git
```

Move into repository

```bash
cd Python-Projects
```

---

# Connect Existing Local Repository

Suppose you already have:

```
ExpenseTracker/
```

Initialize Git

```bash
git init
```

Add remote

```bash
git remote add origin https://github.com/username/ExpenseTracker.git
```

Check remote

```bash
git remote -v
```

Output

```
origin
origin
```

---

# Push Code

First Add

```bash
git add .
```

Commit

```bash
git commit -m "Initial Commit"
```

Push

```bash
git push -u origin main
```

Now your project is uploaded to GitHub.

---

# Understanding GitHub Workflow

```
Write Code

↓

git add

↓

git commit

↓

git push

↓

GitHub Repository Updated
```

---

# Pull Latest Changes

If someone changes the repository

Use

```bash
git pull origin main
```

This downloads latest changes.

---

# Fetch

Fetch downloads updates but doesn't merge.

```bash
git fetch
```

Difference

```
Fetch

↓

Downloads only

Pull

↓

Downloads + Merge
```

---

# GitHub Branches

Create Branch

```bash
git branch feature-login
```

Switch Branch

```bash
git checkout feature-login
```

New Method

```bash
git switch feature-login
```

Create and Switch

```bash
git checkout -b feature-login
```

---

# List Branches

```bash
git branch
```

Output

```
main

feature-login
```

Current branch has *

---

# Merge Branch

Switch to main

```bash
git checkout main
```

Merge

```bash
git merge feature-login
```

---

# Delete Branch

```bash
git branch -d feature-login
```

---

# Push Branch

```bash
git push origin feature-login
```

---

# Pull Request (PR)

A Pull Request is a request to merge one branch into another.

Workflow

```
Create Branch

↓

Write Code

↓

Push Branch

↓

Open Pull Request

↓

Code Review

↓

Merge
```

Companies use Pull Requests for every feature.

---

# Fork Repository

Fork creates your own copy of another repository.

```
Original Repository

↓

Fork

↓

Your Repository
```

Useful for Open Source Contributions.

---

# Clone vs Fork

| Clone | Fork |
|--------|------|
| Downloads repository | Copies repository to your account |
| Local copy | GitHub copy |
| Used for own projects | Used for open source |

---

# Repository Structure

Example

```
ExpenseTracker/

│

├── README.md

├── main.py

├── requirements.txt

├── data/

├── assets/

└── LICENSE
```

---

# README.md

Every repository should contain:

```
Project Name

Description

Features

Installation

Usage

Screenshots

Technologies

Future Improvements

Author
```

---

# .gitignore

Ignore files that should not be uploaded.

Example

```
__pycache__/

venv/

.env

*.pyc

.idea/

.vscode/
```

---

# GitHub Issues

Used for

- Bug Reports
- Feature Requests
- Tasks

Example

```
Bug

Calculator crashes on division.
```

---

# GitHub Discussions

Used for

- Questions
- Community
- Ideas

---

# GitHub Stars

People can star your repository.

More stars = More visibility.

---

# GitHub Watch

Receive notifications.

---

# GitHub Releases

Create software versions.

Example

```
v1.0

v2.0

v3.0
```

---

# GitHub Actions

Automates tasks.

Example

- Testing
- Deployment
- CI/CD

You'll learn this in later phases.

---

# Best Practices

✅ Commit frequently

✅ Use meaningful commit messages

✅ Write README

✅ Add screenshots

✅ Use branches

✅ Push regularly

✅ Never upload passwords

---

# Mini Project

## Upload Expense Tracker to GitHub

Steps

1. Create repository
2. Initialize Git
3. Add README
4. Commit
5. Push
6. Verify online

---

# Assignment

Upload the following projects:

- Calculator
- BMI Calculator
- Student Management System
- Weather App
- Expense Tracker
- Notes App

Each project should have:

- README
- requirements.txt (if needed)
- Proper folder structure

---

# Practice Exercises

1. Create a GitHub account.
2. Create a new repository.
3. Clone the repository.
4. Push your first project.
5. Create a new branch.
6. Commit changes.
7. Push the branch.
8. Open a Pull Request.
9. Merge the Pull Request.
10. Delete the branch.

---

# Real-World Workflow

```
Developer

↓

Create Branch

↓

Write Code

↓

Commit

↓

Push

↓

Pull Request

↓

Code Review

↓

Merge

↓

Deploy
```

---

# Interview Questions

## Beginner

### 1. What is GitHub?

GitHub is a cloud-based platform for hosting Git repositories and collaborating on software projects.

---

### 2. Difference between Git and GitHub?

Git is a version control system.

GitHub is a cloud platform for hosting Git repositories.

---

### 3. What is a Repository?

A repository is a folder that stores project files and version history.

---

### 4. What is Clone?

Clone downloads a remote repository to your local machine.

---

### 5. What is Push?

Push uploads local commits to GitHub.

---

### 6. What is Pull?

Pull downloads and merges the latest changes from GitHub.

---

### 7. What is Fetch?

Fetch downloads changes without merging them.

---

### 8. What is a Branch?

A branch is an independent line of development.

---

### 9. What is a Pull Request?

A Pull Request is a request to merge code from one branch into another.

---

### 10. What is Fork?

A fork creates your own copy of another person's repository.

---

## Intermediate

### 11. Difference between Pull and Fetch?

Pull = Fetch + Merge

Fetch = Download only

---

### 12. Why use branches?

To develop features independently without affecting the main code.

---

### 13. What is Origin?

`origin` is the default name for the remote repository.

---

### 14. What is README?

A Markdown file that explains the project.

---

### 15. Why use .gitignore?

To prevent unnecessary or sensitive files from being tracked.

---

## Advanced

### 16. What is GitHub Actions?

A CI/CD automation service provided by GitHub.

---

### 17. Why are Pull Requests important?

They enable code review, discussion, and safe merging.

---

### 18. What is Open Source Contribution?

Contributing improvements, bug fixes, or features to public repositories.

---

### 19. How do you resolve merge conflicts?

By manually editing conflicting files, testing the code, and committing the resolved version.

---

### 20. Why is GitHub important for AI Engineers?

GitHub showcases projects, collaboration skills, coding practices, and serves as a professional portfolio for recruiters.

---

# Day 20 Summary

Today you learned:

- GitHub Fundamentals
- Remote Repositories
- Clone
- Push
- Pull
- Fetch
- Branches
- Pull Requests
- Fork
- README.md
- .gitignore
- Repository Structure
- GitHub Workflow
- Best Practices

---

# GitHub Portfolio Checklist

- ✅ Professional profile picture
- ✅ Clear bio
- ✅ Public repositories
- ✅ Well-written README files
- ✅ Meaningful commit history
- ✅ Organized folder structure
- ✅ Project screenshots
- ✅ License file
- ✅ Topics and tags
- ✅ Consistent activity

---

# Git Commands Cheat Sheet

```bash
git init
git clone <url>
git status
git add .
git commit -m "message"
git push origin main
git pull origin main
git fetch
git branch
git checkout branch-name
git checkout -b new-branch
git merge branch-name
git branch -d branch-name
git remote -v
git log
```

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 20: Learned GitHub fundamentals, remote repositories, branches, and pull requests"
git push origin main
```

---

# 🚀 Next Day

## **Day 21 – Mini Project: Expense Tracker**

Topics:
- Project Planning
- File Organization
- CRUD Operations
- File Handling
- Exception Handling
- Git & GitHub Workflow
- Writing a Professional README
- Project Deployment Preparation