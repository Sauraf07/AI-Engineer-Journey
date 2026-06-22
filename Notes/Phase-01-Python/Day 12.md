# Day 12 - Exception Handling in Python

> Phase 1: Programming Foundation  
> Roadmap: AI/ML Engineer → GenAI Engineer → Agentic AI Engineer

---

# 🎯 Learning Objectives

By the end of this day, you will be able to:

- Understand why exceptions occur
- Handle runtime errors gracefully
- Use `try`, `except`, `else`, and `finally`
- Handle multiple exceptions
- Raise custom exceptions
- Create robust and user-friendly applications
- Build a calculator with proper error handling
- Answer Python Exception Handling interview questions confidently

---

# 📌 What is Exception Handling?

Exception Handling is a mechanism that allows a program to continue running even when unexpected errors occur.

Without exception handling, the program crashes immediately when an error occurs.

### Example Without Exception Handling

```python
num = int(input("Enter a number: "))
print(10 / num)
```

### Input

```text
0
```

### Output

```text
ZeroDivisionError: division by zero
```

Program crashes.

---

# Why Exception Handling Matters

Real-world applications must handle:

- Invalid user input
- Missing files
- Database failures
- API failures
- Network issues
- Authentication errors

Without exception handling:

❌ Application crashes

With exception handling:

✅ Application continues running

---

# Common Python Exceptions

| Exception | Description |
|------------|-------------|
| ValueError | Invalid value |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |
| AttributeError | Missing object attribute |
| ImportError | Import failed |

---

# The try Block

Code that might produce an error is placed inside the `try` block.

```python
try:
    num = int(input("Enter number: "))
    print(num)
except:
    print("Something went wrong")
```

---

# The except Block

Used to catch exceptions.

```python
try:
    num = int(input("Enter number: "))
except:
    print("Invalid Input")
```

### Input

```text
abc
```

### Output

```text
Invalid Input
```

---

# Catch Specific Exceptions

Recommended approach.

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Please enter valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Multiple Exceptions

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Division by zero not allowed")
```

---

# Exception as Variable

Capture error message.

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except Exception as e:
    print("Error:", e)
```

---

# The else Block

Runs only if no exception occurs.

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
```

---

# The finally Block

Always executes.

Used for:

- Closing files
- Closing database connections
- Cleaning resources

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except:
    print("Error occurred")

finally:
    print("Execution Completed")
```

Output:

```text
Execution Completed
```

always executes.

---

# Complete Flow

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program Ended")
```

---

# Raising Exceptions

Sometimes we intentionally generate exceptions.

```python
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")
```

---

# Custom Exceptions

Create your own exceptions.

```python
class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise InvalidAgeError("Age too low")

print("Eligible")
```

---

# Practical Example 1

## Safe Division Program

```python
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Calculation Completed")
```

---

# Practical Example 2

## Safe List Access

```python
numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("Enter valid number")
```

---

# Practical Example 3

## Safe Dictionary Access

```python
student = {
    "name": "John",
    "age": 20
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key does not exist")
```

---

# Practical Example 4

## File Handling Exception

```python
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Operation Completed")
```

---

# Mini Project

# Robust Calculator

## Requirements

- Addition
- Subtraction
- Multiplication
- Division
- Handle invalid input
- Handle divide by zero
- Continue running until user exits

---

## Solution

```python
while True:

    try:
        print("\n===== Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Choose Option: "))

        if choice == 5:
            print("Goodbye!")
            break

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            print("Result:", num1 / num2)

        else:
            print("Invalid Option")

    except ValueError:
        print("Please enter valid numbers")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except Exception as e:
        print("Unexpected Error:", e)
```

---

# Practice Questions

## Easy

1. Handle ValueError while taking integer input.
2. Handle ZeroDivisionError.
3. Handle IndexError in a list.
4. Handle KeyError in dictionary.
5. Handle FileNotFoundError.

---

## Medium

6. Build safe calculator.
7. Build ATM simulator with exception handling.
8. Create login validation system.
9. Create file reader program.
10. Create student record lookup system.

---

## Advanced

11. Create custom exception.
12. Create banking application.
13. Create inventory management system.
14. Create API error handler.
15. Create exception logging system.

---

# Real World Use Cases

## Banking Applications

```python
try:
    withdraw(amount)
except InsufficientBalance:
    print("Insufficient Balance")
```

---

## API Calls

```python
try:
    response = requests.get(url)
except requests.ConnectionError:
    print("Network Error")
```

---

## Database Connections

```python
try:
    connect_database()
except DatabaseError:
    print("Database Offline")
```

---

# Interview Questions

## Beginner Level

### 1. What is Exception Handling?

Exception Handling is a technique used to manage runtime errors and prevent program crashes.

---

### 2. Why do we use Exception Handling?

To handle unexpected errors gracefully and keep applications running.

---

### 3. What is an Exception?

An exception is an event that interrupts normal program execution.

---

### 4. What is the difference between Syntax Error and Exception?

| Syntax Error | Exception |
|-------------|------------|
| Occurs before execution | Occurs during execution |
| Prevents program start | Happens while running |

---

### 5. What is try block?

Contains code that may generate an exception.

---

### 6. What is except block?

Handles exceptions generated in try block.

---

### 7. What is finally block?

Always executes regardless of exception occurrence.

---

### 8. What is else block?

Runs only if no exception occurs.

---

### 9. Can one try have multiple except blocks?

Yes.

---

### 10. Can finally run without exception?

Yes.

---

# Intermediate Level

### 11. Difference between Exception and Error?

Errors are serious issues while Exceptions can be handled.

---

### 12. What is Exception as e?

Captures exception object.

```python
except Exception as e:
    print(e)
```

---

### 13. What is raising exception?

Manually generating exception using `raise`.

---

### 14. What is custom exception?

User-defined exception class.

---

### 15. Why use custom exceptions?

To represent business-specific errors.

---

# Advanced Level

### 16. What is exception propagation?

Exceptions move up the call stack until handled.

---

### 17. What is exception hierarchy?

Python exceptions are organized in inheritance tree.

---

### 18. Difference between BaseException and Exception?

Exception is derived from BaseException.

---

### 19. Why avoid bare except?

It catches every exception and hides bugs.

Bad:

```python
except:
    pass
```

Good:

```python
except ValueError:
    print("Invalid input")
```

---

### 20. Best Practices for Exception Handling

✅ Catch specific exceptions

✅ Use finally for cleanup

✅ Use meaningful error messages

✅ Avoid bare except

✅ Log exceptions

✅ Create custom exceptions when needed

---

# Day 12 Summary

Today you learned:

- Exception Handling
- try block
- except block
- else block
- finally block
- Multiple exceptions
- Custom exceptions
- Raising exceptions
- Real-world applications
- Robust Calculator Project
- Interview Questions

---

# GitHub Commit Message

```bash
git add .
git commit -m "Day 12: Learned Python Exception Handling and Built Robust Calculator"
git push origin main
```

# 🚀 Next Day

**Day 13: Object-Oriented Programming (OOP) Part 1**
- Classes
- Objects
- Constructors
- Instance Variables
- Methods
- Student Management System Project