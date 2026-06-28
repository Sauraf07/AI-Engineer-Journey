# Day 18 - Python Problem Solving & Logic Building

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Machine Learning Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of Day 18, you will be able to:

- Strengthen your Python programming skills through problem-solving
- Improve logical thinking and analytical skills
- Solve common coding interview problems
- Write optimized and readable Python code
- Understand different approaches to solving problems
- Prepare for coding rounds in internships and placements
- Gain confidence in solving LeetCode and HackerRank problems

---

# 📖 Why Problem Solving Matters?

Problem-solving is one of the most important skills for every software engineer.

Companies don't just hire developers who know syntax—they hire developers who can think logically and solve real-world problems.

Whether you're applying for:

- AI Engineer
- ML Engineer
- Python Developer
- Backend Developer
- GenAI Engineer

you will almost always face coding questions during interviews.

---

# 🚀 Problem Solving Strategy

Before writing code, follow these steps:

1. Read the problem carefully.
2. Understand the input and output.
3. Identify edge cases.
4. Think of a simple approach.
5. Optimize if necessary.
6. Write clean code.
7. Test with multiple inputs.

---

# Problem 1 - Reverse a String

## Problem Statement

Write a Python program to reverse a string.

### Solution 1

```python
text = input("Enter a string: ")

print(text[::-1])
```

### Solution 2

```python
text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)
```

---

# Problem 2 - Check Palindrome

## Problem Statement

Determine whether a string is a palindrome.

