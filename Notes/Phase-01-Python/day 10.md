# 🚀 Day 10 — Pandas Fundamentals

## 🎯 Goal of Day 10

Today’s goal is to learn **Pandas**, one of the most important Python libraries for:

* Data Analysis
* Data Cleaning
* Machine Learning
* Data Science
* AI Applications

By the end of today, you should be able to:

* Create DataFrames
* Read CSV files
* Filter and sort data
* Handle missing values
* Perform basic statistical analysis
* Use GroupBy operations
* Save processed data

---

# 📚 1. What is Pandas? (15 min)

## Understand

* Why Pandas is used
* DataFrame
* Series
* Rows and Columns

## Example

```python
import pandas as pd

data = {
    "Name": ["Sauraf", "Rahul", "Aman"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
     Name  Age
0  Sauraf   21
1   Rahul   22
2    Aman   20
```

---

# 📚 2. Creating DataFrames (20 min)

## Learn

* `pd.DataFrame()`

## Create DataFrames From

* Dictionary
* List
* CSV File

### Example

```python
students = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70]
}

df = pd.DataFrame(students)

print(df)
```

---

# 📚 3. Reading CSV Files (20 min)

## Most Important Topic

### Read CSV

```python
df = pd.read_csv("students.csv")
```

### View Data

```python
print(df.head())
print(df.tail())
```

### Learn

```python
df.shape
df.columns
df.info()
```

### Understand

* Number of Rows
* Number of Columns
* Data Types
* Missing Values

---

# 📚 4. Selecting Data (30 min)

## Single Column

```python
df["Name"]
```

## Multiple Columns

```python
df[["Name", "Marks"]]
```

## Rows Using iloc

```python
df.iloc[0]

df.iloc[0:5]
```

## Rows Using loc

```python
df.loc[0]
```

---

# 📚 5. Filtering Data (30 min)

## Important Interview Topic

### Example

```python
df[df["Marks"] > 80]
```

### Multiple Conditions

```python
df[(df["Marks"] > 80) & (df["Age"] > 20)]
```

### Practice

* Students with Marks > 70
* Students with Age < 22
* Students with Marks between 60 and 90

---

# 📚 6. Handling Missing Values (25 min)

## Check Missing Values

```python
df.isnull()
```

## Count Missing Values

```python
df.isnull().sum()
```

## Fill Missing Values

```python
df.fillna(0)
```

## Remove Missing Rows

```python
df.dropna()
```

### Why It Matters

Handling missing data is extremely common in:

* Machine Learning
* Data Science
* AI Projects

---

# 📚 7. Basic Statistics (20 min)

## Summary Statistics

```python
df.describe()
```

## Individual Operations

### Mean

```python
df["Marks"].mean()
```

### Maximum

```python
df["Marks"].max()
```

### Minimum

```python
df["Marks"].min()
```

### Sum

```python
df["Marks"].sum()
```

---

## Understand These Terms

* Mean
* Median
* Maximum
* Minimum
* Count

---

# 📚 8. Sorting Data (15 min)

## Ascending Order

```python
df.sort_values("Marks")
```

## Descending Order

```python
df.sort_values("Marks", ascending=False)
```

---

# 📚 9. GroupBy (30 min)

## One of the Most Important Pandas Concepts

### Example

```python
df.groupby("Department")["Salary"].mean()
```

## Understand

* Grouping Data
* Aggregation
* Average by Category

### Common Use Cases

* Average Salary by Department
* Total Sales by Category
* Student Marks by Class

---

# 📚 10. Saving Data (10 min)

## Save DataFrame as CSV

```python
df.to_csv("output.csv", index=False)
```

---

# 🚀 Practice Project (1–2 Hours)

# 🎓 Student Performance Analyzer

## Dataset

```python
data = {
    "Name": ["Aman", "Rahul", "Sauraf", "Priya", "Ankit"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [78, 92, 85, 67, 95]
}
```

---

## Tasks

### Task 1

Create DataFrame

### Task 2

Display first 3 rows

### Task 3

Show students with marks > 80

### Task 4

Find average marks

### Task 5

Find topper

### Task 6

Sort by marks descending

### Task 7

Save result to CSV

---

# 💻 What To Upload on GitHub Today

Create Folder:

```text
Day-10-Pandas
```

## Inside It

```text
Day-10-Pandas/
│
├── pandas_practice.py
├── student_analyzer.py
├── students.csv
├── output.csv
└── README.md
```

---

# 🎤 Interview Questions for Day 10

Be able to answer these questions confidently:

### 1. What is Pandas?

### 2. Difference between Series and DataFrame?

### 3. What is a CSV file?

### 4. What does `head()` do?

### 5. Difference between `loc` and `iloc`?

### 6. How do you handle missing values?

### 7. What is `groupby()`?

### 8. What does `describe()` do?

### 9. How do you filter rows in Pandas?

### 10. How do you save a DataFrame?

---

# ✅ End of Day 10 Checklist

* [ ] Learned Pandas Basics
* [ ] Created DataFrames
* [ ] Read CSV Files
* [ ] Selected Data
* [ ] Filtered Data
* [ ] Handled Missing Values
* [ ] Performed Statistics
* [ ] Sorted Data
* [ ] Practiced GroupBy
* [ ] Saved Data to CSV
* [ ] Completed Student Performance Analyzer
* [ ] Uploaded Work to GitHub

---

# 🧠 AI Engineering Connection

Pandas is the foundation of:

* Machine Learning
* Data Science
* Data Preprocessing
* Feature Engineering
* AI Pipelines

Almost every AI project starts with cleaning and analyzing data using Pandas.

---

# 🚀 Motto

> Learn Data → Understand Data → Train Models → Build AI
