# 🚀 Day 6 — Python Environment, Packages & APIs

## 🎯 Main Goal

Learn how professional Python developers manage projects and use external libraries.

By the end of today, you should be able to:

* Create Virtual Environments
* Install packages using pip
* Understand `requirements.txt`
* Use external libraries
* Make API requests
* Build a simple Weather App

---

# 📚 Topic 1: What is a Virtual Environment?

## ❓ Problem

Imagine:

### Project A needs:

```txt
pandas==1.5
```

### Project B needs:

```txt
pandas==2.2
```

Without a virtual environment, these versions can conflict with each other.

---

## ✅ Solution

A Virtual Environment creates an isolated Python environment for each project.

This allows every project to have its own dependencies and package versions.

---

# 🛠️ Topic 2: Creating a Virtual Environment

## Create Project Folder

```bash
mkdir WeatherApp
cd WeatherApp
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Expected Output

You should see:

```bash
(venv)
```

before your terminal prompt.

---

# 📦 Topic 3: pip

## What is pip?

`pip` = Python Package Manager

Used to install and manage Python libraries.

---

## Check Version

```bash
pip --version
```

---

## Install Package

```bash
pip install requests
```

---

## Install Multiple Packages

```bash
pip install numpy pandas matplotlib
```

---

## See Installed Packages

```bash
pip list
```

---

## Uninstall Package

```bash
pip uninstall package_name
```

---

# 📄 Topic 4: requirements.txt

## Save Project Dependencies

```bash
pip freeze > requirements.txt
```

---

## Install Dependencies from File

```bash
pip install -r requirements.txt
```

---

## Why is it Important?

Almost every real-world Python project uses `requirements.txt` to share dependencies.

---

# 🧠 Topic 5: Python Libraries You Must Know

---

# 🔢 NumPy

### Used For:

* Arrays
* Matrix Operations
* Scientific Computing

---

## Installation

```bash
pip install numpy
```

---

## Example

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

---

# 📊 Pandas

### Used For:

* Data Analysis
* CSV Files
* Data Cleaning

---

## Installation

```bash
pip install pandas
```

---

## Example

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Aman"],
    "Age": [20, 22]
}

df = pd.DataFrame(data)

print(df)
```

---

# 🌐 Requests

### Used For:

* Calling APIs
* Fetching Data from Websites

---

## Installation

```bash
pip install requests
```

---

## Example

```python
import requests

response = requests.get(
    "https://api.github.com"
)

print(response.status_code)
```

---

# 🔌 Topic 6: What is an API?

API = Application Programming Interface

Think of an API like a waiter in a restaurant.

### Example Flow

```txt
You → Request Food
Waiter → Takes Request
Kitchen → Prepares Food
Waiter → Returns Food
```

Similarly:

```txt
Your Program → Sends Request
API → Processes Request
API → Returns Data
```

---

# 📄 Topic 7: Understanding JSON

Most APIs return data in JSON format.

---

## Example JSON

```json
{
  "name": "Sauraf",
  "age": 21
}
```

---

## Python Dictionary Equivalent

```python
data = {
    "name": "Sauraf",
    "age": 21
}

print(data["name"])
```

### Output

```txt
Sauraf
```

---

# 💻 Practice Task 1 — API Request

Create:

```python
import requests

response = requests.get(
    "https://api.github.com"
)

print(response.status_code)
print(response.json())
```

---

## Observe

* Status Code
* JSON Response

---

# 💻 Practice Task 2 — NumPy

Install:

```bash
pip install numpy
```

---

Create:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
print(numbers.mean())
```

---

# 💻 Practice Task 3 — Pandas

Install:

```bash
pip install pandas
```

---

Create:

```python
import pandas as pd

students = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(students)

print(df)
```

---

# 🌦️ Mini Project — Weather App

## Objective

Learn:

* API Calls
* JSON
* requests Library

---

## Features

User enters city name.

Application fetches weather data from API.

Display:

* Temperature
* Wind Speed
* Weather Condition

---

## Suggested API

Open-Meteo API

---

## Concepts Used

* requests
* JSON
* Functions
* User Input
* API Integration

---

# 📂 GitHub Task

Create Repository:

```txt
Day-06-Python-Packages-APIs
```

---

## Upload These Files

```txt
numpy_practice.py
pandas_practice.py
api_practice.py
weather_app.py
README.md
```

---

# ✅ Day 6 Deliverables

Before sleeping today, complete:

* [ ] Create Virtual Environment
* [ ] Install NumPy
* [ ] Install Pandas
* [ ] Install Requests
* [ ] Learn API Basics
* [ ] Create 3 Practice Files
* [ ] Build Weather App
* [ ] Push Everything to GitHub

---

# 🧠 Important Concept for AI Engineers

Most modern AI applications rely heavily on:

* APIs
* External Packages
* Cloud Services
* LLM Integrations

Understanding environments, packages, and APIs is a foundational skill for:

* Machine Learning Engineers
* AI Engineers
* Backend Developers
* Generative AI Developers

---

# 🚀 End of Day 6

Today you learned how real-world Python projects are structured and how applications communicate with external services.

This is the beginning of building AI-powered applications that interact with APIs, databases, vector stores, and Large Language Models.

> **Learn → Build → Share → Improve**
