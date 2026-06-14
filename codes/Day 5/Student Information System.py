'''Task 1: Student Information System (Easy)
Objective

Store and display student information using a dictionary.'''
details = {
    'name': 'Saurva Sharma',
    'age': 20,
    'grade': 'A'
}
print("Student Information:")
for key, value in details.items():
    print(f"{key.capitalize()}: {value}")
    