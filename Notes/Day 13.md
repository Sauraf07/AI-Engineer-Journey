# 🚀 Day 13 — Machine Learning Fundamentals (Linear Regression)

## 🎯 Goal

Today you'll build your **first Machine Learning model** and understand how machines "learn" from data.

By the end of Day 13, you should be able to:

* Understand what Machine Learning is
* Understand Linear Regression
* Train your first ML model using Scikit-Learn
* Make predictions
* Evaluate model performance
* Visualize data and regression lines

---

# 🤖 What is Machine Learning?

## Traditional Programming

```text
Input + Rules → Output
```

### Example

```python
marks = 90

if marks > 40:
    print("Pass")
else:
    print("Fail")
```

Input:

```text
Marks = 90
Rule = Marks > 40
```

Output:

```text
Pass
```

---

## Machine Learning

```text
Input + Output → Machine Learns Rules
```

### Example Dataset

| Hours Studied | Marks |
| ------------- | ----- |
| 1             | 30    |
| 2             | 40    |
| 3             | 50    |
| 4             | 60    |
| 5             | 70    |

The machine learns:

```text
More Study Hours → Higher Marks
```

Then predicts future values.

---

# 📚 Types of Machine Learning

## 1️⃣ Supervised Learning

Data contains labels.

### Example

| Hours | Marks |
| ----- | ----- |
| 2     | 40    |
| 4     | 60    |

Machine learns relationship between input and output.

### Real-Life Examples

* House Price Prediction
* Student Marks Prediction
* Salary Prediction
* Spam Detection

---

## 2️⃣ Unsupervised Learning

Data has no labels.

Machine finds patterns automatically.

### Examples

* Customer Segmentation
* Market Basket Analysis
* Recommendation Systems

---

## 3️⃣ Reinforcement Learning

Learning through rewards and penalties.

### Examples

* Self-Driving Cars
* Robotics
* Game AI

---

# 📈 What is Linear Regression?

Linear Regression finds the best straight-line relationship between variables.

### Example Dataset

| Study Hours | Marks |
| ----------- | ----- |
| 1           | 30    |
| 2           | 40    |
| 3           | 50    |
| 4           | 60    |
| 5           | 70    |

Graphically:

Where:

* **y** = Predicted Value (Marks)
* **x** = Input Value (Study Hours)
* **m** = Slope
* **b** = Intercept

---

## Real-Life Example

If:

```text
1 Hour → 30 Marks
2 Hours → 40 Marks
3 Hours → 50 Marks
```

Then:

```text
6 Hours → ?
```

Model predicts approximately:

```text
80 Marks
```

---

# 🛠️ Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

# 💻 Your First Linear Regression Model

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "hours": [1, 2, 3, 4, 5],
    "marks": [30, 40, 50, 60, 70]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])
```

### Expected Output

```text
Predicted Marks: 80
```

---

# 🧠 Understanding `fit()`

```python
model.fit(X, y)
```

This is where learning happens.

The model:

* Looks at data
* Finds patterns
* Creates a mathematical equation
* Learns the relationship between variables

After training:

```text
Hours Studied → Marks
```

relationship is learned.

---

# 🔮 Understanding `predict()`

```python
model.predict([[6]])
```

Meaning:

```text
If a student studies for 6 hours,
what marks should I expect?
```

The model returns a prediction.

---

# 📊 Visualize the Data

```python
import matplotlib.pyplot as plt

plt.scatter(X, y)

plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()
```

This shows data points on a graph.

---

# 📈 Draw Regression Line

```python
plt.scatter(X, y)

plt.plot(
    X,
    model.predict(X)
)

plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()
```

You will see:

* Data Points
* Best Fit Line

This line represents Linear Regression.

---

# 📏 Model Evaluation (Introduction)

## MAE

**Mean Absolute Error**

Measures average prediction error.

---

## MSE

**Mean Squared Error**

Squares prediction errors.

---

## RMSE

**Root Mean Squared Error**

Most commonly used error metric.

---

## R² Score

Measures how well the model fits the data.

Range:

```text
0 → Poor Model
1 → Perfect Model
```

---

# 🧰 Scikit-Learn Concepts to Learn Today

Understand:

```python
LinearRegression()
fit()
predict()
score()
```

⚠️ Don't memorize. Practice.

---

# 💪 Day 13 Practical Tasks

## Task 1 — Salary Prediction

### Dataset

| Experience | Salary |
| ---------- | ------ |
| 1          | 25000  |
| 2          | 30000  |
| 3          | 35000  |
| 4          | 40000  |
| 5          | 45000  |

### Predict

```text
Experience = 6 Years
```

---

## Task 2 — Ice Cream Sales Prediction

### Dataset

| Temperature | Ice Cream Sales |
| ----------- | --------------- |
| 20          | 100             |
| 25          | 120             |
| 30          | 150             |
| 35          | 180             |
| 40          | 220             |

### Predict

```text
Temperature = 45
```

---

## Task 3 — Mini Project

# 🎓 Student Marks Predictor

### Input

```python
hours = float(input("Enter study hours: "))
```

### Output

```text
Predicted Marks = XX
```

### Bonus

* Show Graph
* Save Results
* Upload to GitHub

---

# ✅ What to Learn Today (Checklist)

* [ ] What is Machine Learning
* [ ] Types of Machine Learning
* [ ] Linear Regression
* [ ] Scikit-Learn Basics
* [ ] fit()
* [ ] predict()
* [ ] score()
* [ ] Data Visualization
* [ ] Build First ML Model
* [ ] Student Marks Predictor Project

---

# 📂 Deliverable for Today

```text
Day-13-Linear-Regression/
│
├── linear_regression.py
├── salary_prediction.py
├── student_marks_predictor.py
├── graphs/
├── README.md
```

---

# 🎯 Key Takeaway

Most beginners think Machine Learning is about using libraries.

Reality:

```text
Data → Pattern → Prediction
```

Linear Regression is your first step into understanding how machines learn from data.

---

# 🚀 Next Up

After completing Day 13, you'll move to:

### Day 14 — Model Evaluation + Train/Test Split + Real Dataset Project

This is where Machine Learning starts looking like real industry work.

---

## 💡 Quote of the Day

> "Machine Learning is not magic. It is learning patterns from data and using those patterns to make predictions."
