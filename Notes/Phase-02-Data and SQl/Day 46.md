# 📘 Day 46 – NumPy Array Operations (Part 1: Indexing)

> **Phase 3: Data Analysis with NumPy**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what array indexing is.
- Access elements in 1D, 2D, and 3D arrays.
- Use positive and negative indexing.
- Modify array values using indexing.
- Understand why indexing is important in AI and Machine Learning.
- Solve interview questions related to NumPy indexing.

---

# 📖 What is Array Indexing?

**Array Indexing** means accessing a specific element of an array using its position (index).

Think of an array as a row of lockers.

```text
Locker:   A     B     C     D     E
Index:    0     1     2     3     4
```

If you want item **C**, you use index **2**.

The same concept applies to NumPy arrays.

---

# 🌍 Real-Life Example

Imagine a classroom:

```text
Seat Number

0  1  2  3  4

Rahul
Priya
Aman
Neha
Riya
```

To access **Aman**, you use:

```python
students[2]
```

Output

```text
Aman
```

---

# 📦 Import NumPy

```python
import numpy as np
```

---

# 1️⃣ Indexing in 1D Array

Create an array.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
```

Output

```text
[10 20 30 40 50]
```

---

## Access First Element

```python
print(arr[0])
```

Output

```text
10
```

---

## Access Third Element

```python
print(arr[2])
```

Output

```text
30
```

---

## Access Last Element

```python
print(arr[4])
```

Output

```text
50
```

---

# 📌 Positive Indexing

```text
Array

[10 20 30 40 50]

Index

0 1 2 3 4
```

Example

```python
print(arr[1])
```

Output

```text
20
```

---

# 📌 Negative Indexing

Negative indexing starts from the end.

```text
Array

[10 20 30 40 50]

Negative Index

-5 -4 -3 -2 -1
```

Example

```python
print(arr[-1])
```

Output

```text
50
```

---

Another Example

```python
print(arr[-2])
```

Output

```text
40
```

---

# ✏️ Updating Values

You can modify values using indexing.

```python
arr[1] = 100

print(arr)
```

Output

```text
[10 100 30 40 50]
```

---

# 2️⃣ Indexing in 2D Arrays

Create a matrix.

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr)
```

Output

```text
[[10 20 30]
 [40 50 60]
 [70 80 90]]
```

---

## Understanding Rows and Columns

```text
        Column

       0    1    2

0     10   20   30

1     40   50   60

2     70   80   90

Row
```

Syntax

```python
array[row][column]
```

or

```python
array[row, column]
```

---

## Access First Element

```python
print(arr[0,0])
```

Output

```text
10
```

---

## Access 50

```python
print(arr[1,1])
```

Output

```text
50
```

---

## Access 90

```python
print(arr[2,2])
```

Output

```text
90
```

---

## Access Entire First Row

```python
print(arr[0])
```

Output

```text
[10 20 30]
```

---

## Access Entire Second Column

```python
print(arr[:,1])
```

Output

```text
[20 50 80]
```

Explanation

```text
:

means all rows

1

means second column
```

---

# Updating 2D Arrays

```python
arr[1,2] = 100

print(arr)
```

Output

```text
[[10 20 30]
 [40 50 100]
 [70 80 90]]
```

---

# 3️⃣ Indexing in 3D Arrays

Create a 3D array.

```python
arr = np.array([
[
[1,2],
[3,4]
],
[
[5,6],
[7,8]
]
])

print(arr)
```

Shape

```text
(2,2,2)
```

Meaning

```text
2 Blocks

↓

2 Rows

↓

2 Columns
```

---

## Access First Element

```python
print(arr[0,0,0])
```

Output

```text
1
```

---

## Access Number 8

```python
print(arr[1,1,1])
```

Output

```text
8
```

---

## Access Number 6

```python
print(arr[1,0,1])
```

Output

```text
6
```

---

# 🔥 Why Indexing Matters in AI & ML

Machine Learning datasets are stored as NumPy arrays.

Example:

```python
dataset = np.array([
[25,170,65],
[30,180,70],
[28,175,68]
])
```

Columns represent:

```text
Age

Height

Weight
```

Access only Height column.

```python
print(dataset[:,1])
```

Output

