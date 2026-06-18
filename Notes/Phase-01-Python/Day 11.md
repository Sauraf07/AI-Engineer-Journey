# 🚀 Day 11 — Data Visualization with Python

## 🎯 Goal

Learn how to convert raw data into charts and graphs so you can understand patterns and communicate insights effectively.

---

# 📊 What is Data Visualization?

Data Visualization means presenting data graphically using charts, plots, and graphs.

### Example

Instead of looking at:

| Month | Sales |
| ----- | ----- |
| Jan   | 100   |
| Feb   | 150   |
| Mar   | 120   |

You can create a chart and instantly identify trends and patterns.

---

# 📚 Libraries to Learn

## A. Matplotlib

The most popular Python visualization library.

### Installation

```bash
pip install matplotlib
```

### Import

```python
import matplotlib.pyplot as plt
```

---

## B. Seaborn

Built on top of Matplotlib and provides beautiful statistical visualizations.

### Installation

```bash
pip install seaborn
```

### Import

```python
import seaborn as sns
```

---

# 📈 Line Plot

Used for visualizing trends over time.

### Example

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 200]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

### Learn

* `plt.plot()`
* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.show()`

---

# 📊 Bar Chart

Used for comparing categories.

### Example

```python
import matplotlib.pyplot as plt

students = ["A", "B", "C"]
marks = [80, 90, 70]

plt.bar(students, marks)
plt.title("Student Marks")
plt.show()
```

---

# 📉 Histogram

Used to understand data distribution.

### Example

```python
import matplotlib.pyplot as plt

ages = [18,20,22,23,25,25,26,27,28]

plt.hist(ages)
plt.show()
```

### Understand

* Frequency
* Distribution

---

# 🥧 Pie Chart

Used to show percentages and proportions.

### Example

```python
import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]
labels = ["Python", "Java", "C++", "JS"]

plt.pie(sizes, labels=labels)
plt.show()
```

---

# 🎯 Scatter Plot

Used to find relationships between two variables.

### Example

```python
import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
marks = [40,50,60,75,90]

plt.scatter(hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

### Question

Do more study hours increase marks?

---

# 🎨 Seaborn Basics

## Count Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(x="day", data=tips)

plt.show()
```

---

## Box Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data=tips)

plt.show()
```

### Learn

* Outliers
* Median
* Quartiles

---

# 🐼 Working with Pandas Data

### Example

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Marks"].plot(kind="bar")

plt.show()
```

---

# 🧠 Visualization Concepts

| Concept      | Best Chart   |
| ------------ | ------------ |
| Trend        | Line Chart   |
| Comparison   | Bar Chart    |
| Distribution | Histogram    |
| Relationship | Scatter Plot |
| Percentage   | Pie Chart    |

---

# 💻 Today's Practice Tasks

## Task 1

Create a line chart for monthly expenses.

---

## Task 2

Create a bar chart for student marks.

---

## Task 3

Create a pie chart for favorite programming languages.

---

## Task 4

Create a histogram for ages of 50 students.

---

## Task 5

Create a scatter plot showing:

* Study Hours
* Exam Marks

---

# 🚀 Mini Project (Important)

# 🎓 Student Performance Dashboard

### Dataset

```python
data = {
    "Name": ["Aman", "Rahul", "Priya", "Neha", "Rohit"],
    "Marks": [85, 92, 78, 88, 95]
}
```

---

## Create

* 📊 Bar Chart of Marks
* 🥧 Pie Chart of Marks Contribution
* 🏆 Find Highest Scorer
* 💾 Save Chart as Image

### Hint

```python
plt.savefig("marks_chart.png")
```

---

# 📂 What To Upload on GitHub Today

Create Folder:

```bash
Day-11-Data-Visualization
```

### Inside It

* Line Plot Programs
* Bar Chart Programs
* Histogram Programs
* Pie Chart Programs
* Scatter Plot Programs
* Seaborn Examples
* Student Performance Dashboard Project
* README.md

---

# 📝 README Example

```md
# Day 11 - Data Visualization with Python

## Topics Covered
- Matplotlib
- Seaborn
- Line Plot
- Bar Chart
- Histogram
- Pie Chart
- Scatter Plot

## Project
- Student Performance Dashboard

## Concepts Learned
- Data Visualization
- Trends
- Comparisons
- Distributions
- Relationships
```

---

# ✅ Deliverables for Day 11

By the end of today, you should be able to:

* [ ] Create Line Plots
* [ ] Create Bar Charts
* [ ] Create Histograms
* [ ] Create Pie Charts
* [ ] Create Scatter Plots
* [ ] Use Seaborn Basics
* [ ] Visualize Pandas Data
* [ ] Complete the Student Performance Dashboard Project

---

# 🧠 Important AI Insight

Data Visualization is one of the most important skills in Data Science, Machine Learning, and AI.

Before building models, you must understand your data.

A good AI Engineer doesn't just train models — they analyze and communicate insights effectively through visualizations.

---

# 🚀 Keep Building

**Learn → Visualize → Analyze → Build → Improve**
