# Day 3 - Python Strings & String Slicing

Welcome to **Day 3** of my AI/ML Engineer Roadmap Journey 🚀

Today I learned one of the most important concepts in Python: **Strings**. Since almost every application works with text data (usernames, passwords, emails, chat messages, AI prompts, documents, etc.), understanding strings is essential for becoming a Python Developer, AI Engineer, or Machine Learning Engineer.

---

# 📚 Topics Covered

## 1. What is a String?

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

### Example

```python
name = "Sauraf"
city = 'Indore'

print(name)
print(city)
```

### Output

```text
Sauraf
Indore
```

---

# 2. String Indexing

Each character in a string has a position called an index.

```python
name = "Python"

print(name[0])
print(name[1])
print(name[2])
```

### Output

```text
P
y
t
```

### Index Positions

```text
P  y  t  h  o  n
0  1  2  3  4  5
```

Negative Indexing:

```text
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Example:

```python
print(name[-1])
```

Output:

```text
n
```

---

# 3. String Slicing

String slicing allows us to extract a portion of a string.

### Syntax

```python
string[start:end]
```

Example:

```python
text = "PythonProgramming"

print(text[0:6])
```

Output:

```text
Python
```

---

## More Examples

```python
text = "PythonProgramming"

print(text[:6])
print(text[6:])
print(text[2:10])
```

Output:

```text
Python
Programming
thonProg
```

---

# 4. Step Slicing

Syntax:

```python
string[start:end:step]
```

Example:

```python
text = "PythonProgramming"

print(text[::2])
```

Output:

```text
Pto rgamn
```

---

# 5. Reverse a String

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

# 6. String Methods

Python provides many built-in string methods.

---

## upper()

Converts text to uppercase.

```python
name = "python"

print(name.upper())
```

Output:

```text
PYTHON
```

---

## lower()

Converts text to lowercase.

```python
name = "PYTHON"

print(name.lower())
```

Output:

```text
python
```

---

## capitalize()

```python
name = "python"

print(name.capitalize())
```

Output:

```text
Python
```

---

## title()

```python
text = "python programming"

print(text.title())
```

Output:

```text
Python Programming
```

---

## replace()

```python
text = "Hello World"

print(text.replace("World", "Python"))
```

Output:

```text
Hello Python
```

---

## find()

```python
text = "Python Programming"

print(text.find("Program"))
```

Output:

```text
7
```

---

## count()

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

# 7. String Concatenation

Joining two strings together.

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```text
Hello World
```

---

# 8. String Formatting

### f-Strings

```python
name = "Sauraf"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Sauraf and I am 21 years old.
```

---

# 9. Useful String Operations

## Check Length

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

---

## Check Character Exists

```python
text = "Python"

print("P" in text)
```

Output:

```text
True
```

---

# 🛠 Mini Project 1: Palindrome Checker

A palindrome is a word that reads the same forward and backward.

Examples:

```text
madam
level
racecar
```

### Code

```python
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

---

# 🛠 Mini Project 2: Password Strength Checker

### Code

```python
password = input("Enter Password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
```

---

# 💻 Practice Questions

### Easy

1. Print the first character of a string.
2. Print the last character of a string.
3. Reverse a string.
4. Count vowels in a string.
5. Convert a string to uppercase.

### Medium

6. Check whether a string is palindrome.
7. Count frequency of each character.
8. Find duplicate characters.
9. Remove spaces from a string.
10. Check if two strings are anagrams.

---

# 🎯 Real World Applications of Strings

Strings are used in:

- User Authentication Systems
- Chat Applications
- Search Engines
- AI Chatbots
- Email Validation
- Password Validation
- Data Cleaning
- NLP (Natural Language Processing)

---

# 🧠 Interview Questions

### Q1. What is a string in Python?

A string is a sequence of characters enclosed in quotes.

---

### Q2. What is string slicing?

String slicing is used to extract a portion of a string using indexes.

---

### Q3. Difference between indexing and slicing?

| Indexing | Slicing |
|-----------|----------|
| Returns one character | Returns multiple characters |
| Uses one index | Uses range of indexes |

---

### Q4. How do you reverse a string?

```python
text[::-1]
```

---

### Q5. What is the difference between upper() and capitalize()?

- `upper()` converts all characters to uppercase.
- `capitalize()` converts only the first character to uppercase.

---

# 🚀 Day 3 Summary

Today I learned:

✅ Strings  
✅ Indexing  
✅ Negative Indexing  
✅ String Slicing  
✅ Step Slicing  
✅ String Methods  
✅ String Formatting  
✅ Palindrome Checker  
✅ Password Strength Checker  

---

### Connect With Me

💼 LinkedIn: [Your LinkedIn Profile]

🐙 GitHub: [Your GitHub Profile]

#Python #PythonProgramming #100DaysOfCode #AIEngineer #MachineLearning #GenerativeAI #CodingJourney #GitHub #LearningInPublic