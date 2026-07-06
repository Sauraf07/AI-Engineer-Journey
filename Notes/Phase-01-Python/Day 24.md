# Day 24 - Working with JSON APIs in Python | Build a News App

> **Phase 1: Programming Foundation**
>
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what a JSON API is
- Send HTTP GET requests using the `requests` library
- Parse JSON responses
- Extract required information from API responses
- Handle API errors gracefully
- Understand API authentication basics
- Build a News Application using a public API
- Read and understand API documentation
- Prepare for Python API interview questions

---

# 📖 Table of Contents

1. What is an API?
2. What is JSON?
3. HTTP Methods
4. REST APIs
5. Installing Requests
6. Sending Your First API Request
7. Parsing JSON Data
8. Handling API Errors
9. API Authentication
10. Project: News App
11. Practice Questions
12. Interview Questions
13. Resources
14. Summary

---

# 🌐 What is an API?

API stands for **Application Programming Interface**.

An API allows two applications to communicate with each other.

Example:

```
Python Program
      │
      ▼
   Weather API
      │
      ▼
 Weather Information
```

Instead of collecting weather or news manually, your application requests the data from an API.

---

# 🌍 Real-World API Examples

- Weather Applications
- News Applications
- Google Maps
- Payment Gateways
- ChatGPT
- Gemini AI
- GitHub
- Spotify
- YouTube

Every modern AI application uses APIs.

---

# 📦 What is JSON?

JSON stands for **JavaScript Object Notation**.

It is the standard format used to exchange data between applications.

Example:

```json
{
    "name": "John",
    "age": 22,
    "city": "Delhi"
}
```

Python automatically converts JSON into dictionaries.

---

# HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Fetch Data |
| POST | Create Data |
| PUT | Update Data |
| DELETE | Delete Data |

Today we'll use **GET**.

---

# Installing Requests

```bash
pip install requests
```

Verify installation:

```python
import requests
print(requests.__version__)
```

---

# Your First API Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.status_code)
```

Output

```
200
```

200 means success.

---

# Reading API Response

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.text)
```

---

# Parsing JSON

Instead of using `.text`, use `.json()`.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

print(data)
```

Now `data` is a Python list.

---

# Accessing JSON Data

Example:

```python
print(data[0])
```

Output

```python
{
    "userId":1,
    "id":1,
    "title":"...",
    "body":"..."
}
```

---

Access specific values:

```python
print(data[0]["title"])
```

---

# Loop Through JSON

```python
for post in data:
    print(post["title"])
```

---

# Checking Status Code

Always verify the response.

```python
response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Failed")
```

---

# Handling Exceptions

```python
import requests

try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(e)
```

---

# API Authentication

Some APIs require an API Key.

Example:

```python
params = {
    "apikey": "YOUR_API_KEY"
}

response = requests.get(url, params=params)
```

Never upload your API key to GitHub.

Use environment variables for production applications.

---

# Project: News App

## Features

- Fetch latest news
- Display headlines
- Display source
- Display author
- Handle errors
- User-friendly interface

---

# Project Structure

```
News-App/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Step 1

Install requests

```bash
pip install requests
```

---

# Step 2

```python
import requests
```

---

# Step 3

Replace with your News API endpoint.

```python
url = "YOUR_NEWS_API_URL"
```

---

# Step 4

Fetch news.

```python
response = requests.get(url)
```

---

# Step 5

Convert JSON.

```python
data = response.json()
```

---

# Step 6

Display headlines.

```python
for article in data["articles"]:
    print(article["title"])
```

---

# Improved Version

```python
for article in data["articles"]:
    print("=" * 50)
    print("Title :", article["title"])
    print("Author:", article["author"])
    print("Source:", article["source"]["name"])
    print("URL   :", article["url"])
```

---

# Sample Output

```
==================================================
Title : AI is changing software development
Author: John Doe
Source: Tech News
URL   : https://example.com/article
```

---

# Practice Exercises

### Beginner

- Print all titles
- Print all authors
- Count total articles
- Display only source names

