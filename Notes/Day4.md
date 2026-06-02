# 🚀 Day 4 — File Handling + Exception Handling in Python

## 🎯 Goal of Day 4

Today is important because real AI applications constantly:

* Read files
* Save data
* Handle errors
* Work with logs
* Process documents

⚡ These concepts are used everywhere in AI engineering.

---

# 📚 Topics To Learn Today

---

# 1️⃣ File Handling in Python

Understand:

* Opening files
* Reading files
* Writing files
* Appending data
* Closing files

---

# 📂 Learn These Functions

---

## 📖 Open File

```python id="e2vx0g"
file = open("notes.txt", "r")
```

---

## 📌 File Modes

```python id="u9v9ae"
"r" → Read
"w" → Write
"a" → Append
"x" → Create New File
```

---

## 📖 Read File

```python id="8wd4cr"
file = open("notes.txt", "r")

print(file.read())

file.close()
```

---

## ✍️ Write File

```python id="e0j8qj"
file = open("notes.txt", "w")

file.write("Hello Boss")

file.close()
```

---

## ➕ Append File

```python id="8sv8x3"
file = open("notes.txt", "a")

file.write("\nNew line added")

file.close()
```

---

# 2️⃣ Using `with open()`

## ⭐ VERY IMPORTANT

Best practice:

```python id="s8v1ic"
with open("notes.txt", "r") as file:
    print(file.read())
```

---

## ✅ Why Use It?

* Automatically closes file
* Cleaner code
* Used in real-world projects

---

# 3️⃣ Exception Handling

AI applications should not crash easily.

---

## 📘 Learn

* `try`
* `except`
* `finally`

---

## 🛡️ Basic Example

```python id="7m0h9x"
try:
    num = int(input("Enter number: "))
    print(num)
except:
    print("Invalid input")
```

---

## ⚠️ Multiple Exceptions

```python id="5bqvpf"
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 🔚 Finally Block

```python id="o7m6el"
try:
    print("Hello")
except:
    print("Error")
finally:
    print("Program ended")
```

---

# 4️⃣ Important Errors To Learn

Understand these errors:

* `ValueError`
* `ZeroDivisionError`
* `FileNotFoundError`
* `IndexError`
* `KeyError`

---

# 💻 Practice Tasks (Must Do)

---

# 🟢 Task 1 — Read File

Create:

```bash id="84z0m5"
data.txt
```

Write some text manually.

Your Python program should:

* Open file
* Read content
* Print content

---

# 🟢 Task 2 — Notes Writer

Program should:

* Take note from user
* Save into `notes.txt`

---

# 🟢 Task 3 — Append Notes

Program should:

* Add new notes without deleting old notes

---

# 🟢 Task 4 — Error Handling

Take number input from user.

Handle:

* Invalid input

---

# 🟢 Task 5 — Safe Calculator

Make calculator with exception handling.

Handle:

* Divide by zero
* Wrong input

---

# 🟢 Task 6 — File Checker

Ask user for filename.

If file exists:

* Read it

Otherwise:

* Show proper error message

---

# 🚀 Mini Project (Important)

# 📝 CLI Notes App

---

## Features

* Add note
* View notes
* Exit

---

## Concepts Used

* File handling
* Exception handling
* Loops
* Functions

---

# 📂 Folder Structure

```bash id="9g8q3u"
Day-4/
│
├── notes_app.py
├── calculator.py
├── file_reader.py
├── notes.txt
└── README.md
```

---

# 📤 What To Upload On GitHub Today

Upload:

* All practice programs
* Mini project
* README.md

---

# 📝 Commit Message

```bash id="6u2m4f"
Day 4 - File Handling and Exception Handling
```

---

# 📚 Resources

## 📖 Python File Handling

* Python File Handling Docs

---

## ⚠️ Exception Handling

* Python Errors and Exceptions

---

## 🎥 Video Resource

* CodeWithHarry Python Tutorial

---

# 🎯 End Goal of Day 4

By the end of today you should be able to:

* Read/write files
* Store user data
* Handle errors safely
* Build small terminal apps

---

# 🧠 Why This Matters for AI Engineering

These skills are heavily used later in:

* RAG systems
* Chat history management
* AI memory systems
* PDF processing
* Vector DB storage
* AI logging systems

---

# ✅ End of Day 4 Checklist

* [ ] Learned File Handling
* [ ] Practiced Reading/Writing Files
* [ ] Used `with open()`
* [ ] Learned Exception Handling
* [ ] Handled Common Errors
* [ ] Built CLI Notes App
* [ ] Uploaded Code to GitHub
* [ ] Updated README.md

---

# 🚀 Keep Building

Real AI applications rely heavily on handling data and errors properly.

Today’s skills are part of the foundation of every strong AI system 🔥