```text
[170 180 175]
```

This is useful when selecting features for machine learning models.

---

# 📝 Common Errors

## Index Out of Range

```python
arr = np.array([10,20,30])

print(arr[5])
```

Output

```text
IndexError
```

---

## Wrong Dimensions

```python
arr = np.array([10,20,30])

print(arr[0,1])
```

Output

```text
IndexError
```

Reason

1D arrays have only one dimension.

---

# 💼 Real-World Use Cases

- Image Processing (Access pixel values)
- Medical Data Analysis
- Stock Price Analysis
- Customer Data Processing
- Machine Learning Feature Selection
- Deep Learning Input Preparation

---

# 🧪 Practice Questions

### Easy

1. Create a 1D array and print the first element.
2. Print the last element using negative indexing.
3. Update the second element.
4. Create a 2D array.
5. Print the second row.
6. Print the third column.
7. Access the center element.
8. Create a 3D array.
9. Print the last element.
10. Print the first block.

---

### Medium

11. Replace all values in the first row.
12. Extract the first column.
13. Modify diagonal elements.
14. Access a complete block in a 3D array.
15. Find the maximum indexed element.

---

# 🎤 Interview Questions

### Beginner

### 1. What is indexing in NumPy?

Indexing is the process of accessing elements of a NumPy array using their position.

---

### 2. What is the index of the first element?

```text
0
```

---

### 3. What is negative indexing?

Negative indexing accesses elements from the end of the array.

Example:

```python
arr[-1]
```

---

### 4. How do you access an element in a 2D array?

```python
arr[row, column]
```

---

### 5. How do you access an element in a 3D array?

```python
arr[block, row, column]
```

---

### Intermediate

### 6. Difference between Python List Indexing and NumPy Indexing?

NumPy supports multi-dimensional indexing and is much faster for numerical computations.

---

### 7. Why is indexing important in Machine Learning?

It helps extract specific rows, columns, and features from datasets efficiently.

---

### 8. Can NumPy arrays be modified using indexing?

Yes.

```python
arr[0] = 100
```

---

### 9. What error occurs if an invalid index is used?

```text
IndexError
```

---

### 10. Can negative indexing be used in multi-dimensional arrays?

Yes.

Example:

```python
arr[-1, -1]
```

---

# 🏆 Mini Challenge

Create the following array:

```text
[[10 20 30]
 [40 50 60]
 [70 80 90]]
```

Perform these tasks:

- Print 10
- Print 50
- Print 90
- Print first row
- Print second column
- Replace 60 with 600
- Replace 20 with 200

---

# 📌 Key Takeaways

✅ Indexing accesses specific elements in an array.

✅ Positive indexing starts from `0`.

✅ Negative indexing starts from `-1`.

✅ Multi-dimensional arrays use row and column indexing.

✅ Indexing is widely used in Machine Learning for selecting features and manipulating datasets.

---

# 💡 GitHub Commit

```bash
git add .
git commit -m "Day 46: Learned NumPy Array Indexing"
git push origin main
```

---

# 🚀 Next Part

## 📗 Day 46 – Part 2: Array Slicing

Topics:

- Basic Slicing
- Step Slicing
- Multi-dimensional Slicing
- Fancy Indexing
- Boolean Indexing
- Real-world ML Examples
- Practice Questions
- Interview Questions

# 📘 Day 46 – NumPy Array Operations (Part 2)

> **Phase 3: Python Libraries for AI/ML**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

# 📚 Topic: Array Slicing

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand array slicing
- Slice 1D, 2D, and 3D arrays
- Use positive and negative indexing
- Use step slicing
- Apply Fancy Indexing
- Apply Boolean Indexing
- Understand real-world AI/ML use cases
- Solve interview questions confidently

---

# 📖 What is Array Slicing?

Array slicing is a technique used to extract a portion of an array without modifying the original array.

Instead of accessing one element, slicing allows us to access multiple elements at once.

---

# 🎯 Why is Slicing Important?

In AI and Machine Learning, datasets often contain millions of rows.

Instead of processing the whole dataset, we usually work with only a specific part.

Examples:

- First 1000 rows
- Last 50 records
- Training dataset
- Testing dataset
- Selecting specific columns

---

# 📌 Syntax

