# 🚀 Day 33 - Introduction to NumPy

> **Phase 2: Data Analysis & Machine Learning Foundation**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

* Understand what NumPy is and why it is important
* Install and import NumPy
* Create NumPy arrays
* Differentiate between Python Lists and NumPy Arrays
* Perform basic array operations
* Understand array attributes
* Work with different data types
* Write efficient numerical programs
* Answer common NumPy interview questions

---

# 📖 What is NumPy?

**NumPy (Numerical Python)** is the core library for numerical computing in Python.

It provides:

* Fast multidimensional arrays
* Mathematical operations
* Statistical functions
* Linear algebra
* Random number generation
* Foundation for Machine Learning and Deep Learning

---

# 🌍 Why NumPy Matters

Almost every AI and Machine Learning library is built on top of NumPy.

Examples include:

* Pandas
* Scikit-learn
* TensorFlow
* PyTorch
* OpenCV
* SciPy

If you want to become an AI Engineer, NumPy is one of the most important libraries to master.

---

# 💡 Real-Life Analogy

Imagine you have marks of **10 lakh students**.

Using a normal Python list to calculate averages takes more memory and is slower.

NumPy stores data efficiently and performs operations much faster using optimized C code behind the scenes.

---

# 🛠 Installing NumPy

```bash
pip install numpy
```

Check the installation:

```python
import numpy as np

print(np.__version__)
```

---

# 📥 Importing NumPy

The standard convention is:

```python
import numpy as np
```

Almost every professional Python developer uses `np` as the alias.

---

# 📌 Creating Arrays

## From a List

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output

```text
[10 20 30 40 50]
```

---

## Creating a Float Array

```python
import numpy as np

prices = np.array([99.5, 150.75, 250.25])

print(prices)
```

---

## Creating a Mixed Array

```python
import numpy as np

data = np.array([1, "Python", 3.5])

print(data)
```

NumPy converts the elements into a common compatible type.

---

# 📊 Array Dimensions

## 1D Array

```python
arr = np.array([1, 2, 3, 4])
```

---

## 2D Array

```python
arr = np.array([
    [1, 2],
    [3, 4]
])
```

---

## 3D Array

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])
```

---

# 🔍 Array Attributes

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
```

### Shape

```python
print(arr.shape)
```

Output

```text
(2, 2)
```

---

### Number of Dimensions

```python
print(arr.ndim)
```

Output

```text
2
```

---

### Total Elements

```python
print(arr.size)
```

Output

```text
4
```

---

### Data Type

```python
print(arr.dtype)
```

Output

```text
int64
```

*(The exact type may vary depending on your operating system.)*

---

# 🔢 Creating Special Arrays

## Zeros

```python
import numpy as np

arr = np.zeros((3, 3))

print(arr)
```

---

## Ones

```python
arr = np.ones((2, 4))

print(arr)
```

---

## Full Array

```python
arr = np.full((2, 2), 100)

print(arr)
```

---

## Identity Matrix

```python
arr = np.eye(4)

print(arr)
```

---

# 📈 Creating Number Sequences

## arange()

```python
arr = np.arange(1, 11)

print(arr)
```

Output

```text
[1 2 3 4 5 6 7 8 9 10]
```

---

## linspace()

```python
arr = np.linspace(0, 100, 5)

print(arr)
```

Output

```text
[  0.  25.  50.  75. 100.]
```

---

# ⚡ Basic Mathematical Operations

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 2)
```

Output

```text
[15 25 35]
[ 5 15 25]
[20 40 60]
[ 5. 10. 15.]
```

---

# 📊 Aggregate Functions

```python
arr = np.array([5, 10, 15, 20, 25])

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
```

---

# 🆚 Python List vs NumPy Array

| Feature                 | Python List  | NumPy Array |
| ----------------------- | ------------ | ----------- |
| Speed                   | Slower       | Faster      |
| Memory                  | Higher       | Lower       |
| Mathematical Operations | Limited      | Built-in    |
| Machine Learning        | Not Suitable | Essential   |

---

# 💻 Mini Project

## Student Marks Analyzer

### Features

* Store marks using NumPy arrays
* Calculate total marks
* Calculate average marks
* Find highest score
* Find lowest score

### Solution

```python
import numpy as np

marks = np.array([85, 72, 91, 67, 88])

print("Marks:", marks)
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
```

---

# 📝 Practice Questions

## Easy

1. Create a NumPy array of 10 numbers.
2. Print the shape of the array.
3. Print the data type.
4. Find the sum of all elements.
5. Find the average.

---

## Medium

6. Create a 3×3 matrix of zeros.
7. Create a 4×4 identity matrix.
8. Generate numbers from 1 to 100.
9. Multiply every element by 5.
10. Calculate maximum and minimum values.

---

## Advanced

11. Compare NumPy and Python list performance.
12. Create a random integer array.
13. Calculate standard deviation.
14. Find unique elements.
15. Build a simple marks analysis system.

---

# 🎤 Common Interview Questions

## Beginner

### 1. What is NumPy?

NumPy is the fundamental Python library for numerical computing and multidimensional arrays.

---

### 2. Why is NumPy faster than Python lists?

Because NumPy stores homogeneous data in contiguous memory and performs operations using optimized C implementations.

---

### 3. What is ndarray?

`ndarray` is NumPy's core data structure for storing multidimensional arrays.

---

### 4. Why do we import NumPy as `np`?

It is the community standard alias, making code shorter and more readable.

---

### 5. What is the difference between `arange()` and `linspace()`?

* `arange()` creates values using a step size.
* `linspace()` creates a fixed number of evenly spaced values.

---

## Intermediate

### 6. What does `shape` return?

The number of rows and columns (dimensions) of an array.

---

### 7. What is the difference between `size` and `ndim`?

* `size` → Total number of elements.
* `ndim` → Number of dimensions.

---

### 8. Why is NumPy important for AI?

It provides efficient numerical computation and is the foundation of most AI and ML libraries.

---

## Advanced

### 9. Can NumPy store different data types in one array?

It can, but NumPy converts them into a common compatible data type.

---

### 10. Name some libraries built on NumPy.

* Pandas
* SciPy
* Scikit-learn
* TensorFlow
* PyTorch
* OpenCV

---

# 📚 Best Resources

## Official Documentation

* https://numpy.org/doc/

## Free Resources

* NumPy User Guide
* Kaggle Python Course

## YouTube

* freeCodeCamp
* Corey Schafer
* CampusX
* Krish Naik

## Books

* *Python for Data Analysis* by Wes McKinney
* *Python Data Science Handbook* by Jake VanderPlas

---

# 🎯 Day 33 Summary

Today you learned:

* Introduction to NumPy
* Installing NumPy
* Importing NumPy
* Creating arrays
* Array dimensions
* Array attributes
* Special arrays
* Mathematical operations
* Aggregate functions
* Python List vs NumPy Array
* Student Marks Analyzer project
* NumPy interview questions

---

# 📌 GitHub Commit Message

```bash
git add .
git commit -m "Day 33: Introduction to NumPy and Array Fundamentals"
git push origin main
```

---

# 🚀 Next Day

**Day 34 – NumPy Indexing, Slicing & Array Manipulation**

Topics:

* Indexing
* Slicing
* Reshaping Arrays
* Flattening Arrays
* Concatenation
* Splitting Arrays
* Copy vs View
* Hands-on Exercises
* Real-world Dataset Practice
