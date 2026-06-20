# Day 10: Recursion in Python 🚀

> Part of My AI/ML & Generative AI Engineering Journey

---

# 📌 What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem.

Instead of using loops, recursion breaks a large problem into smaller versions of the same problem until it reaches a stopping condition.

### Basic Structure

```python
def recursive_function():
    # Base Case
    if condition:
        return

    # Recursive Call
    recursive_function()
```

---

# Why Learn Recursion?

Recursion is important because many computer science concepts and algorithms are naturally recursive.

### Real-World Uses

- File System Traversal
- Tree Data Structures
- Graph Algorithms
- Backtracking Problems
- Dynamic Programming
- Divide and Conquer Algorithms
- AI Search Algorithms

### Interview Importance

Many companies ask recursion-based questions because they test:

- Problem-solving ability
- Logical thinking
- Understanding of function calls
- Stack memory concepts

---

# Understanding Recursion Step by Step

A recursive function contains two important parts:

## 1. Base Case

The condition that stops recursion.

Without a base case, recursion will continue forever and cause:

```text
RecursionError: maximum recursion depth exceeded
```

Example:

```python
if n == 0:
    return
```

---

## 2. Recursive Case

The function calls itself with a smaller problem.

Example:

```python
return n * factorial(n - 1)
```

---

# Call Stack in Recursion

Every recursive call gets stored in memory inside a stack.

Example:

```python
factorial(4)
```

Calls:

```text
factorial(4)
factorial(3)
factorial(2)
factorial(1)
```

Then returns:

```text
1
2
6
24
```

This process is called:

### Stack Unwinding

---

# Example 1: Print Numbers Using Recursion

```python
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

Output:

```text
1
2
3
4
5
```

---

# Example 2: Sum of Numbers

Find:

```text
1 + 2 + 3 + 4 + 5
```

### Recursive Solution

```python
def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))
```

Output:

```text
15
```

---

# Factorial Using Recursion

## What is Factorial?

```text
5! = 5 × 4 × 3 × 2 × 1
```

Result:

```text
120
```

---

## Recursive Formula

```text
n! = n × (n-1)!
```

Base Case:

```text
1! = 1
```

---

## Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

---

# Dry Run of Factorial

```python
factorial(5)
```

Step 1:

```text
5 * factorial(4)
```

Step 2:

```text
5 * 4 * factorial(3)
```

Step 3:

```text
5 * 4 * 3 * factorial(2)
```

Step 4:

```text
5 * 4 * 3 * 2 * factorial(1)
```

Base Case:

```text
factorial(1) = 1
```

Now return:

```text
5 × 4 × 3 × 2 × 1 = 120
```

---

# Fibonacci Series Using Recursion

## Fibonacci Sequence

```text
0 1 1 2 3 5 8 13 21 ...
```

Formula:

```text
F(n) = F(n-1) + F(n-2)
```

---

## Code

```python
def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```

Output:

```text
8
```

---

# Print Fibonacci Series

```python
def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))
```

Output:

```text
0
1
1
2
3
5
8
13
21
34
```

---

# Advantages of Recursion

✅ Cleaner Code

✅ Easy to Understand

✅ Useful for Tree Problems

✅ Useful for Graph Problems

✅ Natural Problem Solving Approach

---

# Disadvantages of Recursion

❌ More Memory Usage

❌ Slower Than Loops

❌ Stack Overflow Risk

❌ Hard Debugging

---

# Recursion vs Loop

| Feature | Recursion | Loop |
|----------|------------|--------|
| Memory Usage | High | Low |
| Speed | Slower | Faster |
| Readability | Better | Moderate |
| Stack Usage | Yes | No |
| Complexity | Easier for some problems | Easier for iterative problems |

---

# Common Recursion Problems

## Easy

- Factorial
- Fibonacci
- Sum of Numbers
- Reverse String
- Power Function

## Medium

- Palindrome Check
- Binary Search
- Tower of Hanoi
- Merge Sort
- Quick Sort

## Hard

- N Queens
- Sudoku Solver
- Rat in a Maze
- Word Search
- Graph DFS

---

# Practice Questions

## Beginner

### Question 1

Print numbers from 1 to N using recursion.

---

### Question 2

Print numbers from N to 1 using recursion.

---

### Question 3

Find factorial of a number.

---

### Question 4

Find sum of first N natural numbers.

---

### Question 5

Find power of a number.

Example:

```text
2^5 = 32
```

---

# Mini Project

## Recursive Math Toolkit

Features:

- Factorial Calculator
- Fibonacci Generator
- Power Calculator
- Sum of N Numbers

Example Menu:

```text
1. Factorial
2. Fibonacci
3. Power
4. Sum of Numbers
5. Exit
```

---

# Interview Questions and Answers

## 1. What is recursion?

Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem until a base case is reached.

---

## 2. What is a base case?

A base case is the stopping condition that prevents infinite recursive calls.

Example:

```python
if n == 0:
    return 1
```

---

## 3. What happens if recursion has no base case?

The function keeps calling itself indefinitely and eventually throws:

```text
RecursionError
```

---

## 4. What is the call stack?

The call stack is a memory structure that stores function calls until they are completed.

---

## 5. Why is recursion important?

Recursion helps solve complex problems such as:

- Trees
- Graphs
- Backtracking
- Dynamic Programming

---

## 6. Difference between recursion and iteration?

| Recursion | Iteration |
|------------|------------|
| Uses function calls | Uses loops |
| More memory | Less memory |
| Cleaner code | Faster execution |

---

## 7. What is stack overflow?

Stack overflow occurs when too many recursive calls consume all available stack memory.

---

## 8. Which data structure supports recursion?

```text
Stack
```

---

## 9. Is recursion always better than loops?

No.

Loops are generally faster and more memory-efficient, but recursion can provide cleaner solutions for hierarchical problems.

---

## 10. Name some algorithms that use recursion.

- Merge Sort
- Quick Sort
- DFS
- Binary Search
- Tree Traversal
- Backtracking Algorithms

---

# Resources

## Documentation

- https://docs.python.org/3/

## Practice Platforms

- LeetCode
- HackerRank
- GeeksforGeeks

## YouTube

- Corey Schafer
- CodeWithHarry
- freeCodeCamp

---

# Day 10 Assignment

Complete the following:

- [ ] Factorial using Recursion
- [ ] Fibonacci using Recursion
- [ ] Sum of N Numbers
- [ ] Power Function
- [ ] Reverse String using Recursion
- [ ] Recursive Math Toolkit Project
- [ ] Push Code to GitHub

---

# Day 10 Outcome

After completing Day 10, you should be able to:

✅ Understand recursion deeply

✅ Write recursive functions confidently

✅ Solve factorial and Fibonacci problems

✅ Understand the call stack

✅ Explain recursion in interviews

✅ Build recursive problem-solving skills for DSA and AI/ML algorithms

---

⭐ If you found this useful, consider giving the repository a star and follow my journey toward becoming an AI/ML & Generative AI Engineer.