```python
array[start : stop : step]
```

| Parameter | Meaning |
|-----------|---------|
| start | Starting index |
| stop | Ending index (excluded) |
| step | Jump between elements |

---

# 1️⃣ Basic Slicing (1D Array)

```python
import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[1:4])
```

### Output

```text
[20 30 40]
```

---

# Slice from Beginning

```python
print(arr[:4])
```

Output

```text
[10 20 30 40]
```

---

# Slice Till End

```python
print(arr[2:])
```

Output

```text
[30 40 50 60]
```

---

# Copy Entire Array

```python
print(arr[:])
```

Output

```text
[10 20 30 40 50 60]
```

---

# Step Slicing

```python
print(arr[::2])
```

Output

```text
[10 30 50]
```

---

# Reverse Array

```python
print(arr[::-1])
```

Output

```text
[60 50 40 30 20 10]
```

---

# Reverse Every Second Element

```python
print(arr[::-2])
```

Output

```text
[60 40 20]
```

---

# 2️⃣ Slicing in 2D Arrays

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
```

Array

```
10 20 30
40 50 60
70 80 90
```

---

# First Row

```python
print(arr[0,:])
```

Output

```text
[10 20 30]
```

---

# Second Row

```python
print(arr[1,:])
```

Output

```text
[40 50 60]
```

---

# First Column

```python
print(arr[:,0])
```

Output

```text
[10 40 70]
```

---

# Second Column

```python
print(arr[:,1])
```

Output

```text
[20 50 80]
```

---

# Last Column

```python
print(arr[:,-1])
```

Output

```text
[30 60 90]
```

---

# Sub Matrix

```python
print(arr[0:2,1:3])
```

Output

```text
[[20 30]
 [50 60]]
```

---

# Entire Second Row

```python
print(arr[1])
```

Output

```text
[40 50 60]
```

---

# Last Two Rows

```python
print(arr[-2:])
```

Output

```text
[[40 50 60]
 [70 80 90]]
```

---

# 3️⃣ Slicing 3D Arrays

```python
arr = np.array([
[
[1,2],
[3,4]
],
[
[5,6],
[7,8]
]
])
```

Shape

```
(2,2,2)
```

---

# First Matrix

```python
print(arr[0])
```

---

# Second Matrix

```python
print(arr[1])
```

---

# Specific Element

```python
print(arr[1,0,1])
```

Output

```text
6
```

---

# 🎨 Fancy Indexing

Fancy indexing means selecting elements using a list or array of indices.

```python
arr = np.array([10,20,30,40,50])

print(arr[[0,2,4]])
```

Output

```text
[10 30 50]
```

---

# Fancy Indexing in 2D

```python
arr = np.array([
[10,20],
[30,40],
[50,60]
])

print(arr[[0,2]])
```

Output

```text
[[10 20]
 [50 60]]
```

---

# ✅ Boolean Indexing

Boolean indexing filters data using conditions.

---

Example

```python
arr=np.array([10,20,30,40,50])

print(arr[arr>30])
```

Output

```text
[40 50]
```

---

Even Numbers

```python
arr=np.array([1,2,3,4,5,6])

print(arr[arr%2==0])
```

Output

```text
[2 4 6]
```

---

Odd Numbers

```python
print(arr[arr%2!=0])
```

Output

```text
[1 3 5]
```

---

# Real World Example

Suppose we have employee salaries.

```python
salary=np.array([25000,50000,70000,90000,35000])

print(salary[salary>50000])
```

Output

```text
[70000 90000]
```

Useful for:

- Finding high-paid employees
- Filtering students
- Selecting customers
- Data cleaning

---

# AI/ML Example

```python
marks=np.array([45,67,89,23,91])

passed=marks[marks>=40]

