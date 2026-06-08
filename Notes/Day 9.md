# 🚀 Day 9 — NumPy Fundamentals

## 🎯 Goal of Today

By the end of today, you should be able to:

* Understand what NumPy is
* Create and manipulate arrays
* Perform mathematical operations efficiently
* Understand why NumPy is used in AI/ML

---

# 📚 1. What is NumPy?

**NumPy (Numerical Python)** is a powerful Python library used for:

* Fast mathematical computations
* Working with arrays and matrices
* Data processing for Machine Learning models

---

## Why Not Python Lists?

```python
numbers = [1, 2, 3, 4, 5]
```

Python lists are:

* Slower
* Use more memory

NumPy arrays are:

✅ Faster

✅ Memory Efficient

✅ Optimized for Numerical Computations

---

## Installation

```bash
pip install numpy
```

---

## Import NumPy

```python
import numpy as np
```

---

# 📚 2. Creating Arrays

## 1D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

---

## 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
```

---

# 📚 3. Array Attributes

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
```

---

## Learn

### shape

Rows and Columns

### ndim

Number of Dimensions

### size

Total Number of Elements

### dtype

Data Type of Elements

---

# 📚 4. Special Arrays

## Zeros Matrix

```python
np.zeros((3, 3))
```

### Output

```python
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```

---

## Ones Matrix

```python
np.ones((2, 4))
```

---

## Identity Matrix

```python
np.eye(3)
```

### Output

```python
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

# 📚 5. Range Functions

## arange()

```python
np.arange(1, 11)
```

### Output

```python
[1 2 3 4 5 6 7 8 9 10]
```

---

## linspace()

```python
np.linspace(0, 100, 5)
```

### Output

```python
[  0.  25.  50.  75. 100.]
```

---

# 📚 6. Reshape Arrays

```python
arr = np.arange(1, 13)

new_arr = arr.reshape(3, 4)

print(new_arr)
```

### Output

```python
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

---

# 📚 7. Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
```

---

## Slicing

```python
print(arr[1:4])
```

### Output

```python
[20 30 40]
```

---

## 2D Array Access

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[0, 1])
```

### Output

```python
2
```

---

# 📚 8. Mathematical Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

# 📚 9. Aggregation Functions

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
```

### Important for Machine Learning

* Sum
* Mean
* Maximum
* Minimum

---

# 📚 10. Random Numbers

## Random Float Values

```python
np.random.rand(5)
```

---

## Random Integers

```python
np.random.randint(1, 100, 10)
```

### Output

10 random numbers between 1 and 100.

---

# 📚 11. Broadcasting

```python
arr = np.array([1, 2, 3])

print(arr + 10)
```

### Output

```python
[11 12 13]
```

NumPy automatically applies operations to every element.

This feature is called **Broadcasting**.

---

# 🤖 Why AI Engineers Use NumPy

Machine Learning models work heavily with:

* Vectors
* Matrices
* Tensors

Example Matrix:

```text
1 2 3
4 5 6
7 8 9
```

Almost every Machine Learning algorithm performs operations on matrices like these.

NumPy makes these operations:

* Fast
* Efficient
* Scalable

---

# 💻 Today's Practical Tasks

## Task 1

Create:

```python
[5, 10, 15, 20, 25]
```

using NumPy.

---

## Task 2

Create a:

```python
3 x 3
```

matrix of zeros.

---

## Task 3

Create numbers from:

```python
1 - 50
```

using `arange()`.

---

## Task 4

Create a:

```python
4 x 4
```

identity matrix.

---

## Task 5

Generate:

```python
20 random numbers
```

between:

```python
1 - 100
```

---

## Task 6

Find:

* Sum
* Mean
* Max
* Min

of:

```python
[10,20,30,40,50]
```

---

## Task 7

Create numbers:

```python
1 - 16
```

and reshape them into a:

```python
4 x 4
```

matrix.

---

# 🚀 Mini Project (Must Do)

# 🎓 Student Marks Analyzer

```python
marks = np.array([
    75, 80, 65, 90, 88,
    70, 95, 60, 85, 78
])
```

---

## Find

* Highest Marks
* Lowest Marks
* Average Marks
* Total Marks
* Students Scoring Above 80

---

# 📝 Revision Questions

### 1. What is NumPy?

### 2. Difference between Python List and NumPy Array?

### 3. What is `shape`?

### 4. What is `reshape()`?

### 5. Difference between `arange()` and `linspace()`?

### 6. What is Broadcasting?

### 7. Why is NumPy Important in AI?

---

# 📂 GitHub Folder Structure

```bash
Day-09-NumPy-Fundamentals/
│
├── task1_array_creation.py
├── task2_zero_matrix.py
├── task3_arange.py
├── task4_identity_matrix.py
├── task5_random_numbers.py
├── task6_aggregation.py
├── task7_reshape.py
├── student_marks_analyzer.py
└── README.md
```

---

# ✅ End of Day 9 Checklist

* [ ] Installed NumPy
* [ ] Learned Array Creation
* [ ] Practiced Array Attributes
* [ ] Used Special Arrays
* [ ] Learned arange() and linspace()
* [ ] Practiced Reshaping
* [ ] Learned Indexing & Slicing
* [ ] Performed Mathematical Operations
* [ ] Used Aggregation Functions
* [ ] Generated Random Numbers
* [ ] Understood Broadcasting
* [ ] Completed Practical Tasks
* [ ] Built Student Marks Analyzer
* [ ] Uploaded Everything to GitHub

---

# 🚀 AI Engineer Insight

> NumPy is the foundation of the entire Python AI ecosystem.

Libraries like:

* Pandas
* Scikit-Learn
* TensorFlow
* PyTorch

all rely heavily on NumPy under the hood.

Master NumPy today, and Machine Learning becomes much easier tomorrow.
