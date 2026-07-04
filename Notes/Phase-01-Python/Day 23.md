# Day 23 - Working with REST APIs in Python (Requests Library)

> **Phase 1: Programming Foundation**  
> **Roadmap:** AI/ML Engineer → Generative AI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand what an API is
- Understand REST APIs and HTTP methods
- Make GET and POST requests using Python
- Work with JSON data
- Handle API errors gracefully
- Use query parameters and headers
- Build a Weather App using a public API
- Read API documentation
- Answer REST API interview questions confidently

---

# 📚 Table of Contents

1. What is an API?
2. Why APIs Matter
3. REST APIs
4. HTTP Methods
5. Status Codes
6. Installing Requests Library
7. Making GET Requests
8. Working with JSON
9. Query Parameters
10. Headers
11. POST Requests
12. Error Handling
13. Public APIs
14. Mini Project - Weather App
15. Best Practices
16. Practice Questions
17. Interview Questions
18. Resources
19. Day Summary

---

# 📌 What is an API?

API stands for **Application Programming Interface**.

An API allows two software applications to communicate with each other.

Think of an API like a waiter in a restaurant:

- You (Client)
- Waiter (API)
- Kitchen (Server)

You place an order → API takes the request → Server processes it → API returns the response.

---

# 🌍 Real World Examples

Every day you use APIs without realizing it.

- Google Maps
- Paytm
- UPI
- Instagram
- Spotify
- WhatsApp
- Amazon
- Flipkart
- ChatGPT
- Gemini

---

# 🤖 Why APIs Matter for AI Engineers

Almost every AI application uses APIs.

Examples:

- OpenAI API
- Gemini API
- Hugging Face API
- Weather API
- News API
- Payment API
- Authentication API

Knowing APIs is essential before learning:

- Machine Learning Deployment
- Generative AI
- RAG Systems
- AI Agents
- FastAPI

---

# 🌐 What is REST API?

REST stands for:

**Representational State Transfer**

REST APIs communicate over HTTP and usually exchange data in JSON format.

Example:

```
Client → HTTP Request → Server

Server → JSON Response → Client
```

---

# HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update data |
| PATCH | Partially update data |
| DELETE | Delete data |

---

# HTTP Status Codes

| Code | Meaning |
|--------|-----------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# Installing Requests Library

```bash
pip install requests
```

Check installation:

```bash
pip show requests
```

---

# Importing Requests

```python
import requests
```

---

# Making Your First GET Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

---

# Understanding Response Object

```python
response.status_code
```

Returns:

```
200
```

---

```python
response.text
```

Returns raw response.

---

```python
response.json()
```

Returns Python dictionary.

---

Example

```python
data = response.json()

print(data)
```

Output

```python
{
 'userId':1,
 'id':1,
 'title':'...',
 'body':'...'
}
```

---

# Access JSON Values

```python
print(data["title"])
print(data["body"])
```

---

# Pretty Print JSON

```python
import json

print(json.dumps(data, indent=4))
```

---

# Working with Query Parameters

Example:

```
https://jsonplaceholder.typicode.com/comments?postId=1
```

Python:

```python
params = {
    "postId":1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params=params
)

print(response.json())
```

---

# Headers

Headers provide extra information.

Example:

```python
headers = {
    "User-Agent":"Python"
}

response = requests.get(url, headers=headers)
```

---

# POST Request

```python
data = {
    "title":"Python",
    "body":"Learning APIs",
    "userId":1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.json())
```

---

# Error Handling

Always handle exceptions.

```python
import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    response.raise_for_status()

    print(response.json())

except requests.exceptions.RequestException as e:

    print("Error:", e)
```

---

# Timeout

Avoid waiting forever.

```python
response = requests.get(url, timeout=5)
```

---

# Public APIs for Practice

| API | Website |
|------|----------|
| JSONPlaceholder | https://jsonplaceholder.typicode.com |
| OpenWeather | https://openweathermap.org/api |
| Cat Facts | https://catfact.ninja |
| Dog API | https://dog.ceo/dog-api |
| CoinGecko | https://www.coingecko.com/en/api |
| REST Countries | https://restcountries.com |

---

# Mini Project

# 🌦 Weather Application

## Features

- Enter City Name
- Fetch Weather
- Display:

- Temperature
- Humidity
- Wind Speed
- Description

---

## Example Flow