```python
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# Problem 3 - Find Largest Number

```python
numbers = [10, 45, 2, 89, 54]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
```

---

# Problem 4 - Count Vowels

```python
text = input("Enter string: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)
```

---

# Problem 5 - Factorial

```python
num = int(input("Enter number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)
```

---

# Problem 6 - Fibonacci Series

```python
n = int(input("Enter terms: "))

a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

# Problem 7 - Prime Number

```python
num = int(input("Enter number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
```

---

# Problem 8 - Remove Duplicates from List

```python
numbers = [1,2,2,3,4,4,5]

unique = list(set(numbers))

print(unique)
```

---

# Problem 9 - Second Largest Number

```python
numbers = [5,10,15,25,20]

numbers.sort()

print(numbers[-2])
```

---

# Problem 10 - Count Frequency

```python
text = input("Enter text: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char,0)+1

print(frequency)
```

---

# Problem 11 - Sum of Digits

```python
num = input("Enter number: ")

total = 0

for digit in num:
    total += int(digit)

print(total)
```

---

# Problem 12 - Armstrong Number

```python
num = int(input("Enter number: "))

digits = len(str(num))

total = 0

temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")
```

---

# Problem 13 - Count Words

```python
sentence = input("Enter sentence: ")

words = sentence.split()

print(len(words))
```

---

# Problem 14 - Find Even Numbers

```python
numbers = [1,2,3,4,5,6,7,8]

even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

print(even)
```

---

# Problem 15 - Merge Two Lists

```python
list1 = [1,2,3]
list2 = [4,5,6]

merged = list1 + list2

print(merged)
```

---

# 🎯 Coding Practice

## HackerRank Problems

Complete at least **15 Easy** problems.

Suggested topics:

- Introduction
- Basic Data Types
- Loops
- Strings
- Lists
- Dictionaries
- Functions

---

## LeetCode Problems

Complete at least **15 Easy** problems.

Suggested topics:

- Arrays
- Strings
- Hash Tables
- Loops
- Sorting
- Math
- Simulation

---

# ⭐ Bonus Challenge Problems

Try solving these without looking at the solution.

1. Check Anagram
2. Rotate List
3. Missing Number
4. Maximum Subarray Sum
5. Move Zeroes
6. Valid Parentheses
7. Two Sum
8. Merge Sorted Lists
9. Binary Search
10. Longest Common Prefix

---

# 💡 Problem Solving Tips

- Start with the brute-force solution.
- Optimize only after the correct solution works.
- Break complex problems into smaller parts.
- Dry run your code on paper.
- Use meaningful variable names.
- Practice consistently.

---

# 🏆 Mini Project

# Student Result Analyzer

## Requirements

- Take marks of multiple students.
- Calculate total marks.
- Calculate average marks.
- Find highest marks.
- Find lowest marks.
- Display pass/fail status.
- Display grade.

### Sample Output

```text
Student Results

Total Marks : 450

Average : 90

Highest : 98

Lowest : 75

Grade : A
```

---

# 📝 Practice Assignment

Create programs for:

- Number Guessing Game
- Password Strength Checker
- ATM Simulator
- Expense Tracker Logic
- Student Record Manager
- Library Management Logic
- Voting Eligibility Checker
- Temperature Converter
- Shopping Cart Calculator
- Electricity Bill Calculator

---

# 🎤 Interview Questions

## Beginner Level

### 1. Why is problem-solving important?

Problem-solving helps developers build efficient, scalable, and reliable software solutions.

---

### 2. What is algorithmic thinking?

Breaking a problem into logical steps before writing code.

---

### 3. What is time complexity?

Time complexity measures how the execution time of an algorithm grows as the input size increases.

---

### 4. What is space complexity?

Space complexity measures how much additional memory an algorithm uses.

---

### 5. What is the difference between `==` and `is`?

- `==` compares values.
- `is` compares object identities (memory locations).

---

### 6. How do you reverse a string in Python?

```python
text[::-1]
```

---

### 7. How do you remove duplicates from a list?

```python
list(set(my_list))
```

---

### 8. What is a palindrome?

A palindrome is a word, phrase, or number that reads the same forward and backward.

---

### 9. How do you check if a number is prime?

Test divisibility from `2` to `√n`.

---

### 10. What is the purpose of loops?

Loops allow repeated execution of a block of code until a condition is met.

---

# Intermediate Level

### 11. Difference between list and tuple?

| List | Tuple |
|------|------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Slower | Faster |

---

### 12. What is list comprehension?

A concise way to create lists.

```python
numbers = [x*x for x in range(5)]
```

---

### 13. What is dictionary lookup complexity?

Average time complexity is **O(1)**.

---

### 14. What is the difference between recursion and iteration?

- Recursion uses function calls.
- Iteration uses loops.

---

### 15. Why should code be optimized?

To improve performance, reduce memory usage, and handle large datasets efficiently.

---

# Advanced Level

### 16. What is Big-O notation?

Big-O notation describes the upper bound of an algorithm's time or space complexity.

Examples:

- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n²)

---

### 17. Why are hash tables fast?

Because they use hashing to achieve near O(1) average lookup time.

---

### 18. How do you debug logical errors?

- Print intermediate values.
- Use a debugger.
- Test edge cases.
- Read the problem carefully.

---

### 19. How do you improve coding speed?

- Practice daily.
- Learn common patterns.
- Understand data structures.
- Solve previous interview questions.

---

### 20. How many coding questions should beginners solve?

Aim for:

- 100 Easy
- 75 Medium
- 25 Hard

over time for strong interview preparation.

---

# 📚 Recommended Platforms

## Coding Practice

- LeetCode
- HackerRank
- Codewars
- GeeksforGeeks Practice
- Coding Ninjas Studio

---

# 📖 Recommended Books

- Grokking Algorithms
- Python Crash Course
- Elements of Programming Interviews in Python
- Cracking the Coding Interview

---

# ✅ Day 18 Summary

Today you learned:

- Problem-solving strategy
- Logical thinking
- String problems
- Number problems
- List problems
- Dictionary problems
- Common coding interview patterns
- Time complexity basics
- Student Result Analyzer project
- Coding interview preparation

---

# 🎯 Milestone

By the end of Day 18, you should be able to:

- Solve 15+ easy coding problems independently.
- Explain your approach before writing code.
- Write clean and readable Python solutions.
- Identify basic time complexity.
- Feel confident attempting beginner coding interviews.

---

# 💻 GitHub Commit Message

```bash
git add .
git commit -m "Day 18: Solved Python Problem Solving Challenges and Improved Coding Logic"
git push origin main
```

---

# 🚀 Next Day

**Day 19: Git & GitHub Fundamentals**

Topics:

- Version Control
- Git Basics
- Git Commands
- GitHub Repositories
- Branching
- Commits
- Push & Pull
- Collaboration Workflow
- Upload Your Python Projects