print(passed)
```

Output

```text
[45 67 89 91]
```

This is how datasets are filtered before training models.

---

# Common Mistakes

❌

```python
arr[10]
```

Index out of range.

---

❌

```python
arr[1:100]
```

Doesn't give an error but may return fewer elements than expected.

---

❌

```python
arr[:,5]
```

Column doesn't exist.

---

# Best Practices

✅ Use slicing instead of loops.

✅ Prefer Boolean Indexing for filtering.

✅ Use negative indexing when accessing the end.

✅ Use step slicing for sampling data.

---

# Practice Questions

### Easy

1. Print first 5 elements.
2. Print last 3 elements.
3. Reverse an array.
4. Print every second element.
5. Print middle 4 elements.

---

### Medium

6. Print first row.
7. Print last column.
8. Print first two rows.
9. Print last two columns.
10. Print a 2×2 submatrix.

---

### Advanced

11. Select values greater than 50.
12. Select even numbers.
13. Select odd numbers.
14. Reverse a 2D array.
15. Create a checkerboard slice.

---

# Interview Questions

## Beginner

### 1. What is array slicing?

Array slicing extracts a portion of an array without changing the original array.

---

### 2. What is the syntax?

```python
array[start:stop:step]
```

---

### 3. Is the stop index included?

No.

---

### 4. How do you reverse an array?

```python
arr[::-1]
```

---

### 5. What is Boolean Indexing?

Selecting elements using conditions.

---

## Intermediate

### 6. What is Fancy Indexing?

Selecting elements using a list or array of indices.

---

### 7. Difference between Indexing and Slicing?

| Indexing | Slicing |
|----------|----------|
| Returns one element | Returns multiple elements |

---

### 8. Why is slicing faster than loops?

Because NumPy performs operations in optimized C code, reducing Python-level iteration.

---

### 9. What is negative indexing?

Accessing elements from the end of the array using negative indices.

---

### 10. Where is Boolean Indexing used?

- Data Cleaning
- Feature Selection
- Filtering Data
- Machine Learning
- Data Analysis

---

# 📝 Summary

Today you learned:

- ✅ Array Slicing
- ✅ 1D Slicing
- ✅ 2D Slicing
- ✅ 3D Slicing
- ✅ Step Slicing
- ✅ Reverse Slicing
- ✅ Fancy Indexing
- ✅ Boolean Indexing
- ✅ Real-world AI/ML Examples
- ✅ Interview Questions

---

# 💻 GitHub Commit

```bash
git add .
git commit -m "Day 46: Learned NumPy Array Slicing, Fancy Indexing, and Boolean Indexing"
git push origin main
```

---

# 🚀 Next Lesson

## 📘 Day 46 – Part 3: Array Reshaping

Topics:

- reshape()
- flatten()
- ravel()
- transpose()
- resize()
- squeeze()
- expand_dims()
- Real-world ML examples


# 📘 Day 46 – NumPy Array Operations (Part 3)

> **Phase 3: Data Analysis with NumPy**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

# 🎯 Topic: Array Reshaping

---

# 📚 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what array reshaping is
- Convert 1D arrays into 2D and 3D arrays
- Use `reshape()`
- Understand `flatten()` and `ravel()`
- Use `transpose()`
- Use `resize()`
- Use `expand_dims()`
- Use `squeeze()`
- Solve interview questions
- Perform real-world data preprocessing

---

# 🤔 Why Do We Need Reshaping?

Machine Learning models require data in specific shapes.

For example:

- Images → `(Height × Width × Channels)`
- Student Data → `(Rows × Columns)`
- Neural Networks → `(Samples × Features)`

Sometimes data is stored in one shape but needs another.

That's where reshaping comes in.

---

# 📌 What is Reshape?

`reshape()` changes the shape of an array **without changing its data**.

## Syntax

```python
array.reshape(rows, columns)
```

---

# Example 1

```python
import numpy as np

arr = np.array([1,2,3,4])

print(arr)
```

Output

```text
[1 2 3 4]
```

Now convert it into 2×2.

```python
new_arr = arr.reshape(2,2)

print(new_arr)
```

Output

```text
[[1 2]
 [3 4]]
```

---

# Visual Representation

Before

```text
[1 2 3 4]
```

After

```text
1 2
3 4
```

---

# Example 2

Convert 12 elements into 3×4.

```python
import numpy as np

arr = np.arange(1,13)

print(arr)
```

Output

```text
[1 2 3 4 5 6 7 8 9 10 11 12]
```

Now

```python
arr.reshape(3,4)
```

Output

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

---

# Example 3

Convert into 4×3

```python
arr.reshape(4,3)
```

Output

```text
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

---

# Example 4

