# Day 19 - Git Fundamentals | Version Control for Developers

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 📖 Table of Contents

- Introduction to Git
- What is Version Control?
- Why Git?
- Git vs GitHub
- Installing Git
- Configuring Git
- Creating Your First Repository
- Basic Git Workflow
- Essential Git Commands
- Git File States
- Viewing History
- Undoing Changes
- Hands-on Project
- Best Practices
- Interview Questions
- Practice Exercises
- Resources
- Day 19 Summary

---

# 🎯 Learning Objectives

By the end of Day 19, you will be able to:

- Understand Version Control Systems (VCS)
- Understand Git and GitHub
- Install and configure Git
- Create and manage Git repositories
- Track project changes
- Commit changes with meaningful messages
- View commit history
- Understand Git workflow
- Upload code to GitHub
- Answer common Git interview questions

---

# What is Version Control?

Version Control is a system that records changes to files over time so you can:

- Track every change
- Restore previous versions
- Collaborate with teams
- Manage project history

Without Version Control:

```
Project/
├── project_final.py
├── project_final2.py
├── project_final_latest.py
├── project_final_latest_updated.py
```

With Git:

```
Project/
├── project.py
└── Complete History Managed by Git
```

---

# What is Git?

Git is a **Distributed Version Control System (DVCS)** created by **Linus Torvalds** in 2005.

Git helps developers:

- Track code changes
- Work in teams
- Maintain project history
- Revert mistakes
- Manage multiple versions

---

# Why Git?

Git is one of the most important tools for software developers.

Benefits:

- Tracks changes
- Fast and lightweight
- Easy collaboration
- Supports branching
- Safe backups
- Widely used in the industry

---

# Git vs GitHub

| Git | GitHub |
|------|---------|
| Version Control System | Cloud hosting platform |
| Installed on your computer | Website for Git repositories |
| Tracks changes | Stores repositories online |
| Works offline | Requires internet for syncing |

### Example

- Git manages your project locally.
- GitHub stores your project online.

---

# Installing Git

Download Git from:

https://git-scm.com/

Verify installation:

```bash
git --version
```

Example Output:

```text
git version 2.xx.x
```

---

# Configure Git

Set your username:

```bash
git config --global user.name "Your Name"
```

Set your email:

```bash
git config --global user.email "your@email.com"
```

Check configuration:

```bash
git config --list
```

---

# What is a Repository?

A repository (repo) is a folder where Git tracks all changes.

Example:

```
ExpenseTracker/
```

Initialize Git:

```bash
git init
```

Output:

```
Initialized empty Git repository
```

---

# Git Workflow

```
Working Directory
        │
        ▼
git add
        │
        ▼
Staging Area
        │
        ▼
git commit
        │
        ▼
Local Repository
        │
        ▼
GitHub Repository
```

---

# Git File States

```
Untracked
      │
git add
      ▼
Staged
      │
git commit
      ▼
Committed
```

---

# Essential Git Commands

## Check Status

```bash
git status
```

Shows:

- New files
- Modified files
- Deleted files

---

## Add Specific File

```bash
git add app.py
```

---

## Add All Files

```bash
git add .
```

---

## Commit Changes

```bash
git commit -m "Add login feature"
```

A good commit message should describe **what changed**.

Examples:

```text
Fix login bug
Add expense tracker
Update README
```

---

## View Commit History

```bash
git log
```

Compact version:

```bash
git log --oneline
```

---

## View Differences

```bash
git diff
```

Shows changes before committing.

---

## Rename a File

```bash
git mv old.py new.py
```

---

## Delete a File

```bash
git rm file.py
```

---

# Understanding Git Status

Suppose you create:

```
main.py
```

Run:

```bash
git status
```

Output:

```
Untracked file:
main.py
```

Add file:

```bash
git add main.py
```

Run:

```bash
git status
```

Output:

```
Changes to be committed
```

Commit:

```bash
git commit -m "Initial commit"
```

Now:

```
Working tree clean
```

---

# Creating Your First Project

Create a folder:

```
Calculator
```

Initialize Git:

```bash
git init
```

Create:

```
calculator.py
```

Add:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial Calculator Project"
```

---

# Real-World Git Workflow

```
Create Project

↓

git init

↓

Write Code

↓

git status

↓

git add .

↓

git commit

↓