```
Enter City:

Delhi

Temperature: 36°C

Humidity: 61%

Weather: Clear Sky
```

---

# Bonus Challenge

Create a CLI Weather App with:

- Retry on invalid city
- Better formatting
- Exception handling
- Multiple city search

---

# Best Practices

✅ Always use HTTPS

✅ Read API Documentation

✅ Handle Exceptions

✅ Validate Response

✅ Use Timeouts

✅ Never hardcode API Keys

✅ Store Secrets in `.env`

---

# Practice Questions

## Beginner

1. Fetch one post.
2. Print title.
3. Print body.
4. Print status code.
5. Convert JSON to dictionary.

---

## Intermediate

6. Fetch all users.
7. Search by query parameter.
8. Display formatted JSON.
9. Handle 404 errors.
10. Add custom headers.

---

## Advanced

11. Build Weather App.
12. Build News Reader.
13. Build Currency Converter.
14. Build Country Information App.
15. Build Crypto Price Tracker.

---

# Interview Questions

## Beginner

### 1. What is an API?

An API allows software applications to communicate with each other.

---

### 2. What is REST?

REST is an architectural style for designing web services using HTTP.

---

### 3. What is JSON?

JSON (JavaScript Object Notation) is a lightweight data exchange format.

---

### 4. Difference between API and REST API?

API is a general interface.

REST API follows REST principles over HTTP.

---

### 5. What is HTTP?

HTTP is the communication protocol between client and server.

---

### 6. Difference between GET and POST?

GET retrieves data.

POST creates data.

---

### 7. What is Status Code 200?

Request completed successfully.

---

### 8. What is Status Code 404?

Requested resource not found.

---

### 9. Why use the Requests library?

It simplifies making HTTP requests in Python.

---

### 10. What does `response.json()` do?

Converts JSON response into a Python dictionary.

---

## Intermediate

### 11. Difference between PUT and PATCH?

PUT replaces the entire resource.

PATCH updates only specified fields.

---

### 12. What are Headers?

Metadata sent with HTTP requests.

---

### 13. What are Query Parameters?

Extra values added to the URL for filtering or searching.

---

### 14. What is `raise_for_status()`?

Raises an exception if the HTTP request returned an error status.

---

### 15. Why use timeout?

To prevent applications from waiting indefinitely for a response.

---

## Advanced

### 16. What is API Authentication?

A process to verify the identity of the client (e.g., API keys, OAuth, JWT).

---

### 17. What is Rate Limiting?

Restricts the number of API requests within a time period.

---

### 18. Difference between Authentication and Authorization?

Authentication verifies identity.

Authorization determines access permissions.

---

### 19. Why use environment variables for API keys?

To keep sensitive credentials secure and avoid exposing them in code.

---

### 20. How are APIs used in AI applications?

AI applications use APIs to:
- Access Large Language Models (OpenAI, Gemini)
- Retrieve external data
- Connect tools and services
- Build RAG systems
- Create AI agents

---

# 📝 Assignment

Build a **Weather App** that:

- Accepts city name
- Fetches weather using an API
- Displays:
  - Temperature
  - Humidity
  - Wind Speed
  - Weather Description
- Handles invalid city names gracefully
- Uses exception handling

---

# 📚 Resources

## Official Documentation

- Requests Documentation: https://requests.readthedocs.io/
- JSONPlaceholder: https://jsonplaceholder.typicode.com/
- OpenWeather API: https://openweathermap.org/api

## YouTube

- Corey Schafer - Python Requests
- freeCodeCamp Python API Tutorial
- Programming with Mosh - REST APIs

## Books

- Python Crash Course
- Automate the Boring Stuff with Python

---

# ✅ Day 23 Summary

Today you learned:

- What APIs are
- REST API fundamentals
- HTTP methods
- Status codes
- Using the Requests library
- Making GET and POST requests
- Working with JSON
- Query parameters
- Headers
- Error handling
- Building a Weather App
- REST API interview questions

---

# 🚀 GitHub Commit Message

```bash
git add .
git commit -m "Day 23: Learned REST APIs with Python Requests and built Weather App"
git push origin main
```

---

# ⏭️ Next Day

**Day 24 - Working with JSON Data and Building a News App**

Topics:
- JSON Parsing
- Nested JSON
- News APIs
- Data Formatting
- CLI News Reader Project