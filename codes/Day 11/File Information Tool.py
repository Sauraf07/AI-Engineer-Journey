'''Task 4: File Information Tool
Objective

Use os module.

Requirements

Create a program that:

Shows current directory
Lists all files
Counts total files'''


import os


print("Current Directory:", os.getcwd())
files = os.listdir()
print("Files in Directory:", files)
print("Total Files:", len(files))