Repeat
```

---

# Best Practices

✅ Commit often

✅ Write meaningful commit messages

✅ Keep commits small

✅ Test code before committing

✅ Use Git every day

---

# Mini Project

## Expense Tracker

Create:

```
ExpenseTracker/
│
├── main.py
├── expenses.txt
└── README.md
```

Initialize Git:

```bash
git init
```

Commit after every feature:

- Add expense
- Delete expense
- Monthly report

---

# Practice Exercises

## Beginner

1. Install Git.
2. Configure username and email.
3. Create a repository.
4. Create a Python file.
5. Check Git status.
6. Add the file.
7. Commit the file.
8. View commit history.
9. Modify the file.
10. Commit again.

---

# Git Command Cheat Sheet

| Command | Purpose |
|----------|----------|
| `git init` | Initialize repository |
| `git status` | Check repository status |
| `git add file` | Stage specific file |
| `git add .` | Stage all files |
| `git commit -m "msg"` | Save changes |
| `git log` | View history |
| `git log --oneline` | Compact history |
| `git diff` | Show changes |
| `git mv` | Rename file |
| `git rm` | Delete file |
| `git config --list` | View configuration |
| `git --version` | Check Git version |

---

# Common Mistakes

❌ Forgetting to commit regularly

❌ Using unclear commit messages

```
update
fix
changes
```

Better:

```
Add user authentication
Fix API response handling
Update README documentation
```

---

# Interview Questions

## Beginner

### 1. What is Git?

Git is a distributed version control system used to track changes in source code.

---

### 2. What is Version Control?

A system that records file changes over time, allowing developers to restore previous versions and collaborate.

---

### 3. What is GitHub?

GitHub is a cloud-based platform that hosts Git repositories and enables collaboration.

---

### 4. Difference between Git and GitHub?

| Git | GitHub |
|------|---------|
| Local tool | Online platform |
| Tracks changes | Hosts repositories |

---

### 5. What does `git init` do?

Initializes a new Git repository.

---

### 6. What does `git status` do?

Shows the current state of the repository.

---

### 7. What does `git add` do?

Moves files from the Working Directory to the Staging Area.

---

### 8. What does `git commit` do?

Creates a snapshot of staged changes.

---

### 9. What is a commit?

A saved snapshot of your project at a specific point in time.

---

### 10. What is the Staging Area?

An intermediate area where changes are prepared before committing.

---

## Intermediate

### 11. What is a Repository?

A folder where Git tracks project files and their history.

---

### 12. What is the Working Directory?

The current directory where you edit project files.

---

### 13. What is HEAD?

HEAD points to the latest commit in the current branch.

---

### 14. Why should commit messages be meaningful?

Clear commit messages make project history easier to understand and maintain.

---

### 15. What does `git diff` do?

Shows differences between the current working directory and the last commit.

---

## Advanced (Preview)

### 16. What is Branching?

Creating separate lines of development without affecting the main codebase.

---

### 17. What is Merge?

Combining changes from one branch into another.

---

### 18. What is Merge Conflict?

A conflict that occurs when Git cannot automatically combine changes.

---

### 19. What is Pull Request?

A request to merge changes into another branch, commonly used on GitHub.

---

### 20. Why is Git important for AI Engineers?

AI projects involve experiments, datasets, notebooks, APIs, and deployment code. Git enables version tracking, collaboration, reproducibility, and safe experimentation.

---

# Resources

## Official Documentation

- https://git-scm.com/doc

## Free Learning

- https://learngitbranching.js.org/
- https://www.atlassian.com/git

## YouTube

- freeCodeCamp Git Course
- Traversy Media Git Crash Course
- CodeWithHarry Git & GitHub Tutorial

## Books

- Pro Git (Free)
- Version Control with Git

---

# Assignment

Complete the following:

- Install Git
- Configure Git
- Create a new repository
- Add a Python project
- Make at least **5 commits** with meaningful messages
- Push the project to GitHub (you'll learn this in the next lesson)

---

# Day 19 Summary

Today you learned:

- ✅ What is Git
- ✅ What is Version Control
- ✅ Git vs GitHub
- ✅ Installing Git
- ✅ Configuring Git
- ✅ Creating repositories
- ✅ Git workflow
- ✅ File states
- ✅ Essential Git commands
- ✅ Viewing commit history
- ✅ Best practices
- ✅ Interview questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 19: Learned Git Fundamentals and Version Control"
git push origin main
```

---

# 🚀 Next Day

**Day 20 – GitHub & Remote Repositories**

Topics:
- Creating GitHub repositories
- Connecting local Git with GitHub
- `git remote`
- `git push`
- `git pull`
- `git clone`
- Introduction to Branches
- Uploading your first project to GitHub