---

### Intermediate

- Search by keyword
- Display top 10 articles
- Save articles to JSON file
- Save articles to CSV

---

### Advanced

- Add search functionality
- Create category filters
- Add pagination
- Build CLI News Reader
- Export results to Excel

---

# Common Errors

## Connection Error

```
ConnectionError
```

Cause:

No internet connection.

---

## Invalid API Key

```
401 Unauthorized
```

Cause:

Wrong API key.

---

## Too Many Requests

```
429 Too Many Requests
```

Cause:

Rate limit exceeded.

---

## Server Error

```
500 Internal Server Error
```

Cause:

Problem on API server.

---

# Best Practices

✅ Always check status code

✅ Handle exceptions

✅ Never expose API keys

✅ Read official documentation

✅ Validate response data

✅ Use `.json()` instead of `.text()` when working with JSON APIs

---

# Real-World AI Applications Using APIs

- ChatGPT API
- Gemini API
- GitHub API
- Hugging Face API
- OpenWeather API
- Google Maps API
- Stripe API
- Twilio API

As an AI Engineer, you'll use APIs almost every day.

---

# Interview Questions

## Beginner

### 1. What is an API?

An API allows two software applications to communicate.

---

### 2. What does REST stand for?

Representational State Transfer.

---

### 3. What is JSON?

JavaScript Object Notation used for data exchange.

---

### 4. Difference between API and Database?

API provides access to data or services, while a database stores data.

---

### 5. Difference between GET and POST?

GET retrieves data.

POST sends data.

---

### 6. What is a status code?

A code returned by the server indicating the result of the request.

---

### 7. What does 200 mean?

Request successful.

---

### 8. What does 404 mean?

Resource not found.

---

### 9. What does 500 mean?

Internal server error.

---

### 10. Why use the requests library?

To send HTTP requests easily in Python.

---

# Intermediate

### 11. Why use `.json()` instead of `.text()`?

`.json()` converts the response into Python objects automatically.

---

### 12. What is an API endpoint?

A specific URL that provides access to a resource.

---

### 13. Why check `status_code`?

To verify whether the request succeeded.

---

### 14. What is API Authentication?

A method to verify that the client is authorized to access the API.

---

### 15. What is an API Key?

A unique key used to authenticate API requests.

---

### 16. Difference between REST API and GraphQL?

REST uses multiple endpoints, while GraphQL allows clients to request exactly the data they need from a single endpoint.

---

### 17. What is rate limiting?

Restricting the number of requests allowed within a specific time.

---

### 18. What happens if JSON is invalid?

Parsing the response can raise an exception, so error handling is required.

---

### 19. How do you handle API failures?

- Check the status code
- Use try-except blocks
- Retry if appropriate
- Log the error

---

### 20. Why are APIs important in AI?

AI applications rely on APIs for accessing LLMs, cloud services, embeddings, databases, payment systems, and integrations.

---

# Mini Challenge

Build a CLI News Reader that allows users to:

- Search by keyword
- Display top headlines
- Choose categories
- Save results to a JSON file
- Handle network errors gracefully

---

# Resources

## Documentation

- Python Requests Documentation
- JSON Documentation
- REST API Tutorial

---

## YouTube

- freeCodeCamp Python API Tutorial
- Corey Schafer - Python Requests
- Programming with Mosh - REST APIs

---

## Practice APIs

- JSONPlaceholder
- OpenWeather
- NewsAPI
- GitHub API

---

# Key Takeaways

✅ Understand APIs and JSON

✅ Send GET requests

✅ Parse JSON responses

✅ Handle API errors

✅ Build a News App

✅ Learn API authentication basics

✅ Prepare for AI development using external APIs

---

# GitHub Commit

```bash
git add .
git commit -m "Day 24: Learned JSON APIs and built a Python News App"
git push origin main
```

---

# 🚀 Next Day

**Day 25 – List Comprehensions**

Topics:

- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Nested Comprehensions
- Performance Comparison
- Real-World Use Cases