Convert into 2×2×3

```python
arr.reshape(2,2,3)
```

Output

```text
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

---

# Important Rule

The total number of elements must remain the same.

Correct

```python
12 → 3×4
```

Because

```
3 × 4 = 12
```

Incorrect

```python
12 → 5×3
```

Because

```
5 × 3 = 15
```

Output

```text
ValueError
```

---

# Automatic Dimension (-1)

NumPy can calculate one dimension automatically.

```python
arr.reshape(3,-1)
```

Output

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

Another example

```python
arr.reshape(-1,2)
```

Output

```text
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]
```

---

# Flatten()

Converts multi-dimensional arrays into a 1D array.

```python
arr = np.array([[1,2],[3,4]])

print(arr.flatten())
```

Output

```text
[1 2 3 4]
```

---

# Ravel()

Also converts into a 1D array.

```python
print(arr.ravel())
```

Output

```text
[1 2 3 4]
```

---

# Difference Between flatten() and ravel()

| flatten() | ravel() |
|------------|----------|
| Returns a copy | Returns a view when possible |
| More memory | More efficient |
| Changes don't affect original | May affect original array |

Example:

```python
arr = np.array([[1,2],[3,4]])

flat = arr.flatten()
flat[0] = 100

print(arr)
```

Output

```text
[[1 2]
 [3 4]]
```

Original remains unchanged.

Now with `ravel()`:

```python
arr = np.array([[1,2],[3,4]])

r = arr.ravel()
r[0] = 100

print(arr)
```

Output

```text
[[100   2]
 [  3   4]]
```

---

# Transpose

Rows become columns.

```python
arr = np.array([[1,2,3],[4,5,6]])

print(arr.T)
```

Output

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# Resize()

Changes the shape permanently.

```python
arr = np.array([1,2,3,4])

arr.resize(2,2)

print(arr)
```

Output

```text
[[1 2]
 [3 4]]
```

---

# expand_dims()

Adds a new dimension.

```python
arr = np.array([1,2,3])

new = np.expand_dims(arr, axis=0)

print(new)
```

Output

```text
[[1 2 3]]
```

---

# squeeze()

Removes dimensions of size 1.

```python
arr = np.array([[[1,2,3]]])

print(np.squeeze(arr))
```

Output

```text
[1 2 3]
```

---

# Real-World AI Example

Suppose you have grayscale images.

Shape:

```text
(100, 28, 28)
```

CNN models expect:

```text
(100,28,28,1)
```

Use

```python
images = np.expand_dims(images, axis=-1)
```

---

# Data Science Example

Original sales data

```text
[100,120,150,180]
```

Convert into

```text
Month  Sales
Jan    100
Feb    120
Mar    150
Apr    180
```

```python
sales.reshape(4,1)
```

---

# Mini Project

## Student Marks Formatter

```python
import numpy as np

marks = np.array([80,75,92,60,88,91])

table = marks.reshape(3,2)

print(table)
```

Output

```text
[[80 75]
 [92 60]
 [88 91]]
