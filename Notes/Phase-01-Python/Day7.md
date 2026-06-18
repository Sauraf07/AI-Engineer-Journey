# Day 7 - Python Loops (`for`, `while`, `break`, `continue`, `range()`)

## 📌 Overview

Loops are used to execute a block of code repeatedly. Instead of writing the same code multiple times, loops help automate repetitive tasks efficiently.

In Python, there are two main types of loops:

1. `for` Loop
2. `while` Loop

Additionally, Python provides loop control statements:

- `break`
- `continue`

And a built-in function:

- `range()`

---

# 🎯 Learning Objectives

By the end of Day 7, I can:

- Understand the purpose of loops.
- Use `for` loops to iterate over sequences.
- Use `while` loops for condition-based repetition.
- Control loop execution using `break` and `continue`.
- Generate sequences using `range()`.
- Solve real-world programming problems using loops.

---

# 🔹 Why Loops Matter

Loops are one of the most important programming concepts because they help:

- Process large amounts of data.
- Automate repetitive tasks.
- Build games and applications.
- Work with files and databases.
- Implement AI/ML algorithms efficiently.

---

# 🔹 The `for` Loop

A `for` loop is used to iterate over a sequence such as a list, string, tuple, or range.

## Syntax

```python
for item in sequence:
    # code block
```

## Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

# 🔹 Loop Through a String

```python
name = "Python"

for char in name:
    print(char)
```

### Output

```text
P
y
t
h
o
n
```

---

# 🔹 Loop Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Mango
```

---

# 🔹 The `while` Loop

A `while` loop runs as long as a condition remains true.

## Syntax

```python
while condition:
    # code block
```

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

---

# 🔹 Infinite Loop

```python
while True:
    print("Hello")
```

⚠️ This loop runs forever until manually stopped.

---

# 🔹 `break` Statement

The `break` statement immediately exits the loop.

## Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

# 🔹 `continue` Statement

The `continue` statement skips the current iteration and moves to the next one.

## Example

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
0
1
2
4
5
```

---

# 🔹 `range()` Function

The `range()` function generates a sequence of numbers.

## Example 1

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

## Example 2

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

---

## Example 3

```python
for i in range(0, 10, 2):
    print(i)
```

### Output

```text
0
2
4
6
8
```

---

# 🔹 Real-World Example

## ATM Login Attempts

```python
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1234":
        print("Login Successful")
        break

    attempts -= 1
    print("Wrong PIN")

print("Account Locked")
```

---

# 🛠️ Practice Exercises

## Beginner

### 1. Print Numbers 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

### 2. Print Even Numbers

```python
for i in range(2, 21, 2):
    print(i)
```

---

### 3. Print Multiplication Table

```python
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num * i)
```

---

# 🚀 Mini Project: Number Guessing Game

## Problem Statement

Create a game where:

- User guesses a secret number.
- Program checks the guess.
- Game ends when correct answer is found.

## Solution

```python
secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    print("Try Again!")
```

---

# 🧠 Interview Questions

## Basic Level

### 1. What is a loop?

A loop is a programming structure that repeatedly executes a block of code until a condition is met.

---

### 2. What are the types of loops in Python?

- `for` loop
- `while` loop

---

### 3. When should you use a `for` loop?

Use a `for` loop when the number of iterations is known.

---

### 4. When should you use a `while` loop?

Use a `while` loop when iterations depend on a condition.

---

### 5. What does `range()` do?

`range()` generates a sequence of numbers.

Example:

```python
range(5)
```

Output:

```text
0, 1, 2, 3, 4
```

---

## Intermediate Level

### 6. What is the difference between `break` and `continue`?

| break | continue |
|---------|---------|
| Stops the loop completely | Skips current iteration |
| Exits loop | Continues loop |

---

### 7. What is an infinite loop?

A loop that never stops because its condition always remains true.

Example:

```python
while True:
    print("Infinite")
```

---

### 8. Can a `for` loop be nested?

Yes.

Example:

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

### 9. What is loop nesting?

Using one loop inside another loop.

---

### 10. What is the time complexity of a simple loop?

A loop running `n` times has:

```text
O(n)
```

time complexity.

---

# 📚 Key Takeaways

- `for` loops iterate over sequences.
- `while` loops run based on conditions.
- `break` exits the loop.
- `continue` skips an iteration.
- `range()` generates sequences of numbers.
- Loops are fundamental for automation, AI, ML, and software development.

---

# 🎯 Day 7 Completion Checklist

- [ ] Learned `for` loops
- [ ] Learned `while` loops
- [ ] Practiced `break`
- [ ] Practiced `continue`
- [ ] Understood `range()`
- [ ] Built Number Guessing Game
- [ ] Solved 10+ loop-based problems
- [ ] Uploaded code to GitHub

## 🔥 Progress

✅ Day 7 Completed  
🚀 Moving Towards AI/ML & GenAI Engineering Journey