```

---

# Practice Questions

## Easy

1. Convert a 1D array into 2×2.
2. Convert 16 elements into 4×4.
3. Convert 12 elements into 2×6.
4. Flatten a matrix.
5. Transpose a matrix.

---

## Medium

6. Convert 24 elements into 2×3×4.
7. Use reshape with `-1`.
8. Compare `flatten()` and `ravel()`.
9. Add a new dimension.
10. Remove a dimension using `squeeze()`.

---

## Advanced

11. Convert image data into CNN format.
12. Reshape a dataset for ML training.
13. Build a feature matrix.
14. Prepare batch data.
15. Reshape a time-series dataset.

---

# 🎤 Interview Questions

### Beginner

### 1. What is reshape()?

It changes the shape of an array without changing its data.

---

### 2. Can reshape change the number of elements?

No.

---

### 3. What does `-1` mean in reshape()?

NumPy automatically calculates that dimension.

---

### 4. What is flatten()?

It converts a multi-dimensional array into a 1D copy.

---

### 5. What is ravel()?

It returns a flattened view of the original array whenever possible.

---

### Intermediate

### 6. Difference between flatten() and ravel()?

- `flatten()` returns a copy.
- `ravel()` returns a view when possible.

---

### 7. What is transpose?

It swaps rows and columns.

---

### 8. What is expand_dims()?

It adds a new axis to an array.

---

### 9. What is squeeze()?

It removes axes with size 1.

---

### 10. Why is reshaping important in Machine Learning?

Because ML and Deep Learning models require data in specific shapes before training.

---

# 📝 Summary

Today you learned:

- ✅ reshape()
- ✅ flatten()
- ✅ ravel()
- ✅ transpose()
- ✅ resize()
- ✅ expand_dims()
- ✅ squeeze()
- ✅ Real-world AI examples
- ✅ Interview Questions
- ✅ Hands-on Practice

---

# 💡 GitHub Commit

```bash
git add .
git commit -m "Day 46: Mastered NumPy Array Reshaping Operations"
git push origin main
```

---

# 🚀 Next Day

## 📘 Day 47 – NumPy Mathematical Operations

Topics:

- Arithmetic Operations
- Broadcasting
- Universal Functions (ufuncs)
- Aggregate Functions
- Statistical Operations
- Real-world Data Analysis

# 📘 Day 46 – NumPy Array Operations (Part 4)

> **Phase 3: Data Analysis with NumPy**
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this section, you will be able to:

- Solve interview-level NumPy problems
- Work confidently with indexing, slicing, and reshaping
- Apply NumPy operations in Machine Learning
- Build a small real-world project
- Prepare for AI/ML interviews

---

# 🚀 Mini Project

# 📊 Student Marks Analysis System

## Problem Statement

A school stores marks of students in a NumPy array.

You need to:

- Display all student marks
- Find highest marks
- Find lowest marks
- Calculate average marks
- Reshape the data into rows and columns
- Display marks subject-wise
- Display top-performing students

---

## Sample Dataset

```python
import numpy as np

marks = np.array([
    85, 78, 92,
    88, 76, 95,
    67, 81, 90,
    72, 89, 84
])
```

---

## Step 1: Reshape Data

```python
marks = marks.reshape(4,3)

print(marks)
```

Output

```
[[85 78 92]
 [88 76 95]
 [67 81 90]
 [72 89 84]]
```

---

## Step 2: Average Marks

```python
print(np.mean(marks))
```

---

## Step 3: Highest Marks

```python
print(np.max(marks))
```

---

## Step 4: Lowest Marks

```python
print(np.min(marks))
```

---

## Step 5: Subject-wise Average

```python
print(np.mean(marks, axis=0))
```

---

## Step 6: Student-wise Average

```python
print(np.mean(marks, axis=1))
```

---

# 💼 Real-World Applications

NumPy Array Operations are widely used in:

- Machine Learning
- Data Science
- Image Processing
- Computer Vision
- NLP
- Robotics
- Financial Analysis
- Scientific Computing
- Recommendation Systems
- AI Model Training

---

# 📝 Practice Questions

## Beginner

1. Create a 1D NumPy array.
2. Create a 2D NumPy array.
3. Print the first element.
4. Print the last element.
5. Use negative indexing.
6. Slice the first five elements.
7. Slice alternate elements.
8. Reshape a (6,) array into (2,3).
9. Find maximum value.
10. Find minimum value.

---

## Intermediate

11. Calculate mean.
12. Calculate median.
13. Find standard deviation.
14. Transpose a matrix.
15. Flatten a matrix.
16. Use `ravel()`.
17. Boolean indexing.
18. Fancy indexing.
19. Reverse an array.
20. Extract even numbers.

---

## Advanced

21. Create a 3D array.
22. Reshape (24,) into (2,3,4).
23. Compare `reshape()` vs `resize()`.
24. Compare `flatten()` vs `ravel()`.
25. Create an identity matrix.
26. Create a diagonal matrix.
27. Stack arrays vertically.
28. Stack arrays horizontally.
29. Split arrays.
30. Solve a real dataset using NumPy.

---

# 🎤 Interview Questions

## Beginner

### 1. What is NumPy?

NumPy is a Python library used for numerical computing and working with multidimensional arrays.

---

### 2. Why is NumPy faster than Python Lists?

Because NumPy arrays are:

- Homogeneous
- Memory efficient
- Implemented in C
- Optimized for vectorized operations

---

### 3. What is an ndarray?

The primary data structure provided by NumPy.

---

### 4. What is Indexing?

Accessing a specific element using its position.

Example:

```python
arr[0]
```

---

### 5. What is Slicing?

Extracting multiple elements from an array.

Example:

```python
arr[1:5]
```

---

### 6. What is Reshaping?

Changing the dimensions of an array without changing its data.

Example:

```python
arr.reshape(2,3)
```

---

### 7. Difference between reshape() and resize()?

| reshape() | resize() |
|------------|-----------|
| Returns new array | Modifies original array |
| Shape must match | Can change size |

---

### 8. Difference between flatten() and ravel()?

| flatten() | ravel() |
|------------|---------|
| Returns copy | Returns view (if possible) |

---

### 9. What is Fancy Indexing?

Selecting multiple elements using a list of indices.

```python
arr[[1,3,5]]
```

---

### 10. What is Boolean Indexing?

Selecting elements based on conditions.

```python
arr[arr > 50]
```

---

# ⭐ Frequently Asked Interview Questions

- Difference between Python List and NumPy Array?
- Why NumPy is important for Machine Learning?
- Explain ndarray.
- Explain reshape().
- Explain slicing.
- Explain indexing.
- Explain broadcasting.
- Explain axis parameter.
- Explain flatten().
- Explain transpose().
- Explain copy() vs view().
- Explain vectorization.

---

# 📌 NumPy Cheat Sheet

## Create Array

```python
np.array([1,2,3])
```

---

## Index

```python
arr[0]
```

---

## Slice

```python
arr[1:5]
```

---

## Reshape

```python
arr.reshape(2,3)
```

---

## Flatten

```python
arr.flatten()
```

---

## Ravel

```python
arr.ravel()
```

---

## Transpose

```python
arr.T
```

---

## Maximum

```python
np.max(arr)
```

---

## Minimum

```python
np.min(arr)
```

---

## Mean

```python
np.mean(arr)
```

---

## Sum

```python
np.sum(arr)
```

---

## Shape

```python
arr.shape
```

---

## Dimensions

```python
arr.ndim
```

---

## Data Type

```python
arr.dtype
```

---

## Size

```python
arr.size
```

---

# 🏆 Assignment

Create a **NumPy Student Management System** that performs:

- Create student marks array
- Display student-wise marks
- Calculate average
- Find topper
- Find lowest marks
- Reshape data
- Transpose data
- Apply slicing
- Apply indexing
- Apply Boolean indexing
- Display students scoring above 80

---

# 🎯 Skills Gained

After Day 46, you can confidently:

- Work with NumPy arrays
- Perform indexing and slicing
- Reshape multidimensional arrays
- Analyze datasets
- Prepare data for Machine Learning
- Solve interview-level NumPy questions

---

# 📚 Key Takeaways

✅ NumPy arrays are faster than Python lists.

✅ Indexing retrieves specific elements.

✅ Slicing extracts subsets of data.

✅ Reshaping changes array dimensions.

✅ Flattening converts multi-dimensional arrays into one dimension.

✅ NumPy is the foundation of Pandas, Scikit-learn, TensorFlow, and PyTorch.

---

# 💡 GitHub Repository Structure

```text
Day46-NumPy-Array-Operations/
│
├── README.md
├── indexing_examples.py
├── slicing_examples.py
├── reshape_examples.py
├── practice_questions.py
├── student_marks_project.py
└── interview_questions.md
```

---

# 💻 GitHub Commit Message

```bash
git add .
git commit -m "Day 46: Mastered NumPy Array Indexing, Slicing, and Reshaping"
git push origin main
```

---

# 🚀 Next Day

## 📅 Day 47 – NumPy Mathematical Operations

### Topics

- Arithmetic Operations
- Aggregate Functions
- Statistical Functions
- Universal Functions (ufuncs)
- Broadcasting
- Vectorized Computation
- Real-world Numerical Analysis

---

# 🎉 Congratulations!

You have successfully completed **Day 46 – NumPy Array Operations**.

You now have one of the most important foundations required for **Pandas**, **Machine Learning**, **Deep Learning**, and **Generative AI**. Keep practicing with real datasets to strengthen these